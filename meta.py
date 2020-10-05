class Base:
    val = 42

    def do_one_thing(self):
        # Returns one thing
        raise NotImplementedError

    def do_another_thing(self, *args, **kwargs):
        # does something
        raise NotImplementedError


class AnotherType(type):
    pass


class MyClass(Base, metaclass=AnotherType):
    val = 50

    def do_one_thing(self):
        return '1 thing'

    def do_another_thing(self, *args, **kwargs):
        return f'{args} | {kwargs}'


m = MyClass()
m.val = 13
print(MyClass.val, m.val)

print(m.do_one_thing())
m.do_another_thing()
print(m.do_another_thing(1, 2, 3, abc='qwe'))

# print(m.__dir__())

print(MyClass)
print(type(MyClass))

# print(Base.__class__)
