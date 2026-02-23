from langchain_core.prompts import ChatPromptTemplate
from app.llm_support import keywords_prompter
from app.llm_support import educational_level_prompter


def create_template(framework: str) -> ChatPromptTemplate:
    """
    Creates a LLM chat templates. The system prompt is based on a pre-set list of prompts.
    A framework for the educational level is given to select a particular framework.

    :param framework: The name of the framework that is used in the educational level suggestion.
    :type framework: str
    :return: A query to be passed to the LLM.
    :rtype: str
    """

    system_prompt = "You are an assistant that supports the creation of metadata for a learning resource.\n"

    prompts = [
        keywords_prompter.get_prompt(),
        educational_level_prompter.get_prompt(framework)
    ]

    for p in prompts:
        system_prompt += p

    user_prompt = "Please create the metadata for this learning resource: {query}"

    return ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", user_prompt)
    ])
