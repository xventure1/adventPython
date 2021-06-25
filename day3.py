if __name__ == '__main__':
    with open("/Users/tommyheimer/PycharmProjects/adventProject/input.txt", "r")as reader:
        slopes = reader.readlines()
    xs = [1,3,5,7,1]
    ys = [1,1,1,1,2]

    collisions = []
    xthresh = len(slopes.__getitem__(0))-2
    for xa,ya in zip(xs, ys):
        i = 0
        collision = 0
        x = 0
        skip = True
        while i < slopes.__len__():
            if slopes.__getitem__(i)[x] == '#':
                collision += 1
            x += xa
            if x > xthresh:
                x = x - xthresh-1
            i += ya
        collisions.append(collision)
    a = 1
    for col in collisions:
        a = a*col
    print a
