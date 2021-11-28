
def getFib(pos, first, second):
    third = first + second
    if pos==0 or pos==1:
        return pos
    elif pos==3:
        return third
    else:
        first = second
        second = third
        return getFib(pos-1, first, second)

position =  int(input("Enter a position for fibonacci sequence : "))
print(getFib(position, 0, 1))