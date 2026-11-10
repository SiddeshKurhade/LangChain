import os

from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()


model = ChatOllama(
    model="llama3.2:1b",
    temperature=0.7
)

result = model.invoke("What is the capital of India?")
# print(result)
print(result.content)