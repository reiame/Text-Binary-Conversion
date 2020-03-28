def hex(num):
    if(0 <= num < 10):
        return str(num)
    elif(num == 10): return 'a'
    elif(num == 11): return 'b'
    elif(num == 12): return 'c'
    elif(num == 13): return 'd'
    elif(num == 14): return 'e'
    elif(num == 15): return 'f'

def Bin_to_Hex(str):
    output = ""
    for count in range(0,len(str),4):
        output += hex(int(str[count])*8 + int(str[count+1])*4+int(str[count+2])*2+int(str[count+3]))
    return output

def Hex_to_Unicode(str):
    output =""
    for count in range(0,len(str),4):
        output += "\\u"
        for inner in range(0,4,1):
            output += str[count + inner]
    return output

def Unicode_to_Chinese(a):
    output = a.encode('utf-8').decode('unicode_escape')
    return output

def main():
    a = input("Please input the text:\n")
    print(Unicode_to_Chinese(Hex_to_Unicode(Bin_to_Hex(a))))

main()