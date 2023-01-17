import csv

def read_file_data(filename):
    data = ''
    redundant = {}

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        count = 0

        for item in reader:
            count += 1

            if count & 1:
                continue

            value = item[-1]
            hex_code, _ = value.split(' + ')
            print(hex_code)
            

            if hex_code not in redundant:
                data += hex_code
                redundant[hex_code] = hex_code
    return data


def decode_data(data):
    pass


if __name__ == '__main__':
    filename = 'data2.csv'
    data = read_file_data(filename)
    print(data)
