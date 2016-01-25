vowels_count = 0
vowels = ['a','e','i','o','u']

for letter in s:
    if letter in vowels:
        vowels_count+=1

print("Number of vowels: ", vowels_count)
