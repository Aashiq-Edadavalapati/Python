students = ['Nobita', 'Urokodaki', 'Otsutsuki', 'kak','utakat']
length = []
for i in students:
    length.append(len(i))
x = max(length)
ind = length.index(x)
print(students[ind])