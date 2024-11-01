shirt_price = float(input())
shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.20
shoes_price = (shirt_price + shorts_price) * 2
discount = 1 - 0.15
gift_threshold = float(input())

bill = shirt_price + shorts_price + socks_price + shoes_price
bill *= discount

if bill >= gift_threshold:
    print(f'Yes, he will earn the world-cup replica ball!\nHis sum is {bill:.2f} lv.')
else:
    print(f'No, he will not earn the world-cup replica ball.\nHe needs {gift_threshold - bill:.2f} lv. more.')
