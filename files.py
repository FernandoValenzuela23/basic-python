import os

basePath = os.path.dirname(__file__)
filePath = os.path.join(basePath, 'resources\\countries.txt')
f = open(filePath, mode='r+', encoding='utf-8', newline='\n')
    
exists = False
newCountry = input('Enter the name of the new Country: ')

if f.readable():
    lines = f.readlines()
    print(lines)
    for ln in lines:
        print(ln.find(newCountry))
        if ln.find(newCountry) != -1:
            exists = True

if exists is False:
    f.write('\n'+newCountry)
else:
    print('This country exists already')
    
f.seek(0)
for ln in f.readlines():
    print(ln)
f.close()
