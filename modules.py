def findindexofthecomponent(equation,component) :
    for i in range(len(equation)) :
        if equation[i] == component :
            indexofcomponent = i
        else :
            continue
    return indexofcomponent

def findindedexofthevariable(equation) :
    notvariables = "1234567890x/+-="
    for i in range(len(equation)) :
        counter = 0
        for x in range(len(notvariables)) :
            if equation[i] != notvariables[x] :
                counter += 1
        if counter == len(notvariables) :
            variableindex = i
    return variableindex



def standardform(equation) :
    equation = equation.replace(" ","")
    if findindedexofthevariable(equation) > findindexofthecomponent(equation,"=") :
        part1 = equation[findindexofthecomponent(equation,"=")+1:len(equation)] 
        part2 = equation[0:findindexofthecomponent(equation,"=")]
        equation = part1 + "=" + part2
    return equation



def findnumberafterequal(equation) :
    equation = standardform(equation)
    numberafterequal = equation[findindexofthecomponent(equation,"=")+1:len(equation)]
    return int(numberafterequal)


def findtypeoftequation(equation) :       # 1     2X/8=10   # 2     8/2X=10
    equation = standardform(equation)
    if equation[findindedexofthevariable(equation)+1] == "=" :
        return 2
    else :
        return 1

def findoperatorindex(equation) :
    found = False
    indexofoperators = []
    equation = standardform(equation)
    equation = equation[0:findindexofthecomponent(equation,"=")]
    for i in range(len(equation)) :
        if equation[i] == "/" :            # 1     -2X/-8=10   # 2     -8/-2X=10
            operatorindex = i                # 1     -2X-8=10   # 2     -8-2X=10
            found = True
        elif equation[i] == "x" :
            operatorindex = i
            found = True
    if found == False :
        for x in range(len(equation)) :
            if equation[x] == "+" or equation[x] == "-" :
                indexofoperators.append(x)
        if len(indexofoperators) == 2 :
            operatorindex = indexofoperators[1]
        else:
            operatorindex = indexofoperators[0]
    return operatorindex
    
                
    
def findnumberbeforex(equation) :
    equation = standardform(equation)
    if findtypeoftequation(equation) == 1 :
        if findindedexofthevariable(equation) == 0 :
            numberbeforex = 1
        else :
            numberbeforex = equation[0:findindedexofthevariable(equation)]
        if numberbeforex == "-" :
            numberbeforex = -1   # 1     2X/8=10   # 2     8/2X=10
        return int(numberbeforex)
    else:
        if findoperatorindex(equation)+1 == findindedexofthevariable(equation) :
            numberbeforex = 1
        else :
            numberbeforex = equation[findoperatorindex(equation)+1:findindedexofthevariable(equation)]
        if numberbeforex == "-" :
            numberbeforex = -1
        return int(numberbeforex)


def findlastnumber(equation) :
    equation = standardform(equation)
    if findtypeoftequation(equation) == 1 :              # 1     2X/8=10   # 2     8/2X=10
        lastnumber = equation[findoperatorindex(equation)+1:findindexofthecomponent(equation,"=")]
        return int(lastnumber)
    else:
        lastnumber = equation[0:findoperatorindex(equation)]
        return int(lastnumber) 

def findoperator(equation) :
    equation = standardform(equation)
    operator = equation[findoperatorindex(equation)]
    return operator


                                           