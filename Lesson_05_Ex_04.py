# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


with open("Lesson_05_Ex_04_1.txt", "r", encoding='utf-8') as f1:
    f2 = open("Lesson_05_Ex_04_2.txt", "w", encoding='utf-8')
    linesf1 = f1.readlines()
    g = ["Один", "Два", "Три", "Четыре"]
    for i in range(len(linesf1)):
        linesf1[i] = linesf1[i].replace(((linesf1[i]).split()[0]),g[i])
        print(linesf1[i])
        f2.write(str(linesf1[i]))
print("Данные сохранены в текстовый файл с именем 'Lesson_05_Ex_04_2.txt'")