'''Завдання 3
Реалізуйте метаклас, що забороняє спадкування від
певних класів чи змінює порядок спадкування'''


class InheritanceRestrictionMeta(type):
    def __new__(cls, name, bases, dct):
        forbidden_classes = (ForbiddenClass1, ForbiddenClass2)
        if any(base in forbidden_classes for base in bases):
            bases = tuple(b for b in bases if b not in forbidden_classes)
            print("Inheritance from ForbiddenClass is not allowed. Forbidden Class removed from inheritance list")
        return super().__new__(cls, name, bases, dct)


class ForbiddenClass1:
    pass


class ForbiddenClass2:
    pass


class BaseClass:
    pass


class DerivedClass(BaseClass, ForbiddenClass1, metaclass=InheritanceRestrictionMeta):
    pass


print(DerivedClass.__mro__)