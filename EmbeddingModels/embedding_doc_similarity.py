from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import torch
import sentence_transformers
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()


#docs=["What is the capital of Australia?","What is the capital of India?","What is the capital of France?"]

docs=[
    'virat kohli is a great cheaser and he has won many chanshing matches and made test cricket famous',
    'sachin tendulkar is a great cricketer and he is known as the god of cricket and he hit 100 centuries',
    'ms dhoni is a great wicket-keeper and he is known for his cool demeanor and he won many matches and many icc trophies for india and he is a great captain',
    'rohit sharma is a great hitter and he is known for his big hitting and he has scored many double centuries in odi cricket',
    'rahul dravid is a great defender and he is known as the wall of indian cricket and he has played many test matches for india'
]
query="who won many icc trophies for india"
#query='tell me about ms dhoni'

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
doc_embeddings=embeddings.embed_documents(docs)
query_embedding=embeddings.embed_query(query)

#print(cosine_similarity([query_embedding], doc_embeddings))

scores = cosine_similarity([query_embedding], doc_embeddings)[0]
print(docs[sorted(list(enumerate(scores)), key=lambda x: x[1], reverse=True)[0][0]])