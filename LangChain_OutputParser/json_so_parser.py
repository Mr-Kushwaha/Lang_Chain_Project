from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic")
]



parser= StructuredOutputParser.from_response_schemas(schema
)
temp = PromptTemplate(
    input_variables=['topic'],
    template="3 fact about {topic}? \n{format_instructions}",
    partial_variables={"format_instructions": parser.get_format_instructions()}
)           


prompt=temp.format_prompt(topic="Iron man")

print(prompt)

res=model.invoke(prompt)
final_output=parser.invoke(res.content[0]['text'])
print(final_output)