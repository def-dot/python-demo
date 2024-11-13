"""
自定义model：继承BaseChatModel
refer：https://python.langchain.com/docs/how_to/custom_chat_model/
"""
from collections.abc import Iterator
from typing import Any
from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import BaseMessage, AIMessage, AIMessageChunk, HumanMessage
from langchain_core.outputs import ChatGenerationChunk, ChatResult, ChatGeneration


# class CustomChatModel(BaseChatModel):
#     model_name: str
#     n: int

#     def _generate(self, messages: list[BaseMessage], stop: list[str] | None = None, run_manager: CallbackManagerForLLMRun | None = None, **kwargs: Any) -> ChatResult:
#         last_message = messages[-1]
#         tokens = last_message.content[:self.n]
#         message = AIMessage(
#             content=tokens,
#             additional_kwargs={},
#             response_metadata={
#                 "time_in_seconds": 3,
#             }
#         )
#         gen = ChatGeneration(message=message)
#         return ChatResult(generations=[gen])
    
#     def _stream(self, messages: list[BaseMessage], stop: list[str] | None = None, run_manager: CallbackManagerForLLMRun | None = None, **kwargs: Any) -> Iterator[ChatGenerationChunk]:
#         last_message = messages[-1]
#         tokens = last_message.content[:self.n]
#         for token in tokens:
#             chunk = ChatGenerationChunk(message=AIMessageChunk(content=token))
#             yield chunk

#         chunk = ChatGenerationChunk(message=AIMessageChunk(content="", response_metadata={"time_in_seconds": 3,}))
#         yield chunk
    
#     @property
#     def _llm_type(self):
#         return "custom_chat_model_type"
    
#     @property
#     def _identifying_params(self):
#         return {"model_name": self.model_name}



# model = CustomChatModel(model_name="custom_model", n=3)
# r = model.invoke(
#     [
#         HumanMessage(content="hello world"),
#     ]
# )
# print(r)
# print("----------")
# r = model.batch(["hello", "world"])
# print(r)
# print("------------")
# for chunk in model.stream("cat"):
#     print(chunk.content, end="|")


# from langchain.chat_models import BaseChatModel

class MyChatModel(BaseChatModel):
    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        message = AIMessage(content="Hello, world!")
        gen = ChatGeneration(message=message)
        return ChatResult(generations=[gen])
    
    @property
    def _llm_type(self):
        return "custom_chat_model_type"

chat_model = MyChatModel()
result = chat_model.generate(messages=[HumanMessage(content="Hello")])
print(result)
