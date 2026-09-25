from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import torch
import sentence_transformers

load_dotenv()

# for single line embedding model use embedding query and after that we see we can use embedding documents for document embedding. Here we are using sentence-transformers/all-MiniLM-L6-v2 model for embedding query and documents and file
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2")
# res=embeddings.embed_query("What is the capital of Australia?") 
# print(res)

docs=["What is the capital of Australia?","What is the capital of India?","What is the capital of France?"]
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
res=embeddings.embed_documents(docs)
print(str(res))