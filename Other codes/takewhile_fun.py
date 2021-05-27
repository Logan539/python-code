from itertools import *
numbers = list(accumulate(range(8))) #accumulate = keeps on adding numbers
print(numbers)
print(list(takewhile(lambda x:x <=10,numbers)))