import re


class Str:
    def __init__(self, num=input('Какой тест вы хотите выбрать? ')):
        self.st = ''
        for i in open(num):
            self.st += i

    def get_test(self) -> str:
        return self.st


class Emoji:
    def __init__(self, isu=int(input('Введите ваш ИСУ для определения персонального эмодзи: '))):
        eyes = ('8', ';', 'X', ':', '=', '[')
        nose = ('-', '<', '-{', '<{')
        mouth = ('(', ')', 'P', '|', "\\", '/', 'O', '=')
        self.res = eyes[isu % 6] + nose[isu % 4] + mouth[isu % 8]

    def get_Emoji(self) -> str:
        return self.res


class Re(Emoji, Str):
    REG = Emoji().get_Emoji()
    reg = re.findall(REG, Str().get_test())

    def num_Of_Emojis(self) -> int:
        return len(self.reg)


print(f'Your message: {Str().get_test()}\n' + f'Your Emoji: {Emoji().get_Emoji()}\n' + f'The number of your emojis: \
{Re().num_Of_Emojis()}')
