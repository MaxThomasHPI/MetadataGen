PROMT = "You are asked to create metadata for a learning resource.\n"


def create_query(title: str, description: str, promts: list = None):
    query = PROMT

    for p in promts:
        query += p

    query += f"title: {title}\n" \
             f"description: {description}"

    return query
