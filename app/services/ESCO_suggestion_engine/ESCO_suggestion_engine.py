from ..ESCO_suggestion_engine import skills, index, model


def find_skills(query):
    query_embedding = model.encode([query], convert_to_numpy=True, normalize_embeddings=True)
    D, I = index.search(query_embedding, 4)

    results = []
    for i, score in zip(I[0], D[0]):
        skill = skills[i]
        results.append({
            "title": skill["title"],
            "description": skill["description"],
            "uri": skill["uri"],
            "score": float(score)
        })

    return results
