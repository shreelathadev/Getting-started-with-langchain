from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

chat_model = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.8, max_output_tokens=256)  # other parameters can be passed here, like temperature, max_completion_tokens(the number of words/tokens in the response we get, (mainly useful when we are using paid versions)), etc.

result = chat_model.invoke("Hello, how are you?")

# print(result)

print(result.text) # this will give us the actual response from the model.
