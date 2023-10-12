def daynmonth(day, month):
    if(day == 20 and month > 3 and month < 6):
        return True
    return False

day = int(input("Enter day : "))
month = int(input(" Enter month :  "))

ans = daynmonth(day, month)

print(ans)
        
