from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-4.1-mini')

result = llm.invoke("What is the capital of india")
print(result)


#HEre code give an error because I uses openai api key 
# OPenAI API key is paid 