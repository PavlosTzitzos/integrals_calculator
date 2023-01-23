# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 19:13:56 2021

@author: user
"""

from sympy import *
from sympy import symbols
from sympy import integrate
from sympy import Integral
from sympy import pprint
from sympy import cos
from sympy import sin
from sympy import latex
from sympy.parsing.sympy_parser import parse_expr
"""
function [I] = DoubleIntegrals(f,x1,x2,y1,y2,pc)
# 
# f = f(x,y)
# x1 <= x <= x2
# y1 <= y <= y2
# pc = 1, for polar coordinates
# pc = 0, for cartesian -//-
# 
# I = Integral result
# 
"""
def sym_compare(a,b):
    d = a-b
    if d.is_positive:
        return 1
    elif d.is_negative:
        return -1
    else:
        return 0
    

def inputs_request(obj_to_check, out_str):
    obj_to_check = symbols('obj_to_check')
    T = obj_to_check.expr_free_symbols
    if T:
        a = 1
    else:
        a = 0
        
    while(obj_to_check.is_number==0 and a==0):
        #Check if f is symbolic
        #Not symbolic
        print("Type ""exit"" to exit imidiately.")
        obj_to_check=input(out_str + " again: ")
        if (obj_to_check=="exit"):
            break
        #end
    #end
    

def inputs_call():
    f = parse_expr(input("Give the function f(x,y): "))
    #f = inputs_request(f,"Give the function f(x,y)")
    x1 = parse_expr(input("Give x1: "))
    #x1 = inputs_request(f,"Give x1")
    x2 = parse_expr(input("Give x2: "))
    #x2 = inputs_request(f,"Give x2")
    y1 = parse_expr(input("Give y1: "))
    #y1 = inputs_request(f,"Give y1")
    y2 = parse_expr(input("Give y2: "))
    #y2 = inputs_request(f,"Give y2")
    pc = parse_expr(input("Do you want polar coordinates? Type 1 for yes or 0 for no. "))
    return f, x1, x2, y1, y2, pc
#end

def swap_values(a,b):
    temp = a
    a = b
    b = temp
    return a, b
#end

def warning_one(a,b):
    
    if sym_compare(a,b) ==1:
        print("\nWarning! \n\n Inverting Inputs ... \n\n")
        a,b = swap_values(a,b)
    #end
    return a,b


#main
x, y, r, theta = symbols('x y r theta') #.....?????.....solve at home (1)
x1, x2, y1, y2 = symbols('x1 x2 y1 y2')

f,x1,x2,y1,y2,pc = inputs_call()

#Input Arguments:
# function f(x,y)
# x1 <= x <= x2 , y1 <= y <= y2
print("Calculating Double Integral ... \n")
if (x1.is_number==1 and x2.is_number==1 and y1.is_number==1 and y2.is_number==1 and pc==0):
    x1,x2 = warning_one(x1,x2)
    y1,y2 = warning_one(y1,y2)
    #1.
    #Simple x and y
    I1 = integrate(f,(x,x1,x2))
    I = integrate(I1,(y,y1,y2))
    print("D is Simple x and y.\n")
    print("\nFirst integral is: ")
    pprint(latex(Integral(f,(x,x1,x2))))
    print("\nwhich gives: ")
    pprint(I1)
    print("\nSecond integral is: ")
    pprint(Integral(I1,(y,y1,y2)))
    print("\nwhich gives: ")
    pprint(I)
    #I = integral(integral(f,y1,y2),x1,x2)
    #display result...
elif((x1.is_number==0 or x2.is_number==0) and y1.is_number==1 and y2.is_number==1 and pc==0):
    y1,y2 = warning_one(y1,y2)
    #2.
    #Simple x
    #display result...
    I1 = integrate(f,(x,x1,x2))
    I = integrate(I1,(y,y1,y2))
    print("D is Simple x.\n")
    print("\nFirst integral is: ")
    pprint(Integral(f,(x,x1,x2)))
    print("\nwhich gives: ")
    pprint(I1)
    print("\nSecond integral is: ")
    pprint(Integral(I1,(y,y1,y2)))
    print("\nwhich gives: ")
    pprint(I)
elif(pc==0):
    x1,x2 = warning_one(x1,x2)
    #3.
    #Simple y
    #display result...
    I1 = integrate(f,(y,y1,y2))
    I = integrate(I1,(x,x1,x2))
    print("D is Simple y.\n")
    print("\nFirst integral is: ")
    pprint(Integral(f,(y,y1,y2)))
    print("\nwhich gives: ")
    pprint(I1)
    print("\nSecond integral is: ")
    pprint(Integral(I1,(x,x1,x2)))
    print("\nwhich gives: ")
    pprint(I)
elif(pc==1):
    r1 = parse_expr(input("Give r1: "))
    r2 = parse_expr(input("Give r2: "))
    theta1 = parse_expr(input("Give theta1: "))
    theta2 = parse_expr(input("Give theta2: "))
    fp = f.subs([x, r*cos(theta)],[y, r*sin(theta)])
    I1 = integrate(fp*r,(r,r1,r2))
    I = integrate(I1,(theta,theta1,theta2))
    print("")
    print("Change of variables, using polar coordinates.\n")
    print("Replace x with r*cos(theta) and y with r*sin(theta):")
    pprint(fp)
    print("\nIntegrate with respect to r variable first and then theta.\n")
    print("\nFirst integral is: ")
    pprint(Integral(fp*r,(r,r1,r2)))
    print("\nwhich gives: ")
    pprint(I1)
    print("\nSecond integral is: ")
    pprint(Integral(I1,(theta,theta1,theta2)))
    print("\nwhich gives: ")
    pprint(I)
#end
