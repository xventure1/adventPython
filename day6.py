import re


def checkpid(pid, search=re.compile(r'[^0-9]').search):
    return not bool(search(pid))


if __name__ == '__main__':

    with open("/Users/tommyheimer/PycharmProjects/adventProject/input.txt", "r")as reader:
        allData = reader.readlines()
        answers = []
        groups = []
    for line in allData:
        if line == '\n':
            groups.append(answers)
        else:
            answers.append(line.rstrip('\n'))
        print groups
