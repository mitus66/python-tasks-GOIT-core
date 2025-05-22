from collections import UserDict

# Базовий клас для полів запису
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Клас для зберігання імені контакту. Обов'язкове поле
class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        # Додано перевірку на порожнє ім'я
        if not value:
            raise ValueError("Name cannot be empty")
        self.value = value

# Клас для зберігання номера телефону. Має валідацію формату (10 цифр)
class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

        # Валідація номера телефону: має бути 10 цифр
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain 10 digits")
        self.value = value

# Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів
class Record:
    def __init__(self, name):
        self.name = Name(name)  # Зберігання об'єкта Name
        self.phones = []  # Зберігання списку об'єктів Phone

    def add_phone(self, phone):
        # Додає телефон до списку телефонів запису.
        self.phones.append(Phone(phone))  # Додавання об'єкта Phone

    def remove_phone(self, phone):
        # Видаляє телефон зі списку телефонів запису.
        p = self.find_phone(phone)
        if p:
            self.phones.remove(p)
        else:
            raise ValueError(f"Phone number {phone} not found")

    def edit_phone(self, old_phone, new_phone):
        # Редагує телефон у списку телефонів запису.
        p = self.find_phone(old_phone)
        if p:
            try:
                p.value = Phone(new_phone).value # Валідація нового номера
            except ValueError:
                raise ValueError(f"Invalid new phone number {new_phone}")
        else:
            raise ValueError(f"Phone number {old_phone} not found")

    def find_phone(self, phone):
        # Шукає телефон у списку телефонів запису.
        for p in self.phones:
            if p.value == phone:
                return p  # Повертає об'єкт Phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# Клас для зберігання та управління записами
class AddressBook(UserDict):
    def add_record(self, record):
        # Додає запис до адресної книги.
        self.data[record.name.value] = record  # Ключ - ім'я контакту

    def find(self, name):
        # Знаходить запис за ім'ям.
        return self.data.get(name)  # Повертає об'єкт Record або None

    def delete(self, name):
        # Видаляє запис за ім'ям.
        if name in self.data:
            del self.data[name]

    def __str__(self):
        # Повертає рядкове представлення адресної книги.
        return "\n".join(str(record) for record in self.data.values())


# Приклад використання
if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    print(book)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    # Видалення запису Jane
    book.delete("Jane")
    print(book)

    # Додаткові тести
    try:
        john.edit_phone("1112223333", "invalid_phone")  # Виклик помилки валідації
    except ValueError as e:
        print(e)

    try:
        john.remove_phone("non_existent_phone")
    except ValueError as e:
        print(e)
