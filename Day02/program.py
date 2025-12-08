# Day02

def find_repeats(number):
    num_str = str(number)
    mid = len(num_str) // 2
    if num_str[0:mid] == num_str[mid:]:
        # print(f"*** repeated: {number}")
        return True
    else:
        return False
    
def process_file(filename):
    sum = 0

    with open(filename) as file:
    # with open("Day02/realdata.txt") as file:
        line = file.read()
        groups = line.split(",")
        for group in groups:
            limit = group.split("-")
            start = int(limit[0])
            stop = int(limit[1]) + 1
            check = list()
            for i in range(start, stop + 1):
                check.append(i)
            for item in check:
                if find_repeats(item):
                    sum += item
            # break

    return sum

# print(process_file("Day02/testdata.txt"))
print(process_file("Day02/realdata.txt"))