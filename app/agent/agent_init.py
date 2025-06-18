# app/agent/agent_init.py

import logging

from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate

from app.agent.tools.calendar_tool import calendar_tool
from app.agent.tools.rag_tool import rag_tool
from app.core.config import llms

# ── Logging ──
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(message)s")
log = logging.getLogger("agent")

# ── Herramientas ──
tools = [rag_tool, calendar_tool]

# ── Memoria de conversación ──
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# ── Prompt del agente ──
prompt = ChatPromptTemplate.from_messages([
    ("system",
     """ Eres el asistente virtual de la clínica BEL AIR. 
         Sigue las siguientes directrices para interactuar con el usuario:
         - 'rag_tool' contiene toda la información relacionada a servicios de la clínica.
         - Usa 'rag_tool' para responder preguntas sobre servicios de la clínica,
           dar recomendaciones a pedido del usuario, etc. 
         - Usa'calendar_tool' para agendar citas. Asegurate de obtener los datos necesarios
           para el agendamiento de la cita"""),
    ("placeholder", "{chat_history}"),
    ("placeholder", "{agent_scratchpad}"),
    ("user", "{input}")
])

# ── Agente con function-calling y herramientas ──
agent = create_openai_functions_agent(
    llm=llms.llm,
    tools=tools,
    prompt=prompt
)

# ── Executor final ──
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True
)
