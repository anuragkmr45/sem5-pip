def grossalary(salary):
    a = salary * (4/10)
    b = salary * (2/10)

    return salary - (a + b)

ans = grossalary(100000)
print("grocess salary : ",ans)
