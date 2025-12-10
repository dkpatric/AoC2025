# Day03 Part 2

def process_file(filename):
    sum = 0

    with open(filename) as file:
        for line in file:
            bank = line.strip()
            print(f"### bank:        {bank}")
            # find the highest number in first 12 digits
            sorted_bank = "".join(sorted(bank[0:12], reverse=True))
            print(f"### sorted_bank: {sorted_bank}")
            # find the highest number after the tens position location
            # sorted_bank = "".join(sorted(bank[loc1 + 1:], reverse=True))
            # print(f"### sorted_bank: {sorted_bank}")
            # ones = sorted_bank[0]
            # joltage = int(tens + ones)
            # print(f"joltage: {joltage}\n")
            # sum += joltage
            # break

    return sum

def test(filename):
    sum = 0

    with open(filename) as file:
        for line in file:
            bank = line.strip()
            print(f"### bank:        {bank}")
            # find the highest number in first 12 digits
            sorted_bank = "".join(sorted(bank[0:12], reverse=True))
            print(f"### sorted_bank: {sorted_bank}")
            # find the highest number after the tens position location
            # sorted_bank = "".join(sorted(bank[loc1 + 1:], reverse=True))
            # print(f"### sorted_bank: {sorted_bank}")
            # ones = sorted_bank[0]
            # joltage = int(tens + ones)
            # print(f"joltage: {joltage}\n")
            # sum += joltage
            # break

    return sum

test("Day03/testdata.txt")
# print(f"total joltage: {process_file("Day03/realdata.txt")}")
