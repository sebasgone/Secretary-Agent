import openai
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

from app.core.config import clients, llms, vectorstores


def interpreter(input):
    """
    Función para interpretar el mensaje del usuario y generar prompts:
    """
    role ="""Transforma la pregunta del usuario en una consulta optimizada para búsqueda vectorial.
        La consulta debe:
        1. Incluir los términos clave relevantes
        2. Eliminar palabras irrelevantes
        3. Ser concisa y directa
        4. Mantener los conceptos principales
    """
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": input}
        ]
    )

    # Extraer y mostrar la respuesta
    normalized_prompt=response.choices[0].message.content
    print(normalized_prompt)
    
    return normalized_prompt

def rag_bot():
    """
    Función que define una chain retrieval para respuestas en base a un vectorstore
    """
    system_message = """Eres un asistente conversacional cuya tarea es la de agendar citas para una la clínica Bel AIR,
    una clínica de cirugía plástica.

    Tu objetivo es responder consultas y brindar información según las peticiones del usuario. 

    Directrices:
    - En la sección de contexto encontrarás los chunks más relevantes ya reconstruidos en base a la consulta del usuario.
    - La información dentro de contexto incluye los servicios de la clínica con detalles.
    - Interpreta el deseo del usuario junto con los documentos para generar una respuesta precisa siempre responde los datos más relevantes que tengas.
    - Si la intención del usuario no tiene nada que ver con la propiedad responde que no puedes ayudarlo.
    
    Contexto: {context}
    """

    # Definir el prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("human", "{original_question}")
    ])

    # Crear la cadena de recuperación
    retriever = vectorstores.gen_vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 10, "fetch_k": 20, "lambda_mult": 0.5}
    )
  
    bot = (
        RunnablePassthrough() 
        | (lambda x: {
            "optimized_query": interpreter(x),
            "original_question": x
        })
        |{
            "context": lambda x: "\n\n".join(d.page_content for d in retriever.invoke(x["optimized_query"])),
            "original_question": lambda x: x["original_question"]
        }
        | prompt
        | llms.llm
        )
    
    return bot






