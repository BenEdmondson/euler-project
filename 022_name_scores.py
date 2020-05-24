import time
import string


time_1 = time.time()

# define an alphabet
alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# define reverse lookup dict
rdict = dict([(x[1], x[0] + 1) for x in enumerate(alfabet)])

file1 = open('resources/prob_22.txt', 'r')

for line in file1.readlines():
    line = line[1:-1]
    names = line.split("\",\"")

names.sort()

list_total = 0
for index, name in enumerate(names):
    name_value = 0
    for letter in name:
        name_value += rdict[letter]
    list_total += (index + 1) * name_value

print(list_total)
print(time.time() - time_1)