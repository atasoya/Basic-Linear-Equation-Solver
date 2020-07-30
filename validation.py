import modules as mod
def checkequalsign(equation) :
    found = False
    equation = equation.replace(" ","")
    for i in range(len(equation)) :
        if equation[i] == "=" :
            found = True 
    return found


def checknumberafterequal(equation) :
    equation = equation.replace(" ","")
    if equation[len(equation)-1] == "=" :
        return False
    else:
        return True



def checkoperator(equation) :
    found = False
    indexofoperators = []
    equation = mod.standardform(equation)
    equation = equation[0:mod.findindexofthecomponent(equation,"=")]
    for i in range(len(equation)) :
        if equation[i] == "/" :            # 1     -2X/-8=10   # 2     -8/-2X=10             # 1     -2X-8=10   # 2     -8-2X=10
            found = True
        elif equation[i] == "x" :
            found = True
    if found == False :
        for x in range(len(equation)) :
            if equation[x] == "+" or equation[x] == "-" :
                indexofoperators.append(x)
    if found == False and len(indexofoperators) == 0 :
        return False
    else :
        return True



