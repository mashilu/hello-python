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
