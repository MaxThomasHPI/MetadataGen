from flask import Blueprint, request, jsonify, render_template
from app.services.orchestrator.orchestrator import generate_ed_align_suggestion, generate_teaches_suggestion, \
    generate_keywords_suggestion, generate_educational_level_suggestion
from app.services.metadata_builder.metadata_builder import build_metadata
from app.services.framework_processor.framework_processor import gather_all_framework_data, \
    gather_educational_level_data
from app.services.templatesProcessor.templatesProcessor import gather_all_templates_data


main = Blueprint('main', __name__)


@main.route('/')
def start_client():
    return render_template("index.html")


@main.route('/generate_metadata', methods=['POST'])
def generate_metadata():
    data = request.get_json()
    metadata = build_metadata(data)

    return "ok"

"""
@main.route('/get_ed_align_frameworks')
def get_ed_align_frameworks():
    return jsonify(gather_all_framework_data("educational_alignment"))
"""

@main.route('/get_frameworks')
def get_frameworks():
    return jsonify({"educationalAlignment": gather_all_framework_data("educational_alignment"),
                    "teaches": gather_all_framework_data("teaches"),
                    "educationalLevel": gather_educational_level_data()})


@main.route('/get_templates')
def get_templates():
    return jsonify(gather_all_templates_data())


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
    return jsonify(generate_educational_level_suggestion(data["name"], data["description"], data["educationalFramework"]))
