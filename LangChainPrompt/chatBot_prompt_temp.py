from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# -----------------------------------
# Initialize Gemini
# -----------------------------------

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)


#in lang chain formatted string does not support so below cloc doesn't work
# chat_template = PromptTemplate(
#     SystemMessage(content="You are a helpful {domian} assistant"),
#     HumanMessage(content="Pls explain what is {topic}")
# )

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domian} assistant"),
    ('human', "Pls explain what is {topic}")
])

print(chat_template)
prompt = chat_template.format(domian="AI", topic="LangChain") # in new version invoke is replace by format

print(prompt)