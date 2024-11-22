from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage

import os

os.environ["DASHSCOPE_API_KEY"] = "sk-04097ca9e2e44c4492784fa77f7e0d4a"

llm = ChatTongyi(
    streaming=True,
)
res = llm.invoke([HumanMessage(content="hi")])
print(res)