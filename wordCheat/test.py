wordsOrig = "words_original.txt"
openWO = open(wordsOrig, 'r')

for line in openWO.readlines():
    for length in range(16,2,-1):
        print(length, len(line))
        if length == len(line):
            print(line)
            break
        else:
            pass

openWO.close
