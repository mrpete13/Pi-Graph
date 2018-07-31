import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd

"""
This program charts a histogram of the distribution of the digits in pi.
"""

# Assign variable to the 1 Million digits of Pi
file_object = open('pi_million_digits.txt', 'r')
pi = file_object.read()

# Add the million digits to a list for plotting.
digit_list = []
int_list = []
for digit in pi:
    digit_list.append(digit)

del digit_list[1]  # This removes the '.' string
digit_list.pop()  # This removes the '\n' string
for digit in digit_list:
    digit = int(digit)
    int_list.append(digit)

# Below counts the total occurrence of each number.
# Need to come back and make sure it can read ints not strs, possibly with a
# dictionary.

zero = digit_list.count('0')
one = digit_list.count('1')
two = digit_list.count('2')
three = digit_list.count('3')
four = digit_list.count('4')
five = digit_list.count('5')
six = digit_list.count('6')
seven = digit_list.count('7')
eight = digit_list.count('8')
nine = digit_list.count('9')


x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
y = [zero, one, two, three, four, five, six, seven, eight, nine]
# for totals in y:
# print(totals)

# Change figure draw size.
fig, ax = plt.subplots(figsize = (12, 9))

# index = np.arange(len(y))
rects = ax.bar(x, y,)

bar_width = 0.35
ax.set_title('Distribution of Digits in Pi')
ax.set_xlabel('Digits')
ax.set_ylabel('Times appeared in the first million digits of Pi')

def autolabel(rects, xpos = 'center'):
    """Attach a text label above each bar in *rects*, displaying its height

    *xpos* indicates which side to place the text WRT the center of the bar.
    It can eb one of the following: {'center', 'right', 'left'}.
    """
    xpos = xpos.lower() # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'right', 'left': 'left'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43} # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height,
                '{}'.format(height), ha = ha[xpos], va = 'bottom')


autolabel(rects)
plt.show()
