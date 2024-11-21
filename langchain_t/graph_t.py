from langgraph.graph import StateGraph, START, END
from typing import Any, TypedDict, Annotated
import operator


class State(TypedDict):
    data: Annotated[list, operator.add]
    cond: str


class NodeValue:
    def __init__(self, val) -> None:
        self._val = val

    def __call__(self, state: State) -> Any:
        print(f"adding {self._val} to {state["data"]}")
        return {"data": [self._val]}

builder = StateGraph(State)

def parallel():
    builder.add_node("a", NodeValue("I'm A"))
    builder.add_edge(START, "a")
    builder.add_node("b", NodeValue("I'm B"))
    builder.add_node("b2", NodeValue("I'm B2"))
    builder.add_node("c", NodeValue("I'm C"))
    builder.add_node("d", NodeValue("I'm D"))
    builder.add_edge("a", "b")
    builder.add_edge("a", "c")
    builder.add_edge("b", "b2")
    builder.add_edge(["b2", "c"], "d")
    builder.add_edge("d", END)


def condition():
    """
    根据条件选择
    """
    builder.add_node("a", NodeValue("I'm A"))
    builder.add_edge(START, "a")
    builder.add_node("b", NodeValue("I'm B"))
    builder.add_node("c", NodeValue("I'm C"))
    builder.add_node("d", NodeValue("I'm D"))
    builder.add_node("e", NodeValue("I'm E"))

    def route(state: State):
        if state["cond"] == "bc":
            return ["b", "c"]
        else:
            return ["c", "d"]

    choices = ["b", "c", "d"]
    builder.add_conditional_edges("a", route, choices)

    for i in choices:
        builder.add_edge(i, "e")
  
    builder.add_edge("e", END)

condition()
graph = builder.compile()

img_data = graph.get_graph().draw_mermaid_png()
with open('graph_image.png', 'wb') as f:
    f.write(img_data)

graph.invoke({"data": [], "cond": "cd"}, {"configurable": {"thread_id": "foo"}})
