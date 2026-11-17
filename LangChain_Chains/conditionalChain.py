from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch, RunnableLambda


load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

parser= StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(..., description="The sentiment of the feedback text, either 'positive' or 'negative'.")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    input_variables=["feedback"],
    template="Classify the sentiment of the following feedback text in to positive or negative: {feedback}\n{format_instructions}",
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)


classifier_chain = prompt1 | model | parser2

#res = classifier_chain.invoke({"feedback": '''The product is really good and I am very satisfied with the quality.'''})
# this feedback is coming in any from like a single string or line or multiple lines or paragraphs. So, we use pydantic to make output according to us so we can use in further processing.

#classifier_chain.get_graph().print_ascii()

prompt2 = PromptTemplate(
    input_variables=["feedback"],
    template="Write a positive response to the following feedback text: {feedback}"
)   

prompt3 = PromptTemplate(
    input_variables=["feedback"],
    template="Write a negative response to the following feedback text: {feedback}"
) 

branch_chain = RunnableBranch(     #it is kind of if else condition, if the condition is true then it will run the first chain otherwise second chain.
    (lambda x:x.sentiment=="positive", prompt2 | model | parser),
    (lambda x:x.sentiment=="negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not classify the sentiment of the feedback.")
)

chain = classifier_chain | branch_chain
res = chain.invoke({"feedback": '''The product is really bad and I am very disappointed with the quality of your laptop.'''})
print(res)