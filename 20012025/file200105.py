from fnmatch import fnmatch

for i in range(0,10000000000,3023):
    if fnmatch(str(i), '1?954*21'):
        print(i)