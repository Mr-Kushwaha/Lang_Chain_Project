from typing import TypedDict, Annotated, Optional
from pydantic import BaseModel, EmailStr, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

#model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")


class Student(BaseModel):
    name: str = 'aman'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(ge=0.0, le=4.0, default=3.0, description="CGPA must be between 0.0 and 4.0")


new_stu=Student(name="John Doe", age=20, email="john.doe@example.com", cgpa=3.5)
print(new_stu)

print(new_stu.dict())
