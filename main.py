wse_temy ={'Циклы', 'Списки', 'Кортежи', 'Словари',
'Множества', 'Файлы', 'Функции', 'ООП'}
uzhe =set()
escho = set()
s0 = input('Вывести все темы? YES -если да, NO -если нет ')
if s0 == 'YES':
    print('Все темы: ', *wse_temy, sep=', ')
    s1 =input('Введите темы (по одной через Enter), которые уже выучены. Чтобы закончить ввод , введите NO ')
    while s1 != 'NO':
        uzhe.add(s1)
        s1 =input('Введите темы (по одной через Enter), которые уже выучены. Чтобы закончить ввод , введите NO ')
    print('Список выученых тем: ', *uzhe, sep=', ')
    escho = wse_temy - uzhe
    print('Темы, которые еще надо выучить: ', *escho, sep=', ')
    proz = len(uzhe) / len(wse_temy) * 100
    print()
    print('Процент освоенного материала:', proz )
