import requests

BASE_URL = 'https://fakestoreapi.com'


# Получить продукты цена, которых меньше 20
def task1():
    res = requests.get(f'{BASE_URL}/products')
    all_products = res.json()

    product_with_price_less_than_20 = [
        product for product in all_products if product['price'] < 20]
    print(product_with_price_less_than_20)


# Вывести все категории
def task2():
    res = requests.get(f'{BASE_URL}/products/categories')
    print(res.json())


# Вывести все продукты с категорией "jewelery"
def task3():
    res = requests.get(f'{BASE_URL}/products/category/jewelery')
    print(res.json())


# Вывести всех пользователей
def task4():
    res = requests.get(f'{BASE_URL}/users')
    print(res.json())


# Добавить пользователя со своим именем
def task5():
    new_person = {
        'email': 'igor.gass@gmail.com',
        'username': 'Nokvix',
        'password': 'ASdas12dASD',
        'name': {
            'firstname': 'Igor',
            'lastname': 'Gass',
        },
        'address': {
            'city': 'Los Angeles',
            'street': 'S Mapleton Dr',
            'number': 594,
            'zipcode': 90024,
            'geolocation': {
                'lat': 34.073275,
                'long': -118.428282,
            }
        },
        'phone': '1-234-567-890',
    }

    res = requests.post(f'{BASE_URL}/users', json=new_person)
    print(res.json())
