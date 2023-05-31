spisok = list(map(int, input("Введите числа, которые будут входить в список: ").split()))
last = spisok[-1]
for i in range(len(spisok)-1, 0, -1):
    spisok[i] = spisok[i-1]
spisok[0] = last
print(spisok)
