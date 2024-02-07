# 1. Напишіть програму, яка приймає два цілих числа від користувача і виводить суму діапазону чисел між ними
print(sum(range(int(input('Enter first number: ')), int(input('Enter second number: ')))))

# 2. Напишіть програму, для знаходження суми всіх парних чисел від 1 до 100.
print([x for x in range(1, 101) if not x % 2])

# 3. Напишіть програму, яка приймає рядок від користувача і виводить кожну літеру рядка на окремому рядку.
print('\n'.join(list(input('Enter your word: '))))

# 4. Напишіть програму, яка створює список цілих чисел та виводить новий список, який містить лише парні числа з вихідного списку.
from random import randint as rnd
lst = [rnd(0,100) for _ in range(100)]
print([x for x in lst if not x % 2])

# 5. Напишіть функцію, яка приймає список рядків від користувача і повертає новий список, що містить лише рядки, що починаються з великої літери.
number_of_strings = 5
lst = [input('Enter your string: ') for _ in range(number_of_strings)]
[print(x) for x in lst if x[0].isupper()]

# 6. Напишіть функцію, яка приймає список рядків від користувача і повертає новий список, що містить лише рядки, які містять слово "Python".
number_of_strings = 5
str_to_search = 'Python'
lst = [input('Enter your string: ') for _ in range(number_of_strings)]
[print(x) for x in lst if str_to_search in x]

# 7. (додаткове на кристалики)Напишіть програму, яка створює словник, де ключами є слова, а значеннями - їхні визначення. Дозвольте користувачу додавати, видаляти та шукати слова у цьому словнику.
number_of_words = 3
word_dict = {input('Enter your word: '): input('Enter word description: ') for _ in range(number_of_words)}
print(word_dict)
menu = '''  
    MENU:
1 - Add word
2 - Delete word
3 - Search word
4 - Exit

Enter your choice: '''
while True:
    selection = input(menu)
    match selection:
        case '1':
            word_dict[input('Enter your word: ')] = input('Enter word description: ')
        case '2':
            del word_dict[input('Enter your word: ')]
        case '3':
            print(word_dict.get(input('Enter your word: '), 'Not found'))
        case _:
            print('Exiting...')
            break


# 8. (додаткове на кристалики)Використовуючи лямбдафункцію, напишіть вираз, який сортує список кортежів за другим елементом кожного кортежу (наприклад, [(1, 3), (3, 2), (2, 1)]).
#
lst = [(1, 3), (3, 2), (2, 1)]
print(sorted(lst, key=lambda x: x[1]))