'''You have a tuple of colors, and you need to create a new tuple that contains the complementary colors. How would you do this?'''
colors = ('violet','indigo','blue','green','yellow','orange','red')
color = list(colors)
color.reverse()
complementary = tuple(color)
print(complementary)