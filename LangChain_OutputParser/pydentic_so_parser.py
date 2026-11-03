from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

# Define schema using Pydantic
class Facts(BaseModel):
    name: str = Field(description="name of the topic")
    age: int = Field(gt=18, description="age of the topic")
    power: str = Field(description="power of the topic")

parser = PydanticOutputParser(pydantic_object=Facts)

temp = PromptTemplate(
    input_variables=['topic'],
    template="name of the character, age of the character, and power of the character {topic}?\n{format_instructions}",
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# chain = temp | model | parser
# final_output = chain.invoke({"topic": "Iron Man"})
# print(final_output)

prompt = temp.format_prompt(topic="Iron Man")
print(prompt)

res = model.invoke(prompt)
final_output = parser.invoke(res.content[0]['text'])
print(final_output)