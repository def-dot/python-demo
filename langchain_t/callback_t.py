import asyncio
from langchain.prompts import PromptTemplate
from langchain_core.callbacks import CallbackManager, BaseCallback

from langchain_mistralai import ChatMistralAI
import os
os.environ["MISTRAL_API_KEY"] = "SotgVGWqDkvz1qchuc6FNDmfzzWTlWFX"
llm = ChatMistralAI(model="mistral-large-latest", temperature=0)

prompt = PromptTemplate(input_variables=["question"], template="What is the answer to the following question: {question}?")
chain = prompt | llm

class MyCallback(BaseCallback):
    def on_llm_start(self, prompt: str, llm, **kwargs):
        print(f"开始生成，输入提示：{prompt}")

    def on_llm_new_token(self, token: str, **kwargs):
        print(f"生成新 token：{token}")

    def on_llm_end(self, response: str, **kwargs):
        print(f"任务完成，最终结果：{response}")
callback = CallbackManager([MyCallback()])


async def llm_tasks():
    tasks = []
    questions = ["What is python?", "python is popular or not?", "you like python or not?"]
    for i in questions:
        inputs = {"question": i}
        task = asyncio.create_task(chain.invoke(inputs, run_manager=callback))
        tasks.append(task)
    
    r = await asyncio.gather(*tasks)
    return r


asyncio.run(llm_tasks())
