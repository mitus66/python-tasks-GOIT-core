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