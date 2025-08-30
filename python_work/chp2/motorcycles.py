motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#motorcycles[0] = 'ducati'
#print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')
print(motorcycles2)
motorcycles2.insert(0, 'ducati')
print(motorcycles2)
del motorcycles2[0]
print(motorcycles2)

popped_motorcycle = motorcycles2.pop()
print(motorcycles2)
print(popped_motorcycle)