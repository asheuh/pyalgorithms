from collections import Counter, defaultdict
import pprint

from read_file import read_data

def parser(line):
    return line.split(' ')

def parse_types(hb, card_ranks):
    mapper = defaultdict(list) 

    for h, b in hb:
        counter = Counter(h)
        counts = counter.values()
        length = len(counts)

        match max(counts):
            case 5:
                mapper[7].append((h, int(b), 7))

            case 4:
                mapper[6].append((h, int(b), 6))

            case 3:
                match length:
                    case 2:
                        mapper[5].append((h, int(b), 5))

                    case 3:
                        mapper[4].append((h, int(b), 5))
            case 2:
                match length:
                    case 3:
                        mapper[3].append((h, int(b), 3))

                    case 4:
                        mapper[2].append((h, int(b), 2))
            case 1:
                mapper[1].append((h, int(b), 1))
    return mapper

def solve(hand_bids):
    card_ranks = {
        'A': 13, 'K': 12, 'Q': 11,
        'J': 10, 'T': 9, '9': 8,
        '8': 7, '7': 6, '6': 5,
        '5': 4, '4': 3, '3': 2, '2': 1
    }
    types = parse_types(hand_bids, card_ranks)
    pprint.pprint(types)
    ranks = []
    r = 1

    for key in sorted(types.keys()):
        games = types[key]

        if ranks:
            prev = ranks[-1]
            r = prev[2] + 1

        if len(games) > 1:
            new_ranks = []

            while games: 
                game = games.pop()
                h, bid, _ = game
                if not new_ranks:
                    new_ranks.append((h, bid, r))
                    continue

                last = new_ranks[-1]
                r = last[2]
                i = 0
                while h[i] == last[0][i]:
                    i += 1

                if card_ranks[h[i]] > card_ranks[last[0][i]]:
                    r = r + 1
                    new_ranks.append((h, bid, r))
                else:
                    n_ranks = []
                    new_ranks.pop()
                    c =  len(new_ranks) - 1
                    i = 0
                    while new_ranks and card_ranks[h[i]] < card_ranks[new_ranks[c][0][i]]:
                        r = new_ranks[c][-1]
                        n_ranks.append((new_ranks[c][0], new_ranks[c][1], r+1))
                        new_ranks.pop()
                        i += 1
                        c -= 1
                        if c < 0 or i >= len(h):
                            break

                    new_ranks.extend([(h, bid, r), *n_ranks])
                    games = [last, *games]

            ranks.extend(new_ranks)

        else:
            game = games[0]
            ranks.append((game[0], game[1], r))
    
    pprint.pprint(ranks)
    result = 0
    for rank in ranks:
        _, bid, r = rank
        result += (bid * r)
    return result


if __name__ == '__main__':
    data = read_data('./data/2023/day07_input.txt', parser=parser)
    result = solve(data)
    print('PART ONE: ', result)
