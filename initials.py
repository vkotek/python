firstNames = {
    'a' : 0.4,
    'b' : 0.2,
    'c' : 0.4
    }

surNames = {
    'a' : 0.1,
    'b' : 0.2,
    'c' : 0.7
    }

class initials(object):

    # Instantiate & get user's initials
    def __init__(self):
        print("Initializing initial initials")
#        self.i = str(input("Initials: "))
        self.getCombs()

    def getCombs(self):
        self.combs = {}
        f_check = 0
        for firstName in firstNames:
            for surName in surNames:
                f = firstNames[firstName] * surNames[surName]
                f_check += f
                x = firstName+surName
                self.combs[x] = f
        if round(f_check,5) != 1:
            print(f_check)

    def importNames(self, fileName):
        try:
            with open(fileName) as f:
                for line in f.read():
                    print(line)
        except:
            print("error")
a = initials()
