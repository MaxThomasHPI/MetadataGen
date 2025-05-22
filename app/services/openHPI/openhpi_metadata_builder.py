import json
import io
import zipfile

from app.services.metadata_builder.metadata_builder import build_all_educational_alignments, \
    build_all_teaches


def build_openhpi_metadata_fragments(input_data):
    if len(input_data.keys()) == 0:
        return None

    educational_alignment = None
    competencies = None

    if "educationalAlignment" in input_data.keys():
        educational_alignment = input_data["educationalAlignment"]
        educational_alignment = json.dumps(build_all_educational_alignments(educational_alignment))
        educational_alignment.encode()
    if "teaches" in input_data.keys():
        competencies = input_data["teaches"]
        competencies = json.dumps(build_all_teaches(competencies))
        competencies.encode()

    data_file = io.BytesIO()

    with zipfile.ZipFile(data_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        if competencies:
            zipf.writestr("skills.json", competencies)
        if educational_alignment:
            zipf.writestr("educational_alignment.json", educational_alignment)

        if not zipf.namelist():
            return None

    data_file.seek(0)

    return data_file
