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