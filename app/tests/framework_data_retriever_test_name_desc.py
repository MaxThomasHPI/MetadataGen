from app.framework_handler.framework_data_retriever import get_name_and_description


uri = "https://metadata-generator.xikolo.de/framework/digcomp/5"
framework = "DigComp"
group = "educationalLevel"

print(get_name_and_description(framework, group, uri))
