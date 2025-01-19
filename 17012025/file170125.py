#54?1?3*7

import fnmatch

for i in range(0, 10000000000, 18579):
    if i%18579 == 0 and fnmatch.fnmatch(str(i), '54?1?3*7'):
        print(i, i//18579)