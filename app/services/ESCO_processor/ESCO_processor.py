"""
All functions to extract data from the ESCO graph. This includes finding the
preferred label and all narrower nodes in the hierarchical system.
"""
from rdflib import URIRef
from rdflib.resource import Resource

from app.services.ESCO_processor import g
from rdflib.namespace import SKOS

root_url = "http://data.europa.eu/esco/skill/335228d2-297d-4e0e-a6ee-bc6a8dc110d9"


def get_node_label(node: Resource) -> str:
    """
    Extracts the preferred label of an entry in English language.

    :param node: The node for which the preferred label is identified.
    :type node: :class:`rdflib.resource.Resource`
    :return: The preferred label in English language.
    :rtype: str
    """
    for label in g.objects(node.identifier, SKOS.prefLabel):
        if label.language == "en":
            return label.__str__()


def find_all_narrower(node: Resource) -> list:
    """
    Finds all narrower nodes to a given node (entry).

    :param node: The node for which the narrower nodes are identified.
    :type node: :class:`rdflib.resource.Resource`
    :return: A list of all narrower nodes for the given node.
    :rtype: list
    """
    nodes = set()
    for narrower in g.objects(node.identifier, SKOS.narrower):
        nodes.add(g.resource(narrower))
    return list(nodes)


def get_initial_data() -> dict:
    """
    Extract the data of the toplevel entries of the hierarchical framework.

    :return: A list of the toplevel entries.
    :rtype: dict
    """
    node_data = get_narrower_data(root_url)
    return node_data


def get_node(identifier: URIRef) -> Resource:
    """
    Extracts a single node o the basis of a URI.

    :param identifier: A URI pointing at the node in the graph.
    :type identifier: :class:`rdflib.URIRef`
    :return: The node as identified by the URI.
    :rtype: :class:`rdflib.resource.Resource`
    """
    return g.resource(identifier)


def get_narrower_data(identifier: URIRef | str) -> dict:
    """
    Collects the data of all narrower nodes to a node given by its URI.

    :param identifier: A URI that identifies a node in the framework graph.
    :type identifier: :class:`rdflib.URIRef` or str
    :return: A dictionary with the node uri and an information if there are
    sub-nodes for each node. The preferred label of the node is the key.
    :rtype: dict
    """
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
