lines = []
with open("input.txt") as file:
    for line in file:
        lines.append(line.rstrip())
    for _ in sorted(lines, reverse=True):
        print(f"Hello, {_}")