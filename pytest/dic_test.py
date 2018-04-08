# -*- coding: utf-8 -*-

alien_0 = dict()
alien_0['color'] = 'green'
alien_0['point'] = 5

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

print("The alien is " + alien_0['color'])
alien_0['color'] = 'yellow'
print("The alien is " + alien_0['color'])

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

print(alien_0)
del alien_0['speed']
print(alien_0)

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for k, v in user_0.items():
    print("\nKEY: " + k)
    print("\nVALUE: " + v)