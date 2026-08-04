from address import Address
from mailing import Mailing

from_addr = Address("123456", "Москва", "Ленина", "10", "5")
to_addr = Address("654321", "Санкт-Петербург", "Невский проспект", "20", "12")

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=350,
    track="TRACK12345"
)

print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.index}, "
    f"{mailing.from_address.city}, "
    f"{mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, "
    f"{mailing.to_address.city}, "
    f"{mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
