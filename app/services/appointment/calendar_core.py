import sqlite3
from datetime import date, datetime, time, timedelta


# Inicialización del calendario (solo una vez)
def init_db():
    conn = sqlite3.connect("calendar.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        service_taken TEXT NOT NULL,
        duracion INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def reserve_date(name: str, last_name: str, date_: date, time_: str, service_taken: str, duration: timedelta) -> str:
    conn = sqlite3.connect("calendar.db")
    cursor = conn.cursor()

    # Validación defensiva
    if isinstance(time_, str):
        time_parsed = datetime.strptime(time_, "%H:%M").time()
    else:
        time_parsed = time_

    if isinstance(duration, timedelta):
        duration_minutes = int(duration.total_seconds() // 60)
    else:
        duration_minutes = duration  # asumes que ya es int

    # Verificar si ya existe
    cursor.execute("""
        SELECT * FROM appointments
        WHERE date = ? AND time = ?
    """, (date_.isoformat(), time_parsed.strftime("%H:%M")))

    if cursor.fetchone():
        conn.close()
        return f"Ya existe una cita agendada para {date_} a las {time_}."

    # Insertar nueva cita
    cursor.execute("""
        INSERT INTO appointments (name, last_name, date, time, service_taken, duracion)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, last_name, date_.isoformat(), time_parsed.strftime("%H:%M"), service_taken, duration_minutes))

    conn.commit()
    conn.close()

    return f"Cita agendada para {name} el {date_} a las {time_} para el servicio de {service_taken}."