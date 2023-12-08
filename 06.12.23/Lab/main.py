'''
Завдання 1
Створіть програму роботи зі словником.
Наприклад, англо-іспанський, французько-німецький
або інша мовна пара.
Програма має:
■ надавати початкове введення даних для словника;
■ відображати слово та його переклади;
■ дозволяти додавати, змінювати, видаляти
переклади слова;
■ дозволяти додавати, змінювати, видаляти слово;
■ відображати топ-10 найпопулярніших слів
(визначаємо популярність спираючись на лічильник
звернень);
■ відображати топ-10 найнепопулярніших слів
(визначаємо непопулярність спираючись на лічильник
звернень).
Використовуйте дерево для виконання цього
завдання.
'''


class Node:
    def __init__(self, word, translations=None):
        self.word = word
        self.left = None
        self.right = None
        self.translations = translations if translations else []
        self.count = 0


class Translator:
    def __init__(self):
        self.root = None
        self._top = {}
        self._un_top = {}

    def add(self, word, translation, flag=True):
        self.root = self._add(self.root, word, translation, flag)

    def _add(self, node, word, translation, flag=True):
        if node is None:
            return Node(word, [translation])
        if word < node.word:
            node.left = self._add(node.left, word, translation)
        elif word > node.word:
            node.right = self._add(node.right, word, translation)
        else:
            if flag:
                node.translations.append(translation)
            else:
                node.translations.clear()
                node.translations.append(translation)
        return node

    def _add_to_top(self, word, count):
        if len(self._top) > 9:
            tmp = sorted(list(self._top.items()), key=lambda x: x[1])[-9:]
            self._top = dict(tmp)
        self._top[word] = count

    def top(self):
        return self._top

    def untop(self):
        self._untop(self.root)
        return self._un_top

    def _untop(self, node):
        if node is not None and len(self._un_top) < 10:
            self._untop(node.left)
            if node.count == 0:
                self._un_top[node.word] = node.count
            self._untop(node.right)

    def translate(self, word):
        node: Node = self._search(self.root, word)
        if node:
            node.count += 1
            self._add_to_top(word, node.count)
            return f'{word} ---> {node.translations}', node.count
        else:
            return f"No translations found for the word '{word}'."

    def _search(self, node, word):
        if node is None or word == node.word:
            return node
        if word < node.word:
            return self._search(node.left, word)
        return self._search(node.right, word)

    def _find_min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def _delete_word(self, root, word):
        if root is None:
            return root

        if word < root.word:
            root.left = self._delete_word(root.left, word)
        elif word > root.word:
            root.right = self._delete_word(root.right, word)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.key = self._find_min_node(root.right).word
            root.right = self._delete_word(root.right, root.word)

        return root

    def remove_word(self, word):
        self.root = self._delete_word(self.root, word)


test = Translator()
test.add('hallo', 'Привет')
test.add('hallo', 'Здравствуйте')
test.add('street', 'улица')
test.add('bed', 'кровать')
test.add('window', 'окно')
test.add('table', 'стол')
test.add('lamp', 'лампа')
test.add('apple', 'яблоко')
test.add('snow', 'снег')
test.add('rain', 'дождь')
test.add('sea', 'море')
test.add('floor', 'пол')
test.add('time', 'время')
test.add('maus', 'мышь')
test.add('sofa', 'диван')
test.add('monitor', 'монитор')
test.add('pen', 'ручка')
test.add('pencil', 'карандаш')
test.add('ship', 'пароход')
test.add('hand', 'рука')
test.add('pineapple', 'ананас')
test.add('fish', 'рыба')
test.add('car', 'машина')


print(test.translate('hallo')[0])

test.add('hallo', 'привет', False)

print(test.translate('hallo')[0])
print(test.translate('street')[0])
print(test.translate('street')[0])
print(test.translate('street')[0])
print(test.translate('street')[0])
print(test.translate('bed')[0])
print(test.translate('bed')[0])
print(test.translate('sofa')[0])
print(test.translate('snow')[0])
print(test.translate('maus')[0])
print(test.translate('sea')[0])
print(test.translate('rain')[0])
print(test.translate('window')[0])
print(test.translate('table')[0])
print(test.translate('lamp')[0])
print(test.translate('table')[0])
print(test.translate('pen')[0])
print(test.translate('pen')[0])
print(test.translate('monitor')[0])

print()
print('Top 10:', test.top())
print()
print('UnTop 10:', test.untop())
print()
print(test.translate('maus')[0])
print()
test.remove_word('maus')
print(test.translate('maus'))
