import math

def tower_of_hanoi(n, k, a, b, c):
    p = [i for i in range(n, 0, -1)]
    state = {'L': p, 'C': [], 'R': []}
    m = 2**n - 1 # Minimum number of moves
    mismatch = {'L': 'R', 'R': 'C', 'C': 'L'}
    match = {'L': 'C', 'C': 'R', 'R': 'L'}
    init_move = 'L'
    move_to = 'R'
    pattern = match

    if n & 1:
        pattern = mismatch

    while m:
        piece = state[init_move].pop()
        move_to = pattern[init_move]
        move_set = set([i for i in state.keys()])

        last_value = math.inf
        if state[move_to]:
            last_value = state[move_to][-1]

        if last_value < piece:
            move_to = next(iter({move_to, init_move} ^ move_set)) 

        state[move_to].append(piece)
        init_move = find_initial_move(state, move_to, move_set)
        m -= 1
    return state

def find_initial_move(state, last_move, _set):
    init = None
    small = math.inf
    moves = {last_move} ^ _set
    for move in moves:
        if not state[move]:
            continue

        last = state[move][-1]
        if last < small:
            small = last
            init = move
    return init



if __name__ == '__main__':
    n, k, a, b, c = 3, 7, 2, 4, 6
    final_state = tower_of_hanoi(n, k, a, b, c)
    print(final_state)
