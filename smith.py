
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ["GROQ_API_KEY"] = "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"
os.environ["LANGCHAIN_TRACING_V2"] = "true"

os.environ["LANGCHAIN_PROJECT"] = "LLM APP"
os.environ["Langchain_API_KEY"] = "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"

chat_model = ChatOpenAI(
    openai_api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
    model_name="llama3-8b-8192"
)
#output of a chain is returned as a string,
output_parser=StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant.please response to the user request only baed on the given context"),
    ("user", "Questions:{question}\nContext:{context}")
])
chain=prompt|chat_model|output_parser
question="Answers these questions"
context="""
        {"question": "What is LangChain?"},
        {"question": "What is LangSmith?"},
        {"question": "What is OpenAI?"},
        {"question": "What is Google?"},
        {"question": "What is Mistral?"},
        
        {"what is AI and describe any models"}"""

print(chain.invoke({"question":question,"context":context}))

