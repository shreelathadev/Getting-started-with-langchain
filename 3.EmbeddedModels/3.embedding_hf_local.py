from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)
documents = ["Delhi is the capital of India.", "Mumbai is the financial capital of India."]
vectors = embedding.embed_documents(documents)  # this will give us the embedding vectors for the documents.

print(str(vectors))  # this will give us the embedding vectors for the documents in string format.
