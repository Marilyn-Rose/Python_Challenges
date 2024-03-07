#Create a function in Python that accepts a single word 
#and returns the number of vowels in that word. 
#In this function, only a, e, i, o, and u will be counted as vowels — not y.

def word_to_vowels(word):
    vowels ={"a", "e", "i", "o", "u"}
    vowel_count = 0
    for char in word:
        if char.lower() in vowels:
            vowel_count += 1
        
    return vowel_count

word = str(input("Enter a word: "))
print("The number of vowels in the word is: ", word_to_vowels(word))
