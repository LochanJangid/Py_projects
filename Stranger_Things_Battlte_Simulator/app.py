import sqlite3
import random

# Connect to a database
conn = sqlite3.connect('strange_battle.db')
cursor = conn.cursor()

# Create a table to store battle logs
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS battle_log(
        battle_id INTEGER PRIMARY KEY,
        villian_type TEXT NOT NULL,
        weapon_type TEXT NOT NULL,
        damage INTEGER NOT NULL,
        result  TEXT NOT NULL
        )'''
    )
conn.commit()

# Villian list
villians = ['mindflayer', 'vecna', 'demodogs']
# weapons list
weapons = ['stranger children', 'fire', 'guns']

# Test battles 1000 times
for i in range(1000):
    # pick random alien and weapon
    villian_type = random.choice(villians)
    weapon_type = random.choice(weapons)

    damage = 0
    result = 'won'

    if villian_type == 'mindflayer':
        if weapon_type == 'stranger children':
            damage = random.randint(80, 100)
        else:
            damage = 0
            result = 'loss'
    elif villian_type == 'vecna':
        if weapon_type == 'stranger children':
            damage = random.randint(90, 100)
        elif weapon_type == 'fire':
            damage = random.randint(50, 70)
            # 1/2 probability for win
            if random.random() > 0.5:
                result = 'win'
            else:
                result = 'loss'

        else:
            result = 'loss'
    else:
        if weapon_type == 'stranger children':
            damage = random.randint(95, 100)
        elif weapon_type == 'fire':
            damage = random.randint(80,90)
        else:
            damage = random.randint(50, 80)
    
    # insert battle log
    cursor.execute(
        '''
        INSERT INTO battle_log (villian_type, weapon_type, damage, result)
        VALUES (?, ?, ?, ?)
        ''', (villian_type, weapon_type, damage, result)
    )
    conn.commit()

conn.close()



