#!/usr/bin/python
#reducer to find the total number of sales and the value of the total sales 
#in the prices dataset

import sys

numberSales = 0
valueSales = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    thisSale = line.strip()
    numberSales += 1 #every line is a sale so just need to sum up the line
    valueSales += float(thisSale) #add up all the sales

print "number of sales"
print numberSales
print "value of sales"
print valueSales

