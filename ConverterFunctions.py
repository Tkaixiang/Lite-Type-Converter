def ToDecimal(user_input, user_input_type, Mode):
    
    
    if (Mode == "Byte"):
        
        
        if (user_input_type == "ASCII"): #ASCII Input does not have spaces even in byte mode - Requires special handling
            
            hexa = user_input.encode("utf-8").hex() #Encode ASCII to bytes, then use the .hex() method which only takes bytes
            
            result = ""
            
            for x in range(0, int(len(hexa)/2), 1):
                current_decimal_byte = int(hexa[x*2:(x*2)+2], 16)
                result += str(current_decimal_byte) + " "
            
            return result
        
        
        else:
            list_input = user_input.split()
            result = ""
            
            for x in range(0, len(list_input), 1):
            
                if (user_input_type == "Hex"):
                    result += str(int(list_input[x], 16)) + " "
                
                elif (user_input_type == "Octal"):
                    result += str(int(list_input[x], 8)) + " "
                
                elif (user_input_type == "Binary"):
                    result += str(int(list_input[x], 2)) + " "
            
            return result
                
                
        
    elif (Mode == "Normal"):
        
        if (user_input_type == "ASCII"):
            hexa = user_input.encode("utf-8").hex() #Encode ASCII to bytes, then use the .hex() method which only takes bytes
            
            return int(hexa, 16) #Raw value of string
        
        elif (user_input_type == "Hex"):
            return int(user_input, 16)
        elif (user_input_type == "Octal"):
            return int(user_input, 8)
        elif (user_input_type == "Binary"):
            return int(user_input, 2)

    

def ToHex(user_input, user_input_type, Mode):
    
    if (Mode == "Byte"):
        
        if (user_input_type == "ASCII"):
            hexa = user_input.encode("utf-8").hex() #Encode ASCII to bytes, then use the .hex() method which only takes bytes
            result = ""
        
            for x in range(0, int(len(hexa)/2), 1):
            
                result += str(hexa[x*2:(x*2)+2]) + " "
            
            return result 
        
    
        else:
            
            list_input = user_input.split()
            result = ""
            
            for x in range(0, len(list_input), 1):
                
                if (user_input_type == "Octal"): 
                    result += str(hex(int(list_input[x], 8))[2:]) + " "#Convert to decimal, then to octal
    
                elif (user_input_type == "Decimal"):
                    result += str(hex(int(list_input[x]))[2:]) + " "
    
                elif (user_input_type == "Binary"):
                    result += str(hex(int(list_input[x], 2))[2:]) + " "
                    
            return result
        
        
    elif (Mode == "Normal"):
        
        if (user_input_type == "ASCII"):
            return user_input.encode("utf-8").hex()
        
        elif (user_input_type == "Octal"): 
            return hex(int(user_input, 8))[2:] #Convert to decimal, then to octal
    
        elif (user_input_type == "Decimal"):
            return hex(int(user_input))[2:]
    
        elif (user_input_type == "Binary"):
            return hex(int(user_input, 2))[2:] 
    

def ToOctal(user_input, user_input_type, Mode):
    
    if (Mode == "Byte"):
        
        if (user_input_type == "ASCII"):
        
            hexa = user_input.encode("utf-8").hex() #Encode ASCII to bytes, then use the .hex() method which only takes bytes
            result = ""
        
            for x in range(0, int(len(hexa)/2), 1):
                current_octal_byte = oct(int(hexa[x*2:(x*2)+2], 16))[2:]
                result += str(current_octal_byte) + " "
            
            return result
        
    
        else:
            
            list_input = user_input.split()
            result = ""
            
            for x in range(0, len(list_input), 1):
                
                if (user_input_type == "Hex"): 
                    result += str(oct(int(list_input[x], 16))[2:]) + " "#Convert to decimal, then to octal
    
                elif (user_input_type == "Decimal"):
                    result += str(oct(int(list_input[x]))[2:]) + " "
    
                elif (user_input_type == "Binary"):
                    result += str(oct(int(list_input[x], 2))[2:]) + " "
                    
            return result
        
        
    elif (Mode == "Normal"):
        
        if (user_input_type == "ASCII"):
            return oct(int(user_input.encode("utf-8").hex(), 16))[2:]
        
        elif (user_input_type == "Octal"): 
            return oct(int(user_input, 8))[2:] #Convert to decimal, then to octal
    
        elif (user_input_type == "Decimal"):
            return oct(int(user_input))[2:]
    
        elif (user_input_type == "Binary"):
            return oct(int(user_input, 2))[2:] 
        
    
    
def ToASCII(user_input, user_input_type, Mode):
    
    
    if (Mode == "Byte"):
        
        if (user_input_type == "Hex"):
            hexa_string = user_input.replace(" ", "") #Remove any spaces in hexa string
            return bytes.fromhex(hexa_string).decode('utf-8')
    
        elif (user_input_type == "Octal"):
            strings = user_input.split(" ")
            result = ""
        
            for x in range(0, len(strings), 1): #Convert to decimal, then ASCII
                decimal = int(strings[x], 8)
                result += chr(decimal)
        
            return result        
        
        elif (user_input_type == "Decimal"):
            strings = user_input.split(" ")
            result = ""
            
            for x in range(0, len(strings), 1):
                result += chr(int(strings[x]))
            
            return result
        
        elif (user_input_type == "Binary"):
            strings = user_input.split(" ")
            result = ""
            
            for x in range(0, len(strings), 1): 
                decimal = int(strings[x], 2)
                result += chr(decimal)
            
            return result
    
    elif (Mode == "Normal"):
        
        if (user_input_type == "Hex"):
            return bytes.fromhex(user_input).decode('utf-8')
        
    
def ToBinary(user_input, user_input_type, Mode):
    

    if (Mode == "Byte"):
        
        if (user_input_type == "ASCII"):
        
            hexa = user_input.encode("utf-8").hex() #Encode ASCII to bytes, then use the .hex() method which only takes bytes
            result = ""
        
            for x in range(0, int(len(hexa)/2), 1):
                current_decimal_byte = bin(int(hexa[x*2:(x*2)+2], 16))[2:]
                result += str(current_decimal_byte) + " "
            
            return result
        
    
        else:
            
            list_input = user_input.split()
            result = ""
            
            for x in range(0, len(list_input), 1):
                
                if (user_input_type == "Hex"): 
                    result += str(bin(int(list_input[x], 16))[2:]) + " "#Convert to decimal, then to octal
    
                elif (user_input_type == "Decimal"):
                    result += str(bin(int(list_input[x]))[2:]) + " "
    
                elif (user_input_type == "Octal"):
                    result += str(bin(int(list_input[x], 8))[2:]) + " "
                    
            return result
        
        
    elif (Mode == "Normal"):
        
        if (user_input_type == "ASCII"):
            return bin(int(user_input.encode("utf-8").hex(), 16))[2:]
        
        elif (user_input_type == "Hex"): 
            return bin(int(user_input, 16))[2:] #Convert to decimal, then to binary
    
        elif (user_input_type == "Decimal"):
            return bin(int(user_input))[2:]
    
        elif (user_input_type == "Octal"):
            return bin(int(user_input, 8))[2:] 
        
    
    
    
            
    