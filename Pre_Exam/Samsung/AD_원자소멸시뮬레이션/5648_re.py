vector = [(0, 1), (0, -1), (-1, 0), (1, 0)]
aside = {
    0: 1,
    1: 0,
    2: 3,
    3: 2,
}

for ro in range(int(input())):
    N = int(input())

    board = [[0 for _ in range(2002)] for _ in range(2002)]

    energys = 0
    atoms = []
    temp_locations = []

    for _ in range(N):
        x, y, v, e = map(int, input().split())
        x += 1000
        y += 1000
        board[x][y] = (v, e, 0)
        atoms.append((x, y, v, e, 0))

    before = 0
    while atoms:
        while True:

            atom = atoms.pop(0)

            ax, ay, av, ae, t = atom
            print(atom)

            if t != before:
                atoms.append(atom)
                before = t + 1
                break

            dx, dy = vector[av]
            rx = ax + dx
            ry = ay + dy

            if not board[ax][ay] or not 0 <= rx <= 2000 or not 0 <= ry <= 2000:
                continue

            board[ax][ay] = 0

            if board[rx][ry] and board[rx][ry][2] == t + 1:
                temp_locations.append((rx, ry))
                energys += ae
                continue
            board[rx][ry] = (av, ae, t + 1)

            if board[ax + 2 * dx][ay + 2 * dy] and board[ax + 2 * dx][ay + 2 * dy][0] == aside[av]:
                energys += (ae + board[ax + 2 * dx][ay + 2 * dy][1])
                continue

            atoms.append((rx, ry, av, ae, t + 1))

            before = t
        for _ in range(len(temp_locations)):
            x, y = temp_locations.pop()
            energys += board[x][y][1]

    print(energys)