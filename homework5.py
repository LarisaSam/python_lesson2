my_list = [9, 8, 7, 6, 5, 4]
print(my_list)
num = int(input("Введите элемент рейтинга"))
my_list.append(num)
my_list.sort(reverse=True)
print(my_list)