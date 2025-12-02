
def main(filename):
    with open(filename) as file:
        for line in file:
            print(line.strip())
    # starting location for dial
    dial = 50
    print("testing")

main("demofile.txt")