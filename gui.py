import modules as mod
import maths
import validation as valid
import tkinter as tk

"""
equation = "2a=4"  #      # 1     2X/8=10   # 2     8/2X=10

print("after equal part :  ",mod.findnumberafterequal(equation))
print("variable component :   ",mod.findnumberbeforex(equation))
print("last number :   ",mod.findlastnumber(equation))
print("operator :  ",mod.findoperator(equation))
print(mod.findindedexofthevariable(equation))

print(mod.findtypeoftequation(equation))

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
"""
answer = ""

window = tk.Tk()
window.title("Linear")

label = tk.Label(text="Enter The Equation")

entry = tk.Entry()

def myclick():
    equation = entry.get()
    if valid.checknumberafterequal(equation) == False or valid.checkequalsign(equation) == False or valid.checkoperator(equation) == False :
        answer = "wrong format"
    else :
        if mod.findtypeoftequation(equation) == 1 :
            answer = maths.calculatetype1(mod.findlastnumber(equation),mod.findnumberbeforex(equation),mod.findnumberafterequal(equation),mod.findoperator(equation))
        else :
            answer = maths.calculatetype2(mod.findlastnumber(equation),mod.findnumberbeforex(equation),mod.findnumberafterequal(equation),mod.findoperator(equation))
    entry.delete(0,len(entry.get()))
    entry.insert(0,answer)




button = tk.Button(text="Calculate",command=myclick)
window.geometry("200x100")
window.configure(bg="#58FA82")

label.pack()
entry.pack()
button.pack()



window.mainloop()
