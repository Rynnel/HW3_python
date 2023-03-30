def can_eat(h1,h2,f1,f2):
    if (abs((h1 - f1)) == 2 and abs((h2 - f2)) == 1) or (abs((h1 - f1)) == 1 and abs((h2 - f2)) == 2): # Проверяем может ли конь съесть фигуру, путем нахождения модуля разницы x коня и x фигуры, а также y коня и y фигуры. 
        return "TRUE"
    else:
        return "FALSE"
h1 = int(input('Координата x коня: '))
h2 = int(input('Координата y коня: '))
f1 = int(input('Координата x другой фигуры: '))
f2 = int(input('Координата y другой фигуры: '))
print(can_eat(h1,h2,f1,f2))