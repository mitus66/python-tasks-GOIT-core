from pathlib import Path

file_name = 'cats.txt'
file_path = Path(file_name)

# input - path 2 file
# output - list with dictionary with keys: "id", "name", "age"
def get_cats_info(path: Path):
    cats_list = []
    try:
        # read file
        with open(path, 'r', encoding='utf-8') as file:
            # read file by lines
            for line in file:
                # split id, name, age
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:
                    cat_id, cat_name, cat_age = cat_data
                    # add list 2 dictionary
                    cats_list.append({"id": cat_id, "name": cat_name, "age": cat_age})
                elif cat_data:  # check empty str after split
                    print(f"Увага: некоректний формат рядка: '{line.strip()}', очікується 'id,name,age'.")
    # catch exceptions
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
    except Exception as e:
        print(f"Помилка при читанні файлу '{path}': {e}")

    return cats_list


cats_info = get_cats_info(file_path)
print(cats_info)
