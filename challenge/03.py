#! /usr/local/bin/python3

fl = "/Users/ares/Documents/Scripts/python/challenge/03.txt"

t = open(fl, 'r').read().replace('\n','')
tx   = "sxbXzJwjxAITPpPWoGOnPWcSbHFZjBizKEBUECMLUKQRvVvWgIudKQkNjJmlUoUCaAHiTKVKcIpMelTTTtJ\nAYlVsrjBTLsWuyYwCJuJaewQSrzwXJNLAflzrZXBBEOCTtItNptaJkriIEhufpNysjJpeWbWcFqdEsiGDDdDDD".replace('\n','')

out = ""

# non regex function
for x in range(3, len(t)-3):
    a = t[x-3:x]
    b = t[x]
    c = t[x+1:x+4]
    if a.isupper() and b.islower() and c.isupper():
        #print(t[x-3:x+4])
        out += t[x]

# print(out)

# regex attempt
import re

reg = "[A-Z]{3}"

m = re.search(reg, t)
print(m.group(0))
