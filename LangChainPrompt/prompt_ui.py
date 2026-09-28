from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st 
from dotenv import load_dotenv
import torch

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-3.6-flash")

paper_input=st.selectbox("Select the researchpaper Name:", ["Quantum Physics", "Black Holes", "Data Science", "Artificial Intelligence", "Machine Learning", "Natural Language Processing", "Computer Vision", "Robotics", "Data Structures And Algorithms", "Neuroscience"])
style_input=st.selectbox("Select the style of writing:", ["beginner ", "intermediate", "technical", "expert"])
length_input=st.selectbox("Select the length of the summary:", ["short - 1 paragraph", "medium - 2 paragraphs", "long - 3 paragraphs"])


if st.button("Generate Summary"):
    prompt=f"Summarize the research paper '{paper_input}' in a '{style_input}' style and '{length_input}' length."
    res=model.invoke(prompt) #unless llms(return string) it return the json response with content and metadata
    st.write(res.content[0]['text'])



