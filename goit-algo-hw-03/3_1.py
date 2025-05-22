# Task 3.1.
# Calculates the number of days between a given date and the current date
from datetime import datetime, date


def get_days_from_today(date_str):
    """
    Розраховує кількість днів між заданою датою та поточною датою.

    Args:
        date_str (str): Рядок, що представляє дату у форматі 'РРРР-ММ-ДД'.

    Returns:
        int: Кількість днів від заданої дати до поточної.
    """
    try:
        given_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        current_date = date.today()
        days_past = (current_date - given_date).days
        return days_past
    except ValueError:
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."
    except TypeError:
        return "Неправильний тип даних. Введіть рядок"


# Приклад використання функції
date_string = '2014-03-20'
days_past = get_days_from_today(date_string)
print(f"Між заданою датою і поточною датою минуло днів: {days_past}")  # Виведеться різниця в днях

date_string = '2024.13.20'
days_past = get_days_from_today(date_string)
print(days_past)

date_string = 2024
days_past = get_days_from_today(date_string)
print(days_past)