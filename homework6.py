

n = int(input("Введите количество позиций товаров"))

my_list = []
my_tuple = ()

for i in range(0, n):
    product = (int(input("Введите id-номер товара")),
                dict(название=input("Введите название товара"), цена=int(input("Введите цену")),
                     количество=int(input("Введите количество")), ед=input("Введите единицу измерения")))
    my_list.append(product)

print(my_list)



