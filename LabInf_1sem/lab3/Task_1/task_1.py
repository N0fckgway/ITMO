import re


class Str:
    def __init__(self, num=input('Какой тест вы хотите выбрать? ')):
        self.st = ''
        for i in open(num):
            self.st += i

    def print1(self) -> str:
        return self.st


class Emoji:
    def __init__(self, isu=int(input('Введите ваш ИСУ для определения персонального эмодзи: '))):
        eyes = ('8', ';', 'X', ':', '=', '[')
        nose = ('-', '<', '-{', '<{')
        mouth = ('(', ')', 'P', '|', "\\", '/', 'O', '=')
        self.res = eyes[isu % 6] + nose[isu % 4] + mouth[isu % 8]

    def print2(self) -> str:
        return self.res


class Re(Emoji, Str):
    REG = Emoji().print2()
    reg = re.findall(REG, Str().print1())

    def print(self) -> int:
        return len(self.reg)


print('')
print(f'Your message: {Str().print1()}\n' + f'Your Emoji: {Emoji().print2()}\n' + f'The number of your emojis: \
{Re().print()}')
