balls = int(input())

total_points = 0
points = {'red': 5, 'orange': 10, 'yellow': 15, 'white': 20}
counters = {'red': 0, 'orange': 0, 'yellow': 0, 'white': 0, 'black': 0, 'other': 0}

for i in range(balls):
    var = input()
    if var == "black":
        total_points /= 2
        counters[var] += 1
    elif var in points:
        total_points += points[var]
        counters[var] += 1
    else:
        counters['other'] += 1

print(f'Total points: {int(total_points)}\n'
      f'Red balls: {counters["red"]}\n'
      f'Orange balls: {counters["orange"]}\n'
      f'Yellow balls: {counters["yellow"]}\n'
      f'White balls: {counters["white"]}\n'
      f'Other colors picked: {counters["other"]}\n'
      f'Divides from black balls: {counters["black"]}')
