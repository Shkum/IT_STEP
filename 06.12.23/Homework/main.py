'''
Завдання 1
Реалізуйте базу даних зі штрафами податкової
інспекції. Ідентифікувати кожну конкретну людину буде
персональний ідентифікаційний код. В однієї людини може
бути багато штрафів.
Реалізуйте:
1. Повний друк бази даних; ---
2. Друк даних за конкретним кодом; ---
3. Друк даних за конкретним типом штрафу; ---
4. Друк даних за конкретним містом; ---
5. Додавання нової людини з інформацією про неї; ----
6. Додавання нових штрафів для вже існуючого запису; ---
7. Видалення штрафу;
8. Заміна інформації про людину та її штрафи. ---
Використайте дерево для реалізації цього завдання.
'''
from dataclasses import dataclass


@dataclass
class Person:
    id: str
    place: str
    penalties: list

    def __str__(self):
        return f'Person: {self.id}, Place: {self.place}, Penalties: {self.penalties}'

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def __eq__(self, other):
        return self.id == other.id

    def add_penalty(self, penalty):
        self.penalties.extend(penalty)

    def del_penalty(self, penalty):
        if penalty in self.penalties:
            self.penalties.remove(penalty)

    def if_has_penalty(self, penalty):
        if penalty in self.penalties:
            return True
        else:
            return False

    def is_place(self, place):
        return place == self.place

    def change_id(self, new_id):
        self.id = new_id


class Node:
    def __init__(self, person: Person):
        self.person = person
        self.right = None
        self.left = None


class Tree:

    def __init__(self):
        self._root = None

    def add(self, person: Person):
        self._root = self._add(self._root, person)

    def _add(self, node, person: Person):
        if node is None:
            return Node(person)
        if person < node.person:
            node.left = self._add(node.left, person)
        elif person > node.person:
            node.right = self._add(node.right, person)
        else:
            node.person.add_penalty(person.penalties)
        return node

    def search(self, ids=None, place=None, penalty=None):
        self._search(self._root, ids, place, penalty)

    def _search(self, node, ids=None, place=None, penalty=None):
        if node:
            self._search(node.left, ids, place, penalty)
            if ids == node.person.id or place == node.person.place or penalty in node.person.penalties:
                print(node.person)
            self._search(node.right, ids, place, penalty)

    def change_id(self, old_id, new_id):
        self._change_id(self._root, old_id, new_id)

    def _change_id(self, node, old_id, new_id):
        if node:
            self._change_id(node.left, old_id, new_id)
            if old_id == node.person.id:
                node.person.change_id(new_id)
            self._change_id(node.right, old_id, new_id)

    def print_all(self):
        print("All persons in the database:")
        self._print_all(self._root)

    def _print_all(self, node):
        if node:
            self._print_all(node.left)
            print(node.person)
            self._print_all(node.right)

    def del_penalty(self, person, penalty):
        self._del_penalty(self._root, person, penalty)

    def _del_penalty(self, node, person, penalty):
        if node:
            self._del_penalty(node.left, person, penalty)
            if person == node.person:
                if penalty in node.person.penalties:
                    node.person.del_penalty(penalty)
            self._del_penalty(node.right, person, penalty)


database = Tree()
print('Add persons to database...')
database.add(Person('3533521', 'Odesa', ['red light']))
database.add(Person('3557332', 'Lviv', ['traffic']))
database.add(Person('5832533', 'Kherson', ['cross line']))
database.add(Person('8687634', 'Kyiv', ['double line']))
print()
database.print_all()
print('\nSearch by place...')
database.search(place='Odesa')
print('\nSearch by ID...')
database.search(ids='8687634')
print('\nSearch by penalty...')
database.search(penalty='traffic')
print()
print('\nAdd penalty...')
database.add(Person('3533521', 'Odesa', ['RED', 'Traffic']))
database.print_all()
print('\nChange ID...')
database.change_id('8687634', 'test_id')
database.print_all()
print('\nDelete penalty...')
database.del_penalty(Person('3533521', 'Odesa', ['red light']), 'red light')
database.del_penalty(Person('3533521', 'Odesa', ['red light']), 'RED')
print()
database.print_all()
