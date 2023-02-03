import pdb
import pprint
import math
import copy

from heapq import *
from time import sleep
from collections import defaultdict
from queue import PriorityQueue

from helpers import *


def solver_puzzle(h, w, k, coord=False, first=None, second=None):
    grid = []
    small_grid = []
    number = 1

    for i in range(1, h + 1):
        rows = []
        values = []
        for j in range(w):
            if k:
                rows.append(number)
            else:
                rows.append(0)
            if coord:
                x, y = i - 1, j - 1
                if first[x][y] == 0:
                    values.append(second[x][y])
            number += 1
        grid.append(rows)
        small_grid.append(values)
    return grid, small_grid

def contains(iterable, new_item):
    for item in iterable:
        if item == new_item:
            return True
    return False

def sliding_puzzle_failed_attempt(puzzle):
    mover = 0
    h = len(puzzle) # height
    standard_w = len(puzzle[0]) # width
    w = standard_w
    SOLVED, _ = solver_puzzle(h, w, False)
    solved, _ = solver_puzzle(h, w, True)
    start = (0, 0)
    stack = [(1, start, '0')]
    moves = []
    seen = {}
    small_grid = None
    col, is_col = False, False
    algo = Algorithm()
    sleep(.3)
    added = 1
    
    while stack:
        mapp = create_map(puzzle, 'four')
        target = stack.pop(0)
        value, target_coord, key = target

        actual_coord, neighbours = mapp.get(value)
        value_at = (value, actual_coord)
        x, y = target_coord
        next_value = value + added if isinstance(value, int) else 0
        if value in seen and (key != 'D' and key != 'L'):
            continue

        if SOLVED[standard_w - 3][standard_w - 1] == 1 == SOLVED[standard_w - 3][standard_w - 2]:
            break

        if is_col:
            added = 5
            a, b = 1, 0
            t = x
            cnx, cny = (standard_w - 1, start[0])
            ccnx, ccny = (standard_w - 1, cny + 1)
        else:
            added = 1
            a, b = 0, 1
            t = y
            cnx, cny = (start[0], standard_w - 1)
            ccnx, ccny = (cnx + 1, standard_w - 1)

        nx, ny = (x + a, y + b)
        n2xy = [(next_value, (nx, ny), '0')]
        if t + 1 == (standard_w - 2):
            nx, ny = (cnx, cny)
            nxx, nyy = (ccnx, ccny)
            mover_target = (mover, (nx - a, ny - b), 'L')
            stack = []
            n2xy = [
                (next_value, (nx, ny), '0'),
                (next_value + added, (nxx, nyy), '0'),
                mover_target
            ]

        if key == 'L':
            n_v = puzzle[nx][ny]
            nxx, nyy = (nx + b, ny + a)
            nn_v = puzzle[nxx][nyy]
            mover_target = (mover, (nxx, nyy), 'D')
            n2xy = [
                (n_v, (x, y), '0'),
                (nn_v, (nx, ny), '0'),
                mover_target
            ]
            if is_col:
                col = True
                is_col = False
            else:
                is_col = True
                col = False
            added = w
            to_check = [(n2xy[1][0], n2xy[2][1]), (n2xy[2][0], n2xy[0][1]), (n2xy[0][0], n2xy[1][1])]
            can_swap = True
            for item in to_check:
                item_value, item_coord = item
                icx, icy = item_coord
                if puzzle[icx][icy] != item_value:
                    can_swap = False
                    break

                if item_value:
                    SOLVED[icx][icy] = 1

            if can_swap:
                first_coord = to_check.pop()
                temp_first = first_coord
                moves = [*[to_check[0][1], first_coord[1]], *moves]
                while to_check:
                    fcx, fcy = first_coord[1]
                    second_coord = to_check.pop()
                    ffcx, ffcy = second_coord[1]
                    copy_grid = copy.deepcopy(puzzle)
                    copy_grid[fcx][fcy] = puzzle[ffcx][ffcy]
                    copy_grid[ffcx][ffcy] = puzzle[fcx][fcy]
                    puzzle = copy_grid
                    SOLVED[ffcx][ffcy] = 1
                    temp_first = second_coord
                else:
                    fvalue, ft_coord = temp_first
                    SOLVED[ft_coord[0]][ft_coord[1]] = 0

        if key == 'D':
            if not is_col:
                w -= 1
                s = w
                a = 0
                b = 1
                added = 1
            else:
                a = 1
                b = 0
                s = w
                added = standard_w

            nx, ny = (standard_w - s, standard_w - s) # reset and move to next row
            start = (nx, ny)
            value_now = solved[nx][ny]
            value_next = solved[nx][ny] + added
            n2xy = [(value_now, (nx, ny), '0'), (value_next, (nx + a, ny + b), '0')]
            stack = []

        for next_target in n2xy:
            next_target_value, next_target_coord, _ = next_target
            vx, vy = next_target_coord
            v = Vector(vx, vy, h, standard_w)
            if v.is_inside():
                stack.append(next_target)

        if target_coord == actual_coord:
            if key != 'D':
                SOLVED[x][y] = 1
            continue

        mover_position = mapp.get(mover)
        space_at, mover_neighbours = mover_position
        space_goal = calculate_goal(puzzle, neighbours, target_coord, space_at, actual_coord, SOLVED)
        puzzle, SOLVED, col, moves = algo.solver_algorithm(
            space_at,
            space_goal,
            actual_coord,
            target,
            puzzle,
            SOLVED,
            col,
            moves
        )
        seen[value] = True
    return moves


def calculate_goal(puzzle, neighbours, my_goal, space_at, where_am_at, solved_puzzle):
    i, j = my_goal
    u, v = where_am_at
    r, c = space_at
    value = puzzle[u][v]
    space_goal = None
    pprint.pprint(puzzle)

    manhattan_distance = math.inf 
    space_at_space_goal_dist = math.inf 
    found_neighbours = {}

    for neighbour in neighbours:
        nx, ny = neighbour.x, neighbour.y
        is_outside = (abs(ny - j) > abs(v - j)) or (abs(nx - i) > abs(u - i))
        is_goal = (nx, ny) == my_goal
        solved = solved_puzzle[nx][ny]
        if is_goal:
            return my_goal

        if puzzle[nx][ny] == value or is_outside or solved:
            continue


        distance = abs(i - nx) + abs(j - ny) # calculate distance from neighbour to my goal
        if distance <= manhattan_distance:
            manhattan_distance = distance

            # if short distance found, calculate shortest from space current space position to that neighbour
            ss_distance = abs(nx - r) + abs(ny - c)
            if ss_distance < space_at_space_goal_dist:
                space_at_space_goal_dist = ss_distance
                space_goal = (nx, ny)
    return space_goal


class Algorithm:
    def contains(self, iterable, value):
        for item in iterable:
            if item == value:
                return True
        return False

    def heauristic(self, start, goal):
        sx, sy = start
        gx, gy = goal
        return abs(sx - gx) + abs(sy - gy)

    def solver_algorithm(self, start, goal, where_am_at, target, grid, solved2, col, moves): 
        h = len(grid) # height
        w = len(grid[0]) # width
        target_value, my_goal, kk = target
        # Set solved
        solved, _ = solver_puzzle(h, w, True)
        space_at = start
        if solved[my_goal[0]][my_goal[1]] == True == grid[my_goal[0]][my_goal[1]]:
            pprint.pprint(solved2)
            return grid, solved2, col

        heap, explored = [], set()
        heap.append(start) # start
        cost_score = defaultdict(int)
        cost_score[start] = 0 # Cost
        came_from = {}
        done = {}
        if target_value == 0:
            goal = my_goal

        while heap:
            current = heap.pop(0)
            mapp = create_map(grid, 'four')

            if current == goal:
                temp_current = current
                total_path = [where_am_at, current]
                seen = {}
                while current in came_from:
                    temp = current
                    current = came_from[current]
                    total_path.append(current)
                    if current == space_at:
                        if total_path[0] == total_path[-1]:
                            _ = total_path.pop(0)
                        break

                # Update grid
                actual_coord = total_path.pop()
                if not moves:
                    moves = [current]

                moves = [*total_path, *moves]
                while total_path:
                    fromx, fromy = current
                    tox, toy = total_path.pop()
                    copy_grid = copy.deepcopy(grid)
                    copy_grid[fromx][fromy] = grid[tox][toy]
                    copy_grid[tox][toy] = grid[fromx][fromy]
                    grid = copy_grid
                    actual_coord = current
                    current = (tox, toy)

                if temp_current == my_goal:
                    f, l = my_goal
                    cx, cy = current
                    A = 0
                    B = 1
                    if col:
                        A = 1
                        B = 0

                    if target_value == 0:
                        copy_g = copy.deepcopy(grid)
                        copy_g[f][l] = grid[cx][cy]
                        copy_g[cx][cy] = grid[f][l]
                        f1, f2 = f + A, l + B
                        l1, l2 = f1 + B, f2 + A
                        grid = copy_g
                        copy_g = copy.deepcopy(grid)
                        pprint.pprint(grid)
                        copy_g[f][l] = grid[f1][f2]
                        copy_g[f1][f2] = grid[f][l]
                        grid = copy_g
                        copy_g = copy.deepcopy(grid)
                        copy_g[f1][f2] = grid[l1][l2]
                        copy_g[l1][l2] = grid[f1][f2]
                        grid = copy_g
                        solved2[f][l] = 1

                        solved2[f1][f2] = 1
                        solved2[l1][l2] = 0
                        moves = [*[(l1, l2), (f1, f2)], *moves]
                    else:
                        solved2[f][l] = 1
                    col = False
                    return grid, solved2, col, moves

                mapp = create_map(grid, 'four')
                _, neighbours = mapp.get(grid[actual_coord[0]][actual_coord[1]])
                space_goal = calculate_goal(grid, neighbours, my_goal, current, actual_coord, solved2)
                goal = space_goal
                where_am_at = actual_coord
                heap, explored = [], set()
                cost_score, done = {}, {}
                cost_score[current] = 0
                space_at = current
                heap.append(current)
                continue

            x, y = current
            _, neighbours = mapp.get(grid[x][y])
            for neighbour in neighbours:
                nx, ny = neighbour.x, neighbour.y
                child = (nx, ny)
                if child not in cost_score:
                    cost_score[child] = math.inf

                score = cost_score[current]
                total_score = score + self.heauristic(child, goal)
                is_me = where_am_at == child
                neighbour_solved = solved2[nx][ny]
                is_outside = (abs(ny - my_goal[1]) > abs(y - my_goal[1]) and (goal[0] == nx and goal != child)) or \
                        (abs(nx - my_goal[0]) > abs(x - my_goal[0]) and (goal[1] == ny and goal != child))
                if child in done:
                    continue

                if total_score < cost_score[child] and not is_me and not neighbour_solved and not is_outside:
                    came_from[child] = current
                    cost_score[child] = total_score 

                    if not self.contains(heap, child):
                        heap.append(child)
                done[child] = done
            explored.add(current)
        return grid, solved2, col, moves

def parse_moves(moves):
    reversed_moves = list(reversed(moves))
    l = len(reversed_moves)
    i = 0
    j = 1 
    moves = []

    while j < l:
        x, y = reversed_moves[i]
        xx, yy  = reversed_moves[j]
        v = Vector(x=x, y=y)
        directions = v.directions()

        for direction, coords in directions.items():
            nx, ny = coords
            nv = v.plus(v, nx, ny)
            nxx, nyy = nv.x, nv.y

            if (nxx, nyy) == (xx, yy):
                moves.append(direction)
        i += 1
        j += 1
    print(','.join(moves))

if __name__ == '__main__':
    p4 = [
        [1, 15, 9, 7],
        [5, 14, 4, 0],
        [3, 10, 11, 12],
        [13, 6, 2, 8]
    ]
    p3 = [[7, 5, 4], [3, 2, 0], [1, 8, 6]]
    puzzle = [
        [1, 3, 4, 12, 13],
        [11, 6, 7, 8, 10],
        [17, 16, 5, 19, 0],
        [18, 15, 2, 9, 14],
        [21, 20, 22, 23, 24]
    ]
    puzzle2 = [
        [6, 1, 4, 5, 8],
        [12, 10, 3, 7, 9],
        [11, 16, 0, 2, 14],
        [17, 18, 15, 13, 19],
        [22, 21, 24, 23, 20]
    ]
    puzzle3 = [
        [1, 7, 0, 18, 14],
        [11, 6, 4, 9, 5],
        [12, 13, 2, 3, 10],
        [16, 17, 22, 8, 15],
        [21, 23, 24, 20, 19]
    ]
    puzzle4 = [
        [6, 11, 1, 7, 5],
        [13, 9, 3, 19, 14],
        [16, 8, 2, 4, 10],
        [18, 22, 17, 20, 24],
        [12, 0, 21, 23, 15]
    ]
    p = [[11, 6, 1, 2, 4], [18, 7, 12, 0, 5], [17, 3, 10, 13, 16], [21, 22, 23, 19, 9], [14, 24, 8, 20, 15]] 
    moves = sliding_puzzle_failed_attempt(puzzle4)
    parsed_moves = parse_moves(moves)
