def UppsrCase(a):
    return a.upper()

def checkLower(a):
    return a.islower()

def main():
    a = input("Enter string : ")
    if(checkLower(a) == True):
        return a.upper()

    return "in upper case"

print(main())
    
