from app.services.ESCO_processor import g
from rdflib.namespace import SKOS

root_url = "http://data.europa.eu/esco/skill/335228d2-297d-4e0e-a6ee-bc6a8dc110d9"


def get_node_label(node):
    for label in g.objects(node.identifier, SKOS.prefLabel):
        if label.language == "en":
            return label.__str__()


def find_all_narrower(node):
    nodes = set()
    for narrower in g.objects(node.identifier, SKOS.narrower):
        nodes.add(g.resource(narrower))
    return list(nodes)


def get_initial_data():
    node_data = get_narrower_data(root_url)
    return node_data


def get_node(identifier):
    return g.resource(identifier)


def get_narrower_data(identifier):
    node = get_node(identifier)
    nodes = find_all_narrower(node)
    node_data = dict()
    for node in nodes:
        name = get_node_label(node)
        uri = node.identifier.__str__()
        sub_nodes = find_all_narrower(node)
        node_data[name] = {
            "uri": uri,
            "hasNarrower": len(sub_nodes) > 0
        }
    return node_data
