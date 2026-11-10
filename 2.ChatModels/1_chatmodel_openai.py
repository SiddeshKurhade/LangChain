from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model='gpt-4.1-mini',
    #temperature is a parameter that controls the randomness of a language models output. 
    #It affects how creative or deterministic the responses are
    #lower values(0.0-0.3) -> more deterministic & predictable
    #higher values(0.7-1.5) -> More random creative & diverse
    temperature=0.7,       
    max_tokens=100  #Maximum number of tokens to generate
    )

result = model.invoke("What is the capital of india?")
print(result)  # This returns all metadata with ans
print(result.content) #this only returns content (correct ans)
