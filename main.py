# Import Modules
import math as m
import tkinter as tk

# ----------------------------- BACKEND ---------------------------------

# Function on Click at A Number
def onClick(nbrs):
    global operator
    operator = operator + str(nbrs)
    text_input.set(operator)

# Function on Click at Clear Button
def onClickClr():
    global operator
    operator = ''
    text_input.set('')

# Function on Click on Equal
def onClickEqual():
    global operator
    result = str(eval(operator))
    text_input.set(result)
    operator = result

# ----------------------------- G U I / FRONTEND -----------------------------------

# Create and Implement GUI Window
root = tk.Tk()
root.title('CALCULATOR')
root.iconbitmap('favicon.ico')
root.resizable(False,False)

# Initialise Operator and Text Input
operator = ''
text_input = tk.StringVar()

# Draw The Entry Of the Calculator
input = tk.Entry(root, state = 'disabled', font = ('roboto', 19, 'normal'), textvariable = text_input, bd = 10, insertwidth = 4, justify = 'right').grid(row = 0, column = 0, columnspan = 4,)

# Draw the Buttons for Numbers (1 to 9) in the main frame

# ======================== Row n° 1 ============================
btn_plus = tk.Button(root, padx = 14, pady = 15, bd = 6, font = ('roboto', 15, 'normal'), text = '+', command = lambda:onClick('+')).grid(row = 1, column = 3, padx = 2, pady = 2)
btn_9 = tk.Button(root, padx = 15, pady = 15, bd = 6, font = ('roboto', 15, 'normal'), text = '9', command = lambda:onClick(9)).grid(row = 1, column = 2, padx = 2, pady = 2)
btn_8 = tk.Button(root, padx = 15, pady = 15, bd = 6, font = ('roboto', 15, 'normal'), text = '8', command = lambda:onClick(8)).grid(row = 1, column = 1, padx = 2, pady = 2)
btn_7 = tk.Button(root, padx = 15, pady = 15, bd = 6, font = ('roboto', 15, 'normal'), text = '7', command = lambda:onClick(7)).grid(row = 1, column = 0, padx = 2, pady = 2)

# ======================= Row n° 2 =============================
btn_moins = tk.Button(root, padx = 16, pady = 15, bd = 6, font = ('roboto', 15, 'normal'), text = '-', command = lambda:onClick('-')).grid(row = 2, column = 3, padx = 2, pady = 2)
btn_6 = tk.Button(root, padx = 15, pady = 15, bd = 6, font = ('roboto', 15, 'normal'), text = '6', command = lambda:onClick(6)).grid(row = 2, column = 2, padx = 2, pady = 2)
btn_5 = tk.Button(root, padx = 15, pady = 15, bd = 6, font = ('roboto', 15, 'normal'), text = '5', command = lambda:onClick(5)).grid(row = 2, column = 1, padx = 2, pady = 2)
btn_4 = tk.Button(root, padx = 15, pady = 15, bd = 6, font = ('roboto', 15, 'normal'), text = '4', command = lambda:onClick(4)).grid(row = 2, column = 0, padx = 2, pady = 2)

# ====================== Row n° 3 ==============================
btn_mult = tk.Button(root, padx = 15, pady = 15, bd = 6, font = ('roboto', 15, 'normal'), text = '*', command = lambda:onClick('*')).grid(row = 3, column = 3, padx = 2, pady = 2)
btn_3 = tk.Button(root, padx = 15, pady = 15, bd = 6, font = ('roboto', 15, 'normal'), text = '3', command = lambda:onClick(3)).grid(row = 3, column = 2, padx = 2, pady = 2)
btn_2 = tk.Button(root, padx = 15, pady = 15, bd = 6, font = ('roboto', 15, 'normal'), text = '2', command = lambda:onClick(2)).grid(row = 3, column = 1, padx = 2, pady = 2)
btn_1 = tk.Button(root, padx = 15, pady = 15, bd = 6, font = ('roboto', 15, 'normal'), text = '1', command = lambda:onClick(1)).grid(row = 3, column = 0, padx = 2, pady = 2)

# ===================== Row n° 4 ===============================
btn_div = tk.Button(root, padx = 16, pady = 15, bd = 6, font = ('roboto', 15, 'normal'), text = '/', command = lambda:onClick('/')).grid(row = 4, column = 3, padx = 2, pady = 2)
btn_equal = tk.Button(root, padx = 15, pady = 15, bd = 6, font = ('roboto', 15, 'normal'), text = '=', command = lambda:onClickEqual()).grid(row = 4, column = 2, padx = 2, pady = 2)
btn_0 = tk.Button(root, padx = 15, pady = 15, bd = 6, font = ('roboto', 15, 'normal'), text = '0', command = lambda:onClick(0)).grid(row = 4, column = 1, padx = 2, pady = 2)
btn_delete = tk.Button(root, padx = 12, pady = 22, bd = 6, font = ('roboto', 10, 'normal'), text = 'DEL', command = lambda:onClickClr()).grid(row = 4, column = 0, padx = 2, pady = 2)

# Fill All Components in the Window
root.mainloop()