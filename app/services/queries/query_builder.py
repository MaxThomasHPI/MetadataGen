from app.services.promter.promter_selector import select_all

PROMT = "You are asked to create metadata for a learning resource.\n"


def create_query(title: str, description: str, promts: list = None):
    #if promts is None or len(promts) == 0:
        #promts = select_all()
    query = PROMT

    for p in promts:
        query += p

    query += f"title: {title}\n" \
             f"description: {description}"

    return query
