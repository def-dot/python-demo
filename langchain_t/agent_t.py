import asyncio
from langchain_mistralai import ChatMistralAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
import os
os.environ["MISTRAL_API_KEY"] = "SotgVGWqDkvz1qchuc6FNDmfzzWTlWFX"
os.environ["TAVILY_API_KEY"] = "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"

model = ChatMistralAI(model="mistral-large-latest", temperature=0)

search = TavilySearchResults(max_results=2)
tools = [search]

def agent_with_memory():
    memory = MemorySaver()
    agent_executor = create_react_agent(model, tools, checkpointer=memory)

    config = {"configurable": {"thread_id": "abc123"}}
    for chunk in agent_executor.stream(
        {"messages": [HumanMessage(content="hi im bob! and i live in sf")]}, config
    ):
        print(chunk)
        print("----")

    for chunk in agent_executor.stream(
        {"messages": [HumanMessage(content="whats the weather where I live?")]}, config
    ):
        print(chunk)
        print("----")


def agent():
    agent_executor = create_react_agent(model, tools)
    response = agent_executor.invoke({
        "messages": [HumanMessage(content="whats the weather in sf?")]
    })
    print(response)
    """输出如下：
    1. HumanMessage: whats the weather in sf?
    2. AIMessage：tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'weather in san francisco'}, 'id': 'toolu_01Y5EK4bw2LqsQXeaUv8iueF'}]
    3. ToolMessage: 调用工具后，返回结果：{"url": "https://www.weatherapi.com/", "content": "{\'location\': {\'name\': \'San Francisco\', \'region\': \'California\', \'country\': \'United States of America\',
    4. AIMessage：content=""，将ToolMessage传递给LLM后，LLM根据ToolMessage，推理出HumanMessage的答案
    """

async def agent_event():
    agent_executor = create_react_agent(model, tools)
    async for event in agent_executor.astream_events({
        "messages": [HumanMessage(content="whats the weather in sf?")]
    }, version="v1"):
        kind = event["event"]
        if kind == "on_chain_start":
            if event["name"] == "agent":
                print("============================")
                print(event)

        if kind == "on_chain_end":
            if event["name"] == "agent":
                print("============================")
                print(event)

        if kind == "on_chat_model_stream":
            content = event["data"]["chunk"].content
            if content:
                print(content, end="|")

        if kind == "on_tool_start":
            print("============================")
            print(event)

        if kind == "on_tool_end":
            print("============================")
            print(event)
        
# agent()
asyncio.run(agent_event())
