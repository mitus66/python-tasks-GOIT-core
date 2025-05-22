import sys
from typing import List, Dict, Callable

def parse_log_line(line: str) -> Dict[str, str]:
    """Парсить рядок логу та повертає словник з його компонентами."""
    parts = line.split(' ', 2)
    if len(parts) == 3:
        timestamp, level, message = parts
        date = timestamp.split()[0]
        time = timestamp.split()[1]
        return {"date": date, "time": time, "level": level, "message": message.strip()}
    return {}

def load_logs(file_path: str) -> List[Dict[str, str]]:
    """Завантажує логи з файлу та парсить кожен рядок."""
    logs = []
    try:
        with open(file_path, 'r') as f:
            logs = list(filter(None, (parse_log_line(line.strip()) for line in f)))
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Помилка при читанні файлу '{file_path}': {e}")
    return logs

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """Фільтрує логи за вказаним рівнем."""
    return [log for log in logs if log.get("level", "").upper() == level.upper()]

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """Підраховує кількість записів для кожного рівня логування."""
    counts = {}
    log_levels = ["INFO", "ERROR", "DEBUG", "WARNING"]
    for level in log_levels:
        counts[level] = len(filter_logs_by_level(logs, level))
    return counts

def display_log_counts(counts: Dict[str, int]):
    """Форматує та виводить результати підрахунку логів."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16}| {count}")
    print("-" * 18)

def display_log_details(logs: List[Dict[str, str]], level: str):
    """Виводить деталі логів для вказаного рівня."""
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python script.py <шлях_до_лог_файлу> [рівень_фільтрації]")
        sys.exit(1)

    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)

    if not logs:
        sys.exit(1)

    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    if len(sys.argv) > 2:
        filter_level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, filter_level)
        if filtered_logs:
            display_log_details(filtered_logs, filter_level)
        else:
            print(f"\nНе знайдено записів для рівня '{filter_level.upper()}'.")
# *******************************************************************************
# import sys
# import os
# from collections import defaultdict
# from prettytable import PrettyTable
#
# # 1. Парсинг рядка логів
# def parse_log_line(line: str) -> dict:
#     parts = line.strip().split(' ', 3)  # дата, час, рівень, повідомлення
#     if len(parts) < 4:
#         return {}
#     return {
#         'date': parts[0],
#         'time': parts[1],
#         'level': parts[2].upper(),
#         'message': parts[3]
#     }
#
# # 2. Завантаження лог-файлу
# def load_logs(file_path: str) -> list:
#     logs = []
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             logs = [parse_log_line(line) for line in file if parse_log_line(line)]
#     except FileNotFoundError:
#         print(f"Файл не знайдено: {file_path}")
#         sys.exit(1)
#     except Exception as e:
#         print(f"Помилка при читанні файлу: {e}")
#         sys.exit(1)
#     return logs
#
# # 3. Фільтрація логів за рівнем
# def filter_logs_by_level(logs: list, level: str) -> list:
#     return list(filter(lambda log: log['level'] == level.upper(), logs))
#
# # 4. Підрахунок логів за рівнем
# def count_logs_by_level(logs: list) -> dict:
#     counts = defaultdict(int)
#     for log in logs:
#         counts[log['level']] += 1
#     return dict(counts)
#
# # 5. Виведення статистики
#
# def display_log_counts(counts: dict):
#     table = PrettyTable()
#     table.field_names = ["Рівень логування", "Кількість"]
#     for level in sorted(counts):
#         table.add_row([level, counts[level]])
#     print(table)
#
# # 6. Основна логіка
#
# def main():
#     if len(sys.argv) < 2:
#         print("Використання: python main.py <шлях_до_файлу> [рівень_логування]")
#         sys.exit(1)
#
#     file_path = sys.argv[1]
#     level_filter = sys.argv[2] if len(sys.argv) > 2 else None
#
#     logs = load_logs(file_path)
#     counts = count_logs_by_level(logs)
#     display_log_counts(counts)
#
#     if level_filter:
#         filtered = filter_logs_by_level(logs, level_filter)
#         if filtered:
#             print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
#             for log in filtered:
#                 print(f"{log['date']} {log['time']} - {log['message']}")
#         else:
#             print(f"\nЖодного запису для рівня '{level_filter.upper()}' не знайдено.")
#
# if __name__ == '__main__':
#     main()
