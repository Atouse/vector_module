import numpy as np
import sympy

def dot_product(a,b):
    a = np.array(a)
    b = np.array(b)
    return a.dot(b)

def multiply(a, b):
    a = np.array(a)
    b = np.array(b)
    return a*b

def addition(a, b):
    a = np.array(a)
    b = np.array(b)
    return a+b

def subtraction(a, b):
    a = np.array(a)
    b = np.array(b)
    return a-b

def is_orthogonal(a, b): #format vector parameters as a list ([1,2], [2,-1])
    a = np.array(a)
    b = np.array(b)
    if(a.dot(b) == 0):
        return True
    return False

def ortho_proj(a,b): #orthogonal projection of b onto a
    a = np.array(a)
    b = np.array(b)

    numerator = a.dot(b)
    denominator = a.dot(a)

    proj = (numerator/denominator)*a
    output = []
    for i in range(0,len(proj)):
        output.append (str(Fraction(proj[i]).limit_denominator()))
    return output

a = [1,2]
b = [2,1]

print(ortho_proj(a,b))
