from langchain.tools import StructuredTool

from app.agent.schema import RAGQuery
from app.services.processing.rag_manager import rag_manager


# Handler: recibe un input validado y pasa la consulta
def rag_handler(query:str) -> str:
    return rag_manager(query)


# StructuredTool para el agente
rag_tool = StructuredTool.from_function(
    func=rag_handler,
    name="Buscar_servicios",
    description="Realiza una búsqueda de información en una base vectorizada para responder consultas ",
    args_schema=RAGQuery,
    return_direct=False
)