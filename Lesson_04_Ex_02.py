# Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для
# формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
#  [12, 44, 4, 10, 78, 123].

original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 0, 1, 2, 3, 4, 0, 22, 0, -10, -20, -1,0,1]

original_list.append(0)
new_list = [original_list[i + 1] for i in range(len(original_list) - 1) if original_list[i + 1] > original_list[i]]
print(new_list)
