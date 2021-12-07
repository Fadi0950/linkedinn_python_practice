def multi(*args):
    result=0
    for i in args:
        result=result+i
    return result
print(multi(1,2,3,4,5))