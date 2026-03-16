from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
from memory.conversation import create_memory

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

load_dotenv()

INTERVIEWER_SYSTEM_PROMPT = """You are an expert technical interviewer.

Your role:
- Ask one clear, focused question at a time
- Reference previous answers when relevant
- Build on the conversation naturally
- Be professional but encouraging

Interview type: {interview_type}
Position level: {level}
Focus area: {focus_area}

Remember: You have access to the full conversation history.
Use it to avoid repeating questions and to ask follow-ups.
"""

interviewer_prompt = ChatPromptTemplate.from_messages([
    ("system", INTERVIEWER_SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="history", optional=True),
    ("human", "{input}")
])



# def create_interviewer_chain(
#    model: str = os.getenv('MODEL'),
#     temperature: float = 0.7
# ):
#     """Create a basic interviewer chain."""

#     llm = OllamaLLM(model=model, temperature=temperature)

#     chain = interviewer_prompt | llm | StrOutputParser()

#     return chain

def create_interviewer_chain_with_memory(memory):
    """Create interviewer chain with conversation memory."""

    prompt = ChatPromptTemplate.from_messages([
        ("system", INTERVIEWER_SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

    llm = OllamaLLM(model=os.getenv('MODEL'), temperature=0.7)

    # Chain that loads memory before processing
    chain = (
        RunnablePassthrough.assign(
            history=lambda x: memory.messages  # Load messages from memory
        )
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain