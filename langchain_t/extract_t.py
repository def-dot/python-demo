"""
langchain 返回结构化数据
"""
from typing import Optional

from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate

import os
os.environ["MISTRAL_API_KEY"] = "SotgVGWqDkvz1qchuc6FNDmfzzWTlWFX"

class Person(BaseModel):
    name: Optional[str] = Field(default=None, description="the name")
    hair_color: Optional[str] = Field(default=None, description="the color")
    height_in_meters: Optional[str] = Field(default=None, description="the height")


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an information extraction expert. Please extract the main information from the given data, including the name, hair color, and height. If any of the corresponding attributes are not found, return null."),
    ("human", "{text}")
])


from langchain_mistralai import ChatMistralAI

llm = ChatMistralAI(model="mistral-large-latest", temperature=0)

runnable = prompt | llm.with_structured_output(schema=Person)

text = "Alan Smith is 6 feet tall and has blond hair."
r = runnable.invoke({"text": text})
print(r)