from typing import Annotated

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langchain_experimental.utilities import PythonREPL
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from langgraph.graph import MessagesState, StateGraph, START, END
from langchain_community.chat_models.tongyi import ChatTongyi
import os
os.environ["TAVILY_API_KEY"] = "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"
os.environ["DASHSCOPE_API_KEY"] = "sk-04097ca9e2e44c4492784fa77f7e0d4a"

llm = ChatTongyi()
tavily_tool = TavilySearchResults(max_results=5)

repl = PythonREPL()  # PythonREPL langchain中安全执行python代码

@tool
def python_repl_tool(
    code: Annotated[str, "The python code to execute to generate your chart."],
):
    """Use this to execute python code. If you want to see the output of a value,
    you should print it out with `print(...)`. This is visible to the user."""
    try:
        print(f"--------------------- {code}")
        result = repl.run(code)
    except BaseException as e:
        return f"Failed to execute. Error: {repr(e)}"
    result_str = f"Successfully executed: python {code} Stdout: {result}"
    return (
        result_str + "\n\nIf you have completed all tasks, respond with FINAL ANSWER."
    )

def make_system_prompt(suffix: str) -> str:
    return (
        "You are a helpful AI assistant, collaborating with other assistants."
        " Use the provided tools to progress towards answering the question."
        " If you are unable to fully answer, that's OK, another assistant with different tools "
        " will help where you left off. Execute what you can to make progress."
        " If you or any of the other assistants have the final answer or deliverable,"
        " prefix your response with FINAL ANSWER so the team knows to stop."
        f"\n{suffix}"
    )

research_agent = create_react_agent(
    llm,
    tools=[tavily_tool],
    state_modifier=make_system_prompt(
        "You can only do research. You are working with a chart generator colleague."
    ),
)


def research_node(state: MessagesState) -> MessagesState:
    result = research_agent.invoke(state)

    print("****************************************")
    print(result["messages"])
    print("++++++++++++++++++++++++++++++++++++++++")

    result["messages"][-1] = HumanMessage(
        content=result["messages"][-1].content, name="researcher"
    )
    return {
        "messages": result["messages"],
    }


chart_agent = create_react_agent(
    llm,
    [python_repl_tool],
    state_modifier=make_system_prompt(
        "You can only generate charts. You are working with a researcher colleague."
    ),
)


def chart_node(state: MessagesState) -> MessagesState:
    result = chart_agent.invoke(state)
    result["messages"][-1] = HumanMessage(
        content=result["messages"][-1].content, name="chart_generator"
    )
    return {
        "messages": result["messages"],
    }


def router(state: MessagesState):
    messages = state["messages"]
    last_message = messages[-1]
    if "FINAL ANSWER" in last_message.content:
        return END
    return "continue"


workflow = StateGraph(MessagesState)
workflow.add_node("researcher", research_node)
workflow.add_node("chart_generator", chart_node)

workflow.add_conditional_edges(
    "researcher",
    router,
    {"continue": "chart_generator", END: END},
)
workflow.add_conditional_edges(
    "chart_generator",
    router,
    {"continue": "researcher", END: END},
)

workflow.add_edge(START, "researcher")
graph = workflow.compile()

img_data = graph.get_graph().draw_mermaid_png()
with open('graph_image.png', 'wb') as f:
    f.write(img_data)

events = graph.stream(
    {
        "messages": [
            (
                "user",
                "First, get the UK's GDP over the past 5 years, then make a line chart of it with excel. "
                "Once you make the chart, finish.",
            )
        ],
    },
    {"recursion_limit": 150},
)
for s in events:
    print(s)
    print("----")
