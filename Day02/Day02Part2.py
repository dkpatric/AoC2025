# Day02 - Part2

def find_patterns(number):    
    num_str = str(number)

    # reject single digits
    if len(num_str) == 1:
        return False
    
    # 1 group - check if all same
    check = True
    for i in range(len(num_str)):
        if num_str[0] != num_str[i]:
            check = False
    if check:
        print(f"*** groups(1): {number}")
        return True

    # 2 groups
    if len(num_str) % 2 == 0:
        zone = len(num_str) // 2
        if num_str[0:zone] == num_str[zone:zone * 2]:
            print(f"*** groups(2): {number}")
            return True
    # 3 groups
    if len(num_str) % 3 == 0:
        zone = len(num_str) // 3
        if num_str[0:zone] == num_str[zone:zone * 2] == num_str[zone * 2:zone * 3]:
            print(f"*** groups(3): {number}")
            return True

    # 4 groups
    if len(num_str) % 4 == 0:
        zone = len(num_str) // 4
        if num_str[0:zone] == num_str[zone:zone * 2] == num_str[zone * 2:zone * 3] == \
        num_str[zone * 3:zone * 4]:
            print(f"*** groups(4): {number}")
            return True
        
    # 5 groups
    if len(num_str) % 5 == 0:
        zone = len(num_str) // 5
        if num_str[0:zone] == num_str[zone:zone * 2] == num_str[zone * 2:zone * 3] == \
        num_str[zone * 3:zone * 4] == num_str[zone * 4:zone * 5]:
            print(f"*** groups(5): {number}")
            return True
            
    return False

def process_file(filename):
    sum = 0

    with open(filename) as file:
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
                if find_patterns(item):
                    sum += item
            # break

    return sum

# print(process_file("Day02/testdata.txt"))

# start = int(input("Start value: "))
# stop  = int(input("Stop value:  "))
# for num in range(start, stop + 1):
#     if find_repeats(num):
#         print(f"repeats: {num}")
#     else:
#         if find_pattern(num):
#             print(f"pattern: {num}")

print(process_file("Day02/realdata.txt"))