from app.services.appointment.calendar_core import reserve_date


def make_appointment(name, last_name, date, time, service_taken, duration):
    return reserve_date(name,last_name, date, time, service_taken, duration)