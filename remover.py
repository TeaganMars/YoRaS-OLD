Eu4 = '2707 - Kismayo.txt'

f = open(Eu4, "r")
lines = f.readlines()
f.close()

f = open(Eu4, "w")
for line in lines:
    for i in range(1405, 2000):
        if not line.startswith(str(i)):
            f.write(line)
f.close()

'''

import fileinput

for line in fileinput.input(Eu4, inplace=True):
    i = range(1405, 2020)
    if line.startswith(str(i)):break
print(line.rstrip('\r\n'))

'''
