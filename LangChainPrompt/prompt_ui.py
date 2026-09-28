from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
import json


# Load environment variables from .env
load_dotenv()


# -----------------------------------
# Load Prompt Template from JSON file
# -----------------------------------

with open("LangChainPrompt/template.json", "r", encoding="utf-8") as f:
    template_config = json.load(f)


template = PromptTemplate(
    template=template_config["template"],
    input_variables=template_config["input_variables"],
    template_format=template_config.get("template_format", "f-string"),
    validate_template=template_config.get("validate_template", True)
)


# -----------------------------------
# Initialize Gemini
# -----------------------------------

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)


# -----------------------------------
# Create LangChain Chain
# -----------------------------------

chain = template | model 
#instead of using invoke 2 times we can use the pipe operator to chain the prompt and the model together. This allows us to pass the output of the prompt directly to the model for processing, making the code more concise and readable. The chain will take care of formatting the prompt with the provided input variables and then sending it to the model for generating a response.


# -----------------------------------
# Streamlit UI
# -----------------------------------

st.title("Research Topic Summarizer")


paper_input = st.selectbox(
    "Select the research topic:",
    [
        "Quantum Physics",
        "Black Holes",
        "Data Science",
        "Artificial Intelligence",
        "Machine Learning",
        "Natural Language Processing",
        "Computer Vision",
        "Robotics",
        "Data Structures And Algorithms",
        "Neuroscience"
    ]
)


style_input = st.selectbox(
    "Select the style of explanation:",
    [
        "beginner",
        "intermediate",
        "technical",
        "expert"
    ]
)


length_input = st.selectbox(
    "Select the length:",
    [
        "short - 1 paragraph",
        "medium - 2 paragraphs",
        "long - 3 paragraphs"
    ]
)


# -----------------------------------
# Generate Summary
# -----------------------------------

if st.button("Generate Summary"):

    with st.spinner("Generating summary..."):

        response = chain.invoke({
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input
        })

    st.subheader("Summary")

    # Gemini response can be a string or structured content
    if isinstance(response.content, str):
        st.write(response.content)

    elif isinstance(response.content, list):
        for block in response.content:
            if isinstance(block, dict) and block.get("type") == "text":
                st.write(block.get("text", ""))

    else:
        st.write(response.content)