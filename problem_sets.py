word = str(input("Input word:"))
vowels_count = 0
vowels = ['a','e','i','o','u']

for letter in word:
    if letter in vowels:
        vowels_count+=1

print("There are %d in the word '%s'") % (vowels_count, word)
