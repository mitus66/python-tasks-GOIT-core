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

# _________________________________________________
# Task 3.2.
# Generates a set of unique random numbers within the specified parameters
import random

def get_numbers_ticket(min_num, max_num, quantity):
    """
    Генерує випадковий набір унікальних чисел для лотереї.

    Args:
        min_num (int): Мінімальне можливе число у наборі (не менше 1).
        max_num (int): Максимальне можливе число у наборі (не більше 1000).
        quantity (int): Кількість чисел, які потрібно вибрати (значення між min та max).

    Returns:
        list: Відсортований список випадково вибраних унікальних чисел.
              Повертає пустий список, якщо параметри не відповідають заданим обмеженням.
    """

    if not isinstance(min_num, int) or not isinstance(max_num, int) or not isinstance(quantity, int):
        return []

    if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > (max_num - min_num + 1):
        return []

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min_num, max_num))

    return sorted(list(numbers))

# Приклад використання функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers)

# _________________________________________________
# Task 3.3.
# Normalizes phone numbers to a standard format
import re


def normalize_phone(phone_number: str) -> str:
    # Видаляємо всі зайві символи, залишаючи лише цифри та знак "+" на початку
    phone_number = re.sub(r'[^\d+]', '', phone_number.strip())

    # Якщо номер вже починається з "+", перевіряємо його коректність
    if phone_number.startswith('+'):
        if phone_number.startswith('+380'):
            return phone_number  # Номер уже у вірному форматі
        else:
            return '+38' + phone_number[1:]  # Додаємо код України, якщо інший міжнародний код

    # Якщо номер починається з "380", просто додаємо знак "+" на початку
    if phone_number.startswith('380'):
        return '+' + phone_number

    # Якщо номер не містить коду країни, додаємо "+38" на початок
    return '+38' + phone_number


# Приклад використання
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    " +38(050)123-32-34",
    " 0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11 ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

# _________________________________________________
# Task 3.4.
# Displays a list of colleagues whose birthdays need to be celebrated one week in advance

from datetime import datetime, date, timedelta


def string_to_date(date_str):
    return datetime.strptime(date_str, "%Y.%m.%d").date()


def date_to_string(date_obj):
    return date_obj.strftime("%Y.%m.%d")


def find_next_weekday(start_date, weekday):
    days_ahead = (weekday - start_date.weekday() + 7) % 7
    return start_date + timedelta(days=days_ahead or 7)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:  # Saturday or Sunday
        return find_next_weekday(birthday, 0)  # Move to Monday
    return birthday


def prepare_user_list(users):
    prepared_users = []
    for user in users:
        birth_date = string_to_date(user["birthday"])
        prepared_users.append({"name": user["name"], "birthday": birth_date})
    return prepared_users


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_difference = (birthday_this_year - today).days
        if 0 <= days_difference <= days:
            congratulation_date = adjust_for_weekend(birthday_this_year)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": date_to_string(congratulation_date)
            })

    return upcoming_birthdays


# Приклад використання
users = [
    {"name": "Bill Gates", "birthday": "1955.4.8"},
    {"name": "Steve Jobs", "birthday": "1955.4.9"},
    {"name": "Jinny Lee", "birthday": "1956.4.6"},
    {"name": "Sarah Lee", "birthday": "1957.4.10"},
    {"name": "Jonny Lee", "birthday": "1958.4.11"},
    {"name": "John Doe", "birthday": "1985.04.23"},
    {"name": "Jane Smith", "birthday": "1990.04.27"}
]

prepared_users = prepare_user_list(users)
print(get_upcoming_birthdays(prepared_users, 7))