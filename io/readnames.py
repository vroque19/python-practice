names = []

# read by default
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip().lower())

for name in sorted(names, reverse=True):
    print(f"Hello, {name}")