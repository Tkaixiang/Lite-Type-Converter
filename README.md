# Lite-Type-Converter
A simple GUI program that converts between several types such as Hex, Binary, ASCII, Octal



## Introduction

Welcome adventurer! I wonder what brings you here to this desolated section of Github :thinking:

Anyways, welcome to my first Github repository/project!



Lite Type Converter is a simple program which converts between different types, written in python using tkinter. It was then "compiled" into a single executable file using PyInstaller for it to be launched with a click of the mouse :happy:! 



I wrote this to serve as a simple type conversion tool that I can use offline without having to google every time I need to use 1. I hope that it will find some use with you and that you will enjoy it :). 



P.S Constructive feedback is greatly appreciated ^^



## Main Features

- Lightweight and fast
- Easy to use GUI interface
- Several type conversions supported (Decimal, Hexadecimal, Octal, ASCII(String), Binary)
- No dependencies required



## Usage

For most users, the **"compiled" executable** can be **found under** the <u>"**dist**"</u> folder:

-  https://github.com/Tkaixiang/Lite-Type-Converter/tree/master/dist 

- Simply download it and run it :)

However, if you would like to run the **Original Python tkinter GUI** *(Which is admittedly faster)*:

- Clone the repository
- Run **Main.py**



The GUI itself should be quite intuitive, simply:

1. Select an input type
2. Enter your input into the input field
3. Select an output type
4. Click on the "Converter" button. (**Hint:** You can press "Enter" as a shortcut)



However, do take note of the difference between **Byte Mode** and **Normal Mode**:

**<u>Byte Mode:</u>** 

- **Reads input** as **bytes** separated by **<spaces>** (ASCII input need not have spaces)
- **Output** is also in **bytes** in the type you specified
- *All type conversions supported*

**<u>Normal Mode:</u>** 

- **Reads input** as a **continuous string without spaces** 
- **Output** is also as a **continuous string/raw value**
- *<u>Note:</u>* *Only **Hexadecimal -> ASCII** is supported for converting to ASCII(String) in Normal Mode*



Thank you for reading if you are still here, hope you enjoy :)!



