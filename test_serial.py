'''
Для серіалізації/десеріалізації об'єктів Python, коли важлива швидкість, коректність і невеликий розмір пам'яті, що використовується, найкраще підійде пакет pickle.

У пакета pickle є дві пари парних методів:

Перша пара методів - це dumps, який упаковує в byte-рядок об'єкт, і loads - він розпаковує з byte-рядки в об'єкт.

Ці методи потрібні, коли ми хочемо контролювати, що робити з byte поданням, наприклад, відправити його по мережі або прийняти з мережі.

import pickle

some_data = {
    (1, 3.5): 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}

byte_string = pickle.dumps(some_data)
unpacked = pickle.loads(byte_string)

print(unpacked == some_data)  # True
print(unpacked is some_data)  # False
У цьому прикладі упакований у byte_string словник some_data розпакован в unpacked та unpacked суворо дорівнює some_data, але це все ж таки не той самий об'єкт.

Друга пара методів: dump та load - вони упаковують у відкритий для byte-запису файл і розпаковують з відкритого для byte-читання файлу.

import pickle

some_data = {
    (1, 3.5): 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}

file_name = 'data.bin'

with open(file_name, "wb") as fh:
    pickle.dump(some_data, fh)

with open(file_name, "rb") as fh:
    unpacked = pickle.load(fh)

print(unpacked == some_data)  # True
print(unpacked is some_data)  # False
Результат аналогічний попередньому прикладу. Головна відмінність у тому, що під час виконання цього коду в робочій папці з'явився файл data.bin.
'''

'''
TASK 1. Є список, кожен елемент якого є словником з контактами користувача наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.

Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою пакета pickle та зберігання отриманих даних у бінарному файлі.

Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, contacts - список контактів. Вона зберігає вказаний список у файл, використовуючи метод dump пакету pickle.

Друга функція read_contacts_from_file читає та повертає зазначений список contacts з файлу filename, використовуючи метод load пакету pickle.
'''

# import pickle
      
# def write_contacts_to_file(filename, contacts):
#     with open(filename, "wb") as fh:
#         pickle.dump(contacts, fh)

# def read_contacts_from_file(filename):
#     with open(filename, "rb") as fh:
#         return pickle.load(fh) 

'''
Протокол JSON (розшифровується як JavaScript Object Notation) дуже популярний в інтернеті протокол передачі. Цей протокол має низку переваг:

простий, його легко реалізувати;
читабельний;
відносно компактний (є набагато економніші протоколи).
Перша перевага зробила JSON універсальним, будь-яка сучасна мова програмування підтримує JSON. А якщо ні, то ви самі можете легко реалізувати підтримку JSON.

Недоліки у JSON теж є:

обмежений набір типів;
ресурсомісткий (є і більш вимогливі до ресурсів протоколи).
JSON підтримує такі типи даних:

запис (як словник у Python), в якості ключа можуть бути тільки рядки, значення — будь-який JSON тип;
масив (як список у Python);
число (немає різниці між цілими чи дробовими);
літерал (True, False, None);
рядок.
Як і у Python запис та масив можуть містити вкладені записи і/або словники будь-якої глибини вкладеності.

Слід бути акуратним з конвертацією типів під час роботи з JSON у Python. Кортежі під час розпакування з JSON стають списками, ключі словника, якщо вони були числами, стають рядками ж.

Python підтримує JSON і в стандартному постачанні є пакет json, в якому є все необхідне для роботи з JSON.

Методи dump та load зберігають дані у відкритий для запису файл і читають із відкритого для читання файлу.

import json

some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}
file_name = 'data.json'

with open(file_name, "w") as fh:
    json.dump(some_data, fh)

with open(file_name, "r") as fh:
    unpacked = json.load(fh)

unpacked is some_data  # False
unpacked == some_data  # False

unpacked['key'] == some_data['key']  # True
unpacked['a'] == some_data['a']  # True
unpacked['2'] == some_data[2]  # True
unpacked['tuple'] == [5, 6]  # True
Результатом буде файл data.json із наступною структурою.

{
  "key": "value",
  "2": [
    1,
    2,
    3
  ],
  "tuple": [
    5,
    6
  ],
  "a": {
    "key": "value"
  }
}
'''

'''
Task 2. Є список, кожен елемент якого є словником з контактами користувача наступного виду:

{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.

Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою пакету json та зберігання отриманих даних у текстовому файлі.

Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, contacts - список контактів. Вона зберігає вказаний список у файл, використовуючи метод dump пакету json.

Структура json файлу має бути такою:

{
  "contacts": [
    {
      "name": "Allen Raymond",
      "email": "nulla.ante@vestibul.co.uk",
      "phone": "(992) 914-3792",
      "favorite": false
    },
    ...
  ]
}
Тобто список контактів повинен зберігатися за ключем "contacts", а не просто зберегти список у файл.

Друга функція read_contacts_from_file читає та повертає зазначений список contacts з файлу filename, збереженого раніше функцією write_contacts_to_file, використовуючи метод load пакету json.
'''
# import json

    
# def write_contacts_to_file(filename, contacts):
#     with open(filename, "w") as fh:
#         json.dump({"contacts": contacts}, fh)

# def read_contacts_from_file(filename):
#     with open(filename, "r") as fh:
#         data = json.load(fh)
#         return data.get("contacts", [])

'''
Ще один формат обміну інформацією, що дуже часто використовується — це табличне уявлення. Відкритий формат для зберігання табличних даних, який підтримується будь-яким редактором — це формат csv. Формат csv є, по суті, тим самим текстовим файлом, але з умовою, що вся інформація в ньому розділена на колонки та рядки символами роздільниками. Типово колонки поділяють комою, а рядки — символ нового рядка. Але можна використати будь-яку іншу комбінацію символів.

Python підтримує роботу з табличними даними у форматі csv. Для цього у стандартному постачанні йде пакет csv.

import csv

with open('eggs.csv', 'w', newline='') as fh:
    spam_writer = csv.writer(fh)
    spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

with open('eggs.csv', newline='') as fh:
    spam_reader = csv.reader(fh)
    for row in spam_reader:
        print(', '.join(row))
В результаті виконання цього коду в робочій папці з'явився файл eggs.csv. Якщо відкриєте його табличним редактором, він відкриється як таблиця.

Є два допоміжні класи в пакеті csv, які виконують роботу з табличними даними трохи зручніше:

import csv

with open('names.csv', 'w', newline='') as fh:
    field_names = ['first_name', 'last_name']
    writer = csv.DictWriter(fh, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

with open('names.csv', newline='') as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        print(row['first_name'], row['last_name'])
Класи DictWriter та DictReader дозволяють працювати з рядками таблиці як зі словниками, де як ключі використовуються назви колонок (перший рядок).

Таким чином за допомогою Python можна генерувати табличні дані та імпортувати дані з таблиць.
'''

'''
TASK 3. Є список, кожен елемент якого є словником з контактами користувача наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.

Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою пакету csv та зберігання отриманих даних у текстовому файлі.

Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, contacts - список контактів. Вона зберігає вказаний список у файлі формату csv.

Структура csv файлу має бути такою:

name,email,phone,favorite
Allen Raymond,nulla.ante@vestibul.co.uk,(992) 914-3792,False
Chaim Lewis,dui.in@egetlacus.ca,(294) 840-6685,False
Kennedy Lane,mattis.Cras@nonenimMauris.net,(542) 451-7038,True
Wylie Pope,est@utquamvel.net,(692) 802-2949,False
Cyrus Jackson,nibh@semsempererat.com,(501) 472-5218,True
Зверніть увагу, першим рядком у файлі йдуть заголовки – це назви ключів.

Друга функція read_contacts_from_file читає, виконує перетворення даних та повертає вказаний список contacts із файлу filename, збереженого раніше функцією write_contacts_to_file.

Примітка: При читанні файлу csv ми отримуємо властивість словника favorite у вигляді рядка, тобто. наприклад favorite='False' . Необхідно його привести до логічного виразу назад, щоб стало favorite=False.
'''

# import pickle


# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite


# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         self.filename = filename
#         self.contacts = contacts if contacts is not None else []

#     def save_to_file(self):
#         with open(self.filename, "wb") as f:
#             pickle.dump(self, f)

#     def read_from_file(self):
#         with open(self.filename, "rb") as f:
#             return pickle.load(f)
   
'''
Ви можете зберігати об'єкти для подальшого використання, але за умови, щоб pickle міг коректно зберегти, а потім розпакувати упакований об'єкт класу, необхідно, щоб сам клас був оголошений раніше у коді, де відбувається розпакування.

import pickle


class Human:
    def __init__(self, name):
        self.name = name


bob = Human("Bob")
encoded_bob = pickle.dumps(bob)

decoded_bob = pickle.loads(encoded_bob)

bob.name == decoded_bob.name  # True
Але якби ви захотіли передати об'єкт bob по мережі іншому комп'ютеру, який нічого не знає про клас Human, то ви отримаєте помилку. Якщо ж на обох кінцях каналу зв'язку оголошено клас Human, то такий обмін працюватиме.
'''

'''
Task 4. Розробіть клас Person. Він має чотири властивості: ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.

Приклад створення екземпляра класу:

    Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)
Розробіть клас Contacts. Він повинен ініціалізувати через конструктор дві властивості: filename - ім'я файлу для пакування об'єкта класу Contacts, contacts - список контактів, екземплярів класу Person.

Приклад створення екземпляра класу:

contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)
Розробіть два методи для серіалізації та десеріалізації екземпляра класу Contacts за допомогою пакету pickle та зберігання даних у бінарному файлі.

Перший метод save_to_file зберігає екземпляр класу Contacts у файл, використовуючи метод dump пакету pickle. Ім'я файлу зберігається в атрибуті filename.

Другий метод read_from_file читає та повертає екземпляр класу Contacts з файлу filename, використовуючи метод load пакету pickle.

Приклад роботи:

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True
'''

# import pickle


# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite


# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         self.filename = filename
#         self.contacts = contacts if contacts is not None else []

#     def save_to_file(self):
#         with open(self.filename, "wb") as f:
#             pickle.dump(self, f)

#     def read_from_file(self):
#         with open(self.filename, "rb") as f:
#             return pickle.load(f)
       

   '''
   Не всі об'єкти Python можна серіалізувати. Наприклад, не можна серіалізувати файловий дескриптор або системний ресурс. Але що робити, коли у вас є клас, об'єкт якого ви хочете запакувати, використовуючи pickle, але у нього є атрибути, що не серіалізуються? У такій ситуації ви можете скористатися магічними методами, які керують серіалізацією та десеріалізацією за допомогою pickle.

Магічний метод __getstate__ викликається, коли pickle намагається отримати представлення об'єкта у вигляді byte-рядку. У звичайній реалізації __getstate__ повертає __dict__ словник, де зберігаються всі атрибути класу. Але ви можете змінити цей метод.

import pickle


class Reader:
    def __init__(self, file):
        self.file = file
        self.fh = open(self.file)
        self.position = 0

    def close(self):
        self.fh.close()

    def read(self, size=1):
        data = self.fh.read(size)
        self.position = self.fh.tell()
        return data

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['fh'] = None
        return attributes
У цьому прикладі клас Reader можна серіалізувати, помилки через неможливість упакувати файловий дескриптор не виникне.
   '''

'''
TASK 5. Ми продовжимо розширювати приклад попереднього завдання. Додайте до класу Contacts атрибут count_save, за замовчуванням він повинен мати значення 0. Реалізуйте магічний метод __getstate__ для класу Contacts. При упаковуванні екземпляра метод класу повинен збільшувати значення атрибута count_save на одиницю. Таким чином, ця властивість - лічильник повторних операцій пакування екземпляра класу

Приклад роботи коду:

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print(persons.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3

Формат виконання:
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
'''

# import pickle
# from typing import List, Optional


# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite

#     def __str__(self):
#         return f"Person(name={self.name}, email={self.email}, phone={self.phone}, favorite={self.favorite})"


# class Contacts:
#     def __init__(self, filename: str, contacts: Optional[List[Person]] = None):
#         self.filename = filename
#         self.contacts = contacts if contacts is not None else []
#         self.count_save = 0  # Додано атрибут count_save

#     def save_to_file(self):
#         try:
#             with open(self.filename, "wb") as f:
#                 pickle.dump(self, f)
#         except Exception as e:
#             print(f"Error saving to file: {e}")

#     def read_from_file(self):
#         try:
#             with open(self.filename, "rb") as f:
#                 return pickle.load(f)
#         except FileNotFoundError:
#             print(f"File not found: {self.filename}")
#             return Contacts(self.filename)
#         except Exception as e:
#             print(f"Error reading from file: {e}")
#             return Contacts(self.filename)

#     def add_contact(self, contact: Person):
#         if isinstance(contact, Person):
#             self.contacts.append(contact)
#         else:
#             raise TypeError("contact must be an instance of Person")

#     def get_contacts(self) -> List[Person]:
#         return self.contacts

#     def __str__(self):
#         return "\n".join(str(p) for p in self.contacts)

#     def __repr__(self):
#         return f"Contacts(filename='{self.filename}', contacts={self.contacts})"

#     def __getstate__(self):
#         """
#         Магічний метод __getstate__ для збільшення лічильника збережень.
#         """
#         state = self.__dict__.copy()  # Копіюємо поточний стан об'єкта
#         state['count_save'] = state.get('count_save', 0) + 1  # Збільшуємо count_save
#         return state

'''
Цей магічний метод отримує на вхід словник, розпакований з файлу або byte-рядку. Поведінка за замовчуванням — це записати отримане значення в self.__dict__. Давайте доопрацюємо клас Reader так, щоб він міг після розпакування продовжити читання з того ж місця.

import pickle


class Reader:
    def __init__(self, file):
        self.file = file
        self.fh = open(self.file)
        self.position = 0

    def close(self):
        self.fh.close()

    def read(self, size=1):
        data = self.fh.read(size)
        self.position = self.fh.tell()
        return data

    def __getstate__(self):
        attributes = {**self.__dict__}
        attributes['fh'] = None
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.fh = open(value['file'])
        self.fh.seek(value['position'])
'''

'''
TASK 6. Продовжуємо розширювати приклад із попереднього завдання. Додайте до класу Contacts атрибут is_unpacking, за замовчуванням він повинен мати значення False. Реалізуйте магічний метод __setstate__ для класу Contacts. При розпаковуванні екземпляра класу метод повинен змінювати значення атрибута is_unpacking на значення True. Таким чином, ця властивість визначатиме, що екземпляр класу отримано внаслідок розпакування.

Приклад роботи коду:

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons.is_unpacking)  # False
print(person_from_file.is_unpacking)  # True
'''

# import pickle
# from typing import List, Optional


# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite

#     def __str__(self):
#         return f"Person(name={self.name}, email={self.email}, phone={self.phone}, favorite={self.favorite})"


# class Contacts:
#     def __init__(self, filename: str, contacts: Optional[List[Person]] = None):
#         self.filename = filename
#         self.contacts = contacts if contacts is not None else []
#         self.count_save = 0  # Додано атрибут count_save
#         self.is_unpacking = False  # Додано атрибут is_unpacking

#     def save_to_file(self):
#         try:
#             with open(self.filename, "wb") as f:
#                 pickle.dump(self, f)
#         except Exception as e:
#             print(f"Error saving to file: {e}")

#     def read_from_file(self):
#         try:
#             with open(self.filename, "rb") as f:
#                 return pickle.load(f)
#         except FileNotFoundError:
#             print(f"File not found: {self.filename}")
#             return Contacts(self.filename)
#         except Exception as e:
#             print(f"Error reading from file: {e}")
#             return Contacts(self.filename)

#     def add_contact(self, contact: Person):
#         if isinstance(contact, Person):
#             self.contacts.append(contact)
#         else:
#             raise TypeError("contact must be an instance of Person")

#     def get_contacts(self) -> List[Person]:
#         return self.contacts

#     def __str__(self):
#         return "\n".join(str(p) for p in self.contacts)

#     def __repr__(self):
#         return f"Contacts(filename='{self.filename}', contacts={self.contacts})"

#     def __getstate__(self):
#         """
#         Магічний метод __getstate__ для збільшення лічильника збережень.
#         """
#         state = self.__dict__.copy()  # Копіюємо поточний стан об'єкта
#         state['count_save'] = state.get('count_save', 0) + 1  # Збільшуємо count_save
#         return state

#     def __setstate__(self, state):
#         """
#         Магічний метод __setstate__ для позначення розпакування об'єкта.
#         """
#         self.__dict__.update(state)  # Оновлюємо стан об'єкта
#         self.is_unpacking = True  # Встановлюємо is_unpacking в True


'''
Python намагається заощаджувати пам'ять і не копіювати дані з однієї області пам'яті до іншої. Натомість інтерпретатор створює нове посилання (ще один псевдонім) на об'єкт, що існує, замість копіювання вмісту.

Така поведінка може призводити до помилок, коли справа стосується змінюваних типів, словників, списків, користувацьких класів.

Щоб розв'язувати цю проблему, Python має механізм копіювання — це функції з пакета copy.

Щоб створити "поверхневу" копію об'єкта, у пакеті copy є функція copy. Ця функція створює новий об'єкт такого ж типу і потім створює посилання весь вміст старого об'єкта в новий. Такий механізм досить гарний для роботи з об'єктами, де вже на першому рівні вкладеності немає змінних об'єктів, і вона працює досить швидко. Але для об'єктів із глибокою вкладеністю така функція все ж таки не дасть потрібного ефекту:

import copy

my_list = [1, 2, {1: 'a'}]
copy_list = copy.copy(my_list)
copy_list.append(4)
print(my_list)  # [1, 2, {1: 'a'}]
print(copy_list)  # [1, 2, {1: 'a'}, 4]

copy_list[2][2] = 'b'
print(my_list)  # [1, 2, {1: 'a', 2: 'b'}]
З цього прикладу видно, що хоч copy_list вже є новим об'єктом (не посилання на my_list), але вкладений у нього словник з індексом 2 — це один і той же словник і в copy_list, і в my_list.
'''

'''
TASK 7. Для копіювання екземпляра класу Person із попереднього прикладу реалізуйте функцію copy_class_person. Як параметр вона приймає екземпляр класу person, та повертає "поверхневу" копію об'єкта за допомогою функції copy із пакета copy.

Приклад коду:

person = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

copy_person = copy_class_person(person)

print(copy_person == person)  # False
print(copy_person.name == person.name)  # True
...

Формат виконання:
import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    
'''
# import copy


# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite


# def copy_class_person(person):
#     return copy.copy(person)

'''
Для ситуацій, коли нам потрібно, щоб на будь-якому рівні вкладеності створювалися нові об'єкти, а не посилання на ті що існують, у пакеті copy є функція deepcopy. Ця функція створює рекурсивно нові об'єкти.

import copy

my_list = [1, 2, {1: 'a'}]
copy_list = copy.deepcopy(my_list)
copy_list.append(4)
print(my_list)  # [1, 2, {1: 'a'}]
print(copy_list)  # [1, 2, {1: 'a'}, 4]

copy_list[2][2] = 'b'
print(my_list)  # [1, 2, {1: 'a'}]
'''

'''
TASK 8. Як ви вже зрозуміли, для класу Contacts створення поверхневої копії екземпляра класу не увінчається успіхом через те, що ми маємо атрибут contacts, який є списком екземплярів об'єктів класу Person, а отже, всі вони будуть передані за посиланням. Тому необхідно використовувати глибоке копіювання методом deepcopy з пакета copy

Для класу Contacts реалізуйте функцію copy_class_contacts. Як параметр вона приймає екземпляр класу Contacts і повертає глибоку копію об'єкта за допомогою функції deepcopy з пакета copy.

Приклад коду:

persons = Contacts("user_class.dat", contacts)

new_persons = copy_class_contacts(persons)

new_persons.contacts[0].name = "Another name"

print(persons.contacts[0].name)  # Allen Raymond
print(new_persons.contacts[0].name)  # Another name

Формат виконання:
import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True


def copy_class_contacts(contacts):
'''

# import copy
# import pickle


# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite


# def copy_class_person(person):
#     return copy.copy(person)


# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         if contacts is None:
#             contacts = []
#         self.filename = filename
#         self.contacts = contacts
#         self.is_unpacking = False
#         self.count_save = 0

#     def save_to_file(self):
#         with open(self.filename, "wb") as file:
#             pickle.dump(self, file)

#     def read_from_file(self):
#         with open(self.filename, "rb") as file:
#             content = pickle.load(file)
#         return content

#     def __getstate__(self):
#         attributes = self.__dict__.copy()
#         attributes["count_save"] += 1
#         return attributes

#     def __setstate__(self, value):
#         self.__dict__ = value
#         self.is_unpacking = True


# def copy_class_contacts(contacts):
#     return copy.deepcopy(contacts)

'''
Ще одна проблема вирішується за допомогою пакету copy — це копіювання об'єктів користувача. Щоб створити об'єкт, який буде коректно оброблятися функціями copy та deepcopy, ваш клас повинен реалізувати два магічних метода: __copy__ та __deepcopy__ для поверхневого та глибокого копіювання відповідно.

from copy import deepcopy, copy


class Expenses:
    def __init__(self):
        self.data = {}
        self.places = []

    def spent(self, place, value):
        self.data[str(place)] = value
        self.places.append(place)

    def __copy__(self):
        copy_obj = Expenses()
        copy_obj.data = copy(self.data)
        copy_obj.places = copy(self.places)
        return copy_obj

    def __deepcopy__(self, memo):
        copy_obj = Expenses()
        memo[id(copy_obj)] = copy_obj
        copy_obj.data = deepcopy(self.data)
        copy_obj.places = deepcopy(self.places)
        return copy_obj


e = Expenses()
e.spent('hotel', 100)
e.spent('taxi', 10)
print(e.places)  # ['hotel', 'taxi']

e_copy = copy(e)
print(e_copy is e)  # False
e_copy.spent('bar', 30)
print(e.places)  # ['hotel', 'taxi', 'bar']

e_deep_copy = deepcopy(e)
print(e_deep_copy is e)  # False
e_deep_copy.spent(
    'airport',
    300
)
print(e.places)  # ['hotel', 'taxi', 'bar']
print(e_deep_copy.places)  # ['hotel', 'taxi', 'bar', 'airport']
Використовуючи методи __copy__ та __deepcopy__, ви можете керувати тим, як саме буде створюватися копія вашого об'єкта. Метод __deepcopy__ обов'язково повинен приймати один аргумент — словник, в який записуються усі об'єкти, які піддаються копіюванню. Це необхідно, щоб уникнути нескінченної рекурсії, якщо якийсь об'єкт є спільним для кількох копійованих. В такому випадку алгоритм глибокого копіювання може зайти в безкінечний цикл, копіюючи поперемінно об'єкти із посиланнями один на одного. Словник memo зберігає в якості ключів id об'єктів і самі об'єкти як значення. Коли перевизначаємо як має відбуватися копіювання, ми можемо і не використовувати memo, якщо точно знаємо, що рекурсії не виникне.
'''

'''
TASK 9. Реалізуйте метод __copy__ для класу Person.

Реалізуйте методи __copy__ та __deepcopy__ для класу Contacts.
Приклад коду:
import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        
            
            
            
            
        
        


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        
        

    def __deepcopy__(self, memo):
        
        
'''

# import copy
# import pickle


# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite

#     def __copy__(self):
#         # Повертає новий об’єкт з такими ж атрибутами
#         return Person(self.name, self.email, self.phone, self.favorite)


# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         if contacts is None:
#             contacts = []
#         self.filename = filename
#         self.contacts = contacts
#         self.is_unpacking = False
#         self.count_save = 0

#     def save_to_file(self):
#         with open(self.filename, "wb") as file:
#             pickle.dump(self, file)

#     def read_from_file(self):
#         with open(self.filename, "rb") as file:
#             content = pickle.load(file)
#         return content

#     def __getstate__(self):
#         attributes = self.__dict__.copy()
#         attributes["count_save"] += 1
#         return attributes

#     def __setstate__(self, value):
#         self.__dict__ = value
#         self.is_unpacking = True

#     def __copy__(self):
#         # Поверхнева копія: копіюємо тільки список контактів (без глибокої копії Person)
#         new_contacts = copy.copy(self.contacts)
#         new_instance = Contacts(self.filename, new_contacts)
#         new_instance.count_save = self.count_save
#         return new_instance

#     def __deepcopy__(self, memo):
#         # Глибока копія: рекурсивно копіюємо всі об’єкти в списку contacts
#         new_filename = copy.deepcopy(self.filename, memo)
#         new_contacts = copy.deepcopy(self.contacts, memo)
#         new_instance = Contacts(new_filename, new_contacts)
#         new_instance.count_save = self.count_save
#         return new_instance

'''TESTING'''
# # Створимо вихідний об'єкт
# contacts = [
#     Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False)
# ]
# persons = Contacts("user_class.dat", contacts)

# # Глибока копія
# deep_copy = copy.deepcopy(persons)
# deep_copy.contacts[0].name = "Changed"

# # Поверхнева копія
# shallow_copy = copy.copy(persons)
# shallow_copy.contacts[0].email = "changed@example.com"

# # Перевірка результатів
# print(persons.contacts[0].name)    # Allen Raymond — не змінено
# print(deep_copy.contacts[0].name)  # Changed

# # changed@example.com — змінено в shallow_copy
# print(persons.contacts[0].email)
# print(shallow_copy.contacts[0].email)  # changed@example.com

'''Variant 2'''

import pickle
from typing import List, Optional
import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __str__(self):
        return f"Person(name={self.name}, email={self.email}, phone={self.phone}, favorite={self.favorite})"

    def __copy__(self):
        """
        Реалізує поверхневе копіювання об'єкта Person.
        """
        return Person(self.name, self.email, self.phone, self.favorite)


class Contacts:
    def __init__(self, filename: str, contacts: Optional[List[Person]] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        try:
            with open(self.filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error saving to file: {e}")

    def read_from_file(self):
        try:
            with open(self.filename, "rb") as file:
                content = pickle.load(file)
            return content
        except FileNotFoundError:
            print(f"File not found: {self.filename}")
            return Contacts(self.filename)
        except Exception as e:
            print(f"Error reading from file: {e}")
            return Contacts(self.filename)

    def __getstate__(self):
        """
        Магічний метод __getstate__ для збільшення лічильника збережень.
        """
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        """
        Магічний метод __setstate__ для позначення розпакування об'єкта.
        """
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        """
        Реалізує поверхневе копіювання об'єкта Contacts.
        """
        return Contacts(self.filename, self.contacts)

    def __deepcopy__(self, memo):
        """
        Реалізує глибоке копіювання об'єкта Contacts.
        """
        # Копіюємо основні атрибути
        new_contacts = Contacts(self.filename)
        new_contacts.is_unpacking = self.is_unpacking
        new_contacts.count_save = self.count_save

        # Глибоко копіюємо список контактів
        memo[id(self)] = new_contacts  # Додаємо копію в memo, щоб уникнути рекурсії
        new_contacts.contacts = [copy.deepcopy(contact, memo) for contact in self.contacts]
        return new_contacts


def copy_class_person(person: Person) -> Person:
    """
    Створює поверхневу копію екземпляра класу Person.

    Args:
        person (Person): Екземпляр класу Person для копіювання.

    Returns:
        Person: Поверхнева копія об'єкта person.
    """
    return copy.copy(person)


if __name__ == "__main__":
    # Створення об'єктів Person
    person1 = Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False)
    person2 = Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False)
    person3 = Person("Kennedy Lane", "mattis.Cras@nonenimMauris.net", "(542) 451-7038", True)
    person4 = Person("Wylie Pope", "est@utquamvel.net", "(692) 802-2949", False)
    person5 = Person("Cyrus Jackson", "nibh@semsempererat.com", "(501) 472-5218", True)

    # Створення об'єкта Contacts та додавання Person
    contacts = [person1, person2, person3, person4, person5]
    persons = Contacts("user_class.dat", contacts)
    persons.save_to_file()
    person_from_file = persons.read_from_file()
    print(persons.is_unpacking)  # False
    print(person_from_file.is_unpacking)  # True

    # Копіювання екземпляра класу Person
    person = Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    )
    copy_person = copy_class_person(person)
    print(f"Оригінал: {person}")
    print(f"Копія: {copy_person}")

    print(copy_person == person)  # False
    print(copy_person.name == person.name)  # True

    # Копіювання екземпляра класу Contacts
    contacts_original = Contacts("my_contacts.pkl", [person1, person2])
    contacts_copy = copy.copy(contacts_original)
    contacts_deepcopy = copy.deepcopy(contacts_original)

    print("\nOriginal Contacts:")
    print(contacts_original)
    print("\nShallow Copy Contacts:")
    print(contacts_copy)
    print("\nDeep Copy Contacts:")
    print(contacts_deepcopy)

    # Зміни в оригіналі не впливають на глибоку копію
    contacts_original.add_contact(person3)
    print("\nOriginal Contacts after adding person3:")
    print(contacts_original)
    print("\nDeep Copy Contacts after adding person3 to original:")
    print(contacts_deepcopy)
