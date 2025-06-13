"""
Initializes the ESCO graph. It reads the provided .TTL file and provides a
rdflib.Graph object. Initializing in the __init__ make the graph accessible
in the runtime.
"""

from rdflib import Graph
import os

path = os.path.dirname(__file__)
path = os.path.join(path, "../../frameworks/teaches/ESCO/esco.ttl")

g = Graph()
g.parse(path)
