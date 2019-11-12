from tkinter import *
import tkinter.ttk as ttk
import ConverterFunctions
import time
import winsound

#TO DO: Work on Byte Mode
#Current state: To ASCII & From ASCII is all in byte mode

window = Tk()

window.title("Lite Type Converter 0.1")

window.geometry("485x545") #Width x Height

window.resizable(0, 0) #Fixed Window Size

window.iconbitmap(r"C:\Users\Tkaixiang\Documents\Python Scripts\9. Object Oriented Programing\Type Converter Project\hexa.ico")

Mode = ""

#--Mode Info Label--
ModeLabel = Label(window, width=50, relief=GROOVE, font=("Microsoft Sans Serif", 10), text="")
ModeLabel.grid(row=10, column=0, columnspan=2, pady=(15, 0) )

#--Error/Output Label--
ErrorLabel = Label(window, bg="#cfcfcf", width=52, relief=SUNKEN, font=("Microsoft Sans Serif", 10, "bold"), text="Ready...")
ErrorLabel.grid(row=11, column=0, columnspan=2, pady=(15, 0), padx=(3, 0))

#--Input Label--
Inputlabel = Label(window, text="Input:", font=("Microsoft Sans Serif", 12, "bold"))
Inputlabel.grid(row=1,column=0, pady=(5,0))



#Output to "Error" dialouge
def ErrorOut(Message, Color):
    MaxLength = 70
    
    if (len(Message) > MaxLength):
        Message = Message[:MaxLength]
        
    ErrorLabel["text"] = Message
    ErrorLabel["fg"] = Color
    
    if (Color == "red"): #Play error sound if its an error
        winsound.PlaySound("SystemExclamation", winsound.SND_ASYNC)
    
#--Radio Button--
    
v = IntVar()

def RadioButtonClick():
    global Mode
    
    if (v.get() == 1):
        
        Mode = "Normal"
        ModeLabel["text"] = "[Normal Mode]: Input is read as a continuous string without spaces.\nOutput is the raw value/a string\nNote: For converting to ASCII, only Hex->ASCII is supported"
    elif (v.get() == 2):
        
        Mode = "Byte"
        ModeLabel["text"] = "[Byte Mode]: Input is read as bytes seperated by <spaces>. \nOutput is in bytes. \nNote: No spaces needed in ASCII input. All conversions supported"
    
RB1 = Radiobutton(window, text="Normal Mode", variable=v, value=1, indicatoron=0, command=RadioButtonClick)
RB2 = Radiobutton(window, width=10, text="Byte Mode", variable=v, value=2, indicatoron=0, command=RadioButtonClick)
RB1.grid(row=3, column=1, pady=(30, 0), sticky="ew")
RB2.grid(row=4, column=1, pady=(0, 50), sticky="ew")

v.set(1) #Select default mode as "Normal Mode"
RadioButtonClick()



#--Main Components--
txt = Text(window, width=40, height=10)
txt.grid(row=2, column=0, rowspan=3, padx=(15, 10))
txt.focus_set() #Focus on Input Widget at start

combo = ttk.Combobox(window, width=15, state="readonly")
combo["values"] = ("Decimal", "Hex", "Octal", "ASCII", "Binary")
combo.current(0)
combo.grid(row=2, column=1)

label2 = Label(window, text="Output: ", font=("Microsoft Sans Serif", 12, "bold"))
label2.grid(row=5,column=0, pady=(5, 0))

txt2 = Text(window, width=40, height=10, bg="#a6a6a6")
txt2.grid(row=6, column=0, rowspan=3, padx=(15, 10))
txt2["state"] = "disabled" #Prevent Accidental Editing (At Start)

combo2 = ttk.Combobox(window, width=15, state="readonly")
combo2["values"] = ("Decimal", "Hex", "Octal", "ASCII", "Binary")
combo2.current(0)
combo2.grid(row=6, column=1)




      
#Main Button Click Event Handler
def Clicked():
    user_input = txt.get("1.0", "end-1c") #Get input
    user_input = user_input.strip() #Removes any spaces/illegal input in case
    user_input_type = combo.get()
    user_output_type = combo2.get()
    global Mode
    
    output = "" #Resulting output
    
    
    if (user_output_type == user_input_type):
        
        ErrorOut("Error: Input and Output type can't be the same!", "red")
        
    elif (user_input == ""):
        
        ErrorOut("Error: Input can't be empty!", "red")
        
    elif (Mode == "Normal" and user_output_type == "ASCII" and user_input_type != "Hex"): #Only Hex->ASCII is supported in Normal Mode
        
        ErrorOut("Error: Only Hex->ASCII is supported in Normal Mode", "red") 
        
    else:
        
        ErrorLabel["text"] = ""
        
        
        try:
            if (user_output_type == "Decimal"):
                
                output = ( ConverterFunctions.ToDecimal(user_input, user_input_type, Mode) )
            
            elif (user_output_type == "Hex"):
                output = ( ConverterFunctions.ToHex(user_input, user_input_type, Mode) )
            
            elif (user_output_type == "Octal"):
                output = ( ConverterFunctions.ToOctal(user_input, user_input_type, Mode) )
        
            elif (user_output_type == "ASCII"):
                output = ( ConverterFunctions.ToASCII(user_input, user_input_type, Mode) )
            
            elif (user_output_type == "Binary"):
                output = ( ConverterFunctions.ToBinary(user_input, user_input_type, Mode) )
        
        except Exception as error: #Capture Conversion Errors
            ErrorOut("Conversion Error: " + str(error), "red")
            
        else:
        
            output = str(output).strip() #Remove any possible whitespaces at end (left by ConverterFunctions output)
            
            txt2["state"] = "normal" #To allow output to be inserted in
            txt2.delete("1.0", "end-1c")
            txt2.insert("1.0", output)
            txt2["state"] = "disabled" #Prevent Accidental Editing
            
            #Success Output
            ErrorOut("Success", "green")
    
    
btn = Button(window, text="Convert", command=Clicked, width=30, height=2)
btn.grid(row=9, column=0, pady=(5,0))


#Trigger Button with "Enter" key
def key(event): 
    print ("pressed", repr(event.char))
    
    if (repr(event.char) == "'\\r'"):
             
        #Rather unconventional, but works :3
        #After pressing "Enter" to trigger the button, the input txt widget will have an "enter" still
        #The code below gets the input, strips the enter left behind and inserts it back
        #It then calls Clicked()
        user_input = txt.get("1.0", "end-1c") #Get input
        user_input = user_input.strip()
        
        txt.delete("1.0", "end-1c")
        txt.insert("1.0", user_input)
        
        #Provides the visual effect of pressing the button
        btn.config(relief = "sunken")
        window.update_idletasks()
        time.sleep(.1)
        btn.config(relief = "raised")
        
        btn.invoke() #"Pressing" the button, but the visual effect will not be played
        
        
    
window.bind("<Key>", key) #Binds keypresses to the "key" function



window.mainloop()