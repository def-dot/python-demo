"""
langchain中可运行的对象（可以组合到链条中的对象），如Prompt，LLM，OutputParser等。
包括输入和输出参数，通过invoke、batch、stream等方法运行。
"""

from langchain.prompts import ChatPromptTemplate


template = """问题: {question}"""

prompt = ChatPromptTemplate.from_template(template)

print(ChatPromptTemplate.__dict__.keys())

# import inspect
# print(inspect.getsource(ChatPromptTemplate.__repr_str__))