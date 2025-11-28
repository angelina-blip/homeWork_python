from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "A201", "+79191996890"),
    Smartphone("Apple", "14 Pro", "+79191996891"),
    Smartphone("Xiaomi", "Plus+", "+79191996892"),
    Smartphone("Honor", "Pro10", "+79191996893"),
    Smartphone("Huawei", "Nu333", "+79191996894")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}")