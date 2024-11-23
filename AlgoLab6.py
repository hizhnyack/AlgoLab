# Дана информация о времени заезда и отъезда посетителей отеля. Необходимо определить, в какой день посетителей в отеле единомоментно находилось больше всего.
# Пример входных данных (один элемент данного листа – кортеж, содержащий дату заезда и отъезда одного посетителя): [(“2024-09-15”, “2024-09-15”), (“2024-09-14”, “2024-09-21”)]

from datetime import datetime, timedelta


def max_guests_day(stays):
    events = []

    for check_in, check_out in stays:
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d") + timedelta(days=1)
        events.append((check_in_date, +1))
        events.append((check_out_date, -1))

    events.sort()

    current_guests = 0
    max_guests = 0
    max_guests_date = None

    for date, event in events:
        current_guests += event

        if current_guests > max_guests:
            max_guests = current_guests
            max_guests_date = date

    return max_guests_date.strftime("%Y-%m-%d"), max_guests


stays = [("2024-09-15", "2024-09-15"), ("2024-09-14", "2024-09-21"), ("2024-09-10", "2024-09-27"), ("2024-09-04", "2024-09-14")]
result_date, result_guests = max_guests_day(stays)
print(f"Больше за всех гостей было {result_date}, аж целых {result_guests} номеров.")