money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

number_months = 0
current_money = money_capital

while current_money + salary >= spend:
    current_money = (current_money + salary) - spend
    price_increases = spend * increase
    spend += price_increases
    number_months += 1

print("Количество месяцев, которое можно протянуть без долгов:", number_months)
