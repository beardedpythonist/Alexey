# def plus_perim(func):

#     def wrapper(*args, **kwargs):
#         return (func(*args, **kwargs))
#     return wrapper
#
#
# @plus_perim
# def plosh_tr(a, b, c):
#     p = (a + b + c) / 2
#     s =  (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     return s
# plosh_tr(5, 7 , 8)
#
# print(plus_perim(plus_perim))





def add_dollar_prefix(func):
    def wrapper():
        result = str(func())
        return '$' + result
    return wrapper

@add_dollar_prefix
def get_price(item):
    prices = {'comic book': 5, 'puzzle': 15}
    return prices[item]

print(get_price('comic book'))