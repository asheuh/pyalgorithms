import pprint

from collections import Counter

from read_file import read_data


def part_one(lines, is_p2=False):
    illegal_score = 0
    open_map = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>' 
    }
    score_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    if is_p2:
        autocompletion_scores = []

    for line in lines:
        i = 0
        n = len(line)
        stack = []
        syntax_error = False

        while i < n and not syntax_error:
            curr = line[i]
            while curr in open_map:
                stack.append(curr)
                i += 1
                if i < n:
                    curr = line[i]
                else:
                    break

            prev = stack.pop()
            closing = open_map[prev]

            if closing != curr and prev != curr:
                syntax_error = True
                illegal_score += score_map[curr]
                break # syntax error detected 

            i += 1
            if i >= n and not syntax_error:
                if is_p2: # part two
                    if curr in open_map:
                        stack.append(curr)
                    stack.reverse()
                    completion = ''.join(open_map[i] for i in stack)
                    completion_score_map = {
                        ')': 1,
                        ']': 2,
                        '}': 3,
                        '>': 4
                    }
                    total_score = 0

                    for char in completion:
                        total_score *= 5
                        total_score += completion_score_map[char]

                    autocompletion_scores.append(total_score)
                break # incomplete line or valid
    if is_p2:
        autocompletion_scores.sort()
        mid = len(autocompletion_scores) // 2
        return autocompletion_scores[mid]

    return illegal_score

def part_two(data):
    return part_one(data, True)

if __name__ == '__main__':
    data = read_data('data/2021/day10_input.txt')
    result_p1 = part_one(data)
    result_p2 = part_two(data)
    print(result_p1, result_p2)
