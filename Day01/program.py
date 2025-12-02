# starting location for dial
dial = 50
count = 0

print(f"initial dial: {dial}\n")

with open("realdata.txt") as file:
    for line in file:
        data = line.strip()
        direction = data[0]
        value = int(data[1:])

        if direction == "R":
            dial += value
            if dial > 99:
                dial = dial % 100
            # print(f"data: {data} -- dial: {dial}")
        elif direction == "L":
            dial -= value
            if dial < 0:
                dial = dial % 100
            # print(f"data: {data} -- dial: {dial}")
        else:
            print("*** invalid direction ***")
            SystemExit

        if dial == 0:
            count += 1

print(f"count: {count}")
