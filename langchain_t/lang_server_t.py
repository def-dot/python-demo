from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
from langsmith import traceable

parser = StrOutputParser()

template = """问题: {question}"""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="qwen2.5:7b")

chain = prompt | model | parser

# 5. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 6. Adding chain route
add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
