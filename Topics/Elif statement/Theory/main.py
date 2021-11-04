#  You can experiment here, it won’t be checked

x, y = (int(input()), int(input()))
if x in (1, 8) and y in (1, 8):
    print(1)
elif x in (1, 8) or y in (1, 8):
    print(5)
else:
    print(8)