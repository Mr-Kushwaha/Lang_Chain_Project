from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

# -----------------------------------
# Initialize Gemini
# -----------------------------------

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

message = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="tell me about lang chain"),
]

res=model.invoke(message)
message.append(AIMessage(content=res.content[0]['text']))
print(message)