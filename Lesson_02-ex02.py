# Lesson_02.EX02
# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input()

list_len = int(input(
    "Т.к. список элементов должен быть введён вручную, предварительно определимся с длиной списка. Введите её, пожалуйста. "))
print("Теперь последовательно вводите элементы списка. ")
new_list=[]

for i in range(list_len):
    liel = input("Введите эелмент спика: ")
    new_list.append(liel)
print("Получился такой вот список:\n", new_list)
# new_list = ["a", "b" , "c", "d", "e", "f", 1]
shulist = []

for i in range(len(new_list)):
    if i%2 != 0:
        shulist.append(new_list[i])
        shulist.append(new_list[i-1])

if len(new_list)%2 != 0:
    lastodd = new_list[len(new_list)-1]
    shulist.append(lastodd)
print("Перемешанный по заданным алгоритмам список будет таким: \n", shulist)