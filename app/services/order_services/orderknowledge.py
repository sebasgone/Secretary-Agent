import json

from langchain.text_splitter import RecursiveJsonSplitter
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import Chroma

from app.core.config import routes, vectorstores


def order_knowledge ():

    loader = JSONLoader(
        file_path = routes.BASE_KNOWLEDGE_ADRS,
        jq_schema = ".",
        text_content = False,
    )

    docs = loader.load()

    json_objects = []
    for doc in docs:
        # Convertir el contenido del documento a un objeto JSON
        try:
            # Si el contenido ya es un diccionario
            if isinstance(doc.page_content, dict):
                json_objects.append(doc.page_content)
            # Si el contenido es un string JSON
            else:
                json_objects.append(json.loads(doc.page_content))
        except (json.JSONDecodeError, AttributeError):
            print(f"Error al procesar un documento: {doc.page_content[:100]}...")
            continue

    splitter=RecursiveJsonSplitter(
        max_chunk_size=500,
        min_chunk_size=250
    )

    splited_docs = splitter.create_documents(json_objects) 
    vectorstores.gen_vectorstore.add_documents(splited_docs)
    

