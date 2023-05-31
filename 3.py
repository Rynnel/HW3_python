spisok = list(map(int, input("Введите числа, которые будут входить в список: ").split()))
spisok[0], spisok[-1] = spisok[-1], spisok[0]
print(spisok)
