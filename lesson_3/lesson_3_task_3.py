from address import Address
from mailing import Mailing

to_address = Address(241015, "Брянск", "Новая", 27, 120)
from_address = Address(654321, "Санкт-Петербург", "Пушкина", 20, 15)
track = "AV3792766439RU"
cost = 200
mailing = Mailing(to_address, from_address, 200, "AV3792766439RU")
print(mailing)