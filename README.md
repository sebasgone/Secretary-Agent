# Secretary-Agent 🤖💼

**Secretary-Agent** es un asistente conversacional construido con **LangChain 2024**, diseñado para:  
✅ Agendar citas médicas de forma inteligente.  
✅ Responder preguntas sobre los servicios de una clínica usando un motor de búsqueda con RAG (Retrieval-Augmented Generation).  

El proyecto está en desarrollo; el código fuente es funcional y puede probarse localmente ejecutando el archivo main.

---

## 🚀 Tecnologías principales

- **Python 3.10**
- **LangChain 0.3.25**
- **LangChain OpenAI**
- **LangChain Chroma**
- **ChromaDB** (almacenamiento vectorial)
- **SQLite3** (agendamiento de citas)
- **Pydantic** (validación de inputs)
- **OpenAI GPT-4o-mini** (LLM)

---

## ⚙ Instalación

1️⃣ Clona el repositorio:
```bash
git clone git@github.com:sebasgone/Secretary-Agent.git
cd Secretary-Agent
```

2️⃣ Crea un entorno virtual:
```bash
python3 -m venv env
source env/bin/activate
```

3️⃣ Instala las dependencias:
```bash
pip install -r requirements.txt
```

4️⃣ Configura tus variables de entorno en un archivo `.env`:
```
OPENAI_API_KEY=tu_clave_openai
VECTORSTORE_ADRS=./app/vectorstore
BASE_KNOWLEDGE_ADRS=./app/base_knowledge
```

---

## 🏗 Estructura principal

```
agent-secretary/
 ├── app/
 │    ├── agent/
 │    │     ├── agent_init.py        # Configuración del agente y executor
 │    │     └── tools/               # Herramientas: RAG y calendar_tool
 │    ├── core/
 │    │     └── config.py            # Configuración global y clientes
 │    ├── services/
 │    │     ├── processing/          # Lógica de procesamiento (RAG, calendar_manager)
 │    │     └── rag/                 # Motor de RAG
 │    └── vectorstore/               # Base vectorial (ignorada por Git)
 ├── main.py                         # Entrada principal
 ├── .gitignore                      # Archivos ignorados
 ├── requirements.txt                # Dependencias
 ├── calendar.db                     # DB de citas (ignorada en producción)
 └── .env                            # Variables de entorno (ignorada por Git)
```

---

## 💬 Uso

Lanza el agente:
```bash
python3 -m main
```

Interactúa en la terminal:
```
Asistente de la clínica BEL AIR
Escribe tu consulta (o 'salir' para terminar):

 Tú: Quisiera agendar una cita para dermatología mañana a las 10:00.
 Agente: Cita agendada para Sebastián el 2025-06-10 a las 10:00 para el servicio de dermatología.
```

---

## 📝 Funcionalidades

✅ **Agendamiento de citas**
- Valida nombre, fecha, hora, servicio y duración.
- Almacena en SQLite3 y verifica disponibilidad.

✅ **RAG tool**
- Responde consultas sobre servicios mediante búsqueda en vectorstore ChromaDB.

✅ **Logs**
- Toda interacción se registra en terminal para trazabilidad.

---

## 👨‍💻 Contribución

Pull requests y sugerencias son bienvenidas.  
Por favor, abre un issue para discutir un cambio importante antes de iniciarlo.

---

## ⚠ Notas
  
- El proyecto es de uso educativo y demostrativo.

---

## ✍️ Autor

Sebastián García Tolentino 

IA Developer

[Linkedin](https://www.linkedin.com/in/sebasgone21/)
