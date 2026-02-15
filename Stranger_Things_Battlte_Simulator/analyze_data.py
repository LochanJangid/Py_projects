import sqlite3
import math

# connect to database
conn = sqlite3.connect('strange_battle.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM battle_log')
battles = cursor.fetchall() # for retrieve result

total_battles = {}
winnings = {}
for battle in battles:
    _, villain_type, _, _, result = battle

    if villain_type not in winnings:
        winnings[villain_type] = 0
    if villain_type not in total_battles:
        total_battles[villain_type] = 0
    if battle[-1] == 'won':
        winnings[villain_type] += 1
    # increment battle count
    total_battles[villain_type] += 1
    
win_rate = {}
for villian, win in winnings.items():
    win_rate[villian] = win*100/total_battles[villian]

# print win rate
print('Villians : winning rate')
for villian, winning_rate in win_rate.items():
    try:
        round_win_rate = math.floor(winning_rate)//10
        winning_bar = '#' * round_win_rate
        lossing_bar = '.' * (10 - round_win_rate)
        print(f'{villian} : [{winning_bar}{lossing_bar}] {winning_rate:.2f}')
    except ZeroDivisionError:
        print(f'{villian} : No battle recorded')

conn.close()


