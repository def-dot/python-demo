import os
from langchain_core.tools import tool
from langchain_anthropic import ChatAnthropic

os.environ["ANTHROPIC_API_KEY"] = "sk-ant-api03-mrmRzF-1x397AtlRNiur-PEQ7TlpAf3HxY4YQXeyvfB1p642QIAiMYN4Qwv98mKPCJOhA-ZvoYKgAA"
llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

@tool
def add(a: int, b: int) -> int:
    """Adds a and b."""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b."""
    return a * b


tools = [add, multiply]

llm_with_tools = llm.bind_tools(tools)


from langchain_core.messages import HumanMessage

query = "What is 3 * 12? Also, what is 11 + 49?"

messages = [HumanMessage(query)]

ai_msg = llm_with_tools.invoke(messages)

print(ai_msg.tool_calls)

# messages.append(ai_msg)