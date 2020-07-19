
#month_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#print(month_lst)
result = {'Зима': (1, 2, 12),
          'Весна': (3, 4, 5),
          'Лето': (6, 7, 8),
          'Осень': (9, 10, 11)}

num_month = int(input("Введите номер месяца - число от 1 до 12"))
for key in result.keys():
    if num_month in result[key]:
        print(key)
