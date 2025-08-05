"""Add three list in one and print him"""
alien_0 = {'color':'green', 'points': 5}
alien_1 = {'color':'red', 'points': 15}
alien_2 = {'color':'blue', 'points': 25}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


aliens = []

for alien_numbers in range(30):
    new_alien = {'color':'green','points': 5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)

print(f"Total number of aliens: {len(aliens)}")
