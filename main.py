from app.agent.agent_init import agent_executor
from app.services.appointment.calendar_core import init_db


def main():

    print("Asistente de la clínica BEL AIR")
    print("Escribe tu consulta (o 'salir' para terminar):")

    init_db()

    while True:
        user_input = input("\n Tú:")
        if user_input.strip().lower() in {"salir", "exit", "quit"}:
            print("Gracias por usar el asistente")
            break

        try:
            response = agent_executor.invoke(
                {"input": user_input},
                config={"configurable": {"session_id":"usuario_001"}}
            )
            
            print(f"\n Agente: {response['output']}")

        except Exception as e:
            print(f"\n Ocurrió un error:{e}")


if __name__ == "__main__":
    main()

