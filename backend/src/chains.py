import datetime
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

from src.utils import list_all_topics
from src.llm import Model

EXTRACT_COMPANY_NAME_PROMPT = """**Task**: Extract companies name from the given Details question if possible. Adhere to the specific Rules and Example Response:
**Rules**:
- Return a list even if only one company is found
- If no company name is found, return empty list
- If multiple companies are found, return all of them
- Respond without any pre-amble

**Example Response**:
- ["Apple Inc"]
- ["Microsoft Corp", "Google", "Tesla Inc"]
- []

**Details**:
- Question: {question}

**Response**:"""


ACTION_ROUTE_PROMPT = """The given question could be related to finance topic or an unknown topic. You must clarify the topic in its original name. Respond without any preamble

- List of Topics: {topics}
- Question: {question}
- Topic:"""

SYNTHETIC_PROMPT = """You are a helpful assistant who answers questions based on the information provided.

**Task**: Create a response using the available Details while adhering to the following Rules:

**Rules**:
- Always ensure a response to the input question. 
- Avoid prefaces such as "based on information", "available in the provided data", "according to the provided data", etc.

**Details**:
- Question: {question}
- Companies: {companies}
- Data: {data}
- Today: {today}

If the provided Data does not contain statistics needed to answer Question, you MUST not reply there is no data/no provided data, JUST say 'Here is your info'
"""


DEFAULT_PROMPT = """You are FinSav, a finance expert who can provide information and insights about various aspects of the financial world. Ask questions or seek advice about stocks, investments, market trends, financial analysis, and more. Today is {today}.
Question: {question}
"""


class ChainFactory:
    @staticmethod
    def create_extract_company_chain():
        print('Extract Company Name')
        return (
            {"question": RunnablePassthrough()}
            | PromptTemplate(
                template=EXTRACT_COMPANY_NAME_PROMPT,
                input_variables=["question"],
            )
            | Model.DEFAULT_LLM
            | StrOutputParser()
        )

    @staticmethod
    def create_action_route_chain():
        print('Action Route')
        topics = list_all_topics()
        return (
            {"question": RunnablePassthrough()}
            | PromptTemplate(
                template=ACTION_ROUTE_PROMPT,
                input_variables=["question"],
                partial_variables={"topics": topics}
            )
            | Model.DEFAULT_LLM
            | StrOutputParser()
        )

    @staticmethod
    def create_synthetic_chain(companies, data):
        print('Synthetic chain')
        return (
            {"question": RunnablePassthrough()}
            | PromptTemplate(
                template=SYNTHETIC_PROMPT,
                input_variables=["question"],
                partial_variables={
                    "companies": companies,
                    "data": data,
                    "today": datetime.datetime.now()
                }
            )
            | Model.DEFAULT_LLM
            | StrOutputParser()
        )

    @staticmethod
    def create_default_chain():
        print('Default here')
        return (
            {"question": RunnablePassthrough()}
            | PromptTemplate(
                template=DEFAULT_PROMPT,
                input_variables=["question"],
                partial_variables={
                    "today": datetime.datetime.now()
                }
            )
            | Model.DEFAULT_LLM
            | StrOutputParser()
        )
