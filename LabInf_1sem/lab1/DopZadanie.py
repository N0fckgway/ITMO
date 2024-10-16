s = str(int(input("Введите число в Фибоначчиевой системе счисления: ")))[::-1]
fib = [1, 2]
sum = 0
des = 0
for i in range(0, len(s)):
    sum = fib[i] + fib[i + 1]
    fib.append(sum)

for p in range(len(s)):
    if s[p] == '1':
        des += fib[p]
des = str(des)
print("Ответ в десятичной системе счисления: " + des)
