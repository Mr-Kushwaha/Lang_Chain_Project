from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import torch

load_dotenv()
embeddings = OpenAIEmbeddings(
    model="Qwen/Qwen3-Embedding-0.6B", #closed source required payment
    dimensions=32
)
res=embeddings.embed_query("What is the capital of Australia?") 
print(res)

# model = ChatHuggingFace(llm=llm)
# res=model.invoke("What is the capital of India?") #unless llms(return string) it return the json response with content and metadata
# print(res.content) 