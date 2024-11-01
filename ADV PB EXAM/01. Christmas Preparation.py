PACKAGING_PAPER = 5.80
TEXTILE = 7.20
GLUE = 1.20

rolls_paper = int(input())
rolls_textile = int(input())
litters_glue = float(input())
discount = int(input()) / 100

bill = 0.00

bill += rolls_paper * PACKAGING_PAPER
bill += rolls_textile * TEXTILE
bill += litters_glue * GLUE
bill *= (1 - discount)

print(f'{bill:.3f}')
