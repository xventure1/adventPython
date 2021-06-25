if __name__ == '__main__':
    with open("/Users/tommyheimer/PycharmProjects/adventProject/input.txt", "r")as reader:
        boardingPasses = reader.readlines()
    seatids = []
    rowCol = {}
    for bpass in boardingPasses:
        rowCode = bpass[0:7]
        colCode = bpass[7:10]
        i = 0
        high = 127
        low = 0
        finR = 0
        finC = 0
        for c in rowCode:
            dif = (high - low) / 2
            dif = high - dif
            if c == 'F':
                high = dif - 1
                finR = high
            else:
                low = dif
                finR = low
        high = 7
        low = 0
        for c in colCode:
            dif = (high - low) / 2
            dif = high - dif
            if c == 'L':
                high = dif - 1
                finC = high
            else:
                low = dif
                finC = low
        seatids.append(finR*8+finC)
    seatids.sort()
    i = 63
    for id in seatids:
        if i != id:
            print i
            break
        i += 1
    print seatids


