"""
langchain tool的调用过程时，LLM绑定定义的tool，用户提问，LLM解析用户消息，返回解析后结果，包括适用的工具名称、参数。程序再调用对应的工具函数执行得到结果（这一步和LLM没有关系）
"""
from langchain_core.tools import tool
from pydantic import BaseModel, Field
import os
os.environ["MISTRAL_API_KEY"] = "SotgVGWqDkvz1qchuc6FNDmfzzWTlWFX"
from langchain_mistralai import ChatMistralAI
from typing_extensions import TypedDict, Annotated
from langchain.output_parsers import PydanticToolsParser

llm = ChatMistralAI(model="mistral-large-latest", temperature=0)

def tool_define():
    """python 定义工具执行函数"""
    @tool
    def add(a: int, b: int) -> int:
        """Adds a and b."""
        return a + b


    @tool
    def multiply(a: int, b: int) -> int:
        """Multiplies a and b."""
        return a * b

    tools = [add, multiply]

    return tools


def tool_pydantic():
    """使用pydantic定义工具的结构"""
    class add(BaseModel):
        a: int = Field(..., description="first argument")
        b: int = Field(..., description="second argument")

    class multiply(BaseModel):
        a: int = Field(..., description="first argument")
        b: int = Field(..., description="second argument")

    tools = [add, multiply]
    return tools


def tool_annotated():
    """
    使用附注说明工具的结构
    """
    class add(TypedDict):
        a: Annotated[int, ..., "first argument"]  # Annotated 作注解，没有实际用途
        b: Annotated[int, ..., "second argument"]
    
    class multiply(TypedDict):
        a: Annotated[int, ..., "first argument"]
        b: Annotated[int, ..., "second argument"]

    tools = [add, multiply]

    return tools


tools = tool_pydantic()
llm_with_tools = llm.bind_tools(tools)

from langchain_core.messages import HumanMessage

query = "What is 3 * 12? Also, what is 11 + 49?"

messages = [HumanMessage(query)]

chain = llm_with_tools | PydanticToolsParser(tools=tools)  # 支持PydanticToolsParser解析
ai_msg = chain.invoke(messages)  # AIMessage
print(ai_msg)
# print("===============")
# print(ai_msg.tool_calls)


# for i in ai_msg.tool_calls:  # list [dict]
#     if i["name"] == "add":
#         tool = add
#     elif i["name"] == "multiply":
#         tool = multiply

#     message = tool.invoke(i)  # ToolMessage
#     print(type(message))
#     print(message)
