def say(msg, time = 2):
    print(msg*time)

say('hello')
say('world', 5)


def fun(a = 2, b = 3, c = 7):
    d = a + b
    print(d)

print(fun(2))
