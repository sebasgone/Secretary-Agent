import os

import chromadb
import openai
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Cargar variables de entorno

load_dotenv()

class routes:
    BASE_KNOWLEDGE_ADRS = os.getenv("BASE_KNOWLEDGE_ADRS")
    VECTORSTORE_ADRS = os.getenv("VECTORSTORE_ADRS")

class embedding_models:
    openai_embedding = OpenAIEmbeddings(
        openai_api_key = os.getenv("OPENAI_API_KEY"),
        model = "text-embedding-3-small"
    )

class vectorstores:
    embeddding_models=embedding_models()
    gen_vectorstore = Chroma(
    client=chromadb.PersistentClient(os.getenv("VECTORSTORE_ADRS")),
    embedding_function=embedding_models.openai_embedding
)

class clients:
    openai.api_key=os.getenv("OPENAI_API_KEY")

class llms:
    llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4o-mini", temperature=0)

routes = routes()
vectorstores = vectorstores()
clients = clients()
llms = llms()