from datetime import date, timedelta

from langchain.tools import StructuredTool

from app.agent.schema import AppointmentInput
from app.services.processing.calendar_manager import make_appointment  


# Función intermedia: recibe un input estructurado y delega la ejecución
def agenda_handler(nombre:str, apellido:str,
                    fecha:date, hora:str, servicio:str, duracion:timedelta = timedelta(minutes=30)) -> str:
    return make_appointment(
        nombre,
        apellido,
        fecha,
        hora,
        servicio,
        duracion
    )

# StructuredTool
calendar_tool = StructuredTool.from_function(
    func = agenda_handler,
    name="agendar_cita",
    description="""Agenda una cita médica en la clínica SOLO cuando el usuario lo solicite y te haya brindado los datos necesarios,
     especificando nombre, fecha, hora y tipo de servicio""",
    args_schema=AppointmentInput,
    return_direct=True
)