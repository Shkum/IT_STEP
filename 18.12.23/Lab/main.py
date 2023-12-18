z = '''
Завдання 4
Користувач вводить з клавіатури шлях до файлу та
слово для пошуку. Після чого запускається потік для
пошуку цього слова у файлі. Результат пошуку виведіть
на екран.
'''

from threading import Thread

# file = input('Enter file name: ')
file = 'txt.txt'

# word = input('Enter word to search: ')
word = 'слово'

with open(file, 'w', encoding='UTF-8') as f:
    f.write(z)


def search_word(word, file):
    with open(file, encoding='UTF-8') as f:
        res = f.read()
    if word in res.split():
        print(f'Word "{word}" found in index {res.index(word)}')
    else:
        print(f'Word "{word}" not found')


t = Thread(target=search_word, args=(word, file))

t.start()

t.join()

print('\nSearching completed')
