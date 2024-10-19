import re


class Txt:
    def __init__(self, text=input()):
        self.siteOfCostBitcoin = ''
        for i in open(text):
            self.siteOfCostBitcoin += i

    def printTxt(self):
        s = ''.join(self.siteOfCostBitcoin)
        return s


class Parser:
    def __init__(self):
        Pars = re.search(r'(Bitcoin.+|Биткоин.+|Btc.+)(...........[0-9.,]+)', Txt().printTxt())
        if Pars:
            self.CostBit = Pars.group(2)

    def printBitcoin(self):
        return self.CostBit


print(Parser().printBitcoin())
