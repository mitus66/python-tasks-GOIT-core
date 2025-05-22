from pathlib import Path

file_name = 'salary.txt'
file_path = Path(file_name)

# input - Path to file
# output - tuple with total and average salary
def total_salary(path: Path):
    total_salary_sum = 0
    developer_count = 0
    try:
        # read file
        with open(path, 'r', encoding='utf-8') as file:
            # read file by lines
            for line in file:
                try:
                    # split name and salary
                    name, salary_str = line.strip().split(',')
                    # convert str 2 int
                    salary = int(salary_str)
                    # get total salary with iteration
                    total_salary_sum += salary
                    # get total developers with iteration
                    developer_count += 1
                # catch exceptions
                except ValueError:
                    print(f"Увага: некоректний формат рядка: '{line.strip()}'. Пропущено.")
                except Exception as e:
                    print(f"Увага: помилка при обробці рядка '{line.strip()}': {e}")
        # avoid on zero division
        if developer_count > 0:
            average = total_salary_sum / developer_count
            return total_salary_sum, average
        else:
            return 0, 0
    # catch exceptions
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Помилка при читанні файлу '{path}': {e}")
        return 0, 0

# result = total_salary(file_path)
# result_type = type(result)

# print(result) # (6000, 2000.0)
# print(result_type) # <class 'tuple'>

total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
