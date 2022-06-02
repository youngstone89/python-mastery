# base Namer class
class Namer():
    def __init__(self):
        self.last = ""
        self.first = ""

# derived namer class for First <space> Last


class FirstFirst(Namer):
    def __init__(self, namestring):
        super().__init__()
        i = namestring.find(" ")  # find space
        if i > 0:
            names = namestring.split()
            self.first = names[0]
            self.last = names[1]
        else:
            self.last = namestring

# derived Namer class for Last <comma> First


class LastFirst(Namer):
    def __init__(self, namestring):
        super().__init__()
        i = namestring.find(",")  # find comma
        if i > 0:
            names = namestring.split(",")
            self.last = names[0]
            self.first = names[1]
        else:
            self.last = namestring


class NamerFactory():
    def __init__(self, namestring):
        self.name = namestring

    def getNamer(self):
        i = self.name.find(",")  # if it finds a comma
        if i > 0:
            # get the LastFirst class
            return LastFirst(self.name)
        else:  # else get the FirstFirst

            return FirstFirst(self.name)

class Builder:
    def compute(self, name):
        # get the Namer Factory
        # and then the namer class
        namerFact = NamerFactory(name)
        # get namer
        namer = namerFact.getNamer()

        # print out split name
        print(namer.first, namer.last)

def main():
    bld = Builder()
    bld.compute('yeongseok,kim')
    bld.compute('Kim YeongSeok')

if __name__ == '__main__':
    main()
