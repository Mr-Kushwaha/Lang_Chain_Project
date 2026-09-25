from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
import torch

load_dotenv()
llm = HuggingFacePipeline.from_model_id(
    model_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 200,
        "temperature": 0.9
    }
)

model = ChatHuggingFace(llm=llm)
res=model.invoke("What is the capital of India?") #unless llms(return string) it return the json response with content and metadata
print(res.content) 