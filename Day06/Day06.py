# Day06

def part1(filename):
    sum = 0

    with open(filename) as file:
        table = [line.strip('\n').split() for line in file]
    # print(f"table: {table}")
    
    oper = table[-1]
    table = list(zip(*table[:-1])) # zip(*table) => transposes table
    # print(f"table (trans): {table}")

    result = 0
    for item in range(len(table)):
        result += eval(oper[item].join(table[item]))

    return result

def part2(filename):
    with open(filename) as file:
        table = [list(line.strip('\n'))[::-1] for line in file] # from right to left
    # print(table)
    oper = ''.join(table[-1]).split()
    table = [''.join(t).strip() for t in zip(*table[:-1])] # zip(*table) => transposes table
    table = [s.split('|') for s in '|'.join(table).split('||')]

    result = 0
    for item in range(len(table)):
        # print(oper[item].join(table[item]))
        result += eval(oper[item].join(table[item]))
    
    return result
        
# print(f"Part 1 test: {part1("Day06/testdata.txt")}")
# print(f"Part 1 real: {part1("Day06/realdata.txt")}")
# print(f"Part 2 test: {part2("Day06/testdata.txt")}")
print(f"Part 2 real: {part2("Day06/realdata.txt")}")