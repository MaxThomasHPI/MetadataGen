"""Functions to find an ESCO skill based on a given model and a query."""


from . import skills, index, model


def find_skills(query: str) -> list:
    """
    Selects and returns four skills with title, description and node URI.
    The four skills were selected to be the most similar ones according
    to an input query encoded into a vector on the bases of a given model.

    :param query: A title and a description text of a course for which the skills
    have to be determined.
    :type query: str
    :return: A list of four skills each represented by a dictionary with the name,
    description and URI.
    :rtype: list
    """
    query_embedding = model.encode([query], convert_to_numpy=True, normalize_embeddings=True)
    D, I = index.search(query_embedding, 4)

    results = list()
    for i, score in zip(I[0], D[0]):  # index i is a list index
        skill = skills[i]  # the index i of the FAISS-index is equivalent to the
        # index of the same skill in the .JSON file skill list
        results.append({
            "title": skill["title"],
            "description": skill["description"],
            "uri": skill["uri"],
            "score": float(score)
        })

    return results
