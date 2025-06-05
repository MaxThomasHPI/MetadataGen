import io
import json
from flask import Blueprint, request, jsonify, render_template, send_file, Response
from app.services.orchestrator.orchestrator import generate_ed_align_suggestion, generate_teaches_suggestion, \
    generate_keywords_suggestion, generate_educational_level_suggestion, generate_specified_suggestions, \
    generate_esco_suggestion
from app.services.metadata_builder.metadata_builder import build_metadata
from app.services.framework_processor.framework_processor import gather_all_framework_data, \
    gather_educational_level_data
from app.services.templates_processor.templates_processor import get_all_templates
from app.services.ESCO_processor.ESCO_processor import get_narrower_data
from app.services.openHPI.course_processor import find_dataset
from app.services.openHPI.openhpi_metadata_builder import build_openhpi_metadata_fragments


main = Blueprint('main', __name__)


@main.route('/')
def start_client():
    return render_template("index.html")


@main.route('/generate_metadata', methods=['POST'])
def generate_metadata():
    data = request.get_json()

    data = json.dumps(build_metadata(data), indent=4)

    file_object = io.BytesIO(data.encode('utf-8'))
    file_object.seek(0)

    return send_file(file_object, download_name='metadata.json',
                     mimetype='application/json',
                     as_attachment=True)


@main.route('/get_frameworks')
def get_frameworks():
    return jsonify({"educationalAlignment": gather_all_framework_data("educational_alignment"),
                    "teaches": gather_all_framework_data("teaches"),
                    "educationalLevel": gather_educational_level_data()})


@main.route('/get_templates')
def get_templates():
    return jsonify(get_all_templates())


@main.route('/get_ed_align_suggestion', methods=['POST'])
def get_ed_align_suggestion():
    data = request.get_json()
    return jsonify(generate_ed_align_suggestion(data["name"], data["description"], data["educationalFramework"]))


@main.route('/get_teaches_suggestion', methods=['POST'])
def get_teaches_suggestion():
    data = request.get_json()
    return jsonify(generate_teaches_suggestion(data["name"], data["description"], data["educationalFramework"]))


@main.route('/get_keywords_suggestion', methods=['POST'])
def get_keywords_suggestion():
    data = request.get_json()
    return jsonify(generate_keywords_suggestion(data["name"], data["description"]))


@main.route('/get_educational_level_suggestion', methods=['POST'])
def get_educational_level_suggestion():
    data = request.get_json()
    return jsonify(generate_educational_level_suggestion(data["name"], data["description"],
                                                         data["educationalFramework"]))


@main.route('/get_specified_suggestions', methods=['POST'])
def get_specified_suggestions():
    data = request.get_json()

    metadata = generate_specified_suggestions(data["title"], data["description"], data["services"])
    return jsonify(metadata)


@main.route('/get_esco_fragment', methods=['POST'])
def get_esco_fragment():
    uri = request.get_json()["uri"]

    return get_narrower_data(uri)


@main.route('/get_esco_suggestions', methods=['POST'])
def get_esco_suggestions():
    data = request.get_json()

    return generate_esco_suggestion(data["name"], data["description"])


@main.route('/openhpi')
def render_openhpi():
    return render_template("openhpi.html")


@main.route('/get_course_by_short_code')
def get_course_by_short_code():
    data = find_dataset(request.args.get("shortCode"))

    if data:
        return data
    return {}


@main.route('/generate_openhpi_metadata_fragments', methods=['POST'])
def generate_openhpi_metadata_fragments():
    raw_data = request.get_json()

    buffer = build_openhpi_metadata_fragments(raw_data)

    if buffer:
        response = send_file(buffer, mimetype="application/zip")
        response.headers['Content-Disposition'] = 'attachment; filename=download.zip'

        return response
    return Response(status=204)
