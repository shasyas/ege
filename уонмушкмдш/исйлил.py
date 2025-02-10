from fnmatch import *
#3?6906*4


for i in range(0, 10000000000, 2024):
    if fnmatch(str(i), '3?6906*4'):
        print(i)