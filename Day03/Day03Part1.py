# Day03 Part 1

def process_file(filename):
    sum = 0

    with open(filename) as file:
        for line in file:
            bank = line.strip()
            # print(f"### bank:        {bank}")
            # find the highest number not at the end
            sorted_bank = "".join(sorted(bank[0:-1], reverse=True))
            # print(f"### sorted_bank: {sorted_bank}")
            tens = sorted_bank[0]
            loc1 = bank.find(tens)
            # find the highest number after the tens position location
            sorted_bank = "".join(sorted(bank[loc1 + 1:], reverse=True))
            # print(f"### sorted_bank: {sorted_bank}")
            ones = sorted_bank[0]
            joltage = int(tens + ones)
            # print(f"joltage: {joltage}\n")
            sum += joltage


    return sum

# print(f"total joltage: {process_file("Day03/testdata.txt")}")
print(f"total joltage: {process_file("Day03/realdata.txt")}")
