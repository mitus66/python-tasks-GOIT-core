import re
from typing import Callable, Generator

# Аналізує текст та повертає генератор дійсних чисел (доходів), які чітко відокремлені пробілами.
# INPUT text: рядок для аналізу
# OUTPUT yields: дійсне число, знайдене у тексті
def generator_numbers(text: str) -> Generator[float, None, None]:
    # Варіант 1 - регулярний вираз фільтрує числа
    # pattern = r"\s(-?\d+\.?\d*)\s"
    pattern = r"(?<= )(-?\d+\.?\d*)(?= )" # or simply r" \d+\.\d+ "
    matches = re.findall(pattern, text)
    # генеруємо числа зі знайдених патернів
    for match in matches:
        try:
            yield float(match)
        except ValueError:
            # ця помилка малоймовірна, оскільки регулярний вираз вже фільтрує числа
            print(f"Увага: знайдено недійсне число: '{match}'")
    # # Варіант 2 - без використання регулярних виразів
    # parts = text.split()[1:-1] # не треба брати перше і останнє "слово"
    # for part in parts:
    #     try:
    #         yield float(part)
    #     except ValueError:
    #         # Якщо частина не є дійсним числом, ігноруємо її
    #         pass

# # Перевірка роботи генератора
# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,
#         доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# gen = generator_numbers(text)
#
# print(next(gen)) # 1000.01
# print(next(gen)) # 27.45
# print(next(gen)) # 324.0


# Використовує генератор generator_numbers для обчислення загальної суми чисел у вхідному рядку
# та приймає його як аргумент при виклику
# INPUT text: рядок, що містить числа.
#       func: функція-генератор, яка приймає рядок і повертає генератор чисел.
# OUTPUT загальна сума дійсних чисел у тексті
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    total_profit = 0.0
    # складаємо усі згенеровані числа з тексту
    for number in func(text):
        total_profit += number
    # повертаємо загальний дохід з округленням до другого знаку після крапки
    return round(total_profit, 2)

# Приклад використання:
# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}") # Загальний дохід: 1351.46

text = "5000 Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів. 70"
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}") # Загальний дохід: 1351.46
#
# text_with_negatives = "Доходи склали 500.50, витрати - -120.75, ще дохід 30.20."
# total_result = sum_profit(text_with_negatives, generator_numbers)
# print(f"Загальний результат: {total_result}")
#
# text_without_numbers = "У цьому тексті немає жодних чисел."
# total_zero = sum_profit(text_without_numbers, generator_numbers)
# print(f"Загальний дохід (без чисел): {total_zero}")
#
# text_with_mixed = "Текст з числами 123 45.6 -7.89 та словами."
# total_mixed = sum_profit(text_with_mixed, generator_numbers_no_regex)
# print(f"Загальна сума (з мішаним текстом): {total_mixed}")
#
# text_with_non_separated = "Текст з 123.45слово56.78."
# total_non_separated = sum_profit(text_with_non_separated, generator_numbers_no_regex)
# print(f"Загальна сума (без чіткого розділення): {total_non_separated}")