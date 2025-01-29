def add(a, b):
    return a+b

def sub(a,b):
    return a-b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def mod(a, b):
    return a % b

def exp(a, b):
    return a ** b

def floor_div(a, b):
    if b != 0:
        return a // b
    else:
        return "Cannot divide by zero"

def abs_val(a):
    return abs(a)

def neg(a):
    return -a

print(add(5,10))
print(sub(10,3))
print(mul(4, 6))
print(mul(5,7))
print(div(10, 2))
print(div(10, 0))
print(mod(7, 3))
print(exp(2, 3))
print(floor_div(7, 3))
print(floor_div(7, 0))
print(abs_val(-5))
print(neg(5))