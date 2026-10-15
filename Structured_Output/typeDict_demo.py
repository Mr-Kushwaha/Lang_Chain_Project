from typing import TypeDict

class Person(TypeDict):
    name: str
    age: int
    email: str


#typeDict is a new feature in python 3.11 and it is used to define a dictionary with specific keys and values. It is similar to TypedDict but it is more strict and it does not allow extra keys. It is also more efficient than TypedDict because it uses a fixed size for the dictionary.
new_person: Person = {
    "name": "John Doe",     
    "age": 30,
    "email": "john.doe@example.com"
}