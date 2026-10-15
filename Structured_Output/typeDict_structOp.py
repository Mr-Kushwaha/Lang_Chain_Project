from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Original code:
# model = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0.9, max_output_tokens=220)
#
# Reasons for change:
# 1. 503 UNAVAILABLE Error: 'gemini-3.6-flash' was experiencing high server demand spikes.
#    Google recommends using 'gemini-3.8-flash' for better availability and performance.
# 2. UserWarning for temperature: Newer Gemini Flash models use fixed sampling defaults, so 'temperature' is ignored.
# 3. OutputParserException with max_output_tokens=220: 'gemini-3.8-flash' generates internal reasoning
#    tokens before outputting the structured JSON. A 220-token limit cuts off the output mid-generation,
#    causing JSON parsing failures. Removing this limit (or setting it to 1000+) allows full JSON completion.
model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")


class Review(TypedDict):
    summary: str
    sentiment: str

struct_model = model.with_structured_output(Review)

res = struct_model.invoke("Write a review for the movie 'Inception'.")
print(res)