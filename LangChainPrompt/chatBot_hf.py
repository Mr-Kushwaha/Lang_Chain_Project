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

chat_history = []
while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input.lower() == 'exit':
        break
    result = model.invoke(chat_history)
    print(result)
    res=result.content
    chat_history.append(res)
    print("Response from Gemini: ", res)

print("Chat history: ", chat_history)
