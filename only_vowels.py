#Write a program only_vowels.py that accepts a phrase and returns a string of all the vowels in the phrase.
# You may have to write a program for checking whether a character in the phrase is a vowel or not

p = input("Enter a phrase:")
s = ''
for i in p:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        s = s + i
print(s)