#!/usr/bin/env python3
fobj = open("/tmp/String.txt")
sum = ''
fobj2 = fobj.read()
for x in fobj2:
    print(x)
    flag = x.isdigit()
    print(flag)
    if flag:
        sum = sum + x
print(sum)
fobj.close()
