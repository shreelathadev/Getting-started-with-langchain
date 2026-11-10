from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

llm = OpenAI(model_name="gpt-3.5-turbo-instruct")

result = llm.invoke("Hello, how are you?")

print(result)

