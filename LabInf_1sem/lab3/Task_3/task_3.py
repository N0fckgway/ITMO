import re


class Txt:
    def __init__(self, text=input()):
        self.siteOfCostBitcoin = ''
        for i in open(text):
            self.siteOfCostBitcoin += i

    def get_Txt(self):
        return ''.join(self.siteOfCostBitcoin)


class Parser:
    def __init__(self):
        Pars = re.search(r'(Bitcoin.*₽)([\d,.]+\s)', Txt().get_Txt())
        if Pars:
            self.CostBit = Pars.group(2)

    def print_Bitcoin(self):
        return self.CostBit


print(Parser().print_Bitcoin())
