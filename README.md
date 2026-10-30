Agentic Ai Tutorial:

Command To move in virtual environment: .\venv\Scripts\Activate.ps1

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

img


Prompts:


ChatBot:
continous conversation between ai and humans
langChain provides the fecelity to do a conversation with ai using system message, humand message and ai message
system message: this is the initial message at the starting of the conversation with ai (for example when we tell the ai agent to behave like something to aquire some skills like 'you are an 5 year of senior engineer now rate my pr' by this system message ai agent behave like 5yoexperienced engineer and rate the users pr)

message place holder: it loads the previous chat of the user in between it's current chat(or session) for example : we are making chat bot for the amazon comapany and user ask a question when he will get the refund and bot told that which in 3 days but the refund didn;t occur so user again come and ask the status for refund so the chatbot is taking reference from the previos chat by loading it from db



Structured Output: In langchain structured output refers to the practice of having language models return responses in a well defined format (like: json) this make the model o/p easier to parse

where we can use SO:
data extraction, api building, agents
for example: we have simple math agent which use calculator we told agent to find sqrt of 2 so using structured outout agent filter the operator and operand so calculator can perform their task

In SO, in a backend a kind of prompt generation is happening and that prompt tells the model to genrate SO

In Annotated Dict we can specify our json format so tha model can understood the expectation of this perticular field(or key)

Typedict is not strict even we mention the value is str model will be give it in int and does not give any error. so, we can use pydentic for this coz in pydantic we can not change the type it will give error

SO may use as 3 ways dict, pydentic, json
Opensource models does not capable to give the structured output. we can achive this by Output Parsers
  
OutputParser: it is a some class in langchain with the help of this we can convert rae llm responce to so. Thy ensure consistency, validation, and esae of use in application.

