from rdflib import Graph
import os

path = os.path.dirname(__file__)
path = os.path.join(path, "../../frameworks/teaches/ESCO/esco-v1.1.2.ttl")

g = Graph()
#g.parse(path)
