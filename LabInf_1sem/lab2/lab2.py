# exit() if len(chislo:=input()) != 7 else (XOR1:=(int(chislo[0]) + int(chislo[2]) + int(chislo[4]) + int(chislo[6])) % 2, XOR2:=(int(chislo[1]) + int(chislo[2]) + int(chislo[5]) + int(chislo[6])) % 2, XOR3:=(int(chislo[3]) + int(chislo[4]) + int(chislo[5]) + int(chislo[6])) % 2, s:= XOR1*1 + XOR2*2 + XOR3*4, print(chislo) if s == 0 else print(chislo[:s-1] + ('1' if chislo[s-1] == '0' else '0') + chislo[s:]), s)

chislo = input()
if len(chislo) != 7:
    print('error PISSYAT DVA, only 7 chars')
    exit()

XOR1 = (int(chislo[0]) + int(chislo[2]) + int(chislo[4]) + int(chislo[6])) % 2
XOR2 = (int(chislo[1]) + int(chislo[2]) + int(chislo[5]) + int(chislo[6])) % 2
XOR3 = (int(chislo[3]) + int(chislo[4]) + int(chislo[5]) + int(chislo[6])) % 2

s = XOR1 * 1 + XOR2 * 2 + XOR3 * 4
if s == 0:
    print(str(chislo))
else:
    print(chislo[:s-1] + ('1' if chislo[s-1] == '0' else '0') + chislo[s:], s)
