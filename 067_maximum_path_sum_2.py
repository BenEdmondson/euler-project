import time

time_1 = time.time()

file1 = open('resources/prob_67.txt', 'r')
# Make the triangle list of lists
triangle = []
for line in file1.readlines():
    triangle.append(line.split())

# covert to ints
for index, row in enumerate(triangle):
    triangle[index] = [int(x) for x in row]

# Run the script
for i in range(len(triangle) - 2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

print(triangle[0][0])

print(time.time() - time_1)