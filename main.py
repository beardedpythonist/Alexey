class Car():
    def __init__(self, year, model, price, speed):
        self.year_of_production = year
        self.model = model
        self.price = price
        self.max_speed =speed
    def data_prodazhi(self, year):
        print(f'машина продана в {year} году.С момента выпуска прошло {year - self.year_of_production } лет ')
    def price_now(self):
        year_now = 2023
        koef = (year_now  - self.year_of_production) * 0.1
        print(f'актуальная цена сегодня: {self.price * koef}')


bmw = Car(2010, 'E39', 15000, 180)
audi =  Car(2015, 'A6', 30000, 200)
merc =  Car(2017, 'AMG', 55000, 250)


n = int(input('введи год продажи '))

audi.data_prodazhi(n)
audi.price_now()



