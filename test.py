balance = 10000000
operations = 0
cash = 50

def richness():
    global balance
    if balance > 5000000:
        sum_percent = balance * 0.1
        balance -= sum_percent
        print(f"Вычтен налог на богатство в размере {sum_percent}")
        print(f"Текущий баланс {balance}")


richness()