# starting location for dial
dial = 50
count = 0

print(f"initial dial: {dial}\n")

# with open("Day01/testdata.txt") as file:
with open("Day01/realdata.txt") as file:
    for line in file:
        data = line.strip()
        direction = data[0]
        value = int(data[1:])

        while value > 100:
            count += 1
            value -= 100
        if direction == "R":
            dial += value
            if dial == 100:
                dial = 0
                count += 1
            if dial >= 100: 
                dial = dial % 100
                count += 1
            print(f"data: {data} -- dial: {dial} -- count: {count}")
        elif direction == "L":
            dial -= value
            if dial < 0:
                dial = dial % 100
                if dial + value != 100:
                    count += 1
            if dial == 0:
                count += 1
            print(f"data: {data} -- dial: {dial} -- count: {count}")
        else:
            print("*** invalid direction ***")
            SystemExit

print(f"\nfinal count: {count}")
