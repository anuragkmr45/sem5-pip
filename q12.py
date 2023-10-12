def checkasc(a, b, c):
    if(a < b < c):
        return True
    return False;

def checkdesc(a, b, c):
    if(a > b > c):
        return True
    return False

def main():

    
    if(checkasc(1,44,3) == True):
        return "asc"
    if(checkdesc(1,44,3) == True):
        return "desc"

    return "something wrong"

print(main())
