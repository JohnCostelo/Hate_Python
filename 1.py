import customtkinter as ctk
import json


def search_cars():
    brand = form.get_entry_value("Марка автомобиля:")
    model = form.get_entry_value("Модель автомобиля:")
    price = form.get_entry_value("цены:")
    year = form.get_entry_value("год выпуска:")
    mileage = form.get_entry_value("пробега:")

    results = []
    with open('all_cars.json', 'r') as f:
        data = json.load(f)
        for car in data:
            if car["brand"] == brand and car["model"] == model and car ["price"] == price and car ["year"] == year and car ["mileage"] == mileage:
                results.append(car)

    # Вывод результатов на форме
    # ...


form = ctk.Form()
form.add_entry("Марка автомобиля:")
form.add_entry("Модель автомобиля:")
form.add_entry("цены:")
form.add_entry("год выпуска:")
form.add_entry("пробега:")
form.add_button("Поиск", command=search_cars)
form.run()