import re

from functools import reduce

from read_file import read_data


def exceeds_limit_check(cc):
    color_map = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    count, color = cc
    limit = color_map[color]
    if int(count) > limit:
        return True
    return False

def compile_max_colors(group):
    map_color = {}
    for count, color in group:
        nc = int(count)
        c = map_color.get(color)
        if c is None or nc > c:
            map_color[color] = nc
    return map_color.values()

def solve(games, is_part_one=True):
    n = len(games)
    total_game_ids = (n * (n + 1)) // 2 # calculate the total game ids e.g 1+2+3+4+5

    imp_games_total_ids = 0 # impossible games total ids 
    sum_mul = 0

    for game in games:
        game_id, cubes = game.split(':')
        g_id = re.findall(r"\d+", game_id)

        assert len(g_id) == 1
        assert g_id[0]
        id = g_id[0]
        assert int(id)

        # find impossible 
        parsed_cubes = re.findall(r"(\d+)\s(\w+)", cubes)
        if is_part_one:
            found = list(filter(
                lambda x: exceeds_limit_check(x),
                parsed_cubes
            ))

            if found:
                imp_games_total_ids += int(id)
        else:
            # part two
            _colors_map = compile_max_colors(parsed_cubes)
            mul = reduce(lambda x, y: x * y, _colors_map)
            sum_mul += mul

    if is_part_one:
        result = total_game_ids - imp_games_total_ids
    else:
        result = sum_mul
    return result

if __name__ == '__main__':
    games = read_data("../data/2023/day02_input.txt")
    part_one_result = solve(games)
    print('PART ONE', part_one_result)
    part_two_result = solve(games, False)
    print('PART TWO', part_two_result)
