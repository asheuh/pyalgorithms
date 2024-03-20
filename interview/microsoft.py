def solve(f, s):
    if not f or not s:
        return

    grid = [f, s]
    i = 0
    n = len(f) - 1
    w = len(grid[0])
    h = len(grid)
    stack = [(i, i)]
    goal = (n, n)
    cmax = grid[0][0]
    seen = []

    while stack:
        current = stack.pop()
        x, y = current
        down = (x + 1, y)
        right = (x, y + 1)
        vdown = grid[down[0]][down[1]]
        seen.append(grid[x][y]) 

        if right[1] >= w:
            seen.append(vdown)
            break

        vright = grid[right[0]][right[1]]
        if vdown <= vright:
            drow = grid[1]
            k = down[1]
            downvals = []
            cmax = max(cmax, vright)
            while k <= n and drow[k] < cmax:
                downvals.append(drow[k])
                k += 1

            if k > n:
                seen.extend(downvals)
                break
            stack.append(right)

        elif vright < vdown:
            stack.append(right)

    print('PATH ====>', seen)
    return max(seen)

if __name__ == '__main__':
    A = [-5, -1, -3]
    B = [-5, 5, -2]
    result = solve(A, B)
    print('RESULT ==>', result)
