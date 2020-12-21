# Lesson_02.EX02
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

print("Решение через list")

month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
year_sl = ["Зима", "Весна", "Лето", "Осень"]
cur_s = None
eggor = "Номер месяца введён некорректно\n"

if month > 12 or month <=0:
   print (eggor)
elif month in range(3, 6):
    cur_s = year_sl[1]
elif month in range(5, 9):
    cur_s = year_sl[2]
elif month in range(9, 12):
    cur_s = year_sl[3]
elif month == 11 or month == 12 or month == 1:
    cur_s = year_sl[0]
if month >= 12 or month > 0:
    print("Время года - ", cur_s , "\n")
else:
    None

print("Решение через словарь")
z = "Зима"
v = "Весна"
l = "Лето"
o = "Осень"
year_s = {1: z, 2: z, 3: v, 4: v, 5: v, 6: l, 7: l, 8: l, 9: o, 10: o, 11: o, 12: z}
month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
if month > 12 or month <= 0:
    print(eggor)
else:
    print("Время года - ", year_s[month], "\n")
