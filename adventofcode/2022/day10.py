from read_file import read_data

from time import sleep


def process_signals(signals):
    x = 1
    count = 0
    counters = [19, 59, 99, 139, 179, 219]
    counters2 = [20, 60, 100, 140, 180, 220]
    totals = []

    for signal in signals:
#         sleep(0.3)
        if 'addx' in signal:
            a, b = signal.split(' ')
            k = 2
            if count in counters: 
                totals.append(x * (count + 1))
                k = 1
            elif (count + 2) in counters2:
                totals.append(x * (count + 2))
            count += k
            x += int(b)
        else:
            count += 1
            if count in counters2:
                if count == 220:
                    x -= 1
                totals.append(x * count)
    return sum(totals)


if __name__ == '__main__':
    data = read_data('../data/2022/signals_input.txt')
    res = process_signals(data)
    print(res)
