import re


class Str:
    def __init__(self, txt=input('Введите номер теста: ')):  # Данный класс возвращает текст из файла
        self.stroka = ''
        for i in open(txt):
            self.stroka += i

    def get_Message(self):
        return self.stroka


class Re(Str):

    def proverka(self):
        CntGlag = 0
        NumOfGlag = []
        str1 = ''
        for i in Str().get_Message():
            str1 += i
        str1 += '/'
        for r in range(len(str1)):
            if str1[r] in re.findall(r'[аеёиоуыэюяАЕËИОУЫЭЮЯ]', Str().get_Message()):
                CntGlag += 1
            elif str1[r] == '/':
                NumOfGlag.append(CntGlag)
                CntGlag = 0

        return NumOfGlag

    def spisok(self):
        if Re().proverka() == [5, 7, 5]:
            return 'Хайку!'
        elif len(Re().proverka()) != 3:
            return 'Не хайку. Должно быть 3 строки.'
        elif Re().proverka() != [5, 7, 5]:
            return 'Не хайку.'


print(f'Вот ваше сообщение {Str().get_Message()}\n{Re().spisok()}')

