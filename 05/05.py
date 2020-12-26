#!/usr/bin/python3

CODE_LENGTH = 10

ROW_CODE_LENGTH = 7
N_ROWS = pow(2, ROW_CODE_LENGTH)

COL_CODE_LENGTH = 3
N_COLS = pow(2, COL_CODE_LENGTH)

N_SEATS = N_ROWS * N_COLS

if __name__ == '__main__':
    to_binary = str.maketrans('FBLR', '0101')
    max_seatid = 0
    seats = [0] * N_SEATS

    with open("input") as f:
        for line in f:
            code = line.rstrip()
            code_bin = code.translate(to_binary)

            row = int(code_bin[:ROW_CODE_LENGTH], base=2)
            column = int(code_bin[ROW_CODE_LENGTH:], base=2)
            seatid = row * 8 + column
            seats[seatid] = 1
            max_seatid = max(max_seatid, seatid)

    print("max seatid is {}".format(max_seatid))

    my_seatid = [i for i,x in enumerate(seats) if x == 0 and seats[i-1]==1 and seats]
    for i,state in enumerate(seats):
        if state == 0 and seats[i-1] == 1 and seats[i+1] == 1:
            print("seat {} is free".format(i))
