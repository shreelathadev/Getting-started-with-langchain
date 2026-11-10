# Here we are gonna use the document similarity model from langchain to find the similarity between two documents. 
# We will use the HuggingFaceEmbeddings model to get the embeddings of the documents and then use the cosine similarity to find the similarity between the documents.
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "who is known as the fast bowler?"

doc_vector = embedding.embed_documents(documents)

query_vector = embedding.embed_query(query)

scores = cosine_similarity([query_vector], doc_vector)[0] #Because we passed 1 query and 5 documents, it returns a nested list structure that looks like a box inside a box: [[0.12, 0.15, 0.08, 0.11, 0.78]].
                                                          #The [0] at the very end: That just unwraps the outer box so you get a clean, flat list of numbers

# print(scores)  # this will give us the similarity scores between the query and the documents. The higher the score, the more similar the document is to the query.

score =  sorted(list(enumerate(scores)), key = lambda x: x[1])[-1]

print(score)
print("The query is: ", query)
print("The most similar document to the query is: ", documents[score[0]])
print("The similarity between the query and the document is: ", score[1])