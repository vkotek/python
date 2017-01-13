#! /usr/local/bin/python3
# Python Challenge 1

# Image says 238, we put that in the url, then put 2^38.

# We are given this, and a translation key that has a pattern of +2 index of alphabet.
sentence = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."



# I tried to remember the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def translate_this(text):
    out = ""

    def getnext(y):
        z = alphabet.index(y)+2
        if z >= len(alphabet):
            z = z - len(alphabet)
        return alphabet[z]

    for x in text:
        if x in alphabet:
            x = getnext(x)
        out+=x

    return out

print(translate_this(sentence))

# map.html becomes..
print(translate_this("map")+".html")


# The translated sentence read:

# "i hope you didnt translate it by hand. thats what computers are for. doing
# it in by hand is inefficient and that's why this text is so long. using
# string.maketrans() is recommended. now apply on the url."
