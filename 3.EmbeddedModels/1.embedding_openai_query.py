from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

embedding = OpenAIEmbeddings(model_name="text-embedding-3-large", dimensions=32)  

result = embedding.embed_query("dehlhi is the capital of india")  # this will give us the embedding vector for the query.

print(str(result))  # this will give us the embedding vector for the query in string format.


#the above was for embedding a query, we can also embed documents using the embed_documents method as shown below.


load_dotenv()  # Load environment variables from .env file

embedding = OpenAIEmbeddings(model_name="text-embedding-3-large", dimensions=32) 

documents = ["Delhi is the capital of India.", "Mumbai is the financial capital of India."]

result = embedding.embed_documents(documents)  # this will give us the embedding vectors for the documents.

print(str(result))