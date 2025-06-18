from datetime import date, timedelta

from pydantic import BaseModel, Field


# Input para la herramienta RAG
class RAGQuery(BaseModel):
    query: str = Field(description="Consulta del usuario sobre los servicios de la clínica y su caso en particular.")

# Input para la herramienta de agendamiento de citas
class AppointmentInput(BaseModel):
    nombre: str = Field( description="Nombre del paciente que solicita la cita.")
    apellido: str = Field( description="Apellido del paciente que solicita la cita.")   
    fecha: date = Field(description="Fecha solicitada para la cita.")
    hora: str = Field(description="Hora deseada en formato HH:MM.")
    duracion: timedelta = Field(default=timedelta(minutes=30), description="Duración de la cita")
    servicio: str = Field(description="Servicio médico requerido (ej. rinoplastía).")
