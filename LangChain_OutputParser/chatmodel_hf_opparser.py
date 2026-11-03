from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()
llm = HuggingFacePipeline.from_model_id(
    model_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 200,
        "temperature": 0.9
    }
)


model = ChatHuggingFace(llm=llm)


temp1 = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. Answer the following question: {question}"
)           

temp2 = PromptTemplate( 
    input_variables=["topic"],
    template="Write a 5 line summary of the topic {topic}"
)


prompt1 = temp1.format_prompt(question="What is black hole?")

res1 = model.invoke(prompt1.to_string())
print(res1.content) 

prompt2 = temp2.format_prompt(topic=res1.content)

res2 = model.invoke(prompt2.to_string())
print(res2.content)