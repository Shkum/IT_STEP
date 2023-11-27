'''
Завдання 1
Користувач вводить з клавіатури набір чисел. Збережіть отримані числа до однозв’язного списку. Після
чого покажіть меню, в якому запропонуєте користувачеві
набір пунктів:
1. Додати елемент до списку.
2. Видалити елемент зі списку.
3. Показати вміст списку.
4. Перевірити, чи є значення у списку.
5. Замінити значення у списку.
Дія виконується залежно від вибору користувача,
після чого меню з’являється знову
'''


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f'[{self.data}] -> {self.next}'


node = Node(1)
current_node = node

for i in range(2, 10):
    new_node = Node(i ** 2)
    current_node.next = new_node
    current_node = new_node

print(node)

print()


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return f'{self.head}'

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def replace(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                print(f'Value {old_data} replaced with {new_data}')
                return
            current = current.next
        print(f'Value {old_data} not found')

    def delete(self, data):
        current = self.head
        prev = current
        while current:
            if current.data == data:
                if prev == current:
                    self.head = current.next
                    print(f'Value {data} deleted')
                    return
                if current.next is None:
                    prev.next = None
                    print(f'Value {data} deleted')
                    return
                prev.next = current.next
                print(f'Value {data} deleted')
                return
            prev = current
            current = current.next
        print(f'Value {data} not found')

    def find_vlue(self, value):
        current = self.head
        while current:
            if current.data == value:
                print(f'Value {value} found in LinkedList')
                return
            current = current.next
        print(f'Value {value} not found')


my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
print(my_list)

nums = input("Enter numbers divided by space: ")
for i in nums.split():
    my_list.append(int(i))

print(my_list)

old_value = int(input("Enter number to change: "))
new_value = int(input("Enter new value: "))

my_list.replace(old_value, new_value)
print(my_list)

my_list.delete(1)
print(my_list)

my_list.delete(3)
print(my_list)

my_list.delete(20)
print(my_list)

my_list.find_vlue(3)
my_list.find_vlue(4)
