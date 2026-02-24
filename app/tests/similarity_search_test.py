from app.suggestion_engine.similarity_search import search_frameworks
from pprint import pprint

query = """
    <h2>Welcome to the \"Sustainability in the Digital Age\" series</h2>\\n\\n<p>In an era where "
    digital technologies are reshaping industries and daily life, the environmental impact of AI systems has 
    become a growing concern. This course explores efficient AI methodologies to address these challenges. From 
    deep learning model compression to low-bit quantization and collaborative inference, we delve into techniques 
    that enhance computational efficiency and reduce energy consumption. In Week 2, we focus on low-bit 
    quantization specifically for large language models (LLMs), showcasing cutting-edge open-source tools and 
    models. Join us to learn how to build sustainable AI systems while pushing the boundaries of innovation. 
    </p>\\n\\n<hr>\\n\\n<p>This course is part of the <strong>Sustainability in the Digital Age</strong> series, 
    a collaborative project between colleagues from Stanford University, SAP and the Hasso Plattner Institute. </p>\\n
    """

pprint(search_frameworks([{"educationalFramework": "ESCO"}], query))
pprint(search_frameworks([{"educationalFramework": "ISCED-F"}], query))
