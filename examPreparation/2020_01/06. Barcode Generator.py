start_code = input()
end_code = input()

for n1 in range(int(start_code[0]), int(end_code[0]) + 1):
    for n2 in range(int(start_code[1]), int(end_code[1]) + 1):
        for n3 in range(int(start_code[2]), int(end_code[2]) + 1):
            for n4 in range(int(start_code[3]), int(end_code[3]) + 1):
                if n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0 and n4 % 2 != 0:
                    print(f'{n1}{n2}{n3}{n4}', end=' ')
