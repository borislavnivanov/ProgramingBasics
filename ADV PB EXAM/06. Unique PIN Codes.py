limit_1st = int(input())
limit_2st = int(input())
limit_3st = int(input())

for n1 in range(2, limit_1st + 1, 2):
    for n2 in range(2, limit_2st + 1):
        for n3 in range(2, limit_3st + 1, 2):
            if n2 == 2 or n2 == 3 or n2 == 5 or n2 == 7:
                print(f'{n1} {n2} {n3}')
