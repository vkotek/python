n = 2
with open('quotes-orig.txt', 'r') as f:
    with open('foff.txt','w') as w:
        for line in f:
            if n % 3 == 0:
                w.write(line)
            n += 1
