slovo = input('Введите слово: ')
minind = slovo.find('f') #Ищет минимальный индекс символа 'f'
maxind = slovo.rfind('f') #Ищет максимальный индекс символа 'f'
if minind == -1: #minind выводит -1 только в случае отсутствия символа 'f', поэтому выводим пустую строку
    print('')
elif minind == maxind: #Если minind = maxind, то это значит, что 'f' встречается ровно 1 раз, поэтому выводим только minind
    print(minind)
else: #Если же minind не равно -1 и не равно maxind, то это значит, что в слове встречается несколько символов 'f'. Поэтому, выводим minind и maxind
    print(minind, maxind)