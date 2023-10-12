import math

def areatri(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s*(s - a)*(s - b)*(s - c))

    return area

def sidesum(a, b, c):
    
    if((a + b) > c):
        return "a + b > c"

    if ((a + c) > b):
        return "a + c > b"

    if((c + b) > a):
        return "c + b > a"

    return "sum of two side is not greater then third"



a = areatri(10, 20, 30)
b = sidesum(10, 20, 30)
print(a)
print(b)
