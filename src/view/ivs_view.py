##
# Team Tripple-Double
#
# @file ivs_math.py
#
# @brief Calculator's interface
#
# @section description_doxygen_example Description
# This Python file implements GUI of the calculator
#
# @section author_doxygen_example Author(s)
# - Created by Maksym Podhornyi (xpodho08).
# - Modified by Oleksandr Turytsia (xturyt00) on 24/04/2023.
#
# Copyright (c) GNU GENERAL PUBLIC LICENSE version 3

# Functions


import os
import sys
import platform
import tkinter
import re
from PIL import Image

if platform.system() == "Windows":
    sys.path.append(os.getcwd())
else:
    sys.path.append(os.path.dirname(os.path.abspath("") + "/src"))

import src.customtkinter as customtkinter
from src.parser.ivs_parser import parse, ParserError, ValueTooLongError, IntegerError
from src.math.ivs_math import ZeroDivisonError


def regex(expression, mode):
    """
        Process the given mathematical expression using regular expressions based on the specified mode.

        Args:
            expression (str): The mathematical expression to process.
            mode (str): The mode to apply on the expression. Possible values are:
                - "spaces": Join elements with spaces.
                - "verify": Check if the expression contains only pattern symbols.

        Returns:
            str or bool: The processed expression if mode is "spaces", or a boolean value
                         indicating if the expression contains only pattern symbols if mode is "verify".

        Raises:
            ValueError: If the mode is not one of the accepted values.
    """

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
        else:
            return True

    raise ValueError("Invalid mode")


class Tooltips:

    def __init__(self):
        """
            Initialize the Tooltips class with default parameters and create the help window.
        """

        self.operation_usage = None
        self.helpwindow = customtkinter.CTk()
        self.helpwindow.geometry("420x400")
        self.helpwindow.resizable(False, False)

    def escape(self):
        """
            Close the help window or return to the main tool window depending on the help window title.
        """

        if self.helpwindow.title() == "Usage":
            self.helpwindow.destroy()

        else:
            self.create_help_window()

    def usage(self, target):
        """
            Display the usage of the specified operator in the help window.

            Args:
                target (str): The operator symbol for which the usage will be displayed.
        """
        for widget in self.helpwindow.winfo_children():
            widget.destroy()

        info_label = customtkinter.CTkLabel(master=self.helpwindow, font=("Arial bold", 17),
                                            text="Press 'Enter' or 'Escape' to return to all operators",
                                            width=420, height=35)
        info_label.place(relx=0.5, rely=0.93, anchor=tkinter.CENTER)

        operator_label = customtkinter.CTkLabel(master=self.helpwindow, font=("Arial bold", 20),
                                                text="", width=420, height=35)
        operator_label.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

        if target == "!":
            self.helpwindow.title("Usage: Factorial (!)")
            operator_label.configure(text="Factorial (!)")

        elif target == "√":
            self.helpwindow.title("Usage: Root (√)")
            operator_label.configure(text="Root (√)")

        elif target == "^":
            self.helpwindow.title("Usage: Power (^)")
            operator_label.configure(text="Power (^)")

        elif target == "÷":
            self.helpwindow.title("Usage: Division (÷ or /)")
            operator_label.configure(text="Division (÷ or /)")

        elif target == "*":
            self.helpwindow.title("Usage: Multiplication (*)")
            operator_label.configure(text="Multiplication (*)")

        elif target == "-":
            self.helpwindow.title("Usage: Subtraction (-)")
            operator_label.configure(text="Subtraction (-)")

        elif target == "+":
            self.helpwindow.title("Usage: Addition (+)")
            operator_label.configure(text="Addition (+)")

        elif target == "()":
            self.helpwindow.title("Usage: Brackets ( '(' or ')' )")
            operator_label.configure(text="Brackets ( '(' or ')' )")

        elif target == ".":
            self.helpwindow.title("Usage: Point (.)")
            operator_label.configure(text="Point (.)")

        else:
            return

    # function for opening the help window
    def create_help_window(self):
        """
            Open the help window and display the usage of all available operators.
        """

        self.helpwindow.title("Usage")

        help_label_unary = customtkinter.CTkLabel(master=self.helpwindow, text="Unary operators:", width=420, height=32,
                                                  font=("Arial bold", 20))
        help_label_unary.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

        help_factorial = customtkinter.CTkButton(master=self.helpwindow, text="Factorial (!)", width=420, height=32,
                                                 hover=True, hover_color=("#dfdfdf", "#313131"),
                                                 command=lambda: self.usage("!"), text_color=("black", "white"),
                                                 font=("Arial", 20, "underline"), fg_color="transparent")
        help_factorial.place(relx=0.5, rely=0.13, anchor=tkinter.CENTER)

        help_label_binary = customtkinter.CTkLabel(master=self.helpwindow, text="Binary operators:", width=420,
                                                   height=32, font=("Arial bold", 20))
        help_label_binary.place(relx=0.5, rely=0.21, anchor=tkinter.CENTER)

        help_addition = customtkinter.CTkButton(master=self.helpwindow, text="Addition (+)", width=420, height=32,
                                                hover=True, hover_color=("#dfdfdf", "#313131"),
                                                text_color=("black", "white"), command=lambda: self.usage("+"),
                                                font=("Arial", 20, "underline"), fg_color="transparent")
        help_addition.place(relx=0.5, rely=0.29, anchor=tkinter.CENTER)

        help_subtraction = customtkinter.CTkButton(master=self.helpwindow, text="Subtraction (-)", width=420, height=32,
                                                   hover=True, hover_color=("#dfdfdf", "#313131"),
                                                   text_color=("black", "white"), command=lambda: self.usage("-"),
                                                   font=("Arial", 20, "underline"), fg_color="transparent")
        help_subtraction.place(relx=0.5, rely=0.37, anchor=tkinter.CENTER)

        help_multiplication = customtkinter.CTkButton(master=self.helpwindow, text="Multiplication (*)", width=420,
                                                      hover=True, hover_color=("#dfdfdf", "#313131"), height=32,
                                                      text_color=("black", "white"), command=lambda: self.usage("*"),
                                                      font=("Arial", 20, "underline"), fg_color="transparent")
        help_multiplication.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

        help_division = customtkinter.CTkButton(master=self.helpwindow, text="Division (/ or ÷)", width=420, height=32,
                                                hover=True, hover_color=("#dfdfdf", "#313131"),
                                                text_color=("black", "white"), command=lambda: self.usage("÷"),
                                                font=("Arial", 20, "underline"), fg_color="transparent")
        help_division.place(relx=0.5, rely=0.53, anchor=tkinter.CENTER)

        help_radical = customtkinter.CTkButton(master=self.helpwindow, text="Root (√)", width=420, height=32,
                                               hover=True, hover_color=("#dfdfdf", "#313131"),
                                               text_color=("black", "white"), command=lambda: self.usage("√"),
                                               font=("Arial", 20, "underline"), fg_color="transparent")
        help_radical.place(relx=0.5, rely=0.61, anchor=tkinter.CENTER)

        help_power = customtkinter.CTkButton(master=self.helpwindow, text="Power (^)", width=420, height=32,
                                             hover=True, hover_color=("#dfdfdf", "#313131"),
                                             text_color=("black", "white"), command=lambda: self.usage("^"),
                                             font=("Arial", 20, "underline"), fg_color="transparent")
        help_power.place(relx=0.5, rely=0.69, anchor=tkinter.CENTER)

        help_brackets = customtkinter.CTkButton(master=self.helpwindow, text="Brackets ( '(' or ')' )", width=420,
                                                height=32, hover=True, hover_color=("#dfdfdf", "#313131"),
                                                text_color=("black", "white"), font=("Arial", 20, "underline"),
                                                fg_color="transparent", command=lambda: self.usage("()"))
        help_brackets.place(relx=0.5, rely=0.77, anchor=tkinter.CENTER)

        help_dot = customtkinter.CTkButton(master=self.helpwindow, text="Dot (.)", text_color=("black", "white"),
                                           width=420, height=32, hover=True, hover_color=("#dfdfdf", "#313131"),
                                           font=("Arial", 20, "underline"), fg_color="transparent",
                                           command=lambda: self.usage("."))
        help_dot.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

        info_label = customtkinter.CTkLabel(master=self.helpwindow, font=("Arial bold", 18),
                                            text="Press 'Enter' or 'Escape' to close this window",
                                            width=420, height=35)
        info_label.place(relx=0.5, rely=0.93, anchor=tkinter.CENTER)

        self.helpwindow.bind("<Return>", lambda event: self.escape())
        self.helpwindow.bind("<Escape>", lambda event: self.escape())

    def run(self):
        """
                Start the main loop of the help window.
        """
        self.helpwindow.mainloop()


class Calculator:
    """
    The Calculator class is responsible for creating and managing the calculator's graphical interface.
    """

    def __init__(self):
        """
            Initialize the Calculator class with default parameters, create the main window, and set up the theme.
        """

        customtkinter.set_appearance_mode("Light")
        self.app = customtkinter.CTk()
        self.app.title("Calculator")
        self.app.geometry("425x675")
        self.app.resizable(False, False)

        # tooltip window
        self.tooltips = None

    def change_theme(self):
        """
            Change the theme of the calculator between Light and Dark modes.
        """
        if customtkinter.get_appearance_mode() == "Light":
            customtkinter.set_appearance_mode("Dark")
        else:
            customtkinter.set_appearance_mode("Light")
        self.app.update()

    def create_help_window(self):
        """
            Create and display the tooltip help window.
        """
        self.tooltips = Tooltips()
        self.tooltips.create_help_window()
        self.tooltips.run()

    # def update_size(self, label):
    #     widget_width = 425
    #
    #     if len(label.cget("text")) == 0:
    #         return
    #
    #     print(label.cget("font")[1])
    #
    #     if len(label.cget("text")) > 12 and label.cget("font")[1] > 20:
    #
    #         label.configure(font=("Arial", 55))
    #         self.app.update()
    #
    #     elif len(label.cget("text")) < 12 and label.cget("font")[1] < 60:
    #
    #         label.configure(font=("Arial", 60))
    #         self.app.update()

    def label_changer(self, label, small_label, add):
        """
            Handle button clicks and update the labels accordingly.

            Args:
                label (customtkinter.CTkLabel): The main label for displaying calculations.
                small_label (customtkinter.CTkLabel): The smaller label for displaying previous calculations.
                add (str): The value or operation to add to the label.
        """

        if add == "h" or add == "H":
            self.create_help_window()
            return

        if add == "cls":
            label.configure(text="")
            self.app.update()
            return

        if add == "last":
            try:
                label.configure(text=label.cget("text")[:-1])

            except TypeError:
                label.configure(text="")

            self.app.update()
            return

        if add.isalpha():
            return

        elif add == "=":
            small_label.configure(text=label.cget("text"))
            try:
                label.configure(text=parse(
                    regex(label.cget("text"), "spaces").replace("÷", "/")))

            except ParserError as e:
                label.configure(text=e)

            except IntegerError as e:
                label.configure(text=e)

            except ValueTooLongError as e:
                label.configure(text=e)

            except ZeroDivisionError as e:
                label.configure(text=e)

            self.app.update()
            return

        try:
            if not regex(add, "verify"):
                return
        except ValueError:
            return

        try:
            label.configure(text=label.cget("text") + add)
        except TypeError:
            label.configure(text=add)

        self.app.update()

    def create_main_window(self):
        """
            Creates the main calculator window, including all buttons, labels, and images.
            Sets up the event bindings for keyboard input.
        """

        helpbutton = customtkinter.CTkButton(master=self.app, text="?", command=lambda: self.create_help_window(),
                                             width=20, height=20, hover=True, hover_color=("#dfdfdf", "#313131"),
                                             fg_color="transparent", text_color=("black", "white"), font=("Arial", 20))
        helpbutton.place(relx=0.95, rely=0.05, anchor=tkinter.CENTER)

        small_label = customtkinter.CTkLabel(
            master=self.app, text="", width=290, height=60, font=("Arial", 30))
        small_label.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

        label_img = customtkinter.CTkImage(light_image=Image.open(os.path.join(os.path.dirname(__file__), 'light_shadow.png')),
                                           dark_image=Image.open(os.path.join(
                                               os.path.dirname(__file__), 'shadow.png')),
                                           size=(425, 105))
        label = customtkinter.CTkLabel(master=self.app, image=label_img, text="", width=425, height=100,
                                       font=("Arial", 60))
        label.place(relx=0.5, rely=0.18, anchor=tkinter.CENTER)

        img_theme = customtkinter.CTkImage(light_image=Image.open(os.path.join(os.path.dirname(__file__), "night-mode.png")),
                                           dark_image=Image.open(os.path.join(
                                               os.path.dirname(__file__), "brightness.png")),
                                           size=(30, 30))
        buttonChangeTheme = customtkinter.CTkButton(master=self.app, image=img_theme, text="",
                                                    command=lambda: self.change_theme(), fg_color="transparent",
                                                    width=100, height=80, hover=True, font=("Arial", 40),
                                                    hover_color=("#dfdfdf", "#313131"), text_color="#36b6ab")
        buttonChangeTheme.place(relx=0.14, rely=0.32, anchor=tkinter.CENTER)

        buttonDot = customtkinter.CTkButton(master=self.app, text=".",
                                            command=lambda: self.label_changer(
                                                label, small_label, "."),
                                            width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                            fg_color="transparent", font=("Arial", 40), text_color="#36b6ab")
        buttonDot.place(relx=0.14, rely=0.44, anchor=tkinter.CENTER)

        buttonOne = customtkinter.CTkButton(master=self.app, text="1",
                                            command=lambda: self.label_changer(
                                                label, small_label, "1"),
                                            width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                            fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonOne.place(relx=0.14, rely=0.56, anchor=tkinter.CENTER)

        buttonFour = customtkinter.CTkButton(master=self.app, text="4",
                                             command=lambda: self.label_changer(
                                                 label, small_label, "4"),
                                             width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                             fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonFour.place(relx=0.14, rely=0.68, anchor=tkinter.CENTER)

        buttonSeven = customtkinter.CTkButton(master=self.app, text="7",
                                              command=lambda: self.label_changer(
                                                  label, small_label, "7"),
                                              width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                              fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonSeven.place(relx=0.14, rely=0.8, anchor=tkinter.CENTER)

        buttonClearLast = customtkinter.CTkButton(master=self.app, text="CE",
                                                  command=lambda: self.label_changer(
                                                      label, small_label, "last"),
                                                  width=100, height=80, hover=True, hover_color=("#df7d7d", "#6c0000"),
                                                  text_color="red", fg_color="transparent", font=("Arial", 40))
        buttonClearLast.place(relx=0.14, rely=0.92, anchor=tkinter.CENTER)

        img_degree = customtkinter.CTkImage(light_image=Image.open(os.path.join(os.path.dirname(__file__), 'pow.png')),
                                            dark_image=Image.open(os.path.join(
                                                os.path.dirname(__file__), 'pow.png')),
                                            size=(40, 40))
        buttonDegree = customtkinter.CTkButton(master=self.app, image=img_degree, text="",
                                               command=lambda: self.label_changer(
                                                   label, small_label, "^"),
                                               width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                               text_color="#36b6ab", fg_color="transparent", font=("Arial", 40))
        buttonDegree.place(relx=0.38, rely=0.32, anchor=tkinter.CENTER)

        buttonOpenBracket = customtkinter.CTkButton(master=self.app, text="(",
                                                    command=lambda: self.label_changer(
                                                        label, small_label, "("),
                                                    width=100, height=80, hover=True, text_color="#36b6ab",
                                                    hover_color=("#dfdfdf", "#313131"), fg_color="transparent",
                                                    font=("Arial", 40))
        buttonOpenBracket.place(relx=0.38, rely=0.44, anchor=tkinter.CENTER)

        buttonTwo = customtkinter.CTkButton(master=self.app, text="2",
                                            command=lambda: self.label_changer(
                                                label, small_label, "2"),
                                            width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                            fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonTwo.place(relx=0.38, rely=0.56, anchor=tkinter.CENTER)

        buttonFive = customtkinter.CTkButton(master=self.app, text="5",
                                             command=lambda: self.label_changer(
                                                 label, small_label, "5"),
                                             width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                             fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonFive.place(relx=0.38, rely=0.68, anchor=tkinter.CENTER)

        buttonEight = customtkinter.CTkButton(master=self.app, text="8",
                                              command=lambda: self.label_changer(
                                                  label, small_label, "8"),
                                              width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                              fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonEight.place(relx=0.38, rely=0.8, anchor=tkinter.CENTER)

        buttonZero = customtkinter.CTkButton(master=self.app, text="0",
                                             command=lambda: self.label_changer(
                                                 label, small_label, "0"),
                                             width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                             fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonZero.place(relx=0.38, rely=0.92, anchor=tkinter.CENTER)

        img_radical = customtkinter.CTkImage(light_image=Image.open(os.path.join(os.path.dirname(__file__), 'root.png')),
                                             dark_image=Image.open(os.path.join(
                                                 os.path.dirname(__file__), 'root.png')),
                                             size=(40, 40))
        buttonRadical = customtkinter.CTkButton(master=self.app, image=img_radical, text="",
                                                command=lambda: self.label_changer(
                                                    label, small_label, "√"),
                                                width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                                text_color="#36b6ab", fg_color="transparent", font=("Arial", 40))
        buttonRadical.place(relx=0.62, rely=0.32, anchor=tkinter.CENTER)

        buttonCloseBracket = customtkinter.CTkButton(master=self.app, text=")", width=100, height=80,
                                                     command=lambda: self.label_changer(
                                                         label, small_label, ")"),
                                                     hover=True, hover_color=("#dfdfdf", "#313131"),
                                                     text_color="#36b6ab", fg_color="transparent", font=("Arial", 40))
        buttonCloseBracket.place(relx=0.62, rely=0.44, anchor=tkinter.CENTER)

        buttonThree = customtkinter.CTkButton(master=self.app, text="3",
                                              command=lambda: self.label_changer(
                                                  label, small_label, "3"),
                                              width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                              fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonThree.place(relx=0.62, rely=0.56, anchor=tkinter.CENTER)

        buttonSix = customtkinter.CTkButton(master=self.app, text="6",
                                            command=lambda: self.label_changer(
                                                label, small_label, "6"),
                                            width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                            fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonSix.place(relx=0.62, rely=0.68, anchor=tkinter.CENTER)

        buttonNine = customtkinter.CTkButton(master=self.app, text="9",
                                             command=lambda: self.label_changer(
                                                 label, small_label, "9"),
                                             width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                             fg_color="transparent", text_color=("black", "white"), font=("Arial", 40))
        buttonNine.place(relx=0.62, rely=0.8, anchor=tkinter.CENTER)

        buttonClear = customtkinter.CTkButton(master=self.app, text="C",
                                              command=lambda: self.label_changer(
                                                  label, small_label, "cls"),
                                              width=100, height=80, hover=True, hover_color=("#df7d7d", "#6c0000"),
                                              fg_color="transparent", text_color="red", font=("Arial", 40))
        buttonClear.place(relx=0.62, rely=0.92, anchor=tkinter.CENTER)

        img_factorial = customtkinter.CTkImage(light_image=Image.open(os.path.join(os.path.dirname(__file__), 'factorial.png')),
                                               dark_image=Image.open(os.path.join(
                                                   os.path.dirname(__file__), 'factorial.png')),
                                               size=(40, 40))
        buttonFactorial = customtkinter.CTkButton(master=self.app, image=img_factorial, text="",
                                                  command=lambda: self.label_changer(
                                                      label, small_label, "!"),
                                                  width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                                  text_color="#36b6ab", fg_color="transparent", font=("Arial", 40))
        buttonFactorial.place(relx=0.86, rely=0.32, anchor=tkinter.CENTER)

        buttonDivide = customtkinter.CTkButton(master=self.app, text="÷",
                                               command=lambda: self.label_changer(
                                                   label, small_label, "÷"),
                                               width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                               text_color="#36b6ab", fg_color="transparent", font=("Arial", 40))
        buttonDivide.place(relx=0.86, rely=0.44, anchor=tkinter.CENTER)

        buttonMultiply = customtkinter.CTkButton(master=self.app, text="*", font=("Arial", 40),
                                                 command=lambda: self.label_changer(
                                                     label, small_label, "*"),
                                                 width=100, height=80, hover=True, text_color="#36b6ab",
                                                 hover_color=("#dfdfdf", "#313131"), fg_color="transparent")
        buttonMultiply.place(relx=0.86, rely=0.56, anchor=tkinter.CENTER)

        buttonPlus = customtkinter.CTkButton(master=self.app, text="+",
                                             command=lambda: self.label_changer(
                                                 label, small_label, "+"),
                                             width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                             fg_color="transparent", font=("Arial", 40), text_color="#36b6ab")
        buttonPlus.place(relx=0.86, rely=0.68, anchor=tkinter.CENTER)

        buttonMinus = customtkinter.CTkButton(master=self.app, text="-",
                                              command=lambda: self.label_changer(
                                                  label, small_label, "-"),
                                              width=100, height=80, hover=True, hover_color=("#dfdfdf", "#313131"),
                                              text_color="#36b6ab", fg_color="transparent", font=("Arial", 40))
        buttonMinus.place(relx=0.86, rely=0.8, anchor=tkinter.CENTER)

        buttonEqual = customtkinter.CTkButton(master=self.app, text="=",
                                              command=lambda: self.label_changer(
                                                  label, small_label, "="),
                                              width=100, height=80, hover=True, hover_color="#3a8088",
                                              text_color="white", fg_color="#36b6ab", font=("Arial", 40))
        buttonEqual.place(relx=0.86, rely=0.92, anchor=tkinter.CENTER)

        # Binding keys
        self.app.bind("<KeyPress>", lambda event: self.label_changer(
            label, small_label, event.char))
        self.app.bind("<BackSpace>", lambda event: self.label_changer(
            label, small_label, "last"))
        self.app.bind("<Return>", lambda event: self.label_changer(
            label, small_label, "="))
        self.app.bind("<Escape>", lambda event: self.app.destroy())
        self.app.bind("<Delete>", lambda event: self.label_changer(
            label, small_label, "cls"))
        # self.app.bind("<Configure>", lambda event: self.update_size(label))

    def run(self):
        """
            Starts the customtkinter mainloop to display and run the calculator application.
        """

        self.app.mainloop()

