from random import *

class Human:
    counter = 0
    ls = ['муж', 'жен']
    list_name_m = ['Lionel McCoy', 'Charles Cross', 'John Pitz', 'Jeffry Young', 'Johnathan Randall', 'Edward wnsend']
    list_name_zh = ['Aubrey Gilmore', 'Avice Reynolds', 'Theresa Bradford', 'Shonda Douglas', 'Karen Sanders']
    age = range(18, 100)
    charakter = ['холерик', 'сангвиник', 'меланхолик', 'флегматик']

    def __init__(self, pol, name, age, charakter):
        self.pol = pol
        self.name = name
        self.age = age
        self.charakter = charakter
        Human.counter += 1
    def info(self):
        print(self.name, self.pol, self.age, self.charakter)
        return
    def life(self):
        pass

def sozdaniye():
    num = randrange(2, 6)
    for c in range(num):
        pol = choice(Human.ls)
        charakter = choice(Human.charakter)
        if pol == 'жен':
            name = choice(Human.list_name_zh)
        else:
            name = choice(Human.list_name_m)
        age  = choice(Human.age)
        x = input('введи имя экземпляра ')
        x = Human(pol, name, age, charakter)    # создание экземпляра класса
        x.info()

sozdaniye()
print('итого создано: ', Human.counter)

