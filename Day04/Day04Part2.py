# Day03 Part 2

def howManyAdjacent(data, x, y):
    if data[x][y] != "@":
        return 0
    sum = 0
    for off in ([ 1, 1], [ 1, 0], [ 1, -1],
                [ 0, 1],          [ 0, -1],
                [-1, 1], [-1, 0], [-1, -1]):
        xx = x + off[0]
        yy = y + off[1]
        if xx >= 0 and yy >= 0 and xx < len(data) and yy < len(data[x]) and data[xx][yy] == "@":
            sum += 1
    return 1 if sum < 4 else 0

print()

data = []

with open("Day04/realdata.txt") as file:
    for line in file:
        data.append(list(line.strip()))

sum = 0
for gen in range(1, 1000000):
    next = []
    prev_sum = sum
    for i in range(len(data)):
        next.append([])
        for j in range(len(data[1])):
            if data[i][j] == '.':
                next[-1].append('.')
            else:
                value = howManyAdjacent(data, i, j)
                sum += value
                next[-1].append('.' if value == 1 else '@')
    if sum == prev_sum:
        break
    data = next
    if gen == 1:
        print(f"SOLUTION TO PART 1 - {sum}")
    
print(f"SOLUTION TO PART 2 - {sum}")