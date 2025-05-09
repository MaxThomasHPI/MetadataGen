from sentence_transformers import SentenceTransformer
import json
import faiss
import os

path_skills = os.path.join(os.path.dirname(__file__), "skills.json")
path_index = os.path.join(os.path.dirname(__file__), "esco_index.faiss")

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

with open(path_skills, 'r') as f:
    skills = json.loads(f.read())

index = faiss.read_index(path_index)
