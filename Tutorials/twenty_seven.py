x = 9000
def test():
    x = 9000
test()
print(x)


x = 9000
def test():
    global x
    x = 9000
test()
print(x)


x = [9000]
def test():
    x = [9000]
test()
print(x)


x = [9000]
def test():
    global x
    x = [9000]
test()
print(x)


x = [1]
def test():
    x[0] = 2
test()
print(x)