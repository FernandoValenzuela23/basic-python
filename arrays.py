countries = ['Ecuador', 'China', 'France', 'Thailand', 'Rusia']
print(countries[2])
print(countries[2][0])
print(countries[2:])
print(countries[2:4])
print(countries[-2])
countries[1] = input('Name of the country to replace \''+countries[1]+'\': ')
print(countries)
print('---------------------------')

list1 = [2,3,4,5]
list1.insert(0, 1)
list2 = ['Orange','Banana', 'Mango']
list2.append('Strawberry')
list2.remove('Banana')
list1.extend(list2)
print(list1)

list3 = ['Cat','Dog', 'Cat', 'Duck', 'Elephant']
print(list3.count('Cat'))
list3.sort()
print(list3)
list3.reverse()
print(list3)

list4 = list3.copy()
list4.remove('Cat') # First ocurrence only 
list4.pop()
print(list3)
print(list4)

del list4[1]
print(list4)

for x in range(5):
    print(x)

for x in range(15, 22):
    print(x)