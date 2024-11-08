from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage, HumanMessage


parser = StrOutputParser()

model = OllamaLLM(model="qwen2.5:7b")

chain = model | parser

r = chain.invoke([
    HumanMessage(content="我是张三"),
    AIMessage(content="你好，张三"),
    HumanMessage(content="我是谁？"),
])
print(r)