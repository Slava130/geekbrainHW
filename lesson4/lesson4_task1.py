from sys import argv

script_name, hours, hours_rate, bonus = argv

print('salary =', (int(hours) * int(hour_rate)) + int(bonus))