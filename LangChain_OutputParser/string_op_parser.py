from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

temp1 = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. Answer the following question: {question}"
)           

temp2 = PromptTemplate( 
    input_variables=["topic"],
    template="Write a 5 line summary of the topic {topic}"
)

parser= StrOutputParser()

chain = temp1 | model | parser | temp2 | model | parser
res = chain.invoke({"question": "What is Black Holes?"})


print(res)
