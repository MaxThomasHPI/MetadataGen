from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DataFrameLoader
from langchain_chroma import Chroma
from app.helper.paths import FRAMEWORK_ROOT, EMBEDDINGS_ROOT
import os
import pandas as pd


def create_vector_db(framework_name: str, conf: dict) -> None:
    """
    Creates a vector database for a given framework if not already present in the particular
    folder. The embedding model is chosen according to the respective config file. All data is
    gathered from the framework CSV file containing the entries' data. The CSV file is modified
    if no 'page_content' column is present. This column holds a combination of the 'name' and the
    'description' of the respective entry and added to the framework CSV file. Documents were
    loaded using the huggingface-community DataFrameLoader and cut into batches of a maximum of
    5000 entries each (within the limit of the chromadb 'add()' method). The persistent directory
    of the DB is the folder of the framework.

    :param framework_name: The name of the framework the vector DB is created for.
    :type framework_name: str
    :param conf: The config file that contains information about which model to use for the embedding.
    :type conf: dict
    :rtype: None
    """
    conf = conf[framework_name]
    print(f"Generating vector DB for {framework_name}...")

    path_model = (
        EMBEDDINGS_ROOT /
        conf["MODEL"]
    )

    if path_model.exists():
        print(f"Found local embedding model. Using model at path: {path_model} ...")
        embedding_model = HuggingFaceEmbeddings(model_name=path_model.__str__())
    else:
        print(f"No locally stored model at path {path_model} found. Try loading from HuggingFace ...")

        try:
            embedding_model = HuggingFaceEmbeddings(model_name=conf["MODEL"])
        except OSError as no_model_found:
            print(no_model_found)
            print(f"Model {conf['MODEL']} not found! Please check for e.g. spelling errors in the config!")
            return

    path_framework = (
        FRAMEWORK_ROOT /
        conf["GROUP"] /
        framework_name
    )

    file = [file for file in os.listdir(path_framework) if file[-4:] == ".csv"][0]

    path_framework_file = (
        path_framework /
        file
    )
    framework_data = pd.read_csv(path_framework_file, dtype=str)
    framework_data = framework_data.fillna("")

    if "page_content" not in framework_data.columns:
        print("No page_content column found. Add page_content column ...")
        framework_data["page_content"] = framework_data.apply(
            lambda row: f"{row.loc['name']}. {row.loc['description']}", axis=1)
        framework_data.to_csv(path_framework_file, index=False)
        print("Added page_content column ...")

    if not (path_framework / "chroma.sqlite3").exists():
        loader = DataFrameLoader(framework_data, page_content_column="page_content")
        documents = loader.load()
        print("Loaded documents ...")

        print("Create batches ...")
        batches = list()
        batch_size = 5000
        for i in range(0, len(documents), batch_size):
            batches.append(documents[i:i + batch_size])
        print(f"Created {len(batches)} batches ...")

        vector_db = Chroma(
            embedding_function=embedding_model,
            collection_name=framework_name,
            persist_directory=path_framework.__str__(),
            collection_metadata={"hnsw:space": "cosine"}
        )
        print("Created vector DB ...")

        for i, batch in enumerate(batches):
            vector_db.add_documents(documents=batch)
            print(f"Batch {i+1} of {len(batches)} added.")
        print("Added all documents ...")
        print(f"Creating vector DB for {framework_name} finished!")
    else:
        print(f"Vector DB for {framework_name} already exists! Skipping this step ...")
