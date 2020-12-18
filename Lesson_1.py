# 1.
a = 1
b = 2
c = input("Введите буковки: ")
d = int(input("Ну или циферки: "))
print("Вот так!", a, b, c, d)

# 2. Время в секундах в часы.
user_sec = int(input("Введите время в секундах"))
hours = (user_sec // 3600)
minu = ((user_sec - (hours * 3600)) // 60)
sec = (user_sec - (hours * 3600 + minu * 60))
print(hours, "ч.", minu, "мин.", sec, "сек.")

# 3.Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn
user_num = input("Введите число n, будем вычислять выражение типа 'n+nn+nnn'")
a = user_num * 2
b = user_num * 3
n = int(user_num) + int(a) + int(b)
print(n)

# 4. Пользователь вводит целое положительное число. Найти самую большую цифру в числе.
user_num2 = int(
    input("Товарищ пользователь, вводите целое положительное число,будем искать самую большую цифру в нём:   "))
maxi = user_num2 % 10
user_num2 = user_num2 // 10
while user_num2 > 0:
    if user_num2 % 10 > maxi:
        maxi = user_num2 % 10
    user_num2 = user_num2 // 10
print(maxi)

# 5. Выручка-издержки.

proc = int(input("Выручка фирмы= "))
cost = int(input("Издержки фирмы= "))
if proc > cost:
    print("Чтож, неплохо, Ваша фирма заработала", proc - cost, "золотых дукатов", "при этом рентабельность составила: ",
          round(proc / cost), "%")
    plankton_qty = int(input("Сколько у вас числится душ?: "))
    print("Это получается по ", round(((proc - cost) / plankton_qty), 1), "дуката на одного работника")
if proc < cost:
    print("Шеф, всё пропало, это фиаско, продавай почку, минимум за ", abs(proc - cost), " бачей")

# 6. Спортсмен

a = int(input("Пробежал в 1-й день, км.: "))
b = int(input("Желаемый результат, в км.: "))
c = 1
while a < b:
    c += 1
    a = a * 1.1
print("Господин спортсмен пробежит", b, " км на ", c, "-й день упорных тренировок.")
