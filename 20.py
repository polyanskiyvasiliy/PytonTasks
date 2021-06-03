class Drink:
    def __init__(self):
            self.price  = 0.0
            self.volume = 0.0
            self.name   = ""

balance = int(input("Введите баланс: "))
drinkAmount = int(input("Введите количество напитков: "))

best = Drink()
_input = Drink()

for i in range(drinkAmount):
	_input.name   = input("Имя напитка: ")
	_input.price  = int(input("Цена напитка: "))
	_input.volume = int(input("Объём напитка: "))

	liters = (balance // _input.price) * _input.volume
	if liters == 0:
		continue
	
	if best.price == 0:
		best = _input
		continue
	
	bestLiters = (balance // best.price) * best.volume
	if liters > bestLiters:
		best = _input

if best.price == 0:
	print(-1)
else:
    bottles = balance // best.price
    print("{} {}\n{}\n{}".format(best.name, bottles, bottles * best.volume,
        balance - best.price * bottles))
