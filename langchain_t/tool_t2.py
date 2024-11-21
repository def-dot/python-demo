from langchain_mistralai import ChatMistralAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
import os
os.environ["MISTRAL_API_KEY"] = "SotgVGWqDkvz1qchuc6FNDmfzzWTlWFX"
os.environ["TAVILY_API_KEY"] = "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"

model = ChatMistralAI(model="mistral-large-latest", temperature=0)

memory = MemorySaver()
search = TavilySearchResults(max_results=2)
tools = [search]

model_with_tools = model.bind_tools(tools)
response = model_with_tools.invoke([HumanMessage(content="What's the weather in SF?")]) 

"""
由LLM决定是否需要调用tool，如果需要，会返回tool_calls（决定调用的工具）；否则tool_calls返回[]，表示不需要调用工具
"""
print(f"ContentString: {response.content}")
print(f"ToolCalls: {response.tool_calls}")