# 1     2X-8=10   # 2     8/2X=10
def calculatetype1(firstnumber,xnumber,lastnumber,operator) :
    if operator == "/" :
        lastnumber = lastnumber * firstnumber
        value = lastnumber / xnumber
    elif operator == "x" :
        lastnumber = lastnumber / firstnumber
        value = lastnumber / xnumber
    elif  operator == "+" :
        lastnumber = lastnumber - firstnumber 
        value = lastnumber / xnumber
    elif operator == "-" :
        lastnumber = lastnumber + (firstnumber)
        value = lastnumber / (xnumber)
    return value


def calculatetype2(firstnumber,xnumber,lastnumber,operator) :   # 2     8/2a=10
    if operator == "/" :
        xnumber = lastnumber * xnumber
        value = firstnumber / xnumber
    elif operator == "x" :
        lastnumber = lastnumber / firstnumber
        value = lastnumber / xnumber
    elif  operator == "+" :
        lastnumber = lastnumber - firstnumber
        value = lastnumber / xnumber
    elif operator == "-" :
        lastnumber = firstnumber - lastnumber
        value = lastnumber / xnumber
    return value 




