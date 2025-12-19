# Day05

def part1(filename):
    freshCnt = 0
    ranges = []

    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line == "":
                break
            l, r = (int(x) for x in line.split('-'))
            ranges.append((l, r))
            
        for line in file:
            ing = int(line.strip())
            for l, r in ranges:
                if l <= ing <= r:
                    freshCnt += 1
                    break

    return freshCnt

def part2(filename):
    ranges = []
    valid = 0

    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line == "":
                break
            l, r = (int(x) for x in line.split('-'))
            ranges.append((l, r))
        # print(f"ranges: {ranges}")

        ranges = sorted(ranges, key=lambda r: r[0])
        # print(ranges)

        merged = []
        curr_start, curr_end = ranges[0]

        for start, end in ranges[1:]:
            # Overlapping or contiguous ranges (inclusive)
            if start <= curr_end + 1:
                curr_end = max(curr_end, end)
            else:
                merged.append((curr_start, curr_end))
                curr_start, curr_end = start, end

        merged.append((curr_start, curr_end))
        # print(merged)

        for l, r in merged:
            valid += (r - l + 1)

    return valid

# print(f"Part 1 (test) fresh ingredients: {part1("Day05/testdata.txt")}")
# print(f"Part 1 (real) fresh ingredients: {part1("Day05/realdata.txt")}")
# print(f"Fresh Ingredients: {part2("Day05/testdata.txt")}")
print(f"Fresh Ingredients: {part2("Day05/realdata.txt")}")