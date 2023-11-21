'''
Завдання 3
Завдання для функторів. Створіть клас TextModifier,
який може здійснювати різні операції над текстом:
• Операція перетворення тексту у верхній регістр.
• Операція перетворення тексту у нижній регістр.
• Операція видалення пробілів у тексті.
• Операція шифрування тексту за допомогою зсуву
вліво на задану кількість символів.
'''
from dataclasses import dataclass


@dataclass
class Encoder:
    _text: str

    def _encode(self, flag=True, symbol_count=5):
        symbol_count *= -1 if flag else 1
        result = ''
        for letter in self._text:
            result += chr(ord(letter) + symbol_count)
        return result


@dataclass
class TextModifier(Encoder):

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text):
        print('\n ---> Text successfully updated\n')
        self._text = new_text

    def __call__(self, *command):
        symbol_count = 5 if len(command) == 1 else command[1]
        match command[0]:
            case 'upper':
                return self._text.upper()
            case 'lower':
                return self._text.lower()
            case 'remove_space':
                return self._text.replace(' ', '')
            case 'code':
                self._text = self._encode(True, symbol_count)
                return self._text
            case 'encode':
                self._text = self._encode(False, symbol_count)
                return self._text


txt = TextModifier('Test Test Text')
print(txt('upper'))
print(txt('lower'))
print(txt('remove_space'))
print(txt('code'))
print(txt('encode'))
print(txt('code', 30))
print(txt('encode', 30))
txt.text = 'This is new text'
print(txt.text)
