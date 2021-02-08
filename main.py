# HOMEWORK 01

# Задание 1
number = 2.99
numberInt = int(number)
print(number)

# Задание 2
try:
    kol = input()
    kol = int(kol)
    print(kol, " целого типа")
except ValueError:
    print("Вы ввели не целочисленное число")

# Задание 2 метод 2
try:
    kol = int(input())
    print(kol, " целого типа")
except ValueError:
    print("Вы ввели не целочисленное число")

# Задание 3
try:
    radius = float(input("значения переменной radius типа float "))
    print(radius, " типа float")
except ValueError:
    print("Вы ввели не число")

# Задание 4
try:
    r = float(input("r = "))
    area = 3.14 * (r ** 2)
    print("Area = ", area)
except ValueError:
    print("Вы ввели не число")

# Задание 5
try:
    x = float(input("Вася обычно спит ночью "))
    y = int(input(" часов и устраивает себе днем тихий час на "))
    print(" минут")
    vasyaSleep = int(60 * x) + y
    print("Вася всего спит минут в сутках = ", vasyaSleep)
except ValueError:
    print("Вы ввели не число")

# Задание 6
try:
    sec = int(input("Введите время в секундах "))
    minut = int(sec / 60)
    sec = int(sec % 60)
    hours = int(minut / 60)
    minut = int(minut % 60)
    print(hours, " часов", minut, " минут ", sec, " секунд")
except ValueError:
    print("Вы ввели не число")

# HOMEWORK02

# Задание 1
try:
    current = int(input("Введите номер месяца "))
    months = {"Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь",
              "Декабрь"}
    print(months[current - 1])
except ValueError:
    print("Вы ввели не число")
except IndexError:
    print("Вы ввели не существующий месяц")

# Задание 2
try:
    current = int(input("Введите номер месяца "))
    if current == 1 or current == 2 or current == 12:
        print("Зима")
    elif 2 < current < 6:
        print("Весна")
    elif 5 < current < 9:
        print("Лето")
    elif 8 < current < 12:
        print("Лето")
except ValueError:
    print("Вы ввели не число")

# Задание 3
try:
    first = int(input("Введите первое число "))
    second = int(input("Введите второе число "))
    if first < second:
        print("Первое число меньше ", first)
    elif second < first:
        print("Второе число меньше", second)
    else:
        print("Числа равны")
except ValueError:
    print("Вы ввели не число")

# Задание 4
try:
    one = int(input("Введите первое число "))
    two = int(input("Введите второе число "))
    three = int(input("Введите второе число "))
    if one == two and one == three:
        print(3)
    elif one == two or one == three or three == two:
        print(2)
    else:
        print(0)
except ValueError:
    print("Вы ввели не число")

# Задание 5
try:
    year = int(input("Введите номер года "))
    answer = "NO"
    if year % 4 == 0:
        answer = "YES"
        if year % 100 == 0:
            answer = "NO"
            if year % 400 == 0:
                answer = "YES"
    print(answer)
except ValueError:
    print("Вы ввели не число")
