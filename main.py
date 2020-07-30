import modules as mod
import maths
import validation as valid
"""
equation = "2a=4"  #      # 1     2X/8=10   # 2     8/2X=10

print("after equal part :  ",mod.findnumberafterequal(equation))
print("variable component :   ",mod.findnumberbeforex(equation))
print("last number :   ",mod.findlastnumber(equation))
print("operator :  ",mod.findoperator(equation))
print(mod.findindedexofthevariable(equation))

print(mod.findtypeoftequation(equation))
"""
equation = input("Enter the equation :   ")
if valid.checknumberafterequal(equation) == False or valid.checkequalsign(equation) == False or valid.checkoperator(equation) == False :
    print("wrong format")
else :
    if mod.findtypeoftequation(equation) == 1 :
        print("sa")
        print(maths.calculatetype1(mod.findlastnumber(equation),mod.findnumberbeforex(equation),mod.findnumberafterequal(equation),mod.findoperator(equation)))
    else :
        print("as")
        print(maths.calculatetype2(mod.findlastnumber(equation),mod.findnumberbeforex(equation),mod.findnumberafterequal(equation),mod.findoperator(equation)))
