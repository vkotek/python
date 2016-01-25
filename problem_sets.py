
# PS1, EX1
def count_vowels(s):
    vowels_count = 0
    vowels = ['a','e','i','o','u']

    for letter in s:
        if letter in vowels:
            vowels_count+=1

    print("Number of vowels: ", vowels_count)

# PS1, EX2
def count_bobs(s):
    bobs = 0
    for x in range(0,len(s)):
        if s[x:x+3] == 'bob':
            bobs +=1
    return bobs
    
def odd(x):
    return x % 2 == 0
    

print(count_bobs("Hellobobobral"))