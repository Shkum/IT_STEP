'''
Завдання 2
Користувач вводить з клавіатури набір рядків. Збережіть отримані рядки до двозв’язного списку. Після чого
покажіть меню, в якому запропонуєте користувачеві
набір пунктів:
1. Додати елемент до списку.
2. Видалити елемент зі списку.
3. Показати вміст списку.
4. Перевірити, чи є значення у списку.
5. Замінити значення у списку.
Дія виконується залежно від вибору користувача,
після чого меню з’являється знову.
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
            current = current.next

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
my_list.append("1")
my_list.append('2')
my_list.append('3')
my_list.append('4')
my_list.append('5')
print(my_list)

lst = []
st = ' '
while st:
    st = input("Enter strings divided by ENTER (empty string to stop): ")
    if len(st) > 0:
        lst.append(st)

for i in lst:
    my_list.append(i)

print(my_list)

old_value = input("Enter string to change: ")
new_value = input("Enter new string: ")

my_list.replace(old_value, new_value)
print(my_list)

my_list.delete('1')
print(my_list)

my_list.delete('3')
print(my_list)

my_list.delete('20')
print(my_list)

my_list.find_value('3')
my_list.find_value('4')

msg = ('\n     Please enter your choice:\n'
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
            val = input("Enter value to add: ")
            my_list.append(val)
        case '2':
            val = input("Enter value to delete: ")
            my_list.delete(val)
        case '3':
            pass
        case '4':
            val = input("Enter value to find: ")
            my_list.find_value(val)
        case '5':
            val = input("Enter value to replace: ")
            val_new = input("Enter new value: ")
            my_list.replace(val, val_new)
        case _:
            print('\nExiting...')
            break
    print(my_list)
