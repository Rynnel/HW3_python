kashki = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
num = int(input("Введите число: "))
day = 0 #Инициализация переменной, которая будет использоваться для выбора каши на определенный день
for i in range(num):
    kashkasegodnya = kashki[day] #Выбираем кашу на сегодняшний день
    print(kashkasegodnya) #Выводим кашу на день
    day = (day+1) % len(kashki) #Увеличиваем день на 1, при этом учитывая длину списка каш (чтобы день не выходил за границы списка)
