# -*- coding: utf-8 -*-

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

dimensions = (400, 100, 1000)
for dimension in dimensions:
    print(dimension)


foods = ('rice', 'cola', 'beaf', 'meat', 'dumpling')
for food in foods:
    print(food)

foods = ('rice', 'chicken', 'beaf', 'meat', 'dumpling')
for food in foods:
    print(food)

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

if 'AUDI' in [car.upper() for car in cars]:
    print('True')
