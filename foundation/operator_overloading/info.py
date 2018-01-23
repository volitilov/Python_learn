Operator overloading ::::::::::::::::::::::::::::::::::::::::::::::::

# 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

__new__(cls[, ...])	
# управляет созданием экземпляра. В качестве обязательного 
# аргумента принимает класс (не путать с экземпляром). Должен
# возвращать экземпляр класса для его последующей передачи
# методу __init__.

__init__(self[, ...])
# как уже было сказано выше, конструктор.

__del__(self)
# вызывается при удалении объекта сборщиком мусора.

__repr__(self)
# вызывается встроенной функцией repr; возвращает "сырые" данные, 
# использующиеся для внутреннего представления в python.

__str__(self) 
# вызывается функциями str, print и format. Возвращает строковое 
# представление объекта.

__bytes__(self) 
# вызывается функцией bytes при преобразовании к байтам.

__format__(self, format_spec) 
# используется функцией format (а также методом format у строк).

__lt__(self, other) 
# x < y вызывает x.__lt__(y).

__le__(self, other)
# x ≤ y вызывает x.__le__(y).

__eq__(self, other) 
# x == y вызывает x.__eq__(y).

__ne__(self, other) 
# x != y вызывает x.__ne__(y)

__gt__(self, other) 
# x > y вызывает x.__gt__(y).

__ge__(self, other) 
# x ≥ y вызывает x.__ge__(y).

__hash__(self) 
# получение хэш-суммы объекта, например, для добавления в словарь.

__bool__(self) 
# вызывается при проверке истинности. Если этот метод не определён, 
# вызывается метод __len__ (объекты, имеющие ненулевую длину, 
# считаются истинными).

__getattr__(self, name) 
# вызывается, когда атрибут экземпляра класса не найден в обычных 
# местах (например, у экземпляра нет метода с таким названием).

__setattr__(self, name, value) 
# назначение атрибута.

__delattr__(self, name)
# удаление атрибута (del obj.name).

__call__(self[, args...]) 
# вызов экземпляра класса как функции.

__len__(self) 
# длина объекта.

__getitem__(self, key) 
# доступ по индексу (или ключу).

__setitem__(self, key, value) 
# назначение элемента по индексу.

__delitem__(self, key) 
# удаление элемента по индексу.

__iter__(self) 
# возвращает итератор для контейнера.

__reversed__(self) 
# итератор из элементов, следующих в обратном порядке.

__contains__(self, item) 
# проверка на принадлежность элемента контейнеру (item in self).

#	Перегрузка арифметических операторов..............................

__add__(self, other) 
# сложение. x + y вызывает x.__add__(y).

__sub__(self, other)
# вычитание (x - y).

__mul__(self, other)
# умножение (x * y).

__truediv__(self, other) 
# деление (x / y).

__floordiv__(self, other)
# целочисленное деление (x // y).

__mod__(self, other)
# остаток от деления (x % y).

__divmod__(self, other)
# частное и остаток (divmod(x, y)).

__pow__(self, other[, modulo])
# возведение в степень (x ** y, pow(x, y[, modulo])).

__lshift__(self, other) 
# битовый сдвиг влево (x << y).

__rshift__(self, other) 
# битовый сдвиг вправо (x >> y).

__and__(self, other) 
# битовое И (x & y).

__xor__(self, other) 
# битовое ИСКЛЮЧАЮЩЕЕ ИЛИ (x ^ y).

__or__(self, other) 
# битовое ИЛИ (x | y).

__radd__(self, other)

__rsub__(self, other)

__rmul__(self, other)

__rtruediv__(self, other)

__rfloordiv__(self, other)

__rmod__(self, other)

__rdivmod__(self, other)

__rpow__(self, other)

__rlshift__(self, other)

__rrshift__(self, other)

__rand__(self, other)

__rxor__(self, other)

__ror__(self, other)

# делают то же самое, что и арифметические операторы, перечисленные выше, 
# но для аргументов, находящихся справа, и только в случае, если для 
# левого операнда не определён соответствующий метод.

#	Например, операция x + y будет сначала пытаться вызвать x.__add__(y), и 
#	только в том случае, если это не получилось, будет пытаться вызвать 
#	y.__radd__(x). Аналогично для остальных методов.

__iadd__(self, other)  # +=

__isub__(self, other) # -=

__imul__(self, other) # *=

__itruediv__(self, other) # /=

__ifloordiv__(self, other) # //=

__imod__(self, other) # %=

__ipow__(self, other[, modulo]) # **=

__ilshift__(self, other) # <<=

__irshift__(self, other) # >>=

__iand__(self, other) # &=

__ixor__(self, other) # ^=

__ior__(self, other) # |=

__neg__(self) # унарный -.

__pos__(self) # унарный +.

__abs__(self) # модуль (abs()).

__invert__(self) # инверсия (~).

__complex__(self) # приведение к complex.

__int__(self) # приведение к int.

__float__(self) # приведение к float.

__round__(self[, n]) # округление.

__enter__(self), __exit__(self, exc_type, exc_value, traceback)
# реализация менеджеров контекста.