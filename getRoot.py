def getRoot(x, guess,iters):
    print("Finding root of", x ,"with", iters , "iterations. Starting guess:", guess)
    print("g\t\tx*x\t\tx/g\t\t1/2(g+x/g)")
    while iters != 0:
        a = x / guess
        b = guess**2
        guess_old = guess
        guess = (a+guess)/2
        iters-=1
        print("%f\t%f\t%f\t%f" % (guess_old,b,a,guess))
    return guess

print(getRoot(40,3,10))