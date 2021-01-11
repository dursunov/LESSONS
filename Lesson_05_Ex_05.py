# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

a = None
while a != 1:
    user_input = (input(
        "Введите числа, разделённые пробелом. Они будут программно, как того требуют условия задания записаны в файл с названием 'Lesson_05_Ex_05.txt'\n"))
    checker = user_input.split(" ")
    try:
        for el in checker:
            int(el)
    except Exception:
        print("Обнаружены не цифры. Это плохо... Давайте попробуем ещё раз с начала.")
        continue
    else:
        print("Всё хорошо, среди введённых Вами символов только цифры. ")
        break
f1 = open("Lesson_05_Ex_05.txt", "w", encoding='utf-8')
f1.write(user_input)
print("Файл 'Lesson_05_Ex_05' создан, в него записана последовательность введённых Вами цифр")
f1.close()
f1 = open("Lesson_05_Ex_05.txt", "r", encoding='utf-8')
s = f1.readlines()
summm = 0
lis = s[0].split()

for el in lis:
    summm += int(el)
print("сумма введённых чисел составляет: ", summm)
f1.close()
