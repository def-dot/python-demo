from langchain_mistralai import MistralAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

import os
os.environ["MISTRAL_API_KEY"] = "SotgVGWqDkvz1qchuc6FNDmfzzWTlWFX"

embeddings = MistralAIEmbeddings(
    model="mistral-embed"
)

def embed_query():
    r = embeddings.embed_query("what is the meaning of life?")
    print(r[:5])


def embed_documents():
    r = embeddings.embed_documents(["what is the meaning of life?"])
    print(r)


def retrive_test():
    text = "Python is a popular language"
    vectorstore = InMemoryVectorStore.from_texts(texts=[text], embedding=embeddings)  # 文本转换为嵌入向量并存储
    retrive = vectorstore.as_retriever()  # 检索器 runnable
    r = retrive.invoke("what is python?")
    print(r)

retrive_test()
