from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# -----------------------------------
# Initialize Gemini
# -----------------------------------

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)


chat_template = ChatPromptTemplate([
    ('system', "You are a helpful customer support assistant"),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', "{query}")
])

chat_history = []

with open("LangChainPrompt\\chat_history.txt", "r") as file:
    chat_history = file.read().splitlines()
print(chat_history)

prompt = chat_template.invoke({"chat_history": chat_history, "query": HumanMessage(content="Where is my refund")}) # in new version invoke is replace by format

print(prompt)