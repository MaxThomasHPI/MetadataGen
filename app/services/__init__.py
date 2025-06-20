"""
This module contains the separate parts of the program. This includes

- the actual metadata builder responsible to create the metadata fragments
- the connector to the LLM
- the promt generators and the query builders
- the processing unit parsing the LLM response
- a translator to convert German texts into English
- specific processors for non-LLM suggestions on the basis of embeddings
- a logging module responsible of keeping track of suggestions
"""
