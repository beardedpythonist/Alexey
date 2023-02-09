def zapravka():
    distance = 2000
    consumption = 7.5
    bak = 70
    ostatok_na_nachalo = 20

    dist_na_ostatke = ostatok_na_nachalo * 100 / consumption  # расстояние на остатке
    print(dist_na_ostatke)
    spisok_zapravok  = {x: x * 25 for x in range(1, 40)} # заправки: ключ - номер , значение - километраж
    print(spisok_zapravok)
    first_pitstop = int
    ls = []
    for key, val in spisok_zapravok.items():
        if dist_na_ostatke <= val:
            point = key - 1, spisok_zapravok[key-1]  # первая заправка (номер заправки и км, в ввиде кортежа)
            ls.append(point)
            print(ls)
            break
    dist_na_poln = bak * 100 / consumption  # расстоян на полн баке
    print(dist_na_poln)
    dist_to_finish = distance - point
    

