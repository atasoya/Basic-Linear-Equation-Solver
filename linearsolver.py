import modules as mod
import maths
import validation as valid
def solvelinear(equation) :
    if valid.checknumberafterequal(equation) == False or valid.checkequalsign(equation) == False or valid.checkoperator(equation) == False :
        print("wrong format")
    else :
        if mod.findtypeoftequation(equation) == 1 :
            return(maths.calculatetype1(mod.findlastnumber(equation),mod.findnumberbeforex(equation),mod.findnumberafterequal(equation),mod.findoperator(equation)))
        else :
            return(maths.calculatetype2(mod.findlastnumber(equation),mod.findnumberbeforex(equation),mod.findnumberafterequal(equation),mod.findoperator(equation)))
