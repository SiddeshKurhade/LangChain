
import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Hugging Face model
llm_model = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
    max_new_tokens=100,
    provider="auto"
)

# Convert LLM into a Chat Model
model = ChatHuggingFace(llm=llm_model)

# Send query
result = model.invoke("What is the capital of India?")

# Display response
print(result)
print(result.content)
