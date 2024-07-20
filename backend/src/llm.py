# from langchain_community.chat_models import ChatOllama
from langchain_together import ChatTogether, Together
from langchain_openai import ChatOpenAI
from dataclasses import dataclass

import os                                                                                                                                                                                                          
from dotenv import load_dotenv
load_dotenv('../.env')

@dataclass
class Model:
    DEFAULT_LLM = ChatOpenAI(
    base_url="https://api.together.xyz/v1",
    api_key=os.getenv("TOGETHER_API_KEY"),
    model="meta-llama/Llama-3-70b-chat-hf",
    temperature = 0,
    # top_p = 0.9
)
    
#     Together(
#     together_api_key=os.getenv("TOGETHER_API_KEY"),
#     model="meta-llama/Llama-3-8b-chat-hf",
#     temperature = 0,
#     max_tokens=300,
#     top_p=0.7
# )
    # ChatOllama(model="llama3", temperature=0, base_url = "http://ollama:11434")
