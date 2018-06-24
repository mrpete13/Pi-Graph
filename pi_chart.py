import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

"""
This program charts a histogram of the distribution of the digits in pi.
"""
# Assign variable to the 1 Million digits of Pi
file_object = open('pi_million_digits.txt', 'r')
pi = file_object.read()

# Add the million digits to a list for plotting.
digit_list = []
for digit in pi:
    digit_list.append(digit)

zero = []
one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []

for digit in digit_list:
    if digit == '0':
        zero.append(digit)
    elif digit == '1':
        one.append(digit)
    elif digit == '2':
        two.append(digit)
    elif digit == '3':
        three.append(digit)
    elif digit == '4':
        four.append(digit)
    elif digit == '5':
        five.append(digit)
    elif digit == '6':
        six.append(digit)
    elif digit == '7':
        seven.append(digit)
    elif digit == '8':
        eight.append(digit)
    elif digit == '9':
        nine.append(digit)

zero = len(zero)
one = len(one)
two = len(two)
three = len(three)
four = len(four)
five = len(five)
six = len(six)
seven = len(seven)
eight = len(eight)
nine = len(nine)

digit_count = [zero, one, two, three, four, five, six, seven, eight, nine]

for digit in digit_count:
    print(digit_count.index() + ' : ' + digit)

# bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# plt.hist(digit_list, bins, histtype = 'bar', rwidth = 0.5)
#
#
#
# plt.title('Distribution of Digits in Pi')
# plt.xlabel('Digits')
# plt.ylabel('Times appeared in the first million digits of pi')
#
# plt.show()
