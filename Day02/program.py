
# Day02

with open("Day02/testdata.txt") as file:
# with open("Day02/realdata.txt") as file:
    line = file.read()
    ranges = line.split(",")
    for range in ranges:
        limit = range.split("-")
        start = limit[0]
        stop = limit[1]
        print(f"range to check: {range}")
        print(f"start: {start}")
        print(f"stop:  {stop}")