def getFib(pos, first, second):
    third = first + second
    print(third)
    if pos<=3:
        return third
    else:
        first = second
        second = third
        return getFib(pos-1, first, second)

position =  int(input("Enter a position upto which you want fibonacci sequence : "))

if position <= 2:
    print("0\n1\n")
else:
    print("0\n1")
    getFib(position,0,1)