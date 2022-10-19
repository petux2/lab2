import csv
import os

# Никулин Максим 368594

os.system("cls")

white = '\u001b[47m \u001b[0m'
red = '\u001b[41m \u001b[0m'
black = '\u001b[40m \u001b[0m'
blue = '\u001b[44m \u001b[0m'

print('Флаг:')
print(white * 15)
print(white * 15)
print(red * 15)
print(red * 15)

def uzor(color, amount):
    print(color * 11 * amount)
    print((' ' * 5 + color + ' ' * 5) * amount)
    print(color * 11 * amount)
    print((' ' * 2 + color + ' ' * 5 + color + ' ' * 2) * amount)
    print(color * 11 * amount)

print('Узор:')
uzor(white, 5)

#Значения для целых точек
x = [i**2 for i in range(1, 10)]
y = [i for i in range(1, 10)]
print('График:')
print('↑y')

#1 Вариант вывода графика, на мой взгляд выглядит красивее
# for i in range(8, 0, -1):
#     print('%-3s' % y[i] + ' '*x[i-1] + white * (x[i] - x[i-1]))
# print('1  ' + white)

#2 Вариант вывода, он "точнее"
print('9' + ' '*82 + white)
for i in range(7, -1, -1):
    print('%-3s' % y[i] + ' '*(x[i] - 1) + white * (x[i+1] - x[i]))


#Числа оси x
print('0  1  ', end='')
for i in range(1, 8):
    print(str(x[i]) + ' '*(x[i+1] - x[i] - len(str(x[i]))), end='')
print('81 →x')

print('Диаграмма:')
with open('books.csv') as f:
    reader = csv.reader(f, delimiter=";")

    until_2017 = -1
    after_2017 = 0

    #Считывание данных
    for s in reader:
        if until_2017 == -1:
            until_2017 = 0
            continue

        if int(s[6].split('.')[2].split(' ')[0]) < 2017: until_2017 += 1
        else: after_2017 += 1

    until_2017, after_2017 = round(until_2017 / (until_2017 + after_2017), 2), round(after_2017 / (until_2017 + after_2017), 2)

    #Округление значений до процентов с шагом 5
    u, a, u1, a1 = 0, 0, 1, 1
    percents = [round(0.05 * i, 2) for i in range(21)]

    for i in range(21):
        if abs(until_2017 - percents[i]) < u1:
            u = percents[i]
            u1 = abs(until_2017 - percents[i])
        if abs(after_2017 - percents[i]) < a1:
            a = percents[i]
            a1 = abs(after_2017 - percents[i])
    until_2017, after_2017 = u, a

    #Вывод диаграммы
    for i in range(20, 0, -1):
        print('%-5s' % f'{int(percents[i] * 100)}%', end='')
        if until_2017 >= percents[i]: print(red * 5, end='   ')
        else: print(' ' * 5, end='   ')
        if after_2017 >= percents[i]: print(blue * 5, end='   ')
        else: print(' ' * 5, end='   ')

        if i == 2: print('   ' + red + ' - До 2017', end='')
        if i == 1: print('   ' + blue + ' - После 2017',end='')
        print()
    print()

input()