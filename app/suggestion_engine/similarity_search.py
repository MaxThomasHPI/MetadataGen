from app.helper.load_config import load_suggestion_engine_conf
from app.helper.paths import FRAMEWORK_ROOT, EMBEDDINGS_ROOT
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import chromadb


def search_frameworks(data: list, query: str) -> tuple[list, str]:
    """
    Conducts a similarity search using cosine similarity within the vector database
    of the given framework. It will return only the metadata of the (by default 5)
    selected entries (all information needed for the respective metadata fragment)
    and the name of the framework it belongs to, as necessary information for further
    processing.

    :param data: A data fragment that contains information about the framework the query is fired again.
    :type data: list
    :param query: The query (course title and description) for which the corresponding
    entries are identified.
    :type query: str
    :return: A tuple of a list with the selected entries and the framework the selected entries
    belong to.
    :rtype: tuple[list, str]
    """
    framework = data[0]["educationalFramework"]

    conf = load_suggestion_engine_conf()[framework]

    persist_directory = (
        FRAMEWORK_ROOT /
        conf["GROUP"] /
        framework
    ).__str__()
    path_embedding_func = (
        EMBEDDINGS_ROOT /
        conf["MODEL"]
    ).__str__()

    embedding_func = HuggingFaceEmbeddings(model_name=path_embedding_func)
    client = chromadb.PersistentClient(path=persist_directory)

    vector_store = Chroma(
        client=client,
        embedding_function=embedding_func,
        collection_metadata={"hnsw:space": "cosine"},
        collection_name=framework
    )

    results = vector_store.similarity_search_with_relevance_scores(query, 5)

    data = [(result[0].metadata, result[1]) for result in results]
    return data, framework
