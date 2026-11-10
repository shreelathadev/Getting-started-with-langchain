from langchain_openai import chat_OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

chat_model = chat_OpenAI(model_name="gpt-4")  # other parameters can be passed here, like temperature, max_completion_tokens(the number of words/tokens in the response we get, (mainly useful when we are using paid versions)), etc.

result = chat_model.invoke("Hello, how are you?")

print(result) # if we print this, we get a whole lot of things, like content: where we have the actual response, and other additional kwargs.

print(result.content) # this will give us the actual response from the model.