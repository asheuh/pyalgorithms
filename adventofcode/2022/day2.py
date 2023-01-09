from read_file import read_data


def assumption():
    me = {'X': 1, 'Y': 2, 'Z': 3}
    maops = {'A': me, 'B': me, 'C': me}
    win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    return win, draw, maops

def best_strategy():
    # X means you need to lose: lose 0 points,
    # Y means you need to end the round in a draw: draw = 3 points,
    # Z means you need to win: win = 6 points
    me = {'X': 1, 'Y': 2, 'Z': 3}
    draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    maops = {'X': (0, lose), 'Y': (3, draw), 'Z': (6, win)}
    return maops, me

def rpc(strategy): 
    score = 0
    win, draw, maops = assumption()

    for st in strategy:
        s, t = st
        val = maops[s][t]
        w = win[s]
        d = draw[s]
        if w == t:
            val += 6

        if d == t:
            val += 3

        score += val
    return score

def rpc2(strategy):
    score = 0
    maops, me = best_strategy()

    for st in strategy:
        s, t = st
        sc, mapper = maops[t]
        val = me[mapper[s]] + sc
        score += val
    return score

def parser(inp):
    return tuple(inp.split(' '))


if __name__ == '__main__':
    data = read_data('../data/2022/sg_input.txt', parser)
    result = rpc2(data)
    print(result)
