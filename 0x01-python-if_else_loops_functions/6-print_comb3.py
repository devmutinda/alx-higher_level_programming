#!/usr/bin/python3
for i in range(0, 89):
    if i < 10:
        i = '0' + str(i)
    elif i / 10 >= i % 10:
        i += 1
        continue
    print("{}".format(i), end=", ")
    i = int(i)
    i += 1

print("{}".format(i))
