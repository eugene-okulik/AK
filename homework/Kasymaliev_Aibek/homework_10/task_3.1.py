import re


PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


price = re.findall(r'\d+', PRICE_LIST)
price = list(map(int, price))
item = re.findall(r'[а-яА-Яa-zA-Z]+', PRICE_LIST)
item_list = [word for word in item if word != 'р']
dict_version_price = dict(zip(item_list, price))


print(dict_version_price)
