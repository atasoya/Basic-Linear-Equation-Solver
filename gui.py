import modules as mod
import maths
import validation as valid
import tkinter as tk


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
