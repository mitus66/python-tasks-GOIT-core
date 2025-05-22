'''
Найчастіше використовуваний магічний метод — це метод __init__. Цей метод відповідає за ініціалізацію об'єкта. Коли ви створюєте об'єкт класу, спочатку створюється порожній об'єкт, який містить лише обов'язкові службові атрибути. Після цього (об'єкт вже створено) автоматично викликається метод __init__, який ви можете модифікувати під ваші потреби.

class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Hello! I am {self.name}'


bill = Human('Bill')
print(bill.say_hello())  # Hello! I am Bill
print(bill.age)  # 0

jill = Human('Jill', 20)
print(jill.say_hello())  # Hello! I am Jill
print(jill.age)  # 20
В цьому прикладі ми створили клас Human, у якому визначили метод __init__. У цьому методі ми додаємо об'єктам цього класу поля name та age. Зверніть увагу, що метод __init__ може приймати аргументи позиційні і/або іменні, як будь-який інший метод. Коли ми створюємо об'єкт класу Human, ми повинні класу передати обов'язково хоч один аргумент, оскільки метод __init__ повинен приймати обов'язково name.

__init__ не обов'язково приймає аргументи та містить лише створення полів. Цей метод можна використовувати для реалізації будь-яких дій, які вам потрібні на етапі, коли об'єкт вже створено та його треба ініціалізувати.
'''

'''
TASK 1. Створіть клас Point, який відповідатиме за відображення геометричної точки на площині.

Реалізуйте через конструктор __init__ ініціалізацію двох атрибутів: координати x та координати y.

Приклад:

point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10
'''


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# point = Point(5, 10)

# print(point.x)  # 5
# print(point.y)  # 10

'''
У Python неможливо інкапсулювати (зробити недоступними) атрибути класу. Ви завжди можете отримати доступ до будь-якого атрибуту. Щоб якось вказати розробнику, що доступ до атрибуту безпосередньо небажаний, прийнято називати такі поля чи методи, починаючи з одного нижнього підкреслення. Якщо ж назвати атрибут так, що спочатку буде два нижні підкреслення, то включиться механізм "приховання" імен. Це не означає, що доступ до цього поля буде закрито, просто небагато ускладнений.

class Secret:
    public_field = 'this is public'
    _private_field = 'avoid using this please'
    __real_secret = 'I am hidden'


s = Secret()
print(s.public_field)  # this is public
print(s._private_field)  # avoid using this please
print(s._Secret__real_secret)  # I am hidden
Як видно з цього прикладу, доступу за допомогою s.__real_secret ні, але можна отримати доступ до цього ж поля через s._Secret__real_secret, що загалом нічого не захищає.

Цей механізм можна використовувати для реалізації механізму setter та getter. Буває, виникає необхідність перевірити, що користувач хоче записати в поле. Для цього можна написати окремий метод, який буде перед збереженням значення в полі реалізовувати перевірку, але саме поле, як і раніше, залишиться доступним. Можна ж скористатися декоратором setter. Для обчислення значення "на льоту" або як пару для setter можна скористатися декоратором property, який перетворює будь-який метод на поле. Наприклад, ми хочемо перевірити, що користувач вводить лише додатні числа.

class PositiveNumber:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value > 0:
            self.__value = new_value
        else:
            print('Only numbers greater zero accepted')


p = PositiveNumber()
p.value = 1
print(p.value)  # 1
p.value = -1  # Only numbers greater zero accepted
p._PositiveNumber__value = -1
print(p.value)  # -1
У цьому прикладі поле __value можна вважати прихованим, воно певною мірою інкапсульовано. Однак значення в цьому полі може бути отримано і модифіковано безпосередньо. Ще декоратор property зручний, коли значення у полі треба обчислювати у момент звернення.
'''

'''
TASK 2. У класу Point через конструктор __init__ оголошено два атрибути: координати x та y. Приховати доступ до них з допомогою подвійного підкреслення: __x та __y

Реалізуйте для класу Point механізми setter та getter до атрибутів __x та __y за допомогою декораторів property та setter.

Приклад:

point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10
'''


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, value):
#        self.__x = value

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, value):
#         self.__y = value


# point = Point(5, 10)

# print(point.x)  # 5
# print(point.y)  # 10

'''
Розглянемо таку ситуацію. У нас є клас Person, який має властивість name

class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if (type(name) == str) and (len(name) > 0):
            self.__name = name


person = Person(123)
print(person.name)  # 123
У цьому коді може виникнути помилка. В setter ми робимо перевірку, щоб значення було рядком та чекаємо тільки рядок ненульової довжини. Але при ініціалізації значення в конструкторі, коли привласнюємо self.__name=name ми насправді ігноруємо роботу setter та привласнюємо значення безпосередньо. Що і сталося в нашому коді — властивість __name містить числове значення.

Щоб цього не відбувалося, код треба переписати так:

class Person:
    def __init__(self, name):
        self.__name = None
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if (type(name) == str) and (len(name) > 0):
            self.__name = name


person = Person(123)
print(person.name)  # None
Зараз у конструкторі ми привласнюємо полю __name значення None: self.__name=None. У другому рядку конструктора ми примусово викликаємо setter інструкцією self.name=name. У такому разі setter виконується і не дозволяє нам привласнити полю __name не валідне значення 123 при створенні екземпляра класу person = Person(123).
'''

'''
TASK 3. У класу Point до механізму setter властивостей x і y додайте перевірку на значення, що вводиться. Дозвольте встановлювати значення властивостей x та y для екземпляра класу, тільки якщо вони мають числове значення (int або float).

Приклад:

point = Point("a", 10)

print(point.x)  # None
print(point.y)  # 10
'''

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == float) or (type(x) == int):
#             self.__x = x
            
            
#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == float) or (type(y) == int):
#             self.__y = y
        
# point = Point("a", 10)

# print(point.x)  # None
# print(point.y)  # 10   

'''
Квадратні дужки дозволяють вам звертатися до елементів послідовності індексу або елементів словника по ключу. Коли ви хочете отримати значення, використовуючи квадратні дужки, об'єкт викликається метод __getitem__. Для запису значення з індексом або ключем викликається метод __setitem__. Обидва цих метода приймають першим аргументом self. __getitem__ другим аргументом приймає індекс чи ключ, яким треба знайти елемент, а __setitem__ другим аргументом приймає ключ/індекс, а третім значення, яке треба записати за цим ключем/індексом.

class ListedValuesDict:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [value]

    def __getitem__(self, key):
        result = str(self.data[key][0])
        for value in self.data[key][1:]:
            result += ", " + str(value)
        return result


l_dict = ListedValuesDict()
l_dict[1] = 'a'
l_dict[1] = 'b'
print(l_dict[1])  # a, b
У цьому прикладі ми створили власний клас, який веде себе як словник. ListedValuesDict значення зберігає до списку і вже цей список зберігає як значення ключа. Головна відмінність від словника у тому, що ListedValuesDict не дозволяє перезаписувати значення, завжди додаватиме нове значення в кінець списку. І при отриманні значення повертає рядок, складений із значень у списку.
'''

'''
TASK 4. Реалізуйте клас Vector. Властивість coordinates визначає координати вектора і є екземпляром класу Point. Нагадаємо, що вектором називають спрямований відрізок з початком та кінцем. Початок у нас буде в точці (0, 0), а кінець вектора ми задаватимемо атрибутом coordinates.

Реалізуйте можливість звертатися до координат екземпляра класу Vector через квадратні дужки:

vector = Vector(Point(1, 10))

print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10

vector[0] = 10  # Встановлюємо координату x вектора 10

print(vector[0])  # 10
print(vector[1])  # 10
Щоб отримати значення, використовуючи квадратні дужки об'єкта print(vector[0]), реалізуйте метод __getitem__ у класу Vector.

Для запису значення координат вектора через індекс, як vector[0] = 10, реалізуйте метод __setitem__ у класу Vector.

Звернення до координати x проводиться за індексом 0, а звернення до координати y - за індексом 1.
'''


# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         elif index == 1:
#             self.coordinates.y = value
#         else:
#             raise IndexError("Index out of range. Use 0 for x or 1 for y.")

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         elif index == 1:
#             return self.coordinates.y
#         else:
#             raise IndexError("Index out of range. Use 0 for x or 1 for y.")


# vector = Vector(Point(1, 10))

# print(vector.coordinates.x)  # 1
# print(vector.coordinates.y)  # 10

# vector[0] = 10  # Встановлюємо координату x вектора 10

# print(vector[0])  # 10
# print(vector[1])  # 10

'''
Коли ви в інтерактивному режимі роботи з Python хочете побачити вміст деякого об'єкта, ви просто пишете його ім'я в консолі та інтерпретатор виводить рядком подання цього об'єкта.

l = [1, 2]
l
У консолі ви побачите [1, 2].

За цей механізм внутрішнього читального уявлення об'єктів відповідає магічний метод __repr__. Цей метод приймає лише один аргумент (self звичайно) і повертати повинен рядок.

Якщо ви хочете виводити у випадках, коли програма повинна відобразити об'єкт, якусь корисну інформацію ви можете модифікувати цей метод. Наприклад, клас точки на площині в Декартових координатах:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point ({self.x}, {self.y})'


a = Point(1, 9)
a
Виконайте цей код у консолі Python і ви побачите Point(1, 9).

Дуже схожий на нього метод, який відповідає за те, як об'єкт конвертується в рядок — це метод __str__. Коли ви викликаєте функцію str та передаєте їй якийсь об'єкт, то насправді, цей об'єкт викликається методом __str__.

class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"
        return f'Hello! I am {self.name}'


bill = Human('Bill')
bill_str = str(bill)
print(bill_str)  # Hello! I am Bill
'''

'''
TASK 5. Реалізуйте для класу Point та Vector магічний метод __str__. Для класу Point метод повинен повертати рядок виду Point(x,y), а для класу Vector - рядок Vector(x,y), як у прикладі нижче (замість x,y необхідно підставити значення координат екземпляра класу):

'''


# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __str__(self):
#        return f"Vector({self.coordinates.x},{self.coordinates.y})"


# point = Point(1, 10)
# vector = Vector(point)

# print(point)  # Point(1,10)
# print(vector)  # Vector(1,10)

'''
Функтори — це об'єкти, які поводяться як функції у тому сенсі, що їх можна викликати та передавати їм аргументи. Функція у Python — це такий самий об'єкт, але у ньому реалізовано метод __call__, який відповідає за синтаксис виклику з круглими дужками.

class Adder:
    def __init__(self, add_value):
        self.add_value = add_value

    def __call__(self, value):
        return self.add_value + value


two_adder = Adder(2)
print(two_adder(5))  # 7
print(two_adder(4))  # 6

three_adder = Adder(3)
print(three_adder(5))  # 8
print(three_adder(4))  # 7
В цьому прикладі ми створили клас Adder, у якого є метод __call__. Тепер об'єкти цього класу можна викликати як функцію, надаючи їм аргументи. Ці виклики будуть викликати метод __call__ у об'єктів класу Adder.
'''

'''
TASK 6. Для екземпляра класу Vector реалізуйте функтор. Створіть для класу Vector метод __call__. Він має реалізувати наступну поведінку:

vector = Vector(Point(1, 10))

print(vector())  # (1, 10)
При виклику екземпляра класу як функції він повертає кортеж з координатами вектора.

Якщо при виклику ми передаємо параметр число, ми виконуємо добуток вектора на число — множимо кожну координату на вказане число та повертаємо кортеж з новими координатами вектора.

vector = Vector(Point(1, 10))

print(vector(5))  # (5, 50)
'''


# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, multiplier=None):
#         if multiplier is None:
#             return (self.coordinates.x, self.coordinates.y)
#         elif isinstance(multiplier, (int, float)):
#             return (self.coordinates.x * multiplier, self.coordinates.y * multiplier)
#         else:
#             raise ValueError("Multiplier must be a number.")

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"

'''
Усі математичні оператори можна перевизначити. Для цього є методи, відповідальні за кожний оператор:

__add__ додавання
__sub__ віднімання
__mul__ множення
__div__ ділення
__pow__ зведення в ступінь
та інші. Перевизначення математичних операторів може стати зручним інструментом. Наприклад, створимо клас словників, які підтримують операції додавання та віднімання:

from collections import UserDict
from random import randrange


class MyDict(UserDict):
    def __add__(self, other):
        self.data.update(other)
        return self

    def __sub__(self, other):
        for key in other:
            if key in other:
                self.data.pop(key)
        return self


d1 = MyDict({1: 'a', 2: 'b'})
d2 = MyDict({3: 'c', 4: 'd'})

d3 = d1 + d2
print(d3)  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

d4 = d3 - d2
print(d4)  # {1: 'a', 2: 'b'}
Синтаксис простий і код досить виразний, але треба бути акуратним з перевизначенням математичних операторів, зазвичай така поведінка неочевидна і може навпаки заплутати.
'''
'''
TASK 7. Реалізуйте для класу Vector операції додавання та віднімання векторів. Тобто перевизначите для нього математичні оператори __add__ та __sub__

Є два вектори: a з координатами (x1, y1) та b з координатами (x2, y2).

Тоді додавання векторів b + a - це новий вектор з координатами (x2 + x1, y2 + y1). Віднімання – зворотна операція, b - a - це новий вектор з координатами (x2 - x1, y2 - y1)

Приклад коду:

vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

vector3 = vector2 + vector1
vector4 = vector2 - vector1

print(vector3)  # Vector(11,20)
print(vector4)  # Vector(9,0)
'''

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, other):
#         if isinstance(other, Vector):
#             new_x = self.coordinates.x + other.coordinates.x
#             new_y = self.coordinates.y + other.coordinates.y
#             return Vector(Point(new_x, new_y))
#         else:
#             raise TypeError("Operand must be an instance of Vector")
    
#     def __sub__(self, other):
#         if isinstance(other, Vector):
#             new_x = self.coordinates.x - other.coordinates.x
#             new_y = self.coordinates.y - other.coordinates.y
#             return Vector(Point(new_x, new_y))
#         else:
#             raise TypeError("Operand must be an instance of Vector")
 
#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"


'''
TASK 8. Реалізуйте для класу Vector операцію скалярного добутку векторів. Тобто перевизначте для нього математичний оператор __mul__

Є два вектори: a з координатами (x1, y1) та вектор b з координатами (x2, y2).

Тоді скалярний добуток векторів b*a - це таке число x2*x1+y2*y1.

Приклад коду:

vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

scalar = vector2 * vector1

print(scalar)  # 110
'''


# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x, y))

#     def __mul__(self, other):
#         if isinstance(other, Vector):
#             return (self.coordinates.x * other.coordinates.x) + (self.coordinates.y * other.coordinates.y)
#         else:
#             raise TypeError("Operand must be an instance of Vector")

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"

'''
TASK 9. Перш ніж ми приступимо до операцій порівняння векторів, реалізуйте метод визначення довжини вектора - len для класу Vector

Для вектора a з координатами (x1, y1) його довжина визначається за такою формулою:

(x1 ** 2 + y1 ** 2) ** 0.5.

Приклад коду:

vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

print(vector1.len())  # 10.04987562112089
print(vector2.len())  # 14.142135623730951
'''

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x, y))

#     def __mul__(self, vector):
#         return (
#                 self.coordinates.x * vector.coordinates.x
#                 + self.coordinates.y * vector.coordinates.y
#         )

#     def len(self):
#         return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"

'''
Операції порівняння, як і інші оператори, мають свої "магічні" методи:

__eq__(self, other) — визначає поведінку під час перевірки на відповідність (==).
__ne__(self, other) — визначає поведінку під час перевірки на невідповідність. !=.
__lt__(self, other) — визначає поведінку під час перевірки на менше <.
__gt__(self, other) — визначає поведінку під час перевірки на більше >.
__le__(self, other) — визначає поведінку під час перевірки на менше-дорівнює <=.
__ge__(self, other) — визначає поведінку під час перевірки на більше-дорівнює >=.
Якщо вам потрібно, щоб ваш об'єкт був порівнянний, ви можете реалізувати ці шість методів і тоді будь-яка перевірка на порівняння працюватиме:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y


Point(0, 0) == Point(0, 0)  # True
Point(0, 0) != Point(0, 0)  # False
Point(0, 0) < Point(1, 0)  # False
Point(0, 0) > Point(0, 1)  # False
Point(0, 2) >= Point(0, 1)  # True
Point(0, 0) <= Point(0, 0)  # True
'''

'''
TASK 10. Реалізуйте всі методи порівняння для класу Vector. З метою спрощення порівнювати екземпляри класу Vector будемо тільки за їх довжиною, використовуючи метод len, не враховуючи напрямок векторів.

Приклад коду:

vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(3, 10))

print(vector1 == vector2)  # False
print(vector1 != vector2)  # True
print(vector1 > vector2)  # False
print(vector1 < vector2)  # True
print(vector1 >= vector2)  # False
print(vector1 <= vector2)  # True
'''


# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x, y))

#     def __mul__(self, vector):
#         return (
#             self.coordinates.x * vector.coordinates.x
#             + self.coordinates.y * vector.coordinates.y
#         )

#     def len(self):
#         return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"

#     def __eq__(self, other):
#         return self.len() == other.len()

#     def __ne__(self, other):
#         return self.len() != other.len()

#     def __lt__(self, other):
#         return self.len() < other.len()

#     def __gt__(self, other):
#         return self.len() > other.len()

#     def __le__(self, other):
#         return self.len() <= other.len()

#     def __ge__(self, other):
#         return self.len() >= other.len()


'''
Протокол ітератора у Python реалізований за допомогою методу __iter__. Цей метод має повертати ітератор. Ітератором може бути будь-який об'єкт, який має метод __next__, який за кожного виклику повертає значення. Щоб створити ітератор, достатньо реалізувати метод __next__.

Наприклад створимо клас, яким можна ітеруватися Iterable та клас ітератор:

class Iterable:
    MAX_VALUE = 10

    def __init__(self):
        self.current_value = 0

    def __next__(self):
        if self.current_value < Iterable.MAX_VALUE:
            self.current_value += 1
            return self.current_value
        raise StopIteration


class CustomIterator:
    def __iter__(self):
        return Iterable()


c = CustomIterator()
for i in c:
    print(i)
Зверніть увагу, що метод __next__ повинен викликати виняток StopIteration, щоб вказати, що ітерування завершено, інакше цикл for за таким об'єктом буде нескінченний.

Розглянемо докладніше алгоритм роботи ітератора.

Інтерпретатор python зустрічає ітераційний контекст і об'єкт, що ітерується в цьому контексті.

c = CustomIterator()  # створено об'єкт, що ітерується.
for i in c:  # зустрівся ітераційний контекст (цикл for) та об'єкт, що ітерується, в ньому, екземпляр класу c
    print(i)
Правила роботи інтерпретатора в такій ситуації вказує для ітерованого об'єкта c отримати ітератор - це викликати його метод __iter__, який повертає об'єкт ітератора Iterable(). Після цього викликати для об'єкта ітератора Iterable() його метод __next__. Метод __next__ повертає щось, що передається в змінну циклу (у нашому випадку - послідовність чисел від 1 до 10).

На наступному кроці ітерації (у циклі for) для вже чинного об'єкта ітератора Iterable() викликається ще раз його метод __next__ (точно так же, як і на попередньому кроці) і результат виклику так само присвоюється змінній циклу i і передається у роботу тіла циклу.

Метод __next__ стежить за кількістю можливих викликів себе і коли ліміт вичерпаний, а в нашому випадку це визначається параметром MAX_VALUE, генерує виняток StopIteration. Це сигнал для інтерпретатора до завершення ітераційного контексту — ітерування в циклі for припиняється. Більше не буде викликатись метод __next__ для екземпляра ітератора та управління передається рядку, який є наступним по черзі за ітераційним контекстом, у нашому випадку йдеться про рядок після тіла циклу for.
'''

'''
TASK 11. Необхідно реалізувати клас RandomVectors, який зможе створювати об'єкт, що ітерується, і дозволяти ітеруватися по випадковим векторам.

Формат класу:

RandomVectors(max_vectors: int, max_points: int) -> Iterable(max_vectors, max_points)
де:

max_vectors — визначає максимальну кількість елементів (примірників класу Vector) в ітерованій послідовності
max_points — визначає максимальне значення для координат x та y (в діапазоні 0...max_points)
Щоб екземпляри класу RandomVectors були об'єктами, що ітеруються, в класі повинен бути реалізований метод __iter__, який повертає ітератор. Ітератор – це будь-який об'єкт, який на кожному кроці ітерації (крок ітерації – це виклик методу next() для цього ітератора) повертає таке значення - і так до вичерпання кількості ітерацій (визначається параметром max_vectors).

У нашому випадку ітератором буде клас Iterable, у якому необхідно реалізувати метод __next__. Він у конструкторі отримує ті ж параметри max_vectors та max_points, що і клас RandomVectors.

Метод __next__ повинен видавати кожне наступне значення зі списку self.vectors. Створіть у конструкторі набір випадкових векторів self.vectors завдовжки max_vectors за допомогою randrange. Атрибут current_index вказівник-індекс на поточний вектор зі списку vectors, необхідний для ітерування.

Приклад роботи класу `RandomVectors:

vectors = RandomVectors(5, 10)

for vector in vectors:
    print(vector)
Вивід має бути схожим на цей:

Vector(7,7)
Vector(0,0)
Vector(8,9)
Vector(1,9)
Vector(6,6)
Деталізуємо наше завдання:

Клас RandomVectors повинен мати метод __iter__, який має повернути об'єкт ітератора (клас Iterable)
Об'єкт ітератора (примірник класу Iterable) повинен мати метод __next__
Метод __next__ стежить за кількістю можливих кроків ітерації, вони визначаються параметром max_vectors
Якщо ми вичерпали можливі кроки, то метод __next__ генерує виняток StopIteration
В іншому випадку метод __next__ повертає вектор з випадковими координатами (примірник класу Vector), розмір координат вектора визначається параметром max_points.
'''

class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        return (
            self.coordinates.x * vector.coordinates.x
            + self.coordinates.y * vector.coordinates.y
        )

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

    def __eq__(self, vector):
        return self.len() == vector.len()

    def __ne__(self, vector):
        return self.len() != vector.len()

    def __lt__(self, vector):
        return self.len() < vector.len()

    def __gt__(self, vector):
        return self.len() > vector.len()

    def __le__(self, vector):
        return self.len() <= vector.len()

    def __ge__(self, vector):
        return self.len() >= vector.len()


class RandomVectors:
    def __init__(self, max_vectors: int, max_points: int):
        self.max_vectors = max_vectors
        self.max_points = max_points

    def __iter__(self):
        return Iterable(self.max_vectors, self.max_points)


class Iterable:
    def __init__(self, max_vectors: int, max_points: int):
        self.max_vectors = max_vectors
        self.max_points = max_points
        self.current_index = 0
        self.vectors = [
            Vector(Point(randrange(0, max_points + 1),
                   randrange(0, max_points + 1)))
            for _ in range(max_vectors)
        ]

    def __next__(self):
        if self.current_index < self.max_vectors:
            vector = self.vectors[self.current_index]
            self.current_index += 1
            return vector
        raise StopIteration
