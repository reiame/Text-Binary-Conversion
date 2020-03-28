def Chinese_to_Unicode(str):
   return str.encode('unicode_escape').decode('utf-8')
def Unicode_to_Hex(str):
    return str.replace('\\u','')
def binary(ch):
    if(ch == '0'): return "0000"
    elif(ch == '1'): return "0001"
    elif(ch == '2'): return "0010"
    elif(ch == '3'): return "0011"
    elif(ch == '4'): return "0100"
    elif(ch == '5'): return "0101"
    elif(ch == '6'): return "0110"
    elif(ch == '7'): return "0111"
    elif(ch == '8'): return "1000"
    elif(ch == '9'): return "1001"
    elif(ch == 'a'): return "1010"
    elif(ch == 'b'): return "1011"
    elif(ch == 'c'): return "1100"
    elif(ch == 'd'): return "1101"
    elif(ch == 'e'): return "1110"
    elif(ch == 'f'): return "1111"

        
def Hex_to_Bin(str):
    output = ""
    for count in range(0,len(str),1):
        output += binary(str[count])
    return output

def TextToBin_Chinese(str):
    return Hex_to_Bin(Unicode_to_Hex(Chinese_to_Unicode(str)))

def main():
    print(TextToBin_Chinese(input("Please input the text:\n")))

main()