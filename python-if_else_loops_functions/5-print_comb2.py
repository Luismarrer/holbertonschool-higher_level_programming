#!/usr/bin/python3
i = 0
y = 0
for x in range(99):
    if y == 9:
        i += 1
    if y == 9:
        y = 0
    else:
        y += 1
    if x != 98:
        print("{}{}, " .format(i, y), end="")
print("{}{}" .format(i, y))
