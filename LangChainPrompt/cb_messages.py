from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# -----------------------------------
# Initialize Gemini
# -----------------------------------

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)
# this code does not store the chat history so we can not continue with the previous conversation. If we want to store the chat history we can use the memory class from langchain_core.memory module. This will allow us to store the chat history and continue with the previous conversation.
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit':
#         break
#     result = model.invoke(user_input)
#     print("Response from Gemini: ", result.content[0]['text'])

chat_history = []
while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input.lower() == 'exit':
        break
    result = model.invoke(chat_history)
    res=result.content[0]['text']
    chat_history.append(res)
    print("Response from Gemini: ", res)

print("Chat history: ", chat_history)
