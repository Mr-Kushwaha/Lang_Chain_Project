Agentic Ai Tutorial:

foundation model is like llm(not only for text, it also for images, audios, etc.) and it is 2 types

user perspective(for using llms): prompt engineer, rag, ai agents(do some work using llms), vector database(for implementing rag), fine tuning
builder perspective(for making llms):rlhf(reinforcement learning by human feedback use to make llm relevent so the llm does not give wage or irrelevent response), pre-training, quantization, fine tuning

Builder’s Perspective:

Transformars architechture:
pretaining: for training foundations models
optimizing
fine tune
evaluation
deployement

User’s Perspective

prompt engineering
rag
fine tuning
agents(not only talk do some work also)
LLMops


image

RAG by langchain:

image

image

temperature value in models: for the same given input llm give same output if temp value is around 0 and if we increase the value to around 1 or 1.5 it produces new output every time

 it is like how creative you want to be if it is near to o then it was give factual answers(for math and coding) if it was near to 1 or 1.5 give creative answers(for writing, poem, and jokes)

Max_completion_tokens: it just like how many words you want in your response

Close Source Model: In these models we have to communicate via api and there is some cost related to it and we can not make changes(OpenAi, Claude)

image


Prompts:

