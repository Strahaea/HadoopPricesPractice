#!/usr/bin/python

#mapper to find the total number of sales and the value of the total sales 
#in the prices dataset

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print cost

