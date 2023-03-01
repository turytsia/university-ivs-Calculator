# Tripple-Double
# @author: xpodho08

# encoding: utf-8
import customtkinter
import tkinter

# setting up the default theme
customtkinter.set_appearance_mode("Light")

# creating the main window
app = customtkinter.CTk()
app.title("Calculator")
app.geometry("425x675")
app.resizable(False, False)

isResult = False

# function for changing the theme
def change_theme():
    if customtkinter.get_appearance_mode() == "Light":
        customtkinter.set_appearance_mode("Dark")
    else:
        customtkinter.set_appearance_mode("Light")
    app.update()

# function for handling button clicks and change the label
def label_changer(label, small_label, add):
    global isResult

    if isResult == True:
        isResult = False
        if add == "cls" or add == "last":
            small_label.configure(text = "")
            label.configure(text = "")
            app.update()
            return
        small_label.configure(text = "")
        label.configure(text = add)
        app.update()
        return

    if add == "h" or add == "H":
        help()
        return

    if add == "cls":
        label.configure(text = "")
        app.update()
        return
    
    if add == "last":
        label.configure(text = label.cget("text")[:-1])
        app.update()
        return
    
    if add.isalpha():
        return

    elif add == "=":
        small_label.configure(text = label.cget("text"))
        label.configure(text = "RES OF EQUALS")
        isResult = True
        app.update()
        return
    
    label.configure(text = label.cget("text") + add)
    app.update()
    
# function for opening the help window
def help():
    helpwindow = customtkinter.CTk()
    helpwindow.title("Help")
    helpwindow.geometry("400x400")
    helpwindow.resizable(False, False)

    text = """Some tooltips:
    + adds numbers
    - subtracts numbers
    ÷ divides numbers
    x multiplies numbers
    ! find exponential
    % find a percentage of a number
    ^ raises a number to a power
    √ finds the root of a number
    = calculates the result
    CE erases the last character
    С erases everything written

    Press Enter or Esc to close this window"""

    help_label = customtkinter.CTkLabel(master = helpwindow, text = text, width = 380, height = 380, 
                                    font = ("Arial", 20), fg_color = "transparent")
    help_label.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

    helpwindow.bind("<Return>", lambda event: helpwindow.destroy())
    helpwindow.bind("<Escape>", lambda event: helpwindow.destroy())

    helpwindow.mainloop()

# creating the buttons and labels
switch_theme = customtkinter.CTkSwitch(master=app, text="", command=change_theme,
                                   onvalue="on", offvalue="off")
switch_theme.place(relx = 0.15, rely = 0.05, anchor = tkinter.CENTER)

helpbutton = customtkinter.CTkButton(master = app, text = "?", command = lambda: help(),
                                    width = 20, height = 20, hover = True, hover_color = "grey", fg_color = "transparent",
                                    text_color = ("black", "white"), font = ("Arial", 20))
helpbutton.place(relx = 0.95, rely = 0.05, anchor = tkinter.CENTER)

small_label = customtkinter.CTkLabel(master = app, text = "", width = 290, height = 60, font = ("Arial", 30))
small_label.place(relx = 0.5, rely = 0.05, anchor = tkinter.CENTER)

label = customtkinter.CTkLabel(master = app, text = "", width = 400, height = 100, font = ("Arial", 60))
label.place(relx = 0.5, rely = 0.18, anchor = tkinter.CENTER)

buttonPercent = customtkinter.CTkButton(master = app, text = "%", command = lambda: label_changer(label, small_label, "%"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", text_color = "#36b6ab", fg_color = "transparent", 
                                    font = ("Arial", 40))
buttonPercent.place(relx = 0.14, rely = 0.32, anchor = tkinter.CENTER)

buttonFactorial = customtkinter.CTkButton(master = app, text = "!", command = lambda: label_changer(label, small_label, "!"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", text_color = "#36b6ab", fg_color = "transparent", 
                                    font = ("Arial", 40))
buttonFactorial.place(relx = 0.14, rely = 0.44, anchor = tkinter.CENTER)

buttonOne = customtkinter.CTkButton(master = app, text = "1", command = lambda: label_changer(label, small_label, "1"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", fg_color = "transparent", 
                                    text_color = ("black", "white"), font = ("Arial", 40))
buttonOne.place(relx = 0.14, rely = 0.56, anchor = tkinter.CENTER)

buttonFour = customtkinter.CTkButton(master = app, text = "4", command = lambda: label_changer(label, small_label, "4"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", fg_color = "transparent", 
                                    text_color = ("black", "white"), font = ("Arial", 40))
buttonFour.place(relx = 0.14, rely = 0.68, anchor = tkinter.CENTER)

buttonSeven = customtkinter.CTkButton(master = app, text = "7", command = lambda: label_changer(label, small_label, "7"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", fg_color = "transparent", 
                                    text_color = ("black", "white"), font = ("Arial", 40))
buttonSeven.place(relx = 0.14, rely = 0.8, anchor = tkinter.CENTER)

buttonClearLast = customtkinter.CTkButton(master = app, text = "CE", command = lambda: label_changer(label, small_label, "last"),
                                    width = 100, height = 80, hover = True, hover_color = ("#df7d7d", "#6c0000"), text_color = "red", fg_color = "transparent", 
                                    font = ("Arial", 40))
buttonClearLast.place(relx = 0.14, rely = 0.92, anchor = tkinter.CENTER)

buttonDegree = customtkinter.CTkButton(master = app, text = "^", command = lambda: label_changer(label, small_label, "^"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", text_color = "#36b6ab", fg_color = "transparent",
                                    font = ("Arial", 40))
buttonDegree.place(relx = 0.38, rely = 0.32, anchor = tkinter.CENTER)

buttonOpenBracket = customtkinter.CTkButton(master = app, text = "(", command = lambda: label_changer(label, small_label, "("),
                                    width = 100, height = 80, hover = True, text_color = "#36b6ab", hover_color = "grey", fg_color = "transparent", 
                                    font = ("Arial", 40))
buttonOpenBracket.place(relx = 0.38, rely = 0.44, anchor = tkinter.CENTER)

buttonTwo = customtkinter.CTkButton(master = app, text = "2", command = lambda: label_changer(label, small_label, "2"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", fg_color = "transparent", 
                                    text_color = ("black", "white"), font = ("Arial", 40))
buttonTwo.place(relx = 0.38, rely = 0.56, anchor = tkinter.CENTER)

buttonFive = customtkinter.CTkButton(master = app, text = "5", command = lambda: label_changer(label, small_label, "5"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", fg_color = "transparent", 
                                    text_color = ("black", "white"), font = ("Arial", 40))
buttonFive.place(relx = 0.38, rely = 0.68, anchor = tkinter.CENTER)

buttonEight = customtkinter.CTkButton(master = app, text = "8", command = lambda: label_changer(label, small_label, "8"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", fg_color = "transparent", 
                                    text_color = ("black", "white"), font = ("Arial", 40))
buttonEight.place(relx = 0.38, rely = 0.8, anchor = tkinter.CENTER)

buttonZero = customtkinter.CTkButton(master = app, text = "0", command = lambda: label_changer(label, small_label, "0"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", fg_color = "transparent", 
                                    text_color = ("black", "white"), font = ("Arial", 40))
buttonZero.place(relx = 0.38, rely = 0.92, anchor = tkinter.CENTER)

buttonDot = customtkinter.CTkButton(master = app, text = ".", command = lambda: label_changer(label, small_label, "."),
                                    width = 100, height = 80, hover = True, hover_color = "grey", text_color = "#36b6ab", fg_color = "transparent",
                                    font = ("Arial", 40))
buttonDot.place(relx = 0.62, rely = 0.32, anchor = tkinter.CENTER)

buttonCloseBracket = customtkinter.CTkButton(master = app, text = ")", command = lambda: label_changer(label, small_label, ")"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", text_color = "#36b6ab", fg_color = "transparent", 
                                    font = ("Arial", 40))
buttonCloseBracket.place(relx = 0.62, rely = 0.44, anchor = tkinter.CENTER)

buttonThree = customtkinter.CTkButton(master = app, text = "3", command = lambda: label_changer(label, small_label, "3"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", fg_color = "transparent", 
                                    text_color = ("black", "white"), font = ("Arial", 40))
buttonThree.place(relx = 0.62, rely = 0.56, anchor = tkinter.CENTER)

buttonSix = customtkinter.CTkButton(master = app, text = "6", command = lambda: label_changer(label, small_label, "6"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", fg_color = "transparent", 
                                    text_color = ("black", "white"), font = ("Arial", 40))
buttonSix.place(relx = 0.62, rely = 0.68, anchor = tkinter.CENTER)

buttonNine = customtkinter.CTkButton(master = app, text = "9", command = lambda: label_changer(label, small_label, "9"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", fg_color = "transparent", 
                                    text_color = ("black", "white"), font = ("Arial", 40))
buttonNine.place(relx = 0.62, rely = 0.8, anchor = tkinter.CENTER)

buttonClear = customtkinter.CTkButton(master = app, text = "C", command = lambda: label_changer(label, small_label, "cls"),
                                    width = 100, height = 80, hover = True, hover_color = ("#df7d7d", "#6c0000"), fg_color = "transparent", text_color = "red",
                                    font = ("Arial", 40))
buttonClear.place(relx = 0.62, rely = 0.92, anchor = tkinter.CENTER)

buttonRadical = customtkinter.CTkButton(master = app, text = "√", command = lambda: label_changer(label, small_label, "√"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", text_color = "#36b6ab", fg_color = "transparent",
                                    font = ("Arial", 40))
buttonRadical.place(relx = 0.86, rely = 0.32, anchor = tkinter.CENTER)

buttonDivide = customtkinter.CTkButton(master = app, text = "÷", command = lambda: label_changer(label, small_label, "÷"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", text_color = "#36b6ab", fg_color = "transparent",
                                    font = ("Arial", 40))
buttonDivide.place(relx = 0.86, rely = 0.44, anchor = tkinter.CENTER)

buttonMultiply = customtkinter.CTkButton(master = app, text = "x", command = lambda: label_changer(label, small_label, "x"),
                                    width = 100, height = 80, hover = True, text_color = "#36b6ab", hover_color = "grey", fg_color = "transparent",
                                    font = ("Arial", 40))
buttonMultiply.place(relx = 0.86, rely = 0.56, anchor = tkinter.CENTER)

buttonPlus = customtkinter.CTkButton(master = app, text = "+", command = lambda: label_changer(label, small_label, "+"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", text_color = "#36b6ab", fg_color = "transparent",
                                    font = ("Arial", 40))
buttonPlus.place(relx = 0.86, rely = 0.68, anchor = tkinter.CENTER)

buttonMinus = customtkinter.CTkButton(master = app, text = "-", command = lambda: label_changer(label, small_label, "-"),
                                    width = 100, height = 80, hover = True, hover_color = "grey", text_color = "#36b6ab", fg_color = "transparent", 
                                    font = ("Arial", 40))
buttonMinus.place(relx = 0.86, rely = 0.8, anchor = tkinter.CENTER)

buttonEqual = customtkinter.CTkButton(master = app, text = "=", command = lambda: label_changer(label, small_label, "="),
                                    width = 100, height = 80, hover = True, hover_color = "#3a8088",
                                    text_color = "white", fg_color = "#36b6ab",
                                    font = ("Arial", 40))
buttonEqual.place(relx = 0.86, rely = 0.92, anchor = tkinter.CENTER)

# Bindings
app.bind("<KeyPress>", lambda event: label_changer(label, small_label, event.char))
app.bind("<BackSpace>", lambda event: label_changer(label, small_label, "last"))
app.bind("<Return>", lambda event: label_changer(label, small_label, "="))
app.bind("<Escape>", lambda event: app.destroy())
app.bind("<Delete>", lambda event: label_changer(label, small_label, "cls"))

# Mainloop
app.mainloop()