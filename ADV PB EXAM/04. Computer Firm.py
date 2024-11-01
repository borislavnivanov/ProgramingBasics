RATING_2 = 0
RATING_3 = 0.50
RATING_4 = 0.70
RATING_5 = 0.85
RATING_6 = 1

computers = int(input())

actual_sales = 0.00
rating = 0

for i in range(0, computers):
    data = input()
    predicted_sales = int((data[0] + data[1]))
    current_rating = int(data[2])
    if current_rating == 3:
        actual_sales += predicted_sales * RATING_3
    elif current_rating == 4:
        actual_sales += predicted_sales * RATING_4
    elif current_rating == 5:
        actual_sales += predicted_sales * RATING_5
    elif current_rating == 6:
        actual_sales += predicted_sales * RATING_6
    else:
        pass
    rating += current_rating

rating = rating / computers

print(f'{actual_sales:.2f}\n{rating:.2f}')
