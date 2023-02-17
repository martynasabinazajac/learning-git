#Zadanie 1 Moduł 3
lista_zakupów={'piekarnia':['chleb', 'pączek', 'bułki'],'warzywniak':['marchew', 'seler', 'rukola']}
print('Lista zakupów')
x=0
for keys, values in lista_zakupów.items():
    print(f'Idę do {keys.capitalize()}, kupuję tu następujące rzeczy: {[i.capitalize() for i in values]}')
    values=len(values)
    x+=values
print(f'W sumie kupuję {[x]} produktów.')
#Zadanie 2 Moduł 3
list=[i for i in range(1,101) if i%5==0]
print(list)
list_3=[i**3 for i in list]
print(list_3)