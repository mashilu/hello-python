name = "ma Shilu"

print(name.title())
print(name.upper())
print(name.lower())

test = "   test strip    "
print(test.strip())
print(test.lstrip())
print(test.rstrip())

motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[2]
print(motorcycles)

poppedmotor = motorcycles.pop()
print(motorcycles)
print(poppedmotor)

motorcycles.remove('honda')
print(motorcycles)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

list_len = len(players)
start = (list_len - 3) // 2
print(players[start:start+3])

