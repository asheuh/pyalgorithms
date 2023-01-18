import pprint

from read_file import read_data
from pyalgorithms.utils import *


def validate_neighbours(sg, curr, neighbours, data):
    x, y = curr
    start, goal = sg
    curr_ele = ord(data[x][y]) 
    if curr == start:
        curr_ele = ord('a')

    if curr == goal:
        curr_ele = ord('z')

    for nr in neighbours:
        r, c = nr.x, nr.y
        ele = ord(data[r][c])
        if ele <= curr_ele + 1:
            yield nr

def hill_climbing(data):
    h = len(data) # height
    w = len(data[0]) # width
    s, goal = find_start_goal(data, 'S', 'E')
    start = Node(state=s)
    explored = []
    stack = [start]

    while stack:
        current = stack[0]
        stack = stack[1:]

        if current and current.state == goal:
            explored = []
            while current.root:
                explored.append(current.state)
                current = current.root
            break

        neighbours = validate_neighbours(
            (start.state, goal),
            current.state,
            neighbouring_vectors(current.state, h, w),
            data
        ) 

        for nr in neighbours:
            child = nr.x, nr.y
            x, y = child
            c = Node(root=current, state=child)
            if not contains(stack, c) and not contains(explored, c):
                stack.append(c)
        explored.append(current)
    return explored
    

if __name__ == '__main__':
    data = read_data('../data/2022/elevation_input.txt')
    res = hill_climbing(data)
    print(res)
    print()
    print(len(res))
