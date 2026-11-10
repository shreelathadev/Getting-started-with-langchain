from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

my_secret_key = os.environ.get("HUGGINGFACEHUB_API_TOKEN")

print("Token loaded:", my_secret_key is not None)

llm = HuggingFaceEndpoint(huggingfacehub_api_token=my_secret_key, repo_id="TinyLlama/TinyLlama-1.1B-Chat-v0.6", task="text-generation")

chat_model = ChatHuggingFace(llm=llm)  

result = chat_model.invoke("what is the capital of India?")

print(result)