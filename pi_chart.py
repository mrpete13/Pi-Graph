import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib as mpl
# import pandas as pd

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

del digit_list[1]  # This removes the '.' string
digit_list.pop()  # This removes the '\n' string
for digit in digit_list:
    digit = int(digit)

bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.hist(digit_list, bins, histtype='bar', rwidth=0.5)

plt.title('Distribution of Digits in Pi')
plt.xlabel('Digits')
plt.ylabel('Times appeared in the first million digits of Pi')

plt.show()
