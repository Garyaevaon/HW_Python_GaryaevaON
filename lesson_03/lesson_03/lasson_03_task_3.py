from address import Address
from mailing import Mailing

to_address = Address("678188", "Удачный", "Новый-город", "34", "104")
from_address = Address("958454", "Воронеж", "Ленина", "105", "233")
mailing1 = Mailing(to_address, from_address, "2500", 1431524355)

print(mailing1)