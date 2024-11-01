DELIVERY = 60.00

qty = int(input())
size = input()
with_delivery = True if input() == 'With delivery' else False


bill = 0.00

if qty < 10:
    print("Invalid order")
else:
    if size == '90X130':
        bill += qty * 110
        if qty > 60:
            bill -= bill * 0.08
        elif qty > 30:
            bill -= bill * 0.05
    elif size == '100X150':
        bill += qty * 140
        if qty > 80:
            bill -= bill * 0.10
        elif qty > 40:
            bill -= bill * 0.06
    elif size == '130X180':
        bill += qty * 190
        if qty > 50:
            bill -= bill * 0.12
        elif qty > 20:
            bill -= bill * 0.07
    elif size == '200X300':
        bill += qty * 250
        if qty > 50:
            bill -= bill * 0.14
        elif qty > 25:
            bill -= bill * 0.09

    if with_delivery:
        bill += DELIVERY
    if qty > 99:
        bill -= bill * 0.04
    print(f'{bill:.2f} BGN')
