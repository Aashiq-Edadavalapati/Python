'''You have a list of strings, and you need to find the string that contains the most vowels. How would you do this?'''

lis = ['hooheyy','hooraaaay','hiiiiiiraa','heheheheheheh','goooooooon']
vowel_count = [0]*len(lis)
a = 0
for i in lis:
    for j in i:
        if j in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vowel_count[a] += 1
    a += 1
max_vowel = lis[vowel_count.index(max(vowel_count))]
print(max_vowel)