x,y=100,100
if x > y:
    str="x is greater then y"
elif x == y:
    str="x is equal to y"
else:
    str="x is smaller then y"
print(str)
str="x is less than y" if (x<y) else "x is greater or equal to y"
print(str)