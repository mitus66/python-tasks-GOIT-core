'''
Часто для роботи потрібно створити об'єкти, які поводяться як стандартні контейнери Python, але з модифікованою поведінкою.
Ви, звичайно, можете спробувати успадкувати dict, str, list, але це може призвести до ряду непередбачених помилок.
Правильний спосіб отримати модифікований контейнер — це використовувати пакет collections та класи UserList, UserDict,
UserString, які в ньому є.
Всі ці класи поводяться точно як вбудовані контейнери з тією лише відмінністю, що самі дані лежать у полі data у цих
класів і ви можете використовувати це поле на свій розсуд.

from collections import UserDict

class ValueSearchableDict(UserDict):
    def has_in_values(self, value):
        return value in self.data.values()

as_dict = ValueSearchableDict()
as_dict['a'] = 1
as_dict.has_in_values(1)  # True
as_dict.has_in_values(2)  # False

У цьому прикладі ми створили клас, який поводиться як словник, але в ньому є додатковий метод, який перевіряє наявність
деякого value серед значень у цьому словнику.

from collections import UserList

class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))

countable = CountableList([1, '2', 3, '4'])
countable.append('5')
countable.sum()  # 15

У цьому прикладі ми створили клас, який поводиться як список, але в ньому є метод sum, який повертає суму всього вмісту
цього класу, при цьому перетворюючи рядки на цілі числа.

from collections import UserString

class TruncatedString(UserString):
    MAX_LEN = 7

    def truncate(self):
        self.data = self.data[:self.MAX_LEN]

ts = TruncatedString('abcdefghjklmnop')
ts.truncate()
print(ts)  # abcdefg

Останній приклад показує модифікований рядок з методом truncate, який обмежує розмір рядка до MAX_LEN символів.

Task 9. У четвертому модулі ми реалізували функцію lookup_key для пошуку всіх ключів за значенням у словнику. Першим
параметром у функцію ми передавали словник, а другим – значення, яке хотіли знайти. Результатом був список ключів або
порожній список, якщо ми нічого не знаходили.

def lookup_key(data, value):
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)
    return keys
Створіть клас LookUpKeyDict, батьком якого буде клас UserDict. Зробіть функцію lookup_key методом класу LookUpKeyDict.
'''

# from collections import UserDict
#
#
# class LookUpKeyDict(UserDict):
#     def lookup_key(self, value):
#         keys = []
#         for key in self.data:
#             if self.data[key] == value:
#                 keys.append(key)
#         return keys
#
# # Приклад використання:
# my_dict = LookUpKeyDict({'a': 1, 'b': 2, 'c': 1, 'd': 3})
#
# # Пошук ключів зі значенням 1
# keys_with_value_1 = my_dict.lookup_key(1)
# print(f"Ключі зі значенням 1: {keys_with_value_1}")
#
# # Пошук ключів зі значенням 2
# keys_with_value_2 = my_dict.lookup_key(2)
# print(f"Ключі зі значенням 2: {keys_with_value_2}")
#
# # Пошук ключів зі значенням, якого немає у словнику
# keys_with_value_4 = my_dict.lookup_key(4)
# print(f"Ключі зі значенням 4: {keys_with_value_4}")

'''
Task 10. Перепишемо завдання розрахунку заборгованостей з комунальних послуг за допомогою класу UserList.
payment = [1, -3, 4]

def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum
Нагадаємо умову. У нас є список показань заборгованостей з комунальних послуг наприкінці місяця, список payment. Заборгованості можуть бути від'ємними — у нас переплата, або додатними, якщо потрібно сплатити за рахунками.
Створіть клас AmountPaymentList, успадковуйте його від класу UserList. Зробіть функцію amount_payment методом класу AmountPaymentList.
'''

# from collections import UserList
#
#
# class AmountPaymentList(UserList):
#     def amount_payment(self):
#         total_sum = 0
#         for value in self:
#             if value > 0:
#                 total_sum += value
#         return total_sum

'''
Task 11. Створіть клас NumberString, успадкуйте його від класу UserString, визначте для нього метод number_count(self), який буде рахувати кількість цифр у рядку.
'''

# from collections import UserString
#
#
# class NumberString(UserString):
#     def number_count(self):
#         count = 0
#         for char in self.data:
#             if char.isdigit():
#                 count += 1
#         return count

'''
У Python широко використовується механізм виключень (Exceptions) для того, щоб дати зрозуміти зухвалому коду, що саме пішло не так і що з цим робити. На виключеннях у тому числі будують розгалуження коду, наприклад ми очікуємо, що користувач введе саме число, але він може ввести що завгодно:

def input_number():
    while True:
        try:
            num = input("Enter integer number: ")
            return int(num)
        except:
            print(f'"{num}" is not a number. Try again')


num = input_number()
У цьому прикладі функція input_number вийде з нескінченного циклу тільки, коли користувач введе ціле число. Це приклад використання винятків у Python з метою управління потоком виконання.

Коли ж ви пишете свою програму, вам може знадобитися створити свої власні винятки, щоб обробляти їх на вищому рівні. Наприклад, ви очікуєте, що користувач повинен ввести ім'я, і це ім'я не повинно бути коротшим трьох символів і починатися з великої літери. Ви можете створити власний виняток, який буде викликатися, якщо введення користувача не пройшло цю перевірку. Тоді будь-який код, який викликатиме цю функцію, зможе коректно обробити цей конкретний випадок.

import string


class NameTooShortError(Exception):
    pass


class NameStartsFromLowError(Exception):
    pass


def enter_name():
    name = input("Enter name: ")
    if len(name) < 3:
        raise NameTooShortError
    if name[0] not in string.ascii_uppercase:
        raise NameStartsFromLowError


while True:
    try:
        name = enter_name()
        break
    except NameTooShortError:
        print('Name is too short, need more than 3 symbols. Try again.')
    except NameStartsFromLowError:
        print('Name should start from capital letter. Try again.')
У цьому прикладі ми створили власні винятки, успадковуючи батьківський клас для всіх винятків у Python — клас Exception. Далі у коді коректно обробили два випадки, коли користувач ввів занадто коротке ім'я, або коли ім'я починається не з великої літери.

Task 12. Створіть клас IDException, який успадковуватиме клас Exception.
Також реалізуйте функцію add_id(id_list, employee_id), яка додає до списку id_list ідентифікатор користувача employee_id та повертає вказаний оновлений список id_list.
Функція add_id буде викликати власне виключення IDException, якщо employee_id не починається з '01', інакше employee_id буде додано до списку id_list.
'''

# class IDException(Exception):
#     pass
#
#
# def add_id(id_list, employee_id):
#     if not employee_id.startswith("01"):
#         raise IDException(f"ID працівника {employee_id} повинен починатися з '01'")
#     id_list.append(employee_id)
#     return id_list

'''
Task 14. Реалізуйте клас Contacts, який працюватиме з контактами. На першому етапі ми додамо два методи.
list_contacts повертає список контактів це змінна contacts з поточного екземпляра класу
add_contacts додає новий контакт до списку, який є змінною об'єкту - contacts
Клас Contacts містить змінну класу current_id. Ми будемо використовувати її при додаванні нового контакту як унікального ідентифікатора контакту. Коли ми додаємо новий контакт, то передаємо такі аргументи в метод add_contacts: name, phone, email та favorite. Метод повинен створити словник із зазначеними ключами та значеннями параметрів функції. Також необхідно додати до словника новий ключ id, значенням якого є значення змінної класу current_id.

Приклад отриманого словника:

    {
    "id": 1,
    "name": "Wylie Pope",
    "phone": "(692) 802-2949",
    "email": "est@utquamvel.net",
    "favorite": True,
}
Вказаний словник ми додаємо до списку contacts. Не забуваймо збільшувати змінну current_id на одиницю після кожного виклику методу add_contacts для збереження унікальності ключа id для словника.
Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді.
'''

# class Contacts:
#     current_id = 1
#
#     def __init__(self):
#         self.contacts = []
#
#     def list_contacts(self):
#         return self.contacts
#
#     def add_contacts(self, name, phone, email, favorite):
#         contact = {
#             "id": Contacts.current_id,
#             "name": name,
#             "phone": phone,
#             "email": email,
#             "favorite": favorite,
#         }
#         self.contacts.append(contact)
#         Contacts.current_id += 1

'''
Task 15. Продовжуємо розширювати функціональність класу Contacts. На цьому етапі ми додамо до класу метод get_contact_by_id. Метод повинен шукати контакт по унікальному id у списку contacts та повертати словник з нього із зазначеним ключем id. Якщо словника із зазначеним id у списку contacts не знайдено, метод повертає None.
Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді.
'''

# class Contacts:
#     current_id = 1
#
#     def __init__(self):
#         self.contacts = []
#
#     def list_contacts(self):
#         return self.contacts
#
#     def add_contacts(self, name, phone, email, favorite):
#         self.contacts.append(
#             {
#                 "id": Contacts.current_id,
#                 "name": name,
#                 "phone": phone,
#                 "email": email,
#                 "favorite": favorite,
#             }
#         )
#         Contacts.current_id += 1
#
#     def get_contact_by_id(self, id):
#         for contact in self.contacts:
#             if contact["id"] == id:
#                 return contact
#         return None

'''
Task 16. Завершуємо функціональність класу Contacts. На цьому етапі ми додамо до класу метод remove_contacts. Метод винен видаляти контакт по унікальному id у списку contacts. Якщо словника із зазначеним id у списку contacts не знайдено, метод жодних дій над списком contacts не робить.
Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді.
'''

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        for contact in self.contacts:
            if contact["id"] == id:
                self.contacts.remove(contact)
                return