from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver


def simple():
    class State(TypedDict):
        input: str


    def step_1(state):
        print("---Step 1---")
        pass


    def step_2(state):
        print("---Step 2---")
        pass


    def step_3(state):
        print("---Step 3---")
        pass


    builder = StateGraph(State)
    builder.add_node("step_1", step_1)
    builder.add_node("step_2", step_2)
    builder.add_node("step_3", step_3)
    builder.add_edge(START, "step_1")
    builder.add_edge("step_1", "step_2")
    builder.add_edge("step_2", "step_3")
    builder.add_edge("step_3", END)

    # Set up memory
    memory = MemorySaver()

    # Add
    graph = builder.compile(checkpointer=memory, interrupt_before=["step_3"])

    img_data = graph.get_graph().draw_mermaid_png()
    with open('graph_image.png', 'wb') as f:
        f.write(img_data)

    thread = {"configurable": {"thread_id": "1"}}
    for event in graph.stream({"input": "hello world"}, thread):
        print(event)

    try:
        approval = input("to continue, yes or no ?")
    except Exception as e:
        approval = "yes"

    if approval == "yes":
        for event in graph.stream(None, thread):
            print(event)
    else:
        print("rejected !")


def agent():
    from langchain_core.tools import tool
    from langgraph.graph import MessagesState, START
    from langgraph.prebuilt import ToolNode
    from langgraph.graph import END, StateGraph
    from langgraph.checkpoint.memory import MemorySaver
    from langchain_mistralai import ChatMistralAI
    import os

    @tool
    def search(query: str):
        """Call to surf the web."""
        return [
            "It's sunny in San Francisco, but you better look out if you're a Gemini 😈."
        ]

    tools = [search]
    tool_node = ToolNode(tools)

    os.environ["MISTRAL_API_KEY"] = "SotgVGWqDkvz1qchuc6FNDmfzzWTlWFX"
    model = ChatMistralAI(model="mistral-large-latest", temperature=0)
    model = model.bind_tools(tools)


    def should_continue(state):
        messages = state["messages"]
        last_message = messages[-1]
        if not last_message.tool_calls:
            return "end"
        else:
            return "continue"

    def call_model(state):
        messages = state["messages"]
        response = model.invoke(messages)
        return {"messages": [response]}

    workflow = StateGraph(MessagesState)
    workflow.add_node("agent", call_model)
    workflow.add_node("action", tool_node)
    workflow.add_edge(START, "agent")
    workflow.add_conditional_edges(
        "agent",
        should_continue,
        {
            "continue": "action",
            "end": END,
        },
    )
    workflow.add_edge("action", "agent")
    memory = MemorySaver()
    app = workflow.compile(checkpointer=memory, interrupt_before=["action"])

    img_data = app.get_graph().draw_mermaid_png()
    with open('graph_image.png', 'wb') as f:
        f.write(img_data)

    from langchain_core.messages import HumanMessage

    thread = {"configurable": {"thread_id": "3"}}
    inputs = [HumanMessage(content="search for the weather in sf now")]
    for event in app.stream({"messages": inputs}, thread, stream_mode="values"):
        event["messages"][-1].pretty_print()
    
    for event in app.stream(None, thread, stream_mode="values"):
        event["messages"][-1].pretty_print()


agent()
