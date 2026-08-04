from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S23", "+79001112233"),
    Smartphone("Apple", "iPhone 15", "+79004445566"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79007778899"),
    Smartphone("Google", "Pixel 7", "+79002223344"),
    Smartphone("Nothing", "01", "+79005556677"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
