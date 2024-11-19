from langgraph.prebuilt import create_react_agent
from langchain_mistralai import ChatMistralAI
from langchain_core.tools import tool
import os
os.environ["MISTRAL_API_KEY"] = "SotgVGWqDkvz1qchuc6FNDmfzzWTlWFX"

llm = ChatMistralAI(model="mistral-large-latest", temperature=0)


@tool
def add(a: int, b: int) -> int:
    """Adds a and b."""
    return a + b

tools = [add]

graph = create_react_agent(llm, tools=tools)