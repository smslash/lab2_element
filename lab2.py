# 1. Четные числа
a, b = int(input()), int(input())
while a <= b:
    if a % 2 == 0:
        print(a, end=' ')
    a += 1

# 2. Минимальный делитель
a = int(input())
ans = a
i = a
while i >= 2:
    if a % i == 0:
        ans = i
    i -= 1
print(ans)

# 3. Делители числа
a = int(input())
for i in range (1, a + 1):
    if a % i == 0:
        print(i, end=' ')

# 4. Сумма чисел
a = int(input())
sum = 0
for i in range (0, a):
    x = int(input())
    sum += x
print(sum)

# 5. Перевод числа
a = input()
len_a = len(a)
a = int(a)
ans = 0
for i in range (0, len_a):
    if a % 10 == 1:
        ans += 2**i
    a //= 10
print(ans)

# 6. Степень
def power(a, b):
    return a**b

a = float(input())
n = int(input())
print(power(a, n))

# 7. Голосование
def Election(a, b, c):
    t = 0
    f = 0
    for i in (a, b, c):
        if i: t += 1
        else: f += 1
    if t > f:
        return True
    return False

x, y, z = int(input()), int(input()), int(input())
ans = Election(x, y, z)
if ans:
    print(1)
else:
    print(0)

# 8. Реализуйте следующие функции для банковского счета
def addToBankAccount(cash, total_money):
    total_money += cash
    return total_money

def substractFromBankAccoun(cash, total_money):
    total_money -= cash
    return total_money

def moneyConversion(total_money, str1, str2):
    if str1 == 'USD' and str2 == 'KZT':
        total_money *= 470
        return total_money
    elif str1 == 'KZT' and str2 == 'USD':
        total_money /= 470
        return total_money
    return total_money

total_money = 0
while True:
    print('1 - Добавить деньги')
    print('2 - Снять деньги')
    print('3 - Конвертация счета')
    print('0 - Выйти')
    x = int(input())
    if x == 1:
        n = int(input('Количество денег которые хотите внести: '))
        total_money = addToBankAccount(n, total_money)
        print(total_money)
    elif x == 2:
        n = int(input('Количество денег которые хотите снять: '))
        total_money = substractFromBankAccoun(n, total_money)
        print(total_money)
    elif x == 3:
        print('Для конвертации выберите опцию: \n1 - USD -> KZT \n2 - KZT -> USD')
        n = int(input())
        if n == 1:
            total_money = moneyConversion(total_money, 'USD', 'KZT')
            print(total_money)
        elif n == 2:
            total_money = moneyConversion(total_money, 'KZT', 'USD')
            print(total_money)
        else:
            print('Извините, такой функции нет\n ВОЗВРАТ НА ГЛАВНОЕ МЕНЮ')
    elif x == 0:
        break
    else:
        print('Введите число от 1 до 3, либо 0 если хотите выйти!')


# ДОП ЗАДАЧИ
# 1. Реализуйте сортировку методом пузырьков. 
list = [2, 129, 0, -9, -123, 5]
print(list)
for i in range (0, len(list) - 1):
    for j in range (0, len(list) - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print(list)

# 2. Числа Фибоначчи
def phi(a):
    fib1 = 1
    fib2 = 1
    i = 0
    while i < a - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib1 + fib2

n = int(input())
print(phi(n))