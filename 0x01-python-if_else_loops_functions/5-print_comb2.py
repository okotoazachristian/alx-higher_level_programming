#i/usr/bin/python
for i in range(100):
    if i == 99:
        print(i)
    elif i < 10:
        print("{}{}, ".format(0, i), end="")
    else:
        print("{}, ".format(i) , end="")
