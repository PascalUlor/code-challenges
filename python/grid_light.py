def createGrid(N, lamps):
        row = {}
        col = {}
        left = {}
        right = {}
        l = set()

        for i in lamps:
            row[i[0]] = row.get(i[0], 0) + 1
            col[i[1]] = col.get(i[1], 0) + 1
            left[i[0]-i[1]] = left.get(i[0]-i[1], 0) + 1
            right[i[0] + i[1]] = right.get(i[0]+i[1], 0) + 1
            l.add(tuple(i))

        return row, col, left, right, l

def remove(row, col, N, r, c, l, rg):
    if row < 0 or col < 0 or row >= N or col >= N:
        return
    r[row] -= 1
    c[col] -= 1
    l[row - col] -= 1
    rg[row + col] -= 1
def gridIllumination(N: int, lamps, queries):
    ans = []
    row, col, left, right, lamps = createGrid(N, lamps)

    for q in queries:
        if row.get(q[0]) or col.get(q[1]) or left.get(q[0] - q[1]) or right.get(q[0] + q[1]):
            ans.append(1)
        else:
            ans.append(0)

        for i in range(-1, 2):
            for j in range(-1, 2):
                if (q[0] + i, q[1] + j) in lamps:
                    remove(q[0] + i, q[1] + j, N, row, col, left, right)
                    lamps.remove((q[0] + i, q[1] + j))
    return ans

print('>>>>>>',gridIllumination(10,
[[3,4],[6,6],[1,8],[4,5],[8,7],[0,6],[5,2],[1,9]],
[[7,9],[2,8],[8,6],[6,8],[2,8]]))