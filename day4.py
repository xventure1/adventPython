import re


def checkhcl(hcl, search=re.compile(r'[^a-f0-9]').search):
    return not bool(search(hcl))


def checkpid(pid, search=re.compile(r'[^0-9]').search):
    return not bool(search(pid))


def checkValidity(dic):
    eclList = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    for tag in dic:
        if tag == 'byr':
            if not int(dic[tag]) >= 1920 or not int(dic[tag]) <= 2002:
                return False
        elif tag == 'iyr':
            if not int(dic[tag]) >= 2010 or not int(dic[tag]) <= 2020:
                return False
        elif tag == 'eyr':
            if not int(dic[tag]) >= 2020 or not int(dic[tag]) <= 2030:
                return False
        elif tag == 'hgt':
            if dic[tag].endswith("n"):
                temp = dic[tag].rstrip("in")
                if not int(temp) >= 59 or not int(temp) <= 76:
                    return False
            elif dic[tag].endswith("m"):
                temp = dic[tag].rstrip("cm")
                if not int(temp) >= 150 or not int(temp) <= 193:
                    return False
            else:
                return False
        elif tag == 'hcl':
            if dic[tag][0] != '#' or len(dic[tag]) != 7:
                return False
            temp = dic[tag].lstrip('#')
            if not checkhcl(temp):
                return False
        elif tag == 'ecl':
            if dic[tag] not in eclList:
                return False
        elif tag == 'pid':
            if len(str(dic[tag])) != 9:
                return False
            if not checkpid(dic[tag]):
                return False
    return True


if __name__ == '__main__':
    with open("/Users/tommyheimer/PycharmProjects/adventProject/input.txt", "r")as reader:
        allData = reader.readlines()
    passportInfo = []
    passports = []
    approvedTags = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    validPass = 0
    for data in allData:
        if data != "\n":
            passportInfo.append(data)
        else:
            passports.append(passportInfo)
            passportInfo = []
    passports.append(passportInfo)

    for passport in passports:
        tagsDict = {}
        for line in passport:
            words = line.split(" ")
            for word in words:
                if word.endswith('\n'):
                    word = word.rstrip()
                tagsDict[word[:3]] = word[4:]
        if tagsDict.__len__() == 8:
            if checkValidity(tagsDict):
                validPass += 1
        elif tagsDict.__len__() == 7:
            if not tagsDict.__contains__('cid'):
                if checkValidity(tagsDict):
                    validPass += 1
    print validPass
