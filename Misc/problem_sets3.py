#print "Please think of a number between 0 and 100!"
#l = 0
#h = 100

def guess(l,h):
    g = (l+h)/2
    print "Is your secret number %d?" % g
    print "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",
    x = raw_input()
    if x == 'c':
        print "Game over. Your secret number was: %d" % g
    elif x == 'h':
        guess(l,g)
    elif x == 'l':
        guess(g,h)
    else:
        print "Invalid choice"
        guess(l,h)
        
#guess(l,h)

def recurPowerNew(base, exp):
    if exp == 0:
        return 1
    elif exp > 1:
        return base*recurPowerNew(base,exp-1)
        
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here


    
print recurPowerNew(-7.23,2)