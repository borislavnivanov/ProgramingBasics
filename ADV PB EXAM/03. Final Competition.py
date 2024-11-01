dancers = int(input())
points = float(input())
season = input()
place = input()

awarded_sum = dancers * points
if place == "Abroad":
    awarded_sum += awarded_sum * 0.50

if season == 'summer':
    if place == 'Bulgaria':
        awarded_sum *= 0.95
    else:
        awarded_sum *= 0.90
elif season == 'winter':
    if place == 'Bulgaria':
        awarded_sum *= 0.92
    else:
        awarded_sum *= 0.85

charity = awarded_sum * 0.75
awarded_sum = awarded_sum - charity

print(f'Charity - {charity:.2f}\nMoney per dancer - {awarded_sum / dancers:.2f}')
