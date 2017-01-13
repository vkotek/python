#! /usr/local/bin/python3
# Python Challenge 6

import zipfile

x = 0
comments = ""

def getComments(n):

    zf = "/Users/ares/Downloads/channel.zip"

    with zipfile.ZipFile(zf,'r') as f:
        return f.getinfo("{}.txt".format(n)).comment
        for item in f.namelist():
            return f.getinfo(item).comment

def getNext(n):

    global x, comments, comments_txt

    f = open("/Users/ares/Downloads/channel/{}.txt".format(n), 'r')

    x += 1
    text = f.read()
    f.close()
    b = text.split()

    try:
        c = int(b[-1])
        print(text)
        cmt = getComments(c)
        comments += cmt.decode('utf-8')
        getNext(c)

    except Exception as e:
        print(str(x) + " | " +text)
        print(e)
        print(comments)
        print(comments_txt)

end = getNext(90052)
