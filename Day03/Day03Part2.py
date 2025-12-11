# Day03 Part 2

def process_file(filename, span):
    sum = 0

    for  digits in [span]:
        with open(filename) as file:
            for line in file:
                # print(f"\nline: {line.strip()}")
                line = list(line.strip())

                # set bounds
                start = 0
                end = len(line) - digits

                for i in range(digits):
                    subset = line[start:end+1]
                    # print(f"max(subset): {max(subset)}")
                    # print(f"subset.index(max(subset)): {subset.index(max(subset))}")
                    index = subset.index(max(subset))
                    # print(f"index: {index}")
                    # print(f"adding to sum: {int(subset[index]) * (10 ** (digits - i - 1))}")
                    sum += (int(subset[index]) * (10 ** (digits - i - 1)))
                    start = start + index + 1
                    end += 1
        # print(f"For {digits:2} digits the solution is {sum}")

    return sum

# 2 batteries per bank
# print(f"total joltage: {process_file("Day03/testdata.txt", 2)}")
# print(f"total joltage: {process_file("Day03/realdata.txt", 2)}")

# 12 batteries per bank
# print(f"total joltage: {process_file("Day03/testdata.txt", 12)}")
print(f"total joltage: {process_file("Day03/realdata.txt", 12)}")