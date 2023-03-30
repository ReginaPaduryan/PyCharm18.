all_tickets = int(input('Введите количество билетов'))
age_for_tickets = []
def price(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390
for i in range(0, all_tickets):
    i += 1
    input_value = int(input(f'Для какого возраста билет №{i}? '))
    age_for_tickets.append(input_value)
    full_price = sum(map(price, age_for_tickets))
    discount_price = int(full_price * 0.9)
if all_tickets > 3:
    print('Стоимость всех билетов со скидкой: ', discount_price, "руб.")
else:
    print('Стоимость всех билетов: ', full_price, "руб.")


