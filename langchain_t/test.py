from langchain_ollama.llms import OllamaLLM
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from typing_extensions import Annotated, TypedDict
from typing import Sequence

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    language: str


prompt = ChatPromptTemplate.from_messages([
    ("system", "尽可能简短回答，用{language}"),
    MessagesPlaceholder(variable_name="messages")
])

model = OllamaLLM(model="qwen2.5:7b")


def call_model(state: State):
    chain = prompt | model
    r = chain.invoke(state)
    return {"messages": r}
    
workflow = StateGraph(state_schema=State)
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

mem = MemorySaver()
app = workflow.compile(checkpointer=mem)

config = {"configurable": {"thread_id": "zhangsan"}}

input_messages = [HumanMessage("讲一个笑话，200字内")]
for chunk, metadata in app.stream({"messages": input_messages, "language": "英文"}, config, stream_mode="messages"):
    if isinstance(chunk, AIMessage):
        print(chunk.content, end="|")

# output = app.invoke({"messages": HumanMessage("讲一个笑话，200字内"), "language": "英文"}, config)
# output["messages"][-1].pretty_print()

# output = app.invoke({"messages": HumanMessage("我是谁？")}, config)
# output["messages"][-1].pretty_print()
