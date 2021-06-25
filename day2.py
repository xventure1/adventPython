if __name__ == '__main__':
    with open("/Users/tommyheimer/PycharmProjects/adventProject/input.txt", "r")as reader:
        passwords = reader.readlines()

    if 1 != 2:
        print "Test"

    correct = 0
    for password in passwords:
        instructs = password.split(" ")
        minMax = instructs.__getitem__(0).split("-")
        firstLetter = instructs.__getitem__(2)[int(minMax.__getitem__(0))-1]
        secondLetter = instructs.__getitem__(2)[int(minMax.__getitem__(1))-1]
        key = instructs.__getitem__(1)[0]

        if firstLetter == key or secondLetter == key:
            if(firstLetter != secondLetter):
                correct += 1
    print correct