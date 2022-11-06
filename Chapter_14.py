class Rectangle:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("""{} by {}""".format(self.width, self.len))


r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

# print(Rectangle.recs)


class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


lion = Lion("Dilbert")
# print(lion)


class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)


x = AlwaysPositive(-20)
y = AlwaysPositive(10)


# print(x + y)


class Person:
    def __init__(self):
        self.name = 'Bob'


bob = Person()
same_bob = bob
# print(bob is same_bob)

another_bob = Person()
# print(bob is another_bob)


# x = 10
# if x is None:
#     print("x is None :( ")
# else:
#     print("x is not None")
#
#
# x = None
# if x is None:
#     print("x is None :(")
# else:
#     print("x is not None ")


class Square:
    square_list = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.square_list.append((self.name, self.length))

    def print_size(self):
        print("""{} by {} by {} by {}""".format(self.length,
                                                self.length,
                                                self.length,
                                                self.length))


def compare(sq1, sq2):
    return sq1.length == sq2.length


s1 = Square("s1", 10)
s2 = Square("s2", 3)
s3 = Square("s3", 13)
s4 = Square("s4", 10)

# print(Square.square_list)
# s3.print_size()
# print(compare(s1, s2))
