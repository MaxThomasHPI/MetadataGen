from rdflib import Graph
import os

path = os.path.dirname(__file__)
path = os.path.join(path, "../../frameworks/teaches/ESCO/esco.ttl")

g = Graph()
g.parse(path)
