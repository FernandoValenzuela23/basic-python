def add(num1, num2):
    return num1+num2

print(add(1,4))

def greeting(name):
    return 'Hi '+name

name = input('Input your name: ')
print(greeting(name))

def greetingGroup(*names):
    for n in names:
        if n != 'Fernando':
            print('Hi '+n)
        else:
            print('OMG are you?')

greetingGroup('Fernando', 'Sofia', 'Britany')

def greetingGroup2(*names):
    i = 0
    while i < len(names):
        print('Hi '+names[i])
        i = i +1

greetingGroup2('Sofia', 'Britany','Fernando')