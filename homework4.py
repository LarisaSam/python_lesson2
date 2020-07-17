word = input("Введите строку из нескольких слов, разделённых пробелами").split()
print(word)
n=1
for i in word:
    print(n, i[0:10])
    n +=1