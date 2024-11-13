from typing import Any, Dict, List

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import BaseMessage
from langchain_core.outputs import LLMResult
from langchain_core.prompts import ChatPromptTemplate


class LoggingHandler(BaseCallbackHandler):
    def on_llm_end(self, response: LLMResult, **kwargs) -> None:
        print("on_llm_end--------------")
        print(f"on_llm_end, response: {response}")

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs
    ) -> None:
        print(f"on_chain_start--------------inputs {inputs} ")

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs) -> None:
        print("on_chain_end--------------")
        print(f"on_chain_end, outputs: {outputs}")


from langchain_mistralai import ChatMistralAI
import os
os.environ["MISTRAL_API_KEY"] = "SotgVGWqDkvz1qchuc6FNDmfzzWTlWFX"
llm = ChatMistralAI(model="mistral-large-latest", temperature=0)

callbacks = [LoggingHandler()]
prompt = ChatPromptTemplate.from_template("What is 1 + {number}?")

chain = prompt | llm

chain.invoke({"number": "2"}, config={"callbacks": callbacks})
