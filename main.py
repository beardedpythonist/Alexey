flowers_wse = {'розы', 'тюльпаны', 'ромашки', 'нарциссы', 'васильки', 'хлопок','амариллис'}
flowers_uzhedaril = set()
week_days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
slov1= {}
s1 = 'YES'
c = 0
while s1 == 'YES':
    c += 1
    flowers_wybor = flowers_wse - flowers_uzhedaril
    print('На этой неделе вы можете дарить: ',  f'{flowers_wybor}')
    flower = input('введите название цветка: ' )
    if flower not in flowers_wse:
        print('Такого цветка нет. Добавить в список цветов? YES - если да, NO - если нет ')
        q = input()
        if q == 'YES':
            flowers_wse.add(flower)
            flowers_uzhedaril.add(flower)
            flowers_wybor = flowers_wse - flowers_uzhedaril
    for key, value in slov1.items():
        if flower == value:
            print(f'вы дарили {flower} в {key} !')
    day = input('введите название дня недели: ')
    if day not in week_days:
        print('Ошибка! Напишите снова: ')
        day = input()
    slov1[day] = flower
    flowers_uzhedaril.add(slov1[day])
    if c ==  3:
        flowers_uzhedaril.clear()
        print(flowers_wse)
        print('какой цветок из списка вы хотите удалить:')
        s2 = input()
        if s2 == s2:
            flowers_wse.remove(s2)
        s1 = input("хотите продолжить? 'YES' - если да, 'NO' - если нет  ")
        c = 0

print(slov1)
