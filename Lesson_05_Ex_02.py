# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.


f = open("Lesson_05_Ex_02.txt", "r", encoding='utf-8')
lines = f.readlines()
print("Всего в текстовом файле", len(lines), "строк.")
i = 0
for el in lines:
    i += 1
    elist = el.split()
    print("Кол-во слов в ", i, "-й строке равно", len(elist))
print("Всего строк в файле:", i)
f.close()
