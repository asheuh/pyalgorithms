import math
from time import time

# paper: https://pubsonline.informs.org/doi/epdf/10.1287/ited.3.1.45
# n: the number of rods or pieces
# P: the set of all pieces = {1, 2, 3, ..., n}
# Plaforms or gold rings: {'L': [], 'C': [], 'R': []}
# S = initial state = {'L': {1, 2, 3, ..., n}, 'C': {}, 'R': {}}
# minimum number of moves to solve?
# x(a, b) represents the decision (move a piece from platform a to platform b) i.e x(L, R)
# Rules of the game
#   - Only one piece may be moved at a time.
#   - Each move consists of taking the upper piece from one of the stacks and placing it on top of another stack or on an empty rod.
#   - No piece may be placed on top of a piece that is smaller than it
#
# D(S): is the state of all feasible pairs(those meeting the requirements)
#   e.g if P={1,2,3,4,5}, L={5}, C={1,2,3,4},R={}
#       then D(S) = {(L, R), (C, R), {C, L}}


def f(m):
    # s: initial state, g: goal state, n: number pieces
    # formula: M(s,s') + 1 + M(s",g)
    # where M(a, b) is number of moves required to 
    # move from state a to state b
    # how to find M(a, b)? M(s,s') = f(s,s') ,    M(s",g) = f(s",g)
    
    # function equation of DP? f(({1,...,n},{},{}),({},{},{1,...,n})) 
    #   = f(({1,2,...,n},{},{}),({n},{1,...,n-1},{})) + 1 + f(({},{1,...,n-1},{n}),({},{},{1,...,n-1}))
    #   = F(m) = F(m) + 1 + F(m) = 2F(m) + 1 = F(m) = 2**m - 1 
    # X(m, a, b) = X(m - 1, a, c); X(1, a, b); X(m - 1, c, b)
    # return minimum number of moves to solve the problem
    return 2**m - 1

def find_ring_with_smallest(move_set, state, move):
    smallest = math.inf
    diff = move_set ^ {move}
    init = None
    for mv in diff:
        if not state[mv]:
            continue

        v = state[mv][-1]
        if v < smallest:
            init = mv
            smallest = v
    if not init:
        return move
    return init

def towers_of_hanoi(n):
    """
    start: initial state
    goal: target state
    """
    k = f(n) # k is minimum number of moves to solve problem
    P = [i for i in range(n, 0, -1)] # the set of all pieces
    state = {'L': P, 'C': [], 'R': []}
    # goal_state = {'L': [], 'C': [], 'R': P}
    init_move = 'L'
    move = 'R'
    matchpattern = {'L': 'R', 'R': 'C', 'C': 'L'}
    mismatchpattern = {'L': 'C', 'C': 'R', 'R': 'L'}
    pattern = mismatchpattern

    if n & 1:
        pattern = matchpattern

    for m in range(1, k + 1):
        piece = state[init_move].pop()
        move_set = set(state.keys())

        move = pattern[init_move] 
        last_value = math.inf
        if state[move]:
            last_value = state[move][-1]

        if last_value < piece:
            # handle case where value on top in smaller
            move = next(iter({init_move, move} ^ move_set))

        state[move].append(piece)
#         print('NEW STATE ------>>>>', state)
        init_move = find_ring_with_smallest(move_set, state, move)
        # Next move
    return state

def towers_of_hanoi_recursion(n, a, b, c):
    if n == 1:
        value = a.pop()
        c.append(value)
        print([a, b, c])
        return

    towers_of_hanoi_recursion(n - 1, a, c, b) 
    v = a.pop()
    c.append(v)
    print([a, b, c])
    towers_of_hanoi_recursion(n - 1, b, a, c)

if __name__ == '__main__':
    n = 25
#     P = [i for i in range(n, 0, -1)]
#     goal = towers_of_hanoi_recursion(n, P, [], [])
    for i in range(1, n + 1):
        t1 = time()
        goal = towers_of_hanoi(i)
        t2 = time()
        print('TIME ELAPSED', (t2 - t1))
        print(i, "------->>>>", goal)
