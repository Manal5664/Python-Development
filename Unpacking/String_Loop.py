# count how manytimes 'a' appears in a 'banana'
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print(count)  # Output: 3

# print each character of 'python' using while loop
word = 'python'
index = 0
while word[index:]:
    print(word[index])
    index += 1

# count consonants in a "programming".
word = 'programming'
consonant_count = 0
for letter in word:
    if letter.lower() in 'bcdfghjklmnpqrstvwxyz':
        consonant_count += 1    
print(consonant_count)

# Reverse a string "hello world" using for loop.
word = 'hello world'
reversed_word = ''
for letter in word:
    reversed_word = letter + reversed_word
print(reversed_word)  # Output: dlrow olleh

# print characters+index for "Developer"
word = 'Developer'
for index, char in enumerate(word): #
    print(f"Character: {char}, Index: {index}")