from typing import TypedDict
from langgraph.graph import StateGraph, START, END

def input_output_state():
    class InputState(TypedDict):
        input: str


    class OutputState(TypedDict):
        output: str


    class AllState(TypedDict):
        input: str
        output: str


    def answer_node(state: InputState):
        return {"output": "this is answer", "input": state["input"]}


    builder = StateGraph(AllState, input=InputState, output=OutputState)

    builder.add_node(answer_node)
    builder.add_edge(START, "answer_node")
    builder.add_edge("answer_node", END)

    graph = builder.compile()

    r = graph.invoke({"input": "hi"})
    print(r)


def private_state():
    class AllState(TypedDict):
        a: str

    class PrivateState(TypedDict):
        private_data: str

    def node_1(state: AllState) -> PrivateState:
        output = {"private_data": "set by node_1"}
        print(f"Entered node `node_1`:\n\tInput: {state}.\n\tReturned: {output}")
        return output
    
    def node_2(state: PrivateState) -> AllState:
        output = {"a": "set by node_2"}
        print(f"Entered node `node_2`:\n\tInput: {state}.\n\tReturned: {output}")
        return output
    
    def node_3(state: AllState) -> AllState:
        output = {"a": "set by node_3"}
        print(f"Entered node `node_3`:\n\tInput: {state}.\n\tReturned: {output}")
        return output

    builder = StateGraph(AllState)
    builder.add_node(node_1)
    builder.add_node(node_2)
    builder.add_node(node_3)
    builder.add_edge(START, "node_1")
    builder.add_edge("node_1", "node_2")
    builder.add_edge(
        "node_2", "node_3"
    )
    builder.add_edge("node_3", END)
    graph = builder.compile()
    response = graph.invoke(
        {
            "a": "set at start",
        }
    )
    print(f"========== {response}")


private_state()