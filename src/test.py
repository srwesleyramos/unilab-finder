import random


def generate():
    rows = random.randint(3, 10)
    columns = random.randint(3, 10)

    grid = []

    for i in range(rows):
        grid.append([])

        for j in range(columns):
            if random.random() < 0.3:
                grid[i].append("1")
            else:
                grid[i].append("0")

    robot = (random.randint(0, rows - 1), random.randint(0, columns - 1))

    grid[robot[0]][robot[1]] = "7"

    while True:
        cheese = (random.randint(0, rows - 1), random.randint(0, columns - 1))

        if cheese != robot:
            grid[cheese[0]][cheese[1]] = "9"
            break

    return [" ".join(row) for row in grid]
