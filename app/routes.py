"""The routes to the endpoints"""


import io
import json

import flask
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
def start_client() -> str:
    """
    Renders and returns the initial HTML page.

    :return: The landing page rendered into HTML.
    :rtype: str
    """
    return render_template("index.html")


@main.route('/generate_metadata', methods=['POST'])
def generate_metadata() -> Response:
    """
    Generates the requested metadata in the MOOChub format and returns it via a
    Response.

    :return: The JSON file containing the requested metadata in the MOOChub format.
    :rtype: flask.Response
    """
    data = request.get_json()

    data = json.dumps(build_metadata(data), indent=4)

    file_object = io.BytesIO(data.encode('utf-8'))
    file_object.seek(0)

    return send_file(file_object, download_name='metadata.json',
                     mimetype='application/json',
                     as_attachment=True)


@main.route('/get_frameworks')
def get_frameworks() -> Response:
    """
    Returns the framework data to the client. These are the initial framework information.
    for building the frameworks on the client side.

    :return: A response object with the initial framework data.
    :rtype: flask.Response
    """
    return jsonify({"educationalAlignment": gather_all_framework_data("educational_alignment"),
                    "teaches": gather_all_framework_data("teaches"),
                    "educationalLevel": gather_educational_level_data()})


@main.route('/get_templates')
def get_templates() -> Response:
    """
    Returns all templates for creating the attribute input form on the frontend.

    :return: The templates for creating the frontend.
    :rtype: flask.Response
    """
    return jsonify(get_all_templates())


@main.route('/get_ed_align_suggestion', methods=['POST'])
def get_ed_align_suggestion() -> Response:
    """
    Returns a jsonified metadata fragment for a educationalAlignment attribute.

    :return: A educationalAlignment fragment according to the MOOChub format.
    :rtype: flask.Response
    """
    data = request.get_json()
    return jsonify(generate_ed_align_suggestion(data["name"], data["description"], data["educationalFramework"]))


@main.route('/get_teaches_suggestion', methods=['POST'])
def get_teaches_suggestion() -> Response:
    """
    Returns a jsonified metadata fragment for a teaches attribute.

    :return: A teaches fragment according to the MOOChub format.
    :rtype: flask.Response
    """
    data = request.get_json()
    return jsonify(generate_teaches_suggestion(data["name"], data["description"], data["educationalFramework"]))


@main.route('/get_keywords_suggestion', methods=['POST'])
def get_keywords_suggestion() -> Response:
    """
    Returns a jsonified metadata fragment for a keywords attribute.

    :return: A keywords fragment according to the MOOChub format.
    :rtype: flask.Response
    """
    data = request.get_json()
    return jsonify(generate_keywords_suggestion(data["name"], data["description"]))


@main.route('/get_educational_level_suggestion', methods=['POST'])
def get_educational_level_suggestion() -> Response:
    """
    Returns a jsonified metadata fragment for a educationalLevel attribute.

    :return: A educationalLevel fragment according to the MOOChub format.
    :rtype: flask.Response
    """
    data = request.get_json()
    return jsonify(generate_educational_level_suggestion(data["name"], data["description"],
                                                         data["educationalFramework"]))


@main.route('/get_specified_suggestions', methods=['POST'])
def get_specified_suggestions() -> Response:
    """
    Returns a set of suggestions for the specified attributes.

    :return: A set of metadata fragments for the requested attriibutes.
    :rtype: flask.Response
    """
    data = request.get_json()

    metadata = generate_specified_suggestions(data["title"], data["description"], data["services"])
    return jsonify(metadata)


@main.route('/get_esco_fragment', methods=['POST'])
def get_esco_fragment() -> dict:
    """
    Returns a ESCO fragment. This fragment contains the sub-entries to a given entry
    represented by its URI.

    :return: The narrower entries to a given ESCO entry.
    :rtype: dict
    """
    uri = request.get_json()["uri"]

    return get_narrower_data(uri)


@main.route('/get_esco_suggestions', methods=['POST'])
def get_esco_suggestions() -> list:
    """
    Creates four suggestions for competencies ("teaches" attribute) based on the ESCO
    framework.

    :return: A list of four ESCO competencies for the "teaches" attribute in the MOOChub
    format.
    :rtype: list
    """
    data = request.get_json()

    return generate_esco_suggestion(data["name"], data["description"])


@main.route('/openhpi')
def render_openhpi() -> str:
    """
    Returns the web page specifically designed to serve the openHPI purpose.

    :return: The specific web page for openHPI.
    :rtype: str
    """
    return render_template("openhpi.html")


@main.route('/get_course_by_short_code')
def get_course_by_short_code() -> dict:
    """
    Returns the metadata set of an openHPI course identified by its short code ("courseCode").

    :return: A metadata set according to the MOOChub format from the openHPI MOOChub endpoint.
    :rtype: dict
    """
    data = find_dataset(request.args.get("shortCode"))

    if data:
        return data
    return {}


@main.route('/generate_openhpi_metadata_fragments', methods=['POST'])
def generate_openhpi_metadata_fragments() -> Response:
    """
    Returns the metadata created for an openHPI course.

    :return: The metadata fragments for the "teaches" and the "educationalAlignment"
    attributes according to the MOOChub format.
    :rtype: flask.Response
    """
    raw_data = request.get_json()

    buffer = build_openhpi_metadata_fragments(raw_data)

    if buffer:
        response = send_file(buffer, mimetype="application/zip")
        response.headers['Content-Disposition'] = 'attachment; filename=download.zip'

        return response
    return Response(status=204)
