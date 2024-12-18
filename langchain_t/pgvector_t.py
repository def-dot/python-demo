from langchain_postgres import PGVector
from langchain_mistralai import MistralAIEmbeddings
from langchain_core.documents import Document

import os
os.environ["MISTRAL_API_KEY"] = "SotgVGWqDkvz1qchuc6FNDmfzzWTlWFX"

embeddings = MistralAIEmbeddings(
    model="mistral-embed"
)

connection = "postgresql+psycopg://postgres:sj1107@192.168.9.209:5432/postgres"  # Uses psycopg3!
collection_name = "my_docs"

vector_store = PGVector(
    embeddings=embeddings,
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True,
)

def add_data():
    """插入向量数据"""
    docs = [
        Document(
            page_content="there are cats in the pond",
            metadata={"id": 1, "location": "pond", "topic": "animals"},
        ),
        Document(
            page_content="ducks are also found in the pond",
            metadata={"id": 2, "location": "pond", "topic": "animals"},
        ),
        Document(
            page_content="fresh apples are available at the market",
            metadata={"id": 3, "location": "market", "topic": "food"},
        ),
        Document(
            page_content="the market also sells fresh oranges",
            metadata={"id": 4, "location": "market", "topic": "food"},
        ),
        Document(
            page_content="the new art exhibit is fascinating",
            metadata={"id": 5, "location": "museum", "topic": "art"},
        ),
        Document(
            page_content="a sculpture exhibit is also at the museum",
            metadata={"id": 6, "location": "museum", "topic": "art"},
        ),
        Document(
            page_content="a new coffee shop opened on Main Street",
            metadata={"id": 7, "location": "Main Street", "topic": "food"},
        ),
        Document(
            page_content="the book club meets at the library",
            metadata={"id": 8, "location": "library", "topic": "reading"},
        ),
        Document(
            page_content="the library hosts a weekly story time for kids",
            metadata={"id": 9, "location": "library", "topic": "reading"},
        ),
        Document(
            page_content="a cooking class for beginners is offered at the community center",
            metadata={"id": 10, "location": "community center", "topic": "classes"},
        ),
    ]

    vector_store.add_documents(docs, ids=[doc.metadata["id"] for doc in docs])


def delete_data():
    """删除向量数据"""
    vector_store.delete(ids=["3"])


def find_data():
    r = vector_store.similarity_search(query="kitty", k=10, filter={"id": {"$in": [1, 5, 2, 9]}, "location": {"$in": ["pond", "market"]}})
    for i in r:
        print(i.page_content)


def find_data_retrive():
    retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 1})
    r = retriever.invoke("kitty")
    for i in r:
        print(i.page_content)


find_data_retrive()
