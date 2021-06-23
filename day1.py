

if __name__ == '__main__':

    listNum = []
    with open("/Users/tommyheimer/PycharmProjects/adventProject/input.txt", "r")as reader:
        listNum = reader.readlines()
    i = 0
    answers = []
    for x in listNum:
        x = int(x)
        i = i+1
        j = i

        while j < len(listNum):
            y = listNum.__getitem__(j)
            y = int(y)
            k = j + 1
            while(k < len(listNum)):
                z = listNum.__getitem__(k)
                z = int(z)
                if x + y + z == 2020:
                    answers.append(x*y*z)
                k += 1
            j += 1
    print answers
