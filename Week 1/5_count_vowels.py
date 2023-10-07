# Write a function that takes a word as an argument and returns the number of vowels in the word

def count_vowels(word):
    vowel_count = 0

    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in word:
        if letter in vowels:
            vowel_count += 1
    
    return vowel_count

input_word = "Alphabet"
print("Input Word: ", input_word)
print("Number of Vowels: " + str(count_vowels(input_word)))