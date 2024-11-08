from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage, HumanMessage

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

workflow = StateGraph(state_schema=MessagesState)
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)


def call_model(state: MessagesState):
    messages = state["messages"]
    r = model.invoke(messages)
    return {"messages": r}
    

mem = MemorySaver()
app = workflow.compile(checkpointer=mem)

output = app.invoke({"messages": HumanMessage("我是张三")})
print(output["messages"][-1])