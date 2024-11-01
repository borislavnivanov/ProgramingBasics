best_goal: int = 0
best_player_name: str = ''

while True:
    player_name = input()
    if player_name == 'END':
        break
    goals = int(input())

    if goals > best_goal:
        best_goal = goals
        best_player_name = player_name

    if goals >= 10:
        break

print(f'{best_player_name} is the best player!')

if best_goal >= 3:
    print(f'He has scored {best_goal} goals and made a hat-trick !!!')
else:
    print(f'He has scored {best_goal} goals.')
