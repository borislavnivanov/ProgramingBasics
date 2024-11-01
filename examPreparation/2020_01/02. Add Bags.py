STORAGE_TO_7 = 1.40
STORAGE_7_30 = 1.15
STORAGE_OVER_30 = 1.10

price_luggage_over_20 = float(input())
price_luggage_10_20 = price_luggage_over_20 / 2
price_luggage_under_10 = price_luggage_over_20 * 0.20
luggage_weight = float(input())
days_on_storage = int(input())
number_bags = int(input())

storage_bill = 0.00

if luggage_weight < 10:
    storage_bill += price_luggage_under_10
elif luggage_weight > 20:
    storage_bill += price_luggage_over_20
else:
    storage_bill += price_luggage_10_20

if days_on_storage < 7:
    storage_bill *= STORAGE_TO_7
elif 7 <= days_on_storage <= 30:
    storage_bill *= STORAGE_7_30
else:
    storage_bill *= STORAGE_OVER_30

storage_bill *= number_bags

print(f'The total price of bags is: {storage_bill:.2f} lv.')
