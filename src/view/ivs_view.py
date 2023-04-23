# Tripple-Double
# @author: xpodho08

# encoding: utf-8
import customtkinter
import os
import sys
import platform
import tkinter
import re
from PIL import Image

if platform.system() == "Windows":
    sys.path.append(os.getcwd())
else:
    sys.path.append(os.path.abspath(".."))

from src.parser.ivs_parser import parse, ParserError


def regex(expression, mode):
    # Join elements with spaces
    if mode == "spaces":
        pattern = r'(\d+\.?\d*|\+|\-|\*|\/|\(|\)|\^|\!|\%|\√|\÷)'
        # Find all numbers and operators in the expression
        elements = re.findall(pattern, expression)
        spaced_expression = ' '.join(elements)
        return spaced_expression

    # Check if the expression contains only pattern symbols
    if mode == "verify":
        pattern = r'(\d+\.?\d*|\+|\-|\*|\/|\(|\)|\^|\!|\%|\√|\.|\÷)'
        original_expression = expression
        non_pattern_symbols = re.sub(pattern, '', original_expression)
        if len(non_pattern_symbols) > 0:
            return False


# function for opening the help window
def help_window():
    helpwindow = customtkinter.CTk()
    helpwindow.title("Usage")
    helpwindow.geometry("420x400")
    helpwindow.resizable(False, False)

    # TODO: make more fancy help window
    help_label = customtkinter.CTkLabel(master=helpwindow, text="Unary operators", width=400, height=60,
                                        font=("Arial bold", 20), justify=tkinter.CENTER)
    help_label.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

    helpwindow.bind("<Return>", lambda event: helpwindow.destroy())
    helpwindow.bind("<Escape>", lambda event: helpwindow.destroy())

    helpwindow.mainloop()


def usage(target):
    if target == "label":
        return "0"
    elif target == "small_label":
        return "0"


class Calculator:
    def __init__(self):
        # setting up the default theme
        customtkinter.set_appearance_mode("Light")

        # creating the main window
        self.app = customtkinter.CTk()
        self.app.title("Calculator")
        self.app.geometry("425x675")
        self.app.resizable(False, False)

    # function for changing the theme
    def change_theme(self):
        if customtkinter.get_appearance_mode() == "Light":
            customtkinter.set_appearance_mode("Dark")
        else:
            customtkinter.set_appearance_mode("Light")
        self.app.update()

    # function for handling button clicks and change the label
    def label_changer(self, label, small_label, add):
        if add == "h" or add == "H":
            help_window()
            return

        if add == "cls":
            label.configure(text="")
            self.app.update()
            return

        if add == "last":
            label.configure(text=label.cget("text")[:-1])
            self.app.update()
            return

        if add.isalpha():
            return

        if label.cget("text") == "Error":
            label.configure(text="")
            self.app.update()

        elif add == "=":
            small_label.configure(text=label.cget("text"))
            try:
                label.configure(text=parse(regex(label.cget("text"), "spaces").replace("÷", "/")))
            except ParserError:
                label.configure(text="Error")
            self.app.update()
            return

        if not regex(add, "verify"):
            return

        label.configure(text=label.cget("text") + add)
        self.app.update()

    # creating the buttons and labels
    def create_main_window(self):
        helpbutton = customtkinter.CTkButton(master=self.app, text="?", command=lambda: help_window(),
                                             width=20, height=20, hover=True, hover_color="grey",
                                             fg_color="transparent", text_color=("black", "white"), font=("Arial", 20))
        helpbutton.place(relx=0.95, rely=0.05, anchor=tkinter.CENTER)

        small_label = customtkinter.CTkLabel(master=self.app, text="", width=290, height=60, font=("Arial", 30))
        small_label.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

        label_img = customtkinter.CTkImage(light_image=Image.open("light_shadow.png"),
                                           dark_image=Image.open("shadow.png"),
                                           size=(425, 105))
        label = customtkinter.CTkLabel(master=self.app, image=label_img, text="", width=425, height=100,
                                       font=("Arial", 60))
        label.place(relx=0.5, rely=0.18, anchor=tkinter.CENTER)

        img_theme = customtkinter.CTkImage(light_image=Image.open("night-mode.png"),
                                           dark_image=Image.open("brightness.png"),
                                           size=(30, 30))
        buttonChangeTheme = customtkinter.CTkButton(master=self.app, image=img_theme, text="",
                                                    command=lambda: self.change_theme(),
                                                    width=100, height=80, hover=True, hover_color="grey",
                                                    text_color="#36b6ab", fg_color="transparent", font=("Arial", 40))
        buttonChangeTheme.place(relx=0.14, rely=0.32, anchor=tkinter.CENTER)

        buttonDot = customtkinter.CTkButton(master=self.app, text=".",
                                            command=lambda: self.label_changer(label, small_label, "."),
                                            width=100, height=80, hover=True, hover_color="grey", text_color="#36b6ab",
                                            fg_color="transparent", font=("Arial", 40))
        buttonDot.place(relx=0.14, rely=0.44, anchor=tkinter.CENTER)

        buttonOne = customtkinter.CTkButton(master=self.app, text="1",
                                            command=lambda: self.label_changer(label, small_label, "1"),
                                            width=100, height=80, hover=True, hover_color="grey",
                                            fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonOne.place(relx=0.14, rely=0.56, anchor=tkinter.CENTER)

        buttonFour = customtkinter.CTkButton(master=self.app, text="4",
                                             command=lambda: self.label_changer(label, small_label, "4"),
                                             width=100, height=80, hover=True, hover_color="grey",
                                             fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonFour.place(relx=0.14, rely=0.68, anchor=tkinter.CENTER)

        buttonSeven = customtkinter.CTkButton(master=self.app, text="7",
                                              command=lambda: self.label_changer(label, small_label, "7"),
                                              width=100, height=80, hover=True, hover_color="grey",
                                              fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonSeven.place(relx=0.14, rely=0.8, anchor=tkinter.CENTER)

        buttonClearLast = customtkinter.CTkButton(master=self.app, text="CE",
                                                  command=lambda: self.label_changer(label, small_label, "last"),
                                                  width=100, height=80, hover=True, hover_color=("#df7d7d", "#6c0000"),
                                                  text_color="red", fg_color="transparent", font=("Arial", 40))
        buttonClearLast.place(relx=0.14, rely=0.92, anchor=tkinter.CENTER)

        img_degree = customtkinter.CTkImage(light_image=Image.open("pow.png"),
                                            dark_image=Image.open("pow.png"),
                                            size=(40, 40))
        buttonDegree = customtkinter.CTkButton(master=self.app, image=img_degree, text="",
                                               command=lambda: self.label_changer(label, small_label, "^"),
                                               width=100, height=80, hover=True, hover_color="grey",
                                               text_color="#36b6ab", fg_color="transparent", font=("Arial", 40))
        buttonDegree.place(relx=0.38, rely=0.32, anchor=tkinter.CENTER)

        buttonOpenBracket = customtkinter.CTkButton(master=self.app, text="(",
                                                    command=lambda: self.label_changer(label, small_label, "("),
                                                    width=100, height=80, hover=True, text_color="#36b6ab",
                                                    hover_color="grey", fg_color="transparent",
                                                    font=("Arial", 40))
        buttonOpenBracket.place(relx=0.38, rely=0.44, anchor=tkinter.CENTER)

        buttonTwo = customtkinter.CTkButton(master=self.app, text="2",
                                            command=lambda: self.label_changer(label, small_label, "2"),
                                            width=100, height=80, hover=True, hover_color="grey",
                                            fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonTwo.place(relx=0.38, rely=0.56, anchor=tkinter.CENTER)

        buttonFive = customtkinter.CTkButton(master=self.app, text="5",
                                             command=lambda: self.label_changer(label, small_label, "5"),
                                             width=100, height=80, hover=True, hover_color="grey",
                                             fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonFive.place(relx=0.38, rely=0.68, anchor=tkinter.CENTER)

        buttonEight = customtkinter.CTkButton(master=self.app, text="8",
                                              command=lambda: self.label_changer(label, small_label, "8"),
                                              width=100, height=80, hover=True, hover_color="grey",
                                              fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonEight.place(relx=0.38, rely=0.8, anchor=tkinter.CENTER)

        buttonZero = customtkinter.CTkButton(master=self.app, text="0",
                                             command=lambda: self.label_changer(label, small_label, "0"),
                                             width=100, height=80, hover=True, hover_color="grey",
                                             fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonZero.place(relx=0.38, rely=0.92, anchor=tkinter.CENTER)

        img_radical = customtkinter.CTkImage(light_image=Image.open("root.png"),
                                             dark_image=Image.open("root.png"),
                                             size=(40, 40))
        buttonRadical = customtkinter.CTkButton(master=self.app, image=img_radical, text="",
                                                command=lambda: self.label_changer(label, small_label, "√"),
                                                width=100, height=80, hover=True, hover_color="grey",
                                                text_color="#36b6ab", fg_color="transparent", font=("Arial", 40))
        buttonRadical.place(relx=0.62, rely=0.32, anchor=tkinter.CENTER)

        buttonCloseBracket = customtkinter.CTkButton(master=self.app, text=")",
                                                     command=lambda: self.label_changer(label, small_label, ")"),
                                                     width=100, height=80, hover=True, hover_color="grey",
                                                     text_color="#36b6ab", fg_color="transparent", font=("Arial", 40))
        buttonCloseBracket.place(relx=0.62, rely=0.44, anchor=tkinter.CENTER)

        buttonThree = customtkinter.CTkButton(master=self.app, text="3",
                                              command=lambda: self.label_changer(label, small_label, "3"),
                                              width=100, height=80, hover=True, hover_color="grey",
                                              fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonThree.place(relx=0.62, rely=0.56, anchor=tkinter.CENTER)

        buttonSix = customtkinter.CTkButton(master=self.app, text="6",
                                            command=lambda: self.label_changer(label, small_label, "6"),
                                            width=100, height=80, hover=True, hover_color="grey",
                                            fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonSix.place(relx=0.62, rely=0.68, anchor=tkinter.CENTER)

        buttonNine = customtkinter.CTkButton(master=self.app, text="9",
                                             command=lambda: self.label_changer(label, small_label, "9"),
                                             width=100, height=80, hover=True, hover_color="grey",
                                             fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonNine.place(relx=0.62, rely=0.8, anchor=tkinter.CENTER)

        buttonClear = customtkinter.CTkButton(master=self.app, text="C",
                                              command=lambda: self.label_changer(label, small_label, "cls"),
                                              width=100, height=80, hover=True, hover_color=("#df7d7d", "#6c0000"),
                                              fg_color="transparent", text_color="red", font=("Arial", 40))
        buttonClear.place(relx=0.62, rely=0.92, anchor=tkinter.CENTER)

        img_factorial = customtkinter.CTkImage(light_image=Image.open("factorial.png"),
                                               dark_image=Image.open("factorial.png"),
                                               size=(40, 40))
        buttonFactorial = customtkinter.CTkButton(master=self.app, image=img_factorial, text="",
                                                  command=lambda: self.label_changer(label, small_label, "!"),
                                                  width=100, height=80, hover=True, hover_color="grey",
                                                  text_color="#36b6ab", fg_color="transparent", font=("Arial", 40))
        buttonFactorial.place(relx=0.86, rely=0.32, anchor=tkinter.CENTER)

        buttonDivide = customtkinter.CTkButton(master=self.app, text="÷",
                                               command=lambda: self.label_changer(label, small_label, "÷"),
                                               width=100, height=80, hover=True, hover_color="grey",
                                               text_color="#36b6ab", fg_color="transparent", font=("Arial", 40))
        buttonDivide.place(relx=0.86, rely=0.44, anchor=tkinter.CENTER)

        buttonMultiply = customtkinter.CTkButton(master=self.app, text="*",
                                                 command=lambda: self.label_changer(label, small_label, "*"),
                                                 width=100, height=80, hover=True, text_color="#36b6ab",
                                                 hover_color="grey", fg_color="transparent", font=("Arial", 40))
        buttonMultiply.place(relx=0.86, rely=0.56, anchor=tkinter.CENTER)

        buttonPlus = customtkinter.CTkButton(master=self.app, text="+",
                                             command=lambda: self.label_changer(label, small_label, "+"),
                                             width=100, height=80, hover=True, hover_color="grey", text_color="#36b6ab",
                                             fg_color="transparent", font=("Arial", 40))
        buttonPlus.place(relx=0.86, rely=0.68, anchor=tkinter.CENTER)

        buttonMinus = customtkinter.CTkButton(master=self.app, text="-",
                                              command=lambda: self.label_changer(label, small_label, "-"),
                                              width=100, height=80, hover=True, hover_color="grey",
                                              text_color="#36b6ab", fg_color="transparent", font=("Arial", 40))
        buttonMinus.place(relx=0.86, rely=0.8, anchor=tkinter.CENTER)

        buttonEqual = customtkinter.CTkButton(master=self.app, text="=",
                                              command=lambda: self.label_changer(label, small_label, "="),
                                              width=100, height=80, hover=True, hover_color="#3a8088",
                                              text_color="white", fg_color="#36b6ab", font=("Arial", 40))
        buttonEqual.place(relx=0.86, rely=0.92, anchor=tkinter.CENTER)

        # Binding keys
        self.app.bind("<KeyPress>", lambda event: self.label_changer(label, small_label, event.char))
        self.app.bind("<BackSpace>", lambda event: self.label_changer(label, small_label, "last"))
        self.app.bind("<Return>", lambda event: self.label_changer(label, small_label, "="))
        self.app.bind("<Escape>", lambda event: self.app.destroy())
        self.app.bind("<Delete>", lambda event: self.label_changer(label, small_label, "cls"))

    # Mainloop
    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    calculator = Calculator()
    calculator.create_main_window()
    calculator.run()
