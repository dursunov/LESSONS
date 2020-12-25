# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(words):
    z = any(map(str.isdigit, words))
    if words.islower() == True and words.isascii() == True and z == False:
        return str(words).capitalize()
    else:
        return ("Incorrect input")

words = input("введите слова, разделённые пробелом:\n")
print(int_func(words))

strw = []
if int_func(words) != "Incorrect input":
    lisw = list(map(str, words.split()))
    for el in range(len(lisw)):
        strw.append(int_func(lisw[el]))
    strw = ' '.join(strw)
else:
    print("Incorrect input")

print(strw)
