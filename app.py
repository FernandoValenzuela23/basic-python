from math import *

dog1 = 'Toby'
dog2 = 'Spock'


try:    
    print('hello'.capitalize(), dog1.upper(), '\nand', dog2.capitalize(), ', naugthy dogs')
    print(dog1[2])
    print(25%4)
    print(abs(-456))
    print(max(55, 6869, 88, 100, 250, 4000))
    print(bin(23))
    print(sqrt(36))
    
    print('Controlled exception:')
    print (24/0)
except Exception as ex:
    print(type(ex), ex)

