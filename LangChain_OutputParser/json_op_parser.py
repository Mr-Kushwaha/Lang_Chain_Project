from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

parser= JsonOutputParser()
temp = PromptTemplate(
    input_variables=[],
    template="about Iron man? \n{format_instructions}",
    partial_variables={"format_instructions": parser.get_format_instructions()}
)           

# prompt=temp.format_prompt()
# print(prompt)

# res=model.invoke(prompt)
# final_output=parser.invoke(res)
#2nd method
chain = temp | model | parser
final_output = chain.invoke({})

print(final_output)