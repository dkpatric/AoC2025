# Day03 Part 1

def process_file(filename):
    result = 0
    with open(filename) as file:
        matrix = []
        for line in file:
            line = line.strip().split("\n")
            # print(f"### line: {line}")
            for elem in line:
                matrix.append(elem)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "@" and check_neighbors(matrix, i, j) < 4:
                result += 1

    return result

def check_neighbors(matrix, row, col):
    rolls_nearby = 0
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in neighbors:
        curr_row = row + dx
        curr_col = col + dy
        if curr_row >= len(matrix) or curr_row < 0:
            continue
        if curr_col >= len(matrix[0]) or curr_col < 0:
            continue
        if matrix[curr_row][curr_col] == "@":
            rolls_nearby += 1
    
    return rolls_nearby

# print(f"Result: {process_file("Day04/testdata.txt")}")
print(f"Result: {process_file("Day04/realdata.txt")}")
