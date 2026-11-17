from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


load_dotenv()
model1 = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
model2 = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

temp1 = PromptTemplate(
    input_variables=["text"],
    template="Generate the short and simple notes from the text: {text}"
)

temp2 = PromptTemplate( 
    input_variables=["text"],
    template="Generate the 5 questions about the topic {text}"
)

temp3 = PromptTemplate( 
    input_variables=["notes", 'quiz'],
    template="Merge the following notes and quiz into a single document \n notes: {notes}, quiz: {quiz}"
)

parser= StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": temp1 | model1 | parser,
    "quiz": temp2 | model2 | parser
})

merge_chain = temp3 | model1 | parser
chain = parallel_chain | merge_chain

text='''Square Root Decomposition Technique is one of the most common query optimization techniques used by competitive programmers. This technique helps us to reduce Time Complexity by a factor of sqrt(N) 

The key concept of this technique is to decompose a given array into small chunks specifically of size sqrt(N)

Follow the below steps to solve the problem:

We have an array of n elements and we decompose this array into small chunks of size sqrt(N)
We will be having exactly sqrt(N) such chunks provided that N is a perfect square
Therefore, now our array of N elements is decomposed into sqrt(N) blocks, where each block contains sqrt(N) elements (assuming the size of the array is a perfect square)
Let's consider these chunks or blocks as an individual array each of which contains sqrt(N) elements and you have computed your desired answer(according to your problem) individually for all the chunks
Now, you need to answer certain queries asking you the answer for the elements in the range l to r(l and r are starting and ending indices of the array) in the original n-sized array
Naive Approach: To solve the problem follow the below idea:

Simply iterate over each element in the range l to r and calculate its corresponding answer. Therefore, the Time Complexity per query will be O(N)'''
res = chain.invoke({"text": text})


print(res)
#printting graph
chain.get_graph().print_ascii()