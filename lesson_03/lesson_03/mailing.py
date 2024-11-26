class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost #тип данных число
        self.track = track #тип данных строка

    def __str__(self):
        return f"Отпраление {self.track} из {self.from_address} в {self.to_address}. Стоимость {self.cost} рублей."