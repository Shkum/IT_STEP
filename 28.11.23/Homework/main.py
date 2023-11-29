'''
Завдання
Користувач вводить з клавіатури набір чисел. Отримані
числа необхідно зберегти до списку (тип списку оберіть в залежності від поставленого нижче завдання). Після чого покажіть меню, в якому запропонуєте користувачеві набір пунктів:
1. Додати нове число до списку (якщо таке число існує у
списку, потрібно вивести повідомлення про це користувачеві без додавання числа).
2. Видалити усі входження числа зі списку (користувач вводить з клавіатури число для видалення)
3. Показати вміст списку (залежно від вибору користувача,
покажіть список з початку або з кінця)
4. Перевірити, чи є значення у списку
5. Замінити значення у списку (користувач визначає, чи
замінити тільки перше входження, чи всі)
Дія виконується залежно від вибору користувача, після
чого меню з’являється знову.
'''



class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return f'{self.data}'


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return f"{' <-> '.join(elements)}"

    def reverse(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.head = temp.prev
        return self

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def replace(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                print(f'Value "{old_data}" replaced with "{new_data}"')
            current = current.next

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                print(f'Value "{data}" deleted')
                return
            current = current.next
        print(f'Value "{data}" not found')

    def find_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                print(f'Value "{value}" found in LinkedList')
                return True
            current = current.next
        print(f'Value "{value}" not found')
        return False


my_list = DoubleLinkedList()

msg = ('\n     Please select action:\n'
       '1 - Add element to LinkedList\n'
       '2 - Delete  element from LinkedList\n'
       '3 - Show content of LinkedList\n'
       '4 - Check if value is in LinkedList\n'
       '5 - Replace value at LinkedList\n'
       '6 - Exit\n'
       '---> ')

while True:
    sel = input(msg)
    match sel:
        case '1':
            val = int(input("Enter number to add: "))
            my_list.append(val)
        case '2':
            val = int(input("Enter number to delete: "))
            my_list.delete(val)
        case '3':
            choice = int(input('Please select:\n0 - Normal order\n1 - Reversed order\n---> '))
            print(my_list.reverse() if choice else my_list)
            continue
        case '4':
            val = int(input("Enter number to find: "))
            my_list.find_value(val)
        case '5':
            val = int(input("Enter number to replace: "))
            val_new = int(input("Enter new number: "))
            my_list.replace(val, val_new)
        case _:
            print('\nExiting...')
            break
    print('\n', my_list)
