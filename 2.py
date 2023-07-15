import requests
from bs4 import BeautifulSoup
import json


def parse_edc_sale():
    data = []
    url = "https://edc.sale/ru/ru/vehicles/"  # Замените на фактический URL для EDC.SALE
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Код для извлечения информации с EDC.SALE
    listings = soup.find_all("div", class_="listing-item")  # Пример поиска объявлений

    for listing in listings:
        car = {}
        car["brand"] = listing.find("span", class_="brand").text.strip()  # Пример извлечения марки автомобиля
        car["model"] = listing.find("span", class_="model").text.strip()  # Пример извлечения модели автомобиля
        car["price"] = listing.find("span", class_="price").text.strip()  # Пример извлечения цены
        car["year"] = listing.find("span", class_="year").text.strip()  # Пример извлечения года выпуска
        car["mileage"] = listing.find("span", class_="mileage").text.strip()  # Пример извлечения пробега

        data.append(car)

    return data


def parse_auto_ru():
    data = []
    url = "https://auto.ru/cars/all/"  # Замените на фактический URL для AUTO.RU
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Код для извлечения информации с AUTO.RU
    listings = soup.find_all("div", class_="listing-item")  # Пример поиска объявлений

    for listing in listings:
        car = {}
        car["brand"] = listing.find("span", class_="brand").text.strip()  # Пример извлечения марки автомобиля
        car["model"] = listing.find("span", class_="model").text.strip()  # Пример извлечения модели автомобиля
        car["price"] = listing.find("span", class_="price").text.strip()  # Пример извлечения цены
        car["year"] = listing.find("span", class_="year").text.strip()  # Пример извлечения года выпуска
        car["mileage"] = listing.find("span", class_="mileage").text.strip()  # Пример извлечения пробега

        data.append(car)

    return data

def parse_drom():
    data = []
    url = "https://blagoveshchensk.drom.ru/auto/"  # Замените на фактический URL для drom.ru
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Код для извлечения информации с drom.ru
    listings = soup.find_all("div", class_="listing-item")  # Пример поиска объявлений

    for listing in listings:
        car = {}
        car["brand"] = listing.find("span", class_="brand").text.strip()  # Пример извлечения марки автомобиля
        car["model"] = listing.find("span", class_="model").text.strip()  # Пример извлечения модели автомобиля
        car["price"] = listing.find("span", class_="price").text.strip()  # Пример извлечения цены
        car["year"] = listing.find("span", class_="year").text.strip()  # Пример извлечения года выпуска
        car["mileage"] = listing.find("span", class_="mileage").text.strip()  # Пример извлечения пробега

        data.append(car)

    return data

def parse_cars():
    data = []
    url = "https://car.ru/auto/"  # Замените на фактический URL для car.RU
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Код для извлечения информации с car.RU
    listings = soup.find_all("div", class_="listing-item")  # Пример поиска объявлений

    for listing in listings:
        car = {}
        car["brand"] = listing.find("span", class_="brand").text.strip()  # Пример извлечения марки автомобиля
        car["model"] = listing.find("span", class_="model").text.strip()  # Пример извлечения модели автомобиля
        car["price"] = listing.find("span", class_="price").text.strip()  # Пример извлечения цены
        car["year"] = listing.find("span", class_="year").text.strip()  # Пример извлечения года выпуска
        car["mileage"] = listing.find("span", class_="mileage").text.strip()  # Пример извлечения пробега

        data.append(car)

    return data

def parse_avito():
    data = []
    url = "https://www.avito.ru/amurskaya_oblast_blagoveschensk/avtomobili?cd=1&radius=200&searchRadius=200"  # Замените на фактический URL для AUTO.RU
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Код для извлечения информации с AUTO.RU
    listings = soup.find_all("div", class_="listing-item")  # Пример поиска объявлений

    for listing in listings:
        car = {}
        car["brand"] = listing.find("span", class_="brand").text.strip()  # Пример извлечения марки автомобиля
        car["model"] = listing.find("span", class_="model").text.strip()  # Пример извлечения модели автомобиля
        car["price"] = listing.find("span", class_="price").text.strip()  # Пример извлечения цены
        car["year"] = listing.find("span", class_="year").text.strip()  # Пример извлечения года выпуска
        car["mileage"] = listing.find("span", class_="mileage").text.strip()  # Пример извлечения пробега

        data.append(car)

    return data

def main():
    data = []

    edc_sale_data = parse_edc_sale()
    data.extend(edc_sale_data)

    auto_ru_data = parse_auto_ru()
    data.extend(auto_ru_data)

    drom_data = parse_drom()
    data.extend(drom_data)

    cars_data = parse_cars()
    data.extend(cars_data)

    avito_data = parse_avito()
    data.extend(avito_data)

    # Запись общих данных в общий JSON-файл
    with open('all_cars.json', 'w') as f:
        json.dump(data, f)