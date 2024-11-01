qty_sea = int(input())
qty_mountain = int(input())
profit = 0.00
total_vouchers = qty_sea + qty_mountain

while total_vouchers > 0:
    sale = input()
    if sale == 'Stop':
        break

    if sale == 'sea':
        if qty_sea > 0:
            qty_sea -= 1
            profit += 680
            total_vouchers -= 1
        else:
            continue
    elif sale == 'mountain':
        if qty_mountain > 0:
            qty_mountain -= 1
            profit += 499
            total_vouchers -= 1
        else:
            continue

if total_vouchers == 0:
    print('Good job! Everything is sold.')
print(f'Profit: {profit:.0f} leva.')
