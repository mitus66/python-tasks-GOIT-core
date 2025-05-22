'''
Спосіб організації програм, коли об'єднують дані та функціонал усередині якогось об'єкта, називають об'єктноорієнтованою
парадигмою програмування. Об'єктноорієнтоване програмування (ООП) по праву вважається однією з найефективніших методологій
створення програмних продуктів. Ви пишете класи, що описують реально чинні предмети та ситуації, а потім створюєте об'єкти
на основі цих описів.

Покажемо найпростіший клас на наступному прикладі.

class Person:
    pass  # Порожній блок

p = Person()

Ми створюємо новий клас за допомогою оператора class та імені класу. За цим слідує блок виразів, що формують тіло класу.
В нашому випадку блок у нас порожній, на що вказує оператор pass. Далі ми створюємо об'єкт-екземпляр класу, записуючи
ім'я класу з дужками.
ООП має чотири основні концепції, які відрізняють його від інших методологій програмування:

Абстракція
Інкапсуляція
Наслідування
Поліформізм
З чотирьох концепцій ми розберемо у завданнях три останні, крім абстракції. Це більш просунута категорія, і створення
абстрактних класів ми розглядатимемо в другому блоці навчання. Зараз нагадаю йде перший блок Python. Коротко тільки
зауважимо, що:

Абстракція - це модель якогось об'єкта або явища з реального світу, що відкидає незначні деталі, які не грають істотну
роль в цьому контексті.

Task 1. Створіть клас Animal. Також створіть екземпляр класу Animal (замість реалізації класу можете використовувати
pass) і привласніть змінній animal.
'''

# class Animal:
#     pass
#
# animal = Animal()

'''
Об'єкти можуть зберігати дані у звичайних змінних, які належать об'єкту. Змінні, що належать об'єкту або класу, називають 
полями. Об'єкти можуть мати функції, які належать класу. Такі функції називають методами класу. Всі разом (поля та методи) 
заведено називати атрибутами класу.
За допомогою атрибутів класу ми виконуємо інкапсуляцію — приховуємо деталі реалізації під інтерфейсом класу.
Інкапсуляція — це здатність об'єктів приховувати частину свого стану та поведінки від інших об'єктів, надаючи зовнішньому 
світу лише певний інтерфейс взаємодії із собою.
Методи класу мають одну відмінність від звичайних функцій: вони повинні мати додатково ім'я, яке додається до початку 
списку параметрів. Однак, при виклику методу ніякого значення цьому параметру привласнювати не потрібно його вкаже Python. 
Ця змінна вказує на сам об'єкт екземпляра класу, і за традицією вона називається self.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f"Hi {self.name}"


p = Person("Boris", 34)
Метод __init__() - спеціальний метод, який автоматично виконується під час створення кожного нового екземпляра на базі 
класу Person (конструктор). Ім'я методу починається та закінчується двома символами підкреслення. Причина у тому, що так 
ми запобігаємо конфліктам імен стандартних методів Python і методів ваших класів.

Коли ми створюємо екземпляр Person, Python викликає метод __init__() з класу Person. Ми передаємо в Person() ім'я "Boris" 
та вік 34 як аргументи. Значення self буде передано автоматично, явно передавати його не потрібно.

Зверніть увагу, що метод класу greeting не приймає параметрів, проте має параметр self у визначенні функції.

Task 2. Створіть клас Animal. Також створіть екземпляр класу Animal та привласніть змінній animal. Для класу Animal у 
конструкторі створіть дві властивості: nickname - кличка тварини та weight - вага тварини. Реалізуйте також метод класу 
say. При реалізації методу можна використати оператор pass, поки що головне - це визначення, а не конкретна реалізація.
'''

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#
#     def say(self):
#         pass
#
#
# animal = Animal('Barsik', 50)

'''
Task 3. Для попереднього завдання реалізуйте в класі Animal метод change_weight, який має змінювати вагу тварини.
Викличте функцію change_weight(12) для об'єкта animal та змініть значення початкової ваги з 10 на 12 одиниць.
'''

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#
#     def say(self):
#         pass
#
#     def change_weight(self, weight):
#         self.weight = weight
#
# animal = Animal("Simon", 10)
# animal.change_weight(12)

'''
Існує два типи полів: змінні класи та змінні об'єкта. Як видно з назви вони відрізняються тим, що належать або класу чи 
об'єкту відповідно.

Змінні класу – доступ до них мають усі екземпляри цього класу. Змінна класу існує тільки одна, та будь-який з об'єктів, 
коли змінює змінну класу, змінює її для решти екземплярів цього ж класу.

Змінні об'єкта - належать кожному окремому екземпляру класу. У цьому випадку кожен об'єкт має свою власну копію поля, 
тобто вона жодним чином не пов'язана з іншими такими ж полями в інших екземплярах.

Розглянемо наступний приклад:

class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    def how_many_persons(self):
        print(f"Кількість людей зараз {Person.count}")


first = Person('Boris')
first.how_many_persons()
second = Person('Alex')
first.how_many_persons()
Вивід:

Кількість людей зараз 1
Кількість людей зараз 2
Тут count належить класу Person і є змінною класу. Змінна name належить об'єкту та є змінною об'єкта, і надається 
значення за допомогою self. Як бачимо з прикладу, звернення до змінної класу Person виконується як Person.count, і ми не 
використовуємо звернення self.count. До змінної ж об'єкта name, у всіх методах цього об'єкта, ми звертаємось за допомогою 
позначення self.name.
Але якщо ми введемо змінну об'єкта з тим самим ім'ям, що й змінну класу, це зробить недоступною змінну класу!

class Person:
    count = 0

    def __init__(self):
        pass


person = Person()
print(person.count)  # 0
Ми ще маємо доступ до змінної класу, а у наступному прикладі вже ні.

class Person:
    count = 0

    def __init__(self):
        self.count = 10


person = Person()
print(person.count)  # 10
Примітка
Але ми все ще маємо доступ до змінної через ім'я класу: `Person.count`

Task 4. Додамо в клас Animal змінну класу color, значення якої спочатку дорівнює 'white', і метод change_color, який 
повинен змінювати значення змінної класу color.
Створіть екземпляри об'єкта: first_animal та second_animal
Викличте функцію change_color("red") для будь-якого екземпляра об'єкту Animal та змініть значення змінної класу 
color на "red".
'''
#
# class Animal:
#     color = "white"
#
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#
#     def say(self):
#         pass
#
#     def change_weight(self, weight):
#         self.weight = weight
#
#     @classmethod
#     def change_color(cls, new_color):
#         cls.color = new_color
#
# first_animal = Animal('Adam', 10)
# second_animal = Animal('Eva', 8)
# Animal.change_color("red")

'''
Основна сила об'єктно-орієнтованого програмування полягає саме в можливості успадкування класів. Успадкування дає 
можливість створювати нові класи, що містять атрибути батьківських класів.

class Human:
    name = ''

    def voice(self):
        print(f"Hello! My name is {self.name}")


class Developer(Human):
    field_description = "My Programming language"
    language = ""

    def make_some_code(self):
        return f"{self.field_description} is {self.value}"


class PythonDeveloper(Developer):
    value = "Python"


class JSDeveloper(Developer):
    value = "JavaScript"


p_dev = PythonDeveloper()
p_dev.name = 'Bob'
p_dev.voice()  # Hello! My name is Bob
p_dev.make_some_code()  # My Programming language is Python

js_dev = JSDeveloper()
js_dev.make_some_code()  # My Programming language is JavaScript
У цьому прикладі ми створили батьківський клас Human, який визначив, що у всіх є ім'я та метод voice.

Далі ми розширили функціонал класу Human та створили клас Developer, який успадковується від Human і додає йому поля 
field_description та language і метод make_some_code. І щоб реалізувати функціонал розробника конкретною мовою, ми 
зробили два класи PythonDeveloper та JSDeveloper. Тепер якщо ми захочемо додати функціонал у всі дочірні для Human класи, 
то для цього можна додати потрібні атрибути в Human і вони автоматично з'являться і в PythonDeveloper, і JSDeveloper. 
Якщо потрібно розширити функціонал всіх розробників, то можна додати потрібні атрибути до класу Developer. І якщо треба 
додати особливу поведінку класу розробників конкретною мовою, то можна додати або змінити атрибути класів PythonDeveloper 
або JSDeveloper.

Таким чином у коді має бути лише одне місце, де визначено поведінку об'єкту. І якщо нам треба отримати інший об'єкт, 
який має цю поведінку і якісь свої особливості, ми можемо успадковуватись від класу з потрібними нам спільними атрибутами 
та додати унікальні.

Цей підхід дозволяє писати менше коду та структурувати дані, створюючи моделі реальних об'єктів з їх характеристиками 
(полями) та поведінкою (методами)

Task 5. Створіть клас Cat, батьківським класом якого є клас Animal. У класі Cat виконайте перевизначення методу say, щоб 
він повертав рядок "Meow" для екземплярів класу Cat.
Фактично ми виконуємо при цьому поліморфізм. Поліморфізм - це здатність програми вибирати різні реалізації при виклику 
операцій з однією і тією ж назвою. Тобто при виклику методу say в екземпляра класу Cat викликається нова реалізація, а 
не успадкована від класу Animal
Створіть також змінну cat, яка буде екземпляром класу Cat. При створенні змінної cat ім'я кота має бути "Simon", а 
вага - 10 одиниць.
'''

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#
#     def say(self):
#         pass
#
#     def change_weight(self, weight):
#         self.weight = weight
#
# class Cat(Animal):
#     def say(self):
#         return ("Meow")
#
# cat = Cat("Simon", 10)

'''
Як бачимо, клас, що успадковує від іншого, автоматично отримує всі атрибути та методи першого класу. У наших завданнях 
клас Cat отримує атрибути nickname та weight при ініціалізації екземпляра від класу Animal. Початковий клас Animal 
називається батьком, а новий клас Cat - нащадком. Клас Cat успадковує атрибути та методи батька, але при цьому також 
може визначати власні атрибути та методи.

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


cat = Cat("Simon", 10)
Але що буде якщо нам необхідно для класу Cat ввести нову властивість при створенні екземпляра, як порода breed? І виклик 
екземпляра класу Cat має виглядати так:

cat = Cat("Simon", 10, 'british')
Для цього наш код має прийняти такий вигляд:

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed = breed
        
    def say(self):
        return "Meow"


cat = Cat("Simon", 10, "british")
print(cat.nickname)  # Simon
print(cat.breed)  # british
print(cat.weight)  # 10
Метод __init__() отримує всю інформацію, що необхідна для створення екземпляра Cat. Функція super() спеціальна функція, 
яка допомагає Python пов'язати нащадка з батьком. Ця функція вказує Python явно викликати метод __init__() класу Animal, 
що є батьком Cat, внаслідок чого екземпляр Cat отримує всі атрибути класу батька. Ім'я super відповідає поширеній 
термінології: клас батько називається суперкласом, а клас нащадок - субкласом. Значить, Animal - це суперклас, а Cat - 
субклас.

Task 6. Створіть клас Dog, батьківським класом якого є клас Animal. У класі Dog виконайте перевизначення методу say, щоб 
він повертав рядок "Woof" для екземплярів класу Dog.
У конструкторі класу Dog введіть нову властивість breed - порода, при цьому повинні залишитись всі властивості, 
успадковані від класу Animal.
Створіть у коді наступний екземпляр класу Dog.
dog = Dog("Barbos", 23, "labrador")
'''

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#
#     def say(self):
#         pass
#
#     def change_weight(self, weight):
#         self.weight = weight
#
#
# class Dog(Animal):
#     def __init__(self, nickname, weight, breed):
#         super().__init__(nickname, weight)
#         self.breed = breed
#
#     def say(self):
#         return "Woof"
#
#
# dog = Dog("Barbos", 23, "labrador")

'''
При моделюванні явищ реального світу класи з часом доповнюються дедалі більшою кількістю подробиць. Списки атрибутів і 
методів збільшуються, і через деякий час класи стають довгими та важко підтримуються в розробці. У такій ситуації частину 
одного класу можна виділити у вигляді окремого класу. Код великого класу розбивається на менші класи, що працюють у 
взаємодії один з одним.

Наприклад, при подальшому доопрацюванні класу Cat може виявитися, що в ньому стало занадто багато атрибутів та методів, 
які стосуються господаря кота. У такому разі все, що відноситься до власника кота, можна перемістити в окремий клас 
ім'ям Owner. Потім екземпляр Owner стає атрибутом класу Cat:

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Cat(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Meow"


owner = Owner("Sherlock", 24, "London, 221B Baker Street")
cat = Cat("Simon", 10, "british", owner)
Може здатися, що такий варіант потребує більше додаткової роботи, але тепер господаря кота (клас Owner) можна моделювати 
з будь-яким ступенем деталізації, без втручання у клас Cat.

Task 7. Для минулого завдання додамо клас Owner — власника собаки. У класу є три атрибути: ім'я — name, вік — age та 
адреса — address. Також необхідно реалізувати метод info, який повертає словник з ключами 'name', 'age' і 'address', 
та значення яких дорівнюють відповідним властивостям екземпляра класу.
Реалізувати для класу Dog атрибут owner, який буде екземпляром класу Owner. Додати до класу Dog метод who_is_owner, який 
повертає результат виклику методу info екземпляра класу Owner, тобто це словник з ключами name, age та address власника.
'''

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#
#     def say(self):
#         pass
#
#     def change_weight(self, weight):
#         self.weight = weight
#
#
# class Owner:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def info(self):
#         return {
#             'name': self.name,
#             "age": self.age,
#             "address": self.address
#         }
#
# class Dog(Animal):
#     def __init__(self, nickname, weight, breed, owner):
#         self.breed = breed
#         self.owner = owner
#         super().__init__(nickname, weight)
#
#     def say(self):
#         return "Woof"
#
#     def who_is_owner(self):
#         return owner.info()
#
#
# owner = Owner("Sherlock", 24, "London, 221B Baker Street")
# print(owner.info())

'''
Успадкування — це дуже потужний інструмент. Наслідувати можна не тільки від одного класу, а можна одразу від кількох. 
Таким чином можна отримувати об'єкти, що поєднують у собі властивості багатьох класів. Тут має виникнути питання, а що 
буде, якщо кілька класів мають атрибути з однаковим ім'ям?

Для відповіді на це питання треба зрозуміти, як Python шукає атрибути (поля або методи) в об'єктах. Власне, це є 
MRO (Method Resolution Order). MRO у Python працює наступним чином:

Шукає атрибут серед атрибутів самого класу. Саме завдяки цьому, ви можете "перевизначати" батьківські атрибути.
Шукає атрибут у першого з батьків (той, що вказано першим у списку батьків).
Шукає атрибут у наступного батька у списку батьків, доки такі є.
Шукає атрибут у батьках першого батька.
Повторює п.4 для всіх батьків.
Викликає виключення, що атрибут не знайдено.
Пошуки закінчуються, як тільки атрибут знайдено.

class A:
    x = 'I am A class'


class B:
    x = 'I am B class'
    y = 'I exist only in B'


class C(A, B):
    z = "This exists only in C"


c = C()
print(c.z)  # This exists only in C
print(c.y)  # I exist only in B
print(c.x)  # I am A class
З цього прикладу видно, що у класі C поле x береться з A класу. Якщо ж в цьому ж прикладі змінити список батьків, то отримаємо:

class A:
    x = 'I am A class'


class B:
    x = 'I am B class'
    y = 'I exist only in B'


class C(B, A):
    z = "This exists only in C"


c = C()
print(c.z)  # This exists only in C
print(c.y)  # I exist only in B
print(c.x)  # I am B class
Тепер у класі C поле x береться з B класу.

Task 8. Створіть два класи: CatDog та DogCat. Ці класи повинні наслідуватись від двох класів відразу: Cat та Dog. Після 
успадкування в екземпляра класу CatDog, батьківський метод say повинен повертати "Meow", а у класу DogCat — "Woof". Для 
обох зазначених класів реалізуйте метод info, який повертає рядок у наступному форматі f"{self.nickname}-{self.weight}".
'''

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#
#     def say(self):
#         pass
#
#
# class Cat(Animal):
#     def say(self):
#         return "Meow"
#
#
# class Dog(Animal):
#     def say(self):
#         return "Woof"
#
#
# class CatDog(Cat, Dog):
#     def say(self):
#         return super().say()
#
#     def info(self):
#         return f"{self.nickname}-{self.weight}"
#
#
# class DogCat(Dog, Cat):
#     def say(self):
#         return super().say()
#
#     def info(self):
#         return f"{self.nickname}-{self.weight}"


'''
Качина типізація — це механізм, властивий Python, який дозволяє використовувати будь-які об'єкти один замість іншого, 
аби в обох були потрібні методи та поля. Качиною ця типізація називається від приказки: "Якщо крякає як качка, плаває 
як качка і літає як качка, це качка". Це добре відображає суть підходу, реалізованого у Python. Ні, інтерпретатор не 
перевіряє, що на функцію або метод був переданий об'єкт потрібного або дочірнього класу, достатньо щоб у об'єкта були 
потрібні методи і все буде працювати.

class Mammal:
    phrase = ''

    def voice(self):
        return self.phrase


class Dog(Mammal):
    phrase = 'Bark!'


class Cat(Mammal):
    phrase = 'Meow!'


class Chupakabra:
    def voice(self):
        return 'Whooooo!!!'


class Recorder:
    def record_animal(self, animal):
        voice = animal.voice()
        print(f'Recorded "{voice}"')


r = Recorder()
cat = Cat()
dog = Dog()
strange_animal = Chupakabra()

r.record_animal(cat)  # Recorded "Meow!"
r.record_animal(dog)  # Recorded "Bark!"
r.record_animal(strange_animal)  # Recorded "Whooooo!!!"
В цьому прикладі ми створили батьківський клас Mammal, у якого є метод voice та два дочірніх до нього Dog та Cat. Клас 
Record приймає на вхід методу record_animal об'єкт animal і викликає у нього метод voice, щоб вивести результат виконання 
voice у консоль. При цьому є клас Chupakabra, у якого теж є метод voice, та хоч він і не успадковується від Mammal, але 
об'єкти цього класу так само можна передавати в record_animal. Головне, щоб атрибут називався так само і приймав ті ж 
аргументи (якщо це метод).

Сенс качиної типізації полягає в тому, щоб не дбати про точний клас об'єкта, а дбати про те, які методи для нього можна 
викликати та які операції над ним можна виконувати. Таким чином, треба просто передати об'єкт методу, знаючи, що при 
неправильному використанні буде викинуто виключення.

Tasl 13. Як ми вже говорили, поліморфізм - це здатність програми вибирати різні реалізації при виклику операцій з однією 
і тією ж назвою.
Але поліморфізм - це також здатність об'єктів прикидатись чимось іншим. У наведеному вище прикладі Chupakabra прикидалася 
собакою та кішкою.
Для коду із завдання вам необхідно реалізувати клас CatDog, не використовуючи успадкування від класу Animal, але щоб 
екземпляр класу CatDog поводився як і, як екземпляр класу Cat, тобто. він повинен вдати, що він клас Cat.
'''

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#
#     def say(self):
#         pass
#
#     def change_weight(self, weight):
#         self.weight = weight
#
#
# class Cat(Animal):
#     def say(self):
#         return "Meow"
#
#
# class CatDog:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#
#     def say(self):
#         return "Meow"
#
#     def info(self):
#         return f"{self.nickname}-{self.weight}"
#
#     def change_weight(self, weight):
#         self.weight = weight
#
# # Створення екземпляра CatDog
# cat_dog = CatDog("Мурчик", 7)
#
# # Перевірка методу say
# print(f"{cat_dog.nickname} каже: {cat_dog.say()}")  # Виведе: Мурчик каже: Meow
#
# # Перевірка методу info
# print(f"Інформація про {cat_dog.nickname}: {cat_dog.info()}")  # Виведе: Інформація про Мурчик: Мурчик-7