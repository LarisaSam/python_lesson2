my_list = []

n = int(input("Введите количество элементов списка"))

for i in range(0, n):
    elements = int(input("Введите элемент списка, после ввода каждого элемента - enter"))

    my_list.append(elements)

print(my_list)


j = 0
for i in range(int(len(my_list)/2)):
    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    j += 2
print(my_list)

#my_list = []
#my_list.append(input("Введите элементы списка"))



