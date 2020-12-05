#! /usr/bin/python3

import matplotlib.pyplot as plt
list =[]
numbers = (input("Please write numbers : ")) # <- your data
for number in numbers.split(","):
    list.append(int(number))
num_bins = 20 # <- number of bins for the histogram
plt.hist(list, num_bins)
plt.show()
