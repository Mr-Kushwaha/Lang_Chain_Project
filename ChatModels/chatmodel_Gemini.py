from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0.9, max_output_tokens=220)

res=model.invoke("Write 2 lines for virat kholi") #unless llms(return string) it return the json response with content and metadata
print(res.content[0]['text']) 
