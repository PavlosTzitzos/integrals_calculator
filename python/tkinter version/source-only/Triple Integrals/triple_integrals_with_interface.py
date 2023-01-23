# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 19:09:19 2022

@author: user
"""

from sympy import *
from sympy import symbols
from sympy import integrate
from sympy import Integral
from sympy import sin
from sympy import cos
from sympy import pprint
from sympy.parsing.sympy_parser import parse_expr
from tkinter import *
from tkinter import Label
from tkinter import Button
from tkinter import Entry
import tkinter
import tkinter as tk
from sympy import latex
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')

global cs

"""
function [I] = TripleIntegrals(f,x1,x2,y1,y2,z1,z2,c)
# 
# f = f(x,y)
# c = coordinates
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
    

def swap_values(a,b):
    temp = a
    a = b
    b = temp
    return a, b
#end

def warning_one(a,b):
    
    if sym_compare(a,b) ==1:
        Label(window,text="Warning! Inverting Inputs ...").place(x=400,y=0)
        a,b = swap_values(a,b)
    else:
        Label(window,text="No errors detected").place(x=400,y=0)
    return a,b

def graph_latex(str_a,str_b,str_f,str_var,csx,csy):
    #this function is being used only for the standalone version for triple integrals
    if str_var =="0":
        label = tk.Label(window).place(x=csx,y=csy)
        fig = matplotlib.figure.Figure(figsize=(6, 1), dpi=50)
        ax = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master=label)
        canvas.get_tk_widget().place(x=csx,y=csy)
        canvas._tkcanvas.place(x=csx,y=csy)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        tmptext ="${ "+str_f+" }$"
        ax.clear()
        ax.text(0, 0.3, tmptext, fontsize=20)
        canvas.draw()
    else:
        label = tk.Label(window).place(x=csx,y=csy)
        fig = matplotlib.figure.Figure(figsize=(6, 1),dpi=50)
        ax = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master=label)
        canvas.get_tk_widget().place(x=csx,y=csy)
        canvas._tkcanvas.place(x=csx,y=csy)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        tmptext ="$\int_{ "+str_a+" } ^{ "+str_b+" } "+str_f+" d"+str_var+"$"
        ax.clear()
        ax.text(0, 0.3, tmptext, fontsize=20)
        canvas.draw()
    #end
#end

def my_has_sym(B):
    A,x,y,z = symbols('A x y z')
    A = parse_expr(B)
    if A.is_Number == 0:
        T1 = A.has(x)
        T2 = A.has(y)
        T3 = A.has(z)
        
        if (T1==1 and T2==1 and T3==1):
            O = -1
            #A has x,y,z
        elif (T1==1 and T2==1 and T3==0):
            O = 12
            #A does not have z but has x,y
        elif (T1==1 and T2==0 and T3==1):
            O = 13
            #A does not have y but has x,z
        elif (T1==0 and T2==1 and T3==1):
            O = 23
            #A does not have x but has y,z
        elif (T1==1 and T2==0 and T3==0):
            O = 1
            #A does not have y,z but has x
        elif (T1==0 and T2==1 and T3==0):
            O = 2
            #A does not have x,z but has y
        elif (T1==0 and T2==0 and T3==1):
            O = 3
            #A does not have x,y but has z
        elif (T1==0 and T2==0 and T3==0):
            O = 0
            #A does not have x,y,z
        else:
            Label(window,text="Error! Something whent wrong!").place(x=0,y=0)
            O = 'NaN'
            #Any other case will return NaN to indicate that it is not possible to calculate
        #end
    elif A.is_Number==1:
        O = 0;
        #is a number
    #end
    return O

def checker(A):
    #this function is no longer being used
    #output: [c,p]
    c = [0,0,0,0,0]
    p = [0,0,0,0,0,0]
    for i in range(0,6,1):
        if A[i] == 1:
            c[0] = c[0] + 1
            p[i] = 0
        elif (A[i] - 0.5) == 0:
            c[1]= c[1] + 1
            p[i] = 0
        elif A[i] == 0:
            c[2] = c[2] + 1
            p[i] = 1
        elif (A[i] + 0.5) == 0:
            c[3] = c[3] + 1
            p[i] = 0
        elif (A[i]+1)==0:
            c[4] = c[4] + 1
            p[i] = 1
        else:
            Label(window,text="ERROR").place(x=1,y=1)
        #end
    #end
    return c,p
#end

def ti_cc_main_func(fnct,xa,xb,yc,yd,ze,zf):
    x, y, z = symbols('x y z')
    x1, x2, y1, y2, z1, z2 = symbols('x1 x2 y1 y2 z1 z2')
    f=parse_expr(fnct)
    x1=parse_expr(xa)
    x2=parse_expr(xb)
    y1=parse_expr(yc)
    y2=parse_expr(yd)
    z1=parse_expr(ze)
    z2=parse_expr(zf)
    #Input Arguments:
    # function f(x,y,z)
    # x1 <= x <= x2 , y1 <= y <= y2 , z1 <= z <= z2
    T = [0,1,2,3,4,5]
    T[0] = my_has_sym(str(x1))
    T[1] = my_has_sym(str(x2))
    T[2] = my_has_sym(str(y1))
    T[3] = my_has_sym(str(y2))
    T[4] = my_has_sym(str(z1))
    T[5] = my_has_sym(str(z2))
    #print(T)
    #csx=460
    #csy=20
    #Label(window, text="Calculating Triple Integral ...").place(x=csx,y=csy)
    a = -1 in T
    b = T[0]==1 or T[1]==1 or T[2]==2 or T[3]==2 or T[4]==3 or T[5]==3 or T[0] == 12 or T[1]==12 or T[0]==13 or T[1]==13 or T[2]==12 or T[2]==23 or T[3]==12 or T[3]==23 or T[4]==13 or T[4]==23 or T[5]==13 or T[5]==23
    if b==False and a==False:
        #print("ok")
        c1 = 12 in T and 13 not in T and 23 not in T
        c2 = 13 in T and 12 not in T and 23 not in T
        c3 = 23 in T and 12 not in T and 13 not in T
        c4 = 12 not in T and 13 not in T and 23 not in T
        if c1 == True or c2 == True or c3 == True:
            #print("case 1")
            if T[4] == 12 or T[5] == 12:
                #print("z1(x,y) and/or z2(x,y)")
                if T[2] == 3 or T[3] == 3 or T[0] == 3 or T[1] == 3:
                    #print("wrong input")
                    I1 = 0
                    I2 = 0
                    I3 = 0
                    g = ""
                else:
                    #print("ok")
                    if (T[0] == 2 or T[1] == 2) and (T[2] == 0 and T[3] == 0):
                        #print("x1(y) and/or x2(y) and y1 and y2 : const")
                        g = "dz dx dy"
                        I1 = integrate(f,(z,z1,z2))
                        I2 = integrate(I1,(x,x1,x2))
                        I3 = integrate(I2,(y,y1,y2))
                    elif (T[2] == 1 or T[3] == 1) and (T[0] == 0 and T[1] == 0):
                        #print("y1(x) and/or y2(x) and x1 and x2 : const")
                        g = "dz dy dx"
                        I1 = integrate(f,(z,z1,z2))
                        I2 = integrate(I1,(y,y1,y2))
                        I3 = integrate(I2,(x,x1,x2))
                    elif (T[0] == 0 and T[1] == 0 and T[2] == 0 and T[3] == 0):
                        #print("dz dx dy or dz dy dx")
                        g = "dz dx dy"
                        I1 = integrate(f,(z,z1,z2))
                        I2 = integrate(I1,(x,x1,x2))
                        I3 = integrate(I2,(y,y1,y2))
                    else:
                        #print("cannot calculate")
                        I1 = 0
                        I2 = 0
                        I3 = 0
                        g=""
            elif T[2] == 13 or T[3] == 13:
                #print("y1(x,z) and/or y2(x,z)")
                if T[4] == 2 or T[5] == 2 or T[0] == 2 or T[1] == 2:
                    #print("wrong input")
                    I1 = 0
                    I2 = 0
                    I3 = 0
                    g=""
                else:
                    #print("ok")
                    if (T[0] == 3 or T[1] == 3) and (T[4] == 0 and T[5] == 0):
                        #print("x1(z) and/or x2(z) and z1 and z2 : const")
                        g ="dy dx dz"
                        I1 = integrate(f,(y,y1,y2))
                        I2 = integrate(I1,(x,x1,x2))
                        I3 = integrate(I2,(z,z1,z2))
                    elif (T[4] == 1 or T[5] == 1) and (T[0] == 0 and T[1] == 0):
                        #print("z1(x) and/or z2(x) and x1 and x2 : const")
                        g = "dy dz dx"
                        I1 = integrate(f,(y,y1,y2))
                        I2 = integrate(I1,(z,z1,z2))
                        I3 = integrate(I2,(x,x1,x2))
                    elif (T[0] == 0 and T[1] == 0 and T[4] == 0 and T[5] == 0):
                        g = "dy dz dx"
                        I1 = integrate(f,(y,y1,y2))
                        I2 = integrate(I1,(z,z1,z2))
                        I3 = integrate(I2,(x,x1,x2))
                    else:
                        #print("cannot calculate")
                        I1 = 0
                        I2 = 0
                        I3 = 0
                        g=""
            elif T[0] == 23 or T[1] == 23:
                #print("x1(y,z) and/or x2(y,z)")
                if T[2] == 1 or T[3] == 1 or T[4] == 1 or T[5] == 1:
                    #print("wrong input")
                    I1 = 0
                    I2 = 0
                    I3 = 0
                    g=""
                else:
                    #print("ok")
                    if (T[2] == 3 or T[3] == 3) and (T[4] == 0 and T[5] == 0):
                        #print("y1(z) and/or y2(z) and z1 and z2 : const")
                        g = "dx dy dz"
                        I1 = integrate(f,(x,x1,x2))
                        I2 = integrate(I1,(y,y1,y2))
                        I3 = integrate(I2,(z,z1,z2))
                    elif (T[4] == 2 or T[5] == 2) and (T[2] == 0 and T[3] == 0):
                        #print("z1(y) and/or z2(y) and y1 and y2 : const")
                        g = "dx dz dy"
                        I1 = integrate(f,(x,x1,x2))
                        I2 = integrate(I1,(z,z1,z2))
                        I3 = integrate(I2,(y,y1,y2))
                    elif (T[2] == 0 and T[3] == 0 and T[4] == 0 and T[5] == 0):
                        g = "dx dy dz"
                        I1 = integrate(f,(x,x1,x2))
                        I2 = integrate(I1,(y,y1,y2))
                        I3 = integrate(I2,(z,z1,z2))
                    else:
                        #print("cannot calculate")
                        I1 = 0
                        I2 = 0
                        I3 = 0
                        g = ""
        elif c4 == True:
            #print("case 2")
            d1 = (T[0] == 2 or T[1] == 2) and (T[2] == 1 or T[3] == 1)
            d2 = (T[0] == 3 or T[1] == 3) and (T[4] == 1 or T[5] == 1)
            d3 = (T[2] == 3 or T[3] == 2) and (T[4] == 2 or T[5] == 2)
            if d1 == True or d2 == True or d3 == True:
                #print("wrong input")
                I1 = 0
                I2 = 0
                I3 = 0
                g = ""
            else:
                #print("ok ...")
                e1 = T[0]==0 and T[1]==0 and T[2]==0 and T[3]==0
                e2 = T[0]==0 and T[1]==0 and T[4]==0 and T[5]==0
                e3 = T[2]==0 and T[3]==0 and T[4]==0 and T[5]==0
                if e1 == True:
                    #print("x1,x2,y1,y2 : const")
                    g = "dz dx dy"
                    I1 = integrate(f,(z,z1,z2))
                    I2 = integrate(I1,(x,x1,x2))
                    I3 = integrate(I2,(y,y1,y2))
                elif e2 == True:
                    #print("x1,x2,z1,z2 : const")
                    g = "dy dx dz"
                    I1 = integrate(f,(y,y1,y2))
                    I2 = integrate(I1,(x,x1,x2))
                    I3 = integrate(I2,(z,z1,z2))
                elif e3 == True:
                    #print("y1,y2,z1,z2 : const")
                    g = "dx dy dz"
                    I1 = integrate(f,(x,x1,x2))
                    I2 = integrate(I1,(y,y1,y2))
                    I3 = integrate(I2,(z,z1,z2))
                else:
                    if T[0]==0 and T[1]==0:
                        #print("x1 and x2 : const")
                        if T[2]==3 or T[3]==3:
                            #print("y1(z) and/or y2(z)")
                            g = "dy dz dx"
                            I1 = integrate(f,(y,y1,y2))
                            I2 = integrate(I1,(z,z1,z2))
                            I3 = integrate(I2,(x,x1,x2))
                        elif (T[2]==1 or T[3]==1) and T[2]!=3 and T[3]!=3:
                            #print("y1(x) and/or y2(x)")
                            g = "dz dy dx"
                            I1 = integrate(f,(z,z1,z2))
                            I2 = integrate(I1,(y,y1,y2))
                            I3 = integrate(I2,(x,x1,x2))
                        elif T[4]==2 or T[5]==2:
                            #print("z1(y) and/or z2(y)")
                            g = "dz dy dx"
                            I1 = integrate(f,(z,z1,z2))
                            I2 = integrate(I1,(y,y1,y2))
                            I3 = integrate(I2,(x,x1,x2))
                        elif (T[4]==1 or T[5]==1) and T[2]!=2 and T[3]!=2:
                            #print("z1(x) and/or z2(x)")
                            g = "dy dz dx"
                            I1 = integrate(f,(y,y1,y2))
                            I2 = integrate(I1,(z,z1,z2))
                            I3 = integrate(I2,(x,x1,x2))
                        else:
                            #print("??? 1")
                            I1 = 0
                            I2 = 0
                            I3 = 0
                            g = ""
                    elif T[2]==0 and T[3]==0:
                        #print("y1 and y2 : const")
                        if T[0]==3 or T[1]==3:
                            #print("x1(z) and/or x2(z)")
                            g ="dx dz dy"
                            I1 = integrate(f,(x,x1,x2))
                            I2 = integrate(I1,(z,z1,z2))
                            I3 = integrate(I2,(y,y1,y2))
                        elif (T[0]==2 or T[1]==2) and T[0]!=3 and T[1]!=3:
                            #print("x1(y) and/or x2(y)")
                            g ="dz dx dy"
                            I1 = integrate(f,(z,z1,z2))
                            I2 = integrate(I1,(x,x1,x2))
                            I3 = integrate(I2,(y,y1,y2))
                        elif T[4]==1 or T[5]==1:
                            #print("z1(x) and/or z2(x)")
                            g = "dz dx dy"
                            I1 = integrate(f,(z,z1,z2))
                            I2 = integrate(I1,(x,x1,x2))
                            I3 = integrate(I2,(y,y1,y2))
                        elif (T[4]==2 or T[5]==2) and T[2]!=1 and T[3]!=1:
                            #print("z1(y) and/or z2(y)")
                            g = "dx dz dy"
                            I1 = integrate(f,(x,x1,x2))
                            I2 = integrate(I1,(z,z1,z2))
                            I3 = integrate(I2,(y,y1,y2))
                        else:
                            #print("??? 2")
                            I1 = 0
                            I2 = 0
                            I3 = 0
                            g = ""
                    elif T[4]==0 and T[5]==0:
                        #print("z1 and z2 : const")
                        if T[0]==2 or T[1]==2:
                            #print("x1(y) and/or x2(y)")
                            g = "dx dy dz"
                            I1 = integrate(f,(x,x1,x2))
                            I2 = integrate(I1,(y,y1,y2))
                            I3 = integrate(I2,(z,z1,z2))
                        elif (T[0]==3 or T[1]==3) and T[0]!=2 and T[1]!=2:
                            #print("x1(z) and/or x2(z)")
                            g = "dy dx dz"
                            I1= integrate(f,(y,y1,y2))
                            I2 = integrate(I1,(x,x1,x2))
                            I3 = integrate(I2,(z,z1,z2))
                        elif T[2]==1 or T[3]==1:
                            #print("y1(x) and/or y2(x)")
                            g = "dy dx dz"
                            I1= integrate(f,(y,y1,y2))
                            I2 = integrate(I1,(x,x1,x2))
                            I3 = integrate(I2,(z,z1,z2))
                        elif (T[2]==3 or T[3]==3) and T[2]!=1 and T[3]!=1:
                            #print("y1(z) and/or y2(z)")
                            g = "dx dy dz"
                            I1= integrate(f,(x,x1,x2))
                            I2 = integrate(I1,(y,y1,y2))
                            I3 = integrate(I2,(z,z1,z2))
                        else:
                            #print("??? 3")
                            I1 = 0
                            I2 = 0
                            I3 = 0
                            g = ""
                    else:
                        #print("wrong input")
                        I1=0
                        I2=0
                        I3=0
                        g = ""
    else:
         #print("not ok")
         I1=0
         I2=0
         I3=0
         g = ""  
    #print(I1)
    #print(I2)
    #print(I3)
    if g =="dx dy dz":
        #Label(window, text="A is Simple z.").place(x=csx,y=csy+30)
        mathtext_demos = {
            "Header demo":
                r"$You~entered: \int ^{"+latex(z2)+"} _{"+latex(z1)+"} \int ^{"+latex(y2)+"} _{"+latex(y1)+"} \int ^{"+latex(x2)+"} _{"+latex(x1)+"} "+latex(f)+" dx dy dz$",
            "First Integral is:":
                r"$I_1 = \int^{"+latex(x2)+"} _{"+latex(x1)+"} "+latex(f)+" dx $",
            "which gives I1:":
                r"$I_1 = "+latex(I1)+"$",
            "Second Integral is: ":
                r"$I_2 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(I1)+" dy $",
            "which gives I2:":
                r"$I_2 = "+latex(I2)+"$",
            "Third Integral is:":
                r"$I_3 = \int ^{"+latex(z2)+"} _{"+latex(z1)+"} "+latex(I2)+"dz $",
            "which gives I3, the final result:":
                r"$I_3 = "+latex(I3)+"$"
        }
        """
        print("Calculating Triple Integral ...")
        print("A is simple x space.")
        print("First Integral is:")
        pprint(Integral(f,(x,x1,x2)))
        print("which gives:")
        pprint(I1)
        print("D is simple y.")
        print("Second Integral is:")
        pprint(Integral(I1,(y,y1,y2)))
        print("which gives:")
        pprint(I2)
        print("Third integral is:")
        pprint(Integral(I2,(z,z1,z2)))
        print("which gives the final result:")
        pprint(I3)
        """
        """
        Label(window, text="First integral is:").place(x=csx,y=csy+50)
        graph_latex(latex(x1),latex(x2),latex(f),"x",csx,csy+80)
        Label(window, text="which gives:").place(x=csx,y=csy+130)
        graph_latex("0","0",latex(I1),"0",csx,csy+150)
        Label(window, text="Second integral is:").place(x=csx,y=csy+200)
        graph_latex(latex(y1),latex(y2),latex(I1),"y",csx,csy+220)
        Label(window, text="which gives:").place(x=csx,y=csy+270)
        graph_latex("0","0",latex(I2),"0",csx,csy+290)
        Label(window, text="Third integral is:").place(x=csx,y=csy+340)
        graph_latex(latex(z1),latex(z2),latex(I2),"z",csx,csy+360)
        Label(window, text="which gives:").place(x=csx,y=csy+420)
        graph_latex("0","0",latex(I3),"0",csx,csy+450)
        """
    elif g =="dx dz dy":
        mathtext_demos = {
            "Header demo":
                r"$You~entered: \int ^{"+latex(y2)+"} _{"+latex(y1)+"} \int ^{"+latex(z2)+"} _{"+latex(z1)+"} \int ^{"+latex(x2)+"} _{"+latex(x1)+"} "+latex(f)+" dx dz dy$",
            "First Integral is:":
                r"$I_1 = \int^{"+latex(x2)+"} _{"+latex(x1)+"} "+latex(f)+" dx $",
            "which gives I1:":
                r"$I_1 = "+latex(I1)+"$",
            "Second Integral is: ":
                r"$I_2 = \int^{"+latex(z2)+"}_{"+latex(z1)+"} "+latex(I1)+" dz $",
            "which gives I2:":
                r"$I_2 = "+latex(I2)+"$",
            "Third Integral is:":
                r"$I_3 = \int ^{"+latex(y2)+"} _{"+latex(y1)+"} "+latex(I2)+"dy $",
            "which gives I3, the final result:":
                r"$I_3 = "+latex(I3)+"$"
        }
        """
        print("Calculating Triple Integral ...")
        print("A is simple x space.")
        print("First Integral is:")
        pprint(Integral(f,(x,x1,x2)))
        print("which gives:")
        pprint(I1)
        print("D is simple z.")
        print("Second Integral is:")
        pprint(Integral(I1,(z,z1,z2)))
        print("which gives:")
        pprint(I2)
        print("Third integral is:")
        pprint(Integral(I2,(y,y1,y2)))
        print("which gives the final result:")
        pprint(I3)
        """
        """
        Label(window, text="First integral is:").place(x=csx,y=csy+50)
        graph_latex(latex(x1),latex(x2),latex(f),"x",csx,csy+80)
        Label(window, text="which gives:").place(x=csx,y=csy+130)
        graph_latex("0","0",latex(I1),"0",csx,csy+150)
        Label(window, text="Second integral is:").place(x=csx,y=csy+200)
        graph_latex(latex(z1),latex(z2),latex(I1),"z",csx,csy+220)
        Label(window, text="which gives:").place(x=csx,y=csy+270)
        graph_latex("0","0",latex(I2),"0",csx,csy+290)
        Label(window, text="Third integral is:").place(x=csx,y=csy+340)
        graph_latex(latex(y1),latex(y2),latex(I2),"y",csx,csy+360)
        Label(window, text="which gives:").place(x=csx,y=csy+420)
        graph_latex("0","0",latex(I3),"0",csx,csy+450)
        """
    elif g =="dy dx dz":
        mathtext_demos = {
            "Header demo":
                r"$You~entered: \int ^{"+latex(z2)+"} _{"+latex(z1)+"} \int ^{"+latex(x2)+"} _{"+latex(x1)+"} \int ^{"+latex(y2)+"} _{"+latex(y1)+"} "+latex(f)+" dy dx dz$",
            "First Integral is:":
                r"$I_1 = \int^{"+latex(y2)+"} _{"+latex(y1)+"} "+latex(f)+" dy $",
            "which gives I1:":
                r"$I_1 = "+latex(I1)+"$",
            "Second Integral is: ":
                r"$I_2 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(I1)+" dx $",
            "which gives I2:":
                r"$I_2 = "+latex(I2)+"$",
            "Third Integral is:":
                r"$I_3 = \int ^{"+latex(z2)+"} _{"+latex(z1)+"} "+latex(I2)+"dz $",
            "which gives I3, the final result:":
                r"$I_3 = "+latex(I3)+"$"
        }
        """
        print("Calculating Triple Integral ...")
        print("A is simple y space.")
        print("First Integral is:")
        pprint(Integral(f,(y,y1,y2)))
        print("which gives:")
        pprint(I1)
        print("D is simple x.")
        print("Second Integral is:")
        pprint(Integral(I1,(x,x1,x2)))
        print("which gives:")
        pprint(I2)
        print("Third integral is:")
        pprint(Integral(I2,(z,z1,z2)))
        print("which gives the final result:")
        pprint(I3)
        """
        """
        Label(window, text="First integral is:").place(x=csx,y=csy+50)
        graph_latex(latex(y1),latex(y2),latex(f),"y",csx,csy+80)
        Label(window, text="which gives:").place(x=csx,y=csy+130)
        graph_latex("0","0",latex(I1),"0",csx,csy+150)
        Label(window, text="Second integral is:").place(x=csx,y=csy+200)
        graph_latex(latex(x1),latex(x2),latex(I1),"x",csx,csy+220)
        Label(window, text="which gives:").place(x=csx,y=csy+270)
        graph_latex("0","0",latex(I2),"0",csx,csy+290)
        Label(window, text="Third integral is:").place(x=csx,y=csy+340)
        graph_latex(latex(z1),latex(z2),latex(I2),"z",csx,csy+360)
        Label(window, text="which gives:").place(x=csx,y=csy+420)
        graph_latex("0","0",latex(I3),"0",csx,csy+450)
        """
    elif g =="dy dz dx":
        mathtext_demos = {
            "Header demo":
                r"$You~entered: \int ^{"+latex(x2)+"} _{"+latex(x1)+"} \int ^{"+latex(z2)+"} _{"+latex(z1)+"} \int ^{"+latex(y2)+"} _{"+latex(y1)+"} "+latex(f)+" dy dz dx$",
            "First Integral is:":
                r"$I_1 = \int^{"+latex(y2)+"} _{"+latex(y1)+"} "+latex(f)+" dy $",
            "which gives I1:":
                r"$I_1 = "+latex(I1)+"$",
            "Second Integral is: ":
                r"$I_2 = \int^{"+latex(z2)+"}_{"+latex(z1)+"} "+latex(I1)+" dz $",
            "which gives I2:":
                r"$I_2 = "+latex(I2)+"$",
            "Third Integral is:":
                r"$I_3 = \int ^{"+latex(x2)+"} _{"+latex(x1)+"} "+latex(I2)+"dx $",
            "which gives I3, the final result:":
                r"$I_3 = "+latex(I3)+"$"
        }
        """
        print("Calculating Triple Integral ...")
        print("A is simple y space.")
        print("First Integral is:")
        pprint(Integral(f,(y,y1,y2)))
        print("which gives:")
        pprint(I1)
        print("D is simple z.")
        print("Second Integral is:")
        pprint(Integral(I1,(z,z1,z2)))
        print("which gives:")
        pprint(I2)
        print("Third integral is:")
        pprint(Integral(I2,(x,x1,x2)))
        print("which gives the final result:")
        pprint(I3)
        """
        """
        Label(window, text="First integral is:").place(x=csx,y=csy+50)
        graph_latex(latex(y1),latex(y2),latex(f),"y",csx,csy+80)
        Label(window, text="which gives:").place(x=csx,y=csy+130)
        graph_latex("0","0",latex(I1),"0",csx,csy+150)
        Label(window, text="Second integral is:").place(x=csx,y=csy+200)
        graph_latex(latex(z1),latex(z2),latex(I1),"z",csx,csy+220)
        Label(window, text="which gives:").place(x=csx,y=csy+270)
        graph_latex("0","0",latex(I2),"0",csx,csy+290)
        Label(window, text="Third integral is:").place(x=csx,y=csy+340)
        graph_latex(latex(x1),latex(x2),latex(I2),"x",csx,csy+360)
        Label(window, text="which gives:").place(x=csx,y=csy+420)
        graph_latex("0","0",latex(I3),"0",csx,csy+450)
        """
    elif g =="dz dx dy":
        mathtext_demos = {
            "Header demo":
                r"$You~entered: \int ^{"+latex(y2)+"} _{"+latex(y1)+"} \int ^{"+latex(x2)+"} _{"+latex(x1)+"} \int ^{"+latex(z2)+"} _{"+latex(z1)+"} "+latex(f)+" dz dx dy$",
            "First Integral is:":
                r"$I_1 = \int^{"+latex(z2)+"} _{"+latex(z1)+"} "+latex(f)+" dz $",
            "which gives I1:":
                r"$I_1 = "+latex(I1)+"$",
            "Second Integral is: ":
                r"$I_2 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(I1)+" dx $",
            "which gives I2:":
                r"$I_2 = "+latex(I2)+"$",
            "Third Integral is:":
                r"$I_3 = \int ^{"+latex(y2)+"} _{"+latex(y1)+"} "+latex(I2)+"dy $",
            "which gives I3, the final result:":
                r"$I_3 = "+latex(I3)+"$"
        }
        """
        print("Calculating Triple Integral ...")
        print("A is simple z space.")
        print("First Integral is:")
        pprint(Integral(f,(z,z1,z2)))
        print("which gives:")
        pprint(I1)
        print("D is simple x.")
        print("Second Integral is:")
        pprint(Integral(I1,(x,x1,x2)))
        print("which gives:")
        pprint(I2)
        print("Third integral is:")
        pprint(Integral(I2,(y,y1,y2)))
        print("which gives the final result:")
        pprint(I3)
        """
        """
        Label(window, text="First integral is:").place(x=csx,y=csy+50)
        graph_latex(latex(z1),latex(z2),latex(f),"z",csx,csy+80)
        Label(window, text="which gives:").place(x=csx,y=csy+130)
        graph_latex("0","0",latex(I1),"0",csx,csy+150)
        Label(window, text="Second integral is:").place(x=csx,y=csy+200)
        graph_latex(latex(x1),latex(x2),latex(I1),"x",csx,csy+220)
        Label(window, text="which gives:").place(x=csx,y=csy+270)
        graph_latex("0","0",latex(I2),"0",csx,csy+290)
        Label(window, text="Third integral is:").place(x=csx,y=csy+340)
        graph_latex(latex(y1),latex(y2),latex(I2),"y",csx,csy+360)
        Label(window, text="which gives:").place(x=csx,y=csy+420)
        graph_latex("0","0",latex(I3),"0",csx,csy+450)
        """
    elif g =="dz dy dx":
        mathtext_demos = {
            "Header demo":
                r"$You~entered: \int ^{"+latex(x2)+"} _{"+latex(x1)+"} \int ^{"+latex(y2)+"} _{"+latex(y1)+"} \int ^{"+latex(z2)+"} _{"+latex(z1)+"} "+latex(f)+" dz dy dx$",
            "First Integral is:":
                r"$I_1 = \int^{"+latex(z2)+"} _{"+latex(z1)+"} "+latex(f)+" dz $",
            "which gives I1:":
                r"$I_1 = "+latex(I1)+"$",
            "Second Integral is: ":
                r"$I_2 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(I1)+" dy $",
            "which gives I2:":
                r"$I_2 = "+latex(I2)+"$",
            "Third Integral is:":
                r"$I_3 = \int ^{"+latex(x2)+"} _{"+latex(x1)+"} "+latex(I2)+"dx $",
            "which gives I3, the final result:":
                r"$I_3 = "+latex(I3)+"$"
        }
        """
        print("Calculating Triple Integral ...")
        print("A is simple z space.")
        print("First Integral is:")
        pprint(Integral(f,(z,z1,z2)))
        print("which gives:")
        pprint(I1)
        print("D is simple y.")
        print("Second Integral is:")
        pprint(Integral(I1,(y,y1,y2)))
        print("which gives:")
        pprint(I2)
        print("Third integral is:")
        pprint(Integral(I2,(x,x1,x2)))
        print("which gives the final result:")
        pprint(I3)
        """
        """
        Label(window, text="First integral is:").place(x=csx,y=csy+50)
        graph_latex(latex(z1),latex(z2),latex(f),"z",csx,csy+80)
        Label(window, text="which gives:").place(x=csx,y=csy+130)
        graph_latex("0","0",latex(I1),"0",csx,csy+150)
        Label(window, text="Second integral is:").place(x=csx,y=csy+200)
        graph_latex(latex(y1),latex(y2),latex(I1),"y",csx,csy+220)
        Label(window, text="which gives:").place(x=csx,y=csy+270)
        graph_latex("0","0",latex(I2),"0",csx,csy+290)
        Label(window, text="Third integral is:").place(x=csx,y=csy+340)
        graph_latex(latex(x1),latex(x2),latex(I2),"x",csx,csy+360)
        Label(window, text="which gives:").place(x=csx,y=csy+420)
        graph_latex("0","0",latex(I3),"0",csx,csy+450)
        """
    else:
        mathtext_demos = {
            "Header demo":
                r"$ Wrong Input !! $",
        }
        #print("Wrong Input !!")
        #Label(window, text="Wrong Input").place(x=csx,y=csy+50)
    n_lines = len(mathtext_demos)
    # Colors used in Matplotlib online documentation.
    mpl_grey_rgb = (51 / 255, 51 / 255, 51 / 255)

    # Creating figure and axis.
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.90],
                      facecolor="white", frameon=False)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Calculating Triple Integral ...",
                 color=mpl_grey_rgb, fontsize=14, weight='bold')
    ax.set_xticks([])
    ax.set_yticks([])

    # Gap between lines in axes coords
    line_axesfrac = 1 / n_lines

    # Plot header demonstration formula.
    full_demo = mathtext_demos['Header demo']
    ax.annotate(full_demo,
                xy=(0.5, 1. - 0.59 * line_axesfrac),
                color='tab:grey', ha='center', fontsize=20)

    # Plot feature demonstration formulae.
    for i_line, (title, demo) in enumerate(mathtext_demos.items()):
        #print(i_line, demo)
        if i_line == 0:
            continue

        baseline = 1 - i_line * line_axesfrac
        baseline_next = baseline - line_axesfrac
        fill_color = ['white', 'tab:blue'][i_line % 2]
        ax.fill_between([0, 1], [baseline, baseline],
                        [baseline_next, baseline_next],
                        color=fill_color, alpha=0.2)
        ax.annotate(f'{title}',
                    xy=(0.06, baseline - 0.3 * line_axesfrac),
                    color=mpl_grey_rgb, weight='bold')
        ax.annotate(demo,
                    xy=(0.04, baseline - 0.75 * line_axesfrac),
                    color=mpl_grey_rgb, fontsize=16)

    plt.show()
    #end
def ti_sc_main_func(fnct,rr1,rr2,t1,t2,p1,p2,c1,c2,c3):
    x, y, z, r, theta, phi = symbols('x y z r theta phi')
    x1, x2, y1, y2, z1, z2 = symbols('r1 r2 theta1 theta2 phi1 phi2')
    f=parse_expr(fnct)
    r1=parse_expr(rr1)
    r2=parse_expr(rr2)
    theta1=parse_expr(t1)
    theta2=parse_expr(t2)
    phi1=parse_expr(p1)
    phi2=parse_expr(p2)
    k1=parse_expr(c1)
    k2=parse_expr(c2)
    k3=parse_expr(c3)
    #Input Arguments:
    # function f(x,y,z)
    # r1 <= r <= r2 , theta1 <= theta <= theta2 , phi1 <= phi <= phi2
    #csx=460
    #csy=20
    #Label(window, text="Calculating Triple Integral ...").place(x=csx,y=csy)
    fp = f.subs(x, r*sin(theta)*cos(phi)+k1)
    fpp = fp.subs(y, r*sin(theta)*sin(phi)+k2)
    fppp = fpp.subs(z,r*cos(theta)+k3)
    fnew = fppp*r**2*sin(theta)
    I1 = integrate(fnew, (r, r1, r2))
    I2 = integrate(I1, (theta, theta1, theta2))
    I3 = integrate(I2, (phi, phi1, phi2))
    mathtext_demos = {
        "Header demo":
            r"$You~entered: \int ^{"+latex(phi2)+"} _{"+latex(phi1)+"} \int ^{"+latex(theta2)
            +"} _{"+latex(theta1)+"} \int ^{"+latex(r2)+"} _{"+latex(r1)+"} $"
            r"$f( x( r , $"+
            r"$ \theta , \phi ) , y( r , $"+
            r"$ \theta , \phi ) ) \cdot r^2 \cdot sin( $"+
            r"$ \theta ) dr d $"+
            r"$ \theta d $"+
            r"$\phi $",
        "Change of variables, using spherical coordinates:":
            "Replace: "+r"$x$"+" with "+r"$r \cdot sin( \theta ) \cdot cos( \phi ) + Κ_x $"
            " and: "+r"$y$"+" with "+r"$r \cdot sin( \theta ) \cdot sin( \phi ) + Κ_y $"
            " and: "+r"$z$"+" with "+r"$r \cdot cos( \theta ) + Κ_z $",
        "The new function is:":
            r"$f(r, \theta , \phi ) = "+latex(fnew)+" $",
        "First Integral is:":
            r"$I_1 = \int^{"+latex(r2)+"} _{"+latex(r1)+"} "+latex(fnew)+" dr $",
        "which gives I1:":
            r"$I_1 = "+latex(I1)+"$",
        "Second Integral is: ":
            r"$I_2 = \int^{"+latex(theta2)+"}_{"+latex(theta1)+"} "+latex(I1)+" d $"+
            r"$ \theta $",
        "which gives I2:":
            r"$I_2 = "+latex(I2)+"$",
        "Third Integral is:":
            r"$I_3 = \int ^{"+latex(phi2)+"} _{"+latex(phi1)+"} "+latex(I2)+" d"
            " \phi $",
        "which gives I3, the final result:":
            r"$I_3 = "+latex(I3)+"$"
    }
    n_lines = len(mathtext_demos)
    # Colors used in Matplotlib online documentation.
    mpl_grey_rgb = (51 / 255, 51 / 255, 51 / 255)

    # Creating figure and axis.
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.90],
                      facecolor="white", frameon=False)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Calculating Triple Integral ...",
                 color=mpl_grey_rgb, fontsize=14, weight='bold')
    ax.set_xticks([])
    ax.set_yticks([])

    # Gap between lines in axes coords
    line_axesfrac = 1 / n_lines

    # Plot header demonstration formula.
    full_demo = mathtext_demos['Header demo']
    ax.annotate(full_demo,
                xy=(0.5, 1. - 0.59 * line_axesfrac),
                color='tab:grey', ha='center', fontsize=20)

    # Plot feature demonstration formulae.
    for i_line, (title, demo) in enumerate(mathtext_demos.items()):
        #print(i_line, demo)
        if i_line == 0:
            continue

        baseline = 1 - i_line * line_axesfrac
        baseline_next = baseline - line_axesfrac
        fill_color = ['white', 'tab:blue'][i_line % 2]
        ax.fill_between([0, 1], [baseline, baseline],
                        [baseline_next, baseline_next],
                        color=fill_color, alpha=0.2)
        ax.annotate(f'{title}',
                    xy=(0.06, baseline - 0.3 * line_axesfrac),
                    color=mpl_grey_rgb, weight='bold')
        ax.annotate(demo,
                    xy=(0.04, baseline - 0.75 * line_axesfrac),
                    color=mpl_grey_rgb, fontsize=16)

    plt.show()
    """
    print("Calculating Triple Integral ...")
    print("Change of variables, using spherical coordinates.")
    print("Replace: x with r*sin(θ)*cos(φ) + Κx.")
    print("Replace: y with r*sin(θ)*sin(φ) + Ky.")
    print("Replace: z with r*cos(θ) + Kz.")
    print("The new function f(r,θ,φ) is:")
    pprint(fppp)
    print("First integral is:")
    pprint(Integral(fnew, (r, r1, r2)))
    print("which gives:")
    pprint(I1)
    print("Second integral is:")
    pprint(Integral(I1, (theta, theta1, theta2)))
    print("which gives:")
    pprint(I2)
    print("Third integral is:")
    pprint(Integral(I2, (phi, phi1, phi2)))
    print("which gives the final result:")
    pprint(I3)
    """
    """
    Label(window, text="Change of variables, using spherical coordinates.").place(x=csx,y=csy+30)
    Label(window,text="Replace x with r*sin(θ)*cos(φ)+Κx, y with r*sin(θ)*sin(φ)+Ky and z with r*cos(θ)+Kz.").place(x=csx,y=csy+50)
    graph_latex("0","0",latex(fnew),"0",csx,csy+80)
    Label(window, text="First integral is:").place(x=csx,y=csy+130)
    graph_latex(latex(r1),latex(r2),latex(fnew),"r",csx,csy+150)
    Label(window, text="which gives:").place(x=csx,y=csy+200)
    graph_latex("0","0",latex(I1),"0",csx,csy+220)
    Label(window, text="Second integral is:").place(x=csx,y=csy+270)
    graph_latex(latex(theta1),latex(theta2),latex(I1),latex(theta),csx,csy+290)
    Label(window, text="which gives:").place(x=csx,y=csy+340)
    graph_latex("0","0",latex(I2),"0",csx,csy+360)
    Label(window, text="Third integral is:").place(x=csx,y=csy+410)
    graph_latex(latex(phi1),latex(phi2),latex(I2),latex(phi),csx,csy+430)
    Label(window, text="which gives:").place(x=csx,y=csy+480)
    graph_latex("0","0",latex(I3),"0",csx,csy+500)
    """

def ti_ec_main_func(fnct,rr1,rr2,t1,t2,p1,p2,c1,c2,c3,aa,bb,cc):
    x, y, z, r, theta, phi = symbols('x y z r theta phi')
    x1, x2, y1, y2, z1, z2 = symbols('r1 r2 theta1 theta2 phi1 phi2')
    f=parse_expr(fnct)
    r1=parse_expr(rr1)
    r2=parse_expr(rr2)
    theta1=parse_expr(t1)
    theta2=parse_expr(t2)
    phi1=parse_expr(p1)
    phi2=parse_expr(p2)
    k1=parse_expr(c1)
    k2=parse_expr(c2)
    k3=parse_expr(c3)
    a=parse_expr(aa)
    b=parse_expr(bb)
    c=parse_expr(cc)
    
    #Input Arguments:
    # function f(x,y,z)
    # r1 <= r <= r2 , theta1 <= theta <= theta2 , phi1 <= phi <= phi2
    #csx=460
    #csy=20
    #Label(window, text="Calculating Triple Integral ...").place(x=csx,y=csy)
    fp = f.subs(x, a*r*sin(theta)*cos(phi)+k1)
    fpp = fp.subs(y, b*r*sin(theta)*sin(phi)+k2)
    fppp = fpp.subs(z,c*r*cos(theta)+k3)
    fnew = fppp*a*b*c*r**2*sin(theta)
    I1 = integrate(fnew, (r, r1, r2))
    I2 = integrate(I1, (theta, theta1, theta2))
    I3 = integrate(I2, (phi, phi1, phi2))
    mathtext_demos = {
        "Header demo":
            r"$You~entered: \int ^{"+latex(phi2)+"} _{"+latex(phi1)+"} \int ^{"+latex(theta2)+
            "} _{"+latex(theta1)+"} \int ^{"+latex(r2)+"} _{"+latex(r1)+"} $"
            r"$ f( x( r , \theta , \phi ) , y( r , \theta , \phi ) ) \cdot a \cdot b \cdot c \cdot r^2 \cdot sin( \theta ) dr d $"
            r"$\theta d $"
            r"$\phi $",
        "Change of variables, using ellipsoidal coordinates:":
            "Replace: "+r"$x$"+" with "+r"$a \cdot r \cdot sin( \theta ) \cdot cos( \phi ) + Κ_x $"
            " and: "+r"$y$"+" with "+r"$b \cdot r \cdot sin( \theta ) \cdot sin( \phi ) + Κ_y $"
            " and: "+r"$z$"+" with "+r"$c \cdot r \cdot cos( \theta ) + Κ_z $",
        "The new function is:":
            r"$f(r, \theta , \phi ) = "+latex(fnew)+" $",
        "First Integral is:":
            r"$I_1 = \int^{"+latex(r2)+"} _{"+latex(r1)+"} "+latex(fnew)+" dr $",
        "which gives I1:":
            r"$I_1 = "+latex(I1)+"$",
        "Second Integral is: ":
            r"$I_2 = \int^{"+latex(theta2)+"}_{"+latex(theta1)+"} "+latex(I1)+" d$"
            r"$ \theta $",
        "which gives I2:":
            r"$I_2 = "+latex(I2)+"$",
        "Third Integral is:":
            r"$I_3 = \int ^{"+latex(phi2)+"} _{"+latex(phi1)+"} "+latex(I2)+" d"
            " \phi $",
        "which gives I3, the final result:":
            r"$I_3 = "+latex(I3)+"$"
    }
    n_lines = len(mathtext_demos)
    # Colors used in Matplotlib online documentation.
    mpl_grey_rgb = (51 / 255, 51 / 255, 51 / 255)

    # Creating figure and axis.
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.90],
                      facecolor="white", frameon=False)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Calculating Triple Integral ...",
                 color=mpl_grey_rgb, fontsize=14, weight='bold')
    ax.set_xticks([])
    ax.set_yticks([])

    # Gap between lines in axes coords
    line_axesfrac = 1 / n_lines

    # Plot header demonstration formula.
    full_demo = mathtext_demos['Header demo']
    ax.annotate(full_demo,
                xy=(0.5, 1. - 0.59 * line_axesfrac),
                color='tab:grey', ha='center', fontsize=20)

    # Plot feature demonstration formulae.
    for i_line, (title, demo) in enumerate(mathtext_demos.items()):
        #print(i_line, demo)
        if i_line == 0:
            continue

        baseline = 1 - i_line * line_axesfrac
        baseline_next = baseline - line_axesfrac
        fill_color = ['white', 'tab:blue'][i_line % 2]
        ax.fill_between([0, 1], [baseline, baseline],
                        [baseline_next, baseline_next],
                        color=fill_color, alpha=0.2)
        ax.annotate(f'{title}',
                    xy=(0.06, baseline - 0.3 * line_axesfrac),
                    color=mpl_grey_rgb, weight='bold')
        ax.annotate(demo,
                    xy=(0.04, baseline - 0.75 * line_axesfrac),
                    color=mpl_grey_rgb, fontsize=16)

    plt.show()
    """
    print("Calculating Triple Integral ...")
    print("Change of variables, using ellipsoidal coordinates.")
    print("Replace: x with a*r*sin(θ)*cos(φ) + Κx.")
    print("Replace: y with b*r*sin(θ)*sin(φ) + Ky.")
    print("Replace: z with c*r*cos(θ) + Kz.")
    print("The new function f(r,θ,φ) is:")
    pprint(fppp)
    print("First integral is:")
    pprint(Integral(fnew, (r, r1, r2)))
    print("which gives:")
    pprint(I1)
    print("Second integral is:")
    pprint(Integral(I1, (theta, theta1, theta2)))
    print("which gives:")
    pprint(I2)
    print("Third integral is:")
    pprint(Integral(I2, (phi, phi1, phi2)))
    print("which gives the final result:")
    pprint(I3)
    """
    """
    Label(window, text="Change of variables, using ellipsoidal coordinates.").place(x=csx,y=csy+30)
    Label(window,text="Replace x with a*r*sin(θ)*cos(φ)+Κx, y with b*r*sin(θ)*sin(φ)+Ky and z with c*r*cos(θ)+Kz.").place(x=csx,y=csy+50)
    graph_latex("0","0",latex(fnew),"0",csx,csy+80)
    Label(window, text="First integral is:").place(x=csx,y=csy+130)
    graph_latex(latex(r1),latex(r2),latex(fnew),"r",csx,csy+150)
    Label(window, text="which gives:").place(x=csx,y=csy+200)
    graph_latex("0","0",latex(I1),"0",csx,csy+220)
    Label(window, text="Second integral is:").place(x=csx,y=csy+270)
    graph_latex(latex(theta1),latex(theta2),latex(I1),latex(theta),csx,csy+290)
    Label(window, text="which gives:").place(x=csx,y=csy+340)
    graph_latex("0","0",latex(I2),"0",csx,csy+360)
    Label(window, text="Third integral is:").place(x=csx,y=csy+410)
    graph_latex(latex(phi1),latex(phi2),latex(I2),latex(phi),csx,csy+430)
    Label(window, text="which gives:").place(x=csx,y=csy+480)
    graph_latex("0","0",latex(I3),"0",csx,csy+500)
    """

def ti_cyc_main_func(fnct,rr1,rr2,t1,t2,p1,p2,c1,c2,c3):
    x, y, z, r, phi, rho = symbols('x y z r phi rho')
    x1, x2, y1, y2, z1, z2 = symbols('rho1 rho2 phi1 phi2 z1 z2')
    f=parse_expr(fnct)
    rho1=parse_expr(rr1)
    rho2=parse_expr(rr2)
    phi1=parse_expr(p1)
    phi2=parse_expr(p2)
    z1=parse_expr(t1)
    z2=parse_expr(t2)
    k1=parse_expr(c1)
    k2=parse_expr(c2)
    k3=parse_expr(c3)
    
    #Input Arguments:
    # function f(x,y,z)
    # r1 <= r <= r2 , theta1 <= theta <= theta2 , phi1 <= phi <= phi2
    #csx=460
    #csy=20
    #Label(window, text="Calculating Triple Integral ...").place(x=csx,y=csy)
    fp = f.subs(x, rho*cos(phi)+k1)
    fpp = fp.subs(y, rho*sin(phi)+k2)
    fppp = fpp.subs(z,z+k3)
    fnew = fppp*rho
    I1 = integrate(fnew, (rho, rho1, rho2))
    I2 = integrate(I1, (phi, phi1, phi2))
    I3 = integrate(I2, (z, z1, z2))
    
    mathtext_demos = {
        "Header demo":
            r"$You~entered: \int ^{"+latex(z2)+"} _{"+latex(z1)+"} \int ^{"+latex(phi2)+
            "} _{"+latex(phi1)+"} \int ^{"+latex(rho2)+"} _{"+latex(rho1)+"} $"
            r"$f( x( \rho , \phi , z ) , y( \rho , \phi , z ) ) \cdot \rho d $"
            r"$\rho d $"
            r"$\phi d z $",
        "Change of variables, using ellipsoidal coordinates:":
            "Replace: "+r"$x$"+" with "+r"$a \cdot r \cdot sin( \theta ) \cdot cos( \phi ) + Κ_x $"
            " and: "+r"$y$"+" with "+r"$b \cdot r \cdot sin( \theta ) \cdot sin( \phi ) + Κ_y $"
            " and: "+r"$z$"+" with "+r"$c \cdot r \cdot cos( \theta ) + Κ_z $",
        "The new function is:":
            r"$f(r, \theta , \phi ) = "+latex(fnew)+" $",
        "First Integral is:":
            r"$I_1 = \int^{"+latex(rho2)+"} _{"+latex(rho1)+"} "+latex(fnew)+" d$"
            r"$ \rho $",
        "which gives I1:":
            r"$I_1 = "+latex(I1)+"$",
        "Second Integral is: ":
            r"$I_2 = \int^{"+latex(phi2)+"}_{"+latex(phi1)+"} "+latex(I1)+" d $"
            r"$ \phi $",
        "which gives I2:":
            r"$I_2 = "+latex(I2)+"$",
        "Third Integral is:":
            r"$I_3 = \int ^{"+latex(z2)+"} _{"+latex(z1)+"} "+latex(I2)+" d z $",
        "which gives I3, the final result:":
            r"$I_3 = "+latex(I3)+"$"
    }
    n_lines = len(mathtext_demos)
    # Colors used in Matplotlib online documentation.
    mpl_grey_rgb = (51 / 255, 51 / 255, 51 / 255)

    # Creating figure and axis.
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.90],
                      facecolor="white", frameon=False)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Calculating Triple Integral ...",
                 color=mpl_grey_rgb, fontsize=14, weight='bold')
    ax.set_xticks([])
    ax.set_yticks([])

    # Gap between lines in axes coords
    line_axesfrac = 1 / n_lines

    # Plot header demonstration formula.
    full_demo = mathtext_demos['Header demo']
    ax.annotate(full_demo,
                xy=(0.5, 1. - 0.59 * line_axesfrac),
                color='tab:grey', ha='center', fontsize=20)

    # Plot feature demonstration formulae.
    for i_line, (title, demo) in enumerate(mathtext_demos.items()):
        #print(i_line, demo)
        if i_line == 0:
            continue

        baseline = 1 - i_line * line_axesfrac
        baseline_next = baseline - line_axesfrac
        fill_color = ['white', 'tab:blue'][i_line % 2]
        ax.fill_between([0, 1], [baseline, baseline],
                        [baseline_next, baseline_next],
                        color=fill_color, alpha=0.2)
        ax.annotate(f'{title}',
                    xy=(0.06, baseline - 0.3 * line_axesfrac),
                    color=mpl_grey_rgb, weight='bold')
        ax.annotate(demo,
                    xy=(0.04, baseline - 0.75 * line_axesfrac),
                    color=mpl_grey_rgb, fontsize=16)

    plt.show()
    """
    print("Calculating Triple Integral ...")
    print("Change of variables, using cylindrical coordinates.")
    print("Replace: x with ρ*cos(φ) + Κx.")
    print("Replace: y with ρ*sin(φ) + Ky.")
    print("Replace: z with z + Kz.")
    print("The new function f(r,θ,φ) is:")
    pprint(fppp)
    print("First integral is:")
    pprint(Integral(fnew, (rho, rho1, rho2)))
    print("which gives:")
    pprint(I1)
    print("Second integral is:")
    pprint(Integral(I1, (phi, phi1, phi2)))
    print("which gives:")
    pprint(I2)
    print("Third integral is:")
    pprint(Integral(I2, (z, z1, z2)))
    print("which gives the final result:")
    pprint(I3)
    """
    """
    Label(window, text="Change of variables, using cylindrical coordinates.").place(x=csx,y=csy+30)
    Label(window,text="Replace x with rho*cos(φ)+Κx, y with rho*sin(φ)+Ky and z with z+Kz.").place(x=csx,y=csy+50)
    graph_latex("0","0",latex(fnew),"0",csx,csy+80)
    Label(window, text="First integral is:").place(x=csx,y=csy+130)
    graph_latex(latex(rho1),latex(rho2),latex(fnew),latex(rho),csx,csy+150)
    Label(window, text="which gives:").place(x=csx,y=csy+200)
    graph_latex("0","0",latex(I1),"0",csx,csy+220)
    Label(window, text="Second integral is:").place(x=csx,y=csy+270)
    graph_latex(latex(phi1),latex(phi2),latex(I1),latex(phi),csx,csy+290)
    Label(window, text="which gives:").place(x=csx,y=csy+340)
    graph_latex("0","0",latex(I2),"0",csx,csy+360)
    Label(window, text="Third integral is:").place(x=csx,y=csy+410)
    graph_latex(latex(z1),latex(z2),latex(I2),"z",csx,csy+430)
    Label(window, text="which gives:").place(x=csx,y=csy+480)
    graph_latex("0","0",latex(I3),"0",csx,csy+500)
    """

def btn_di_cc(event):
    global cs
    cs = 0
#cartesian
def btn_di_sc(event):
    global cs
    cs = 1
#shpericaal
def btn_di_ec(event):
    global cs
    cs = 2
#elliptical
def btn_di_cyc(event):
    global cs
    cs = 3
#cylindrical
def call_compute():
    
    ff = ent_func.get()
    global cs
    if cs==0:
        #cartesian coordinates
        a1=ent_cx1.get()
        a2=ent_cx2.get()
        b1=ent_cy1.get()
        b2=ent_cy2.get()
        c1=ent_cz1.get()
        c2=ent_cz2.get()
        ti_cc_main_func(ff,a1,a2,b1,b2,c1,c2)
    elif cs==1:
        #spherical coordinates
        a1=ent_sr1.get()
        a2=ent_sr2.get()
        b1=ent_stheta1.get()
        b2=ent_stheta2.get()
        c1=ent_sphi1.get()
        c2=ent_sphi2.get()
        d1=ent_cx.get()
        d2=ent_cy.get()
        d3=ent_cz.get()        
        ti_sc_main_func(ff,a1,a2,b1,b2,c1,c2,d1,d2,d3)
    elif cs==2:
        #ellipsoidal coordinates
        a1=ent_er1.get()
        a2=ent_er2.get()
        b1=ent_etheta1.get()
        b2=ent_etheta2.get()
        c1=ent_ephi1.get()
        c2=ent_ephi2.get()
        d1=ent_cx.get()
        d2=ent_cy.get()
        d3=ent_cz.get()        
        d4=ent_a.get()
        d5=ent_b.get()
        d6=ent_c.get()
        ti_ec_main_func(ff,a1,a2,b1,b2,c1,c2,d1,d2,d3,d4,d5,d6)
    elif cs==3:
        #cylindrical coordinates
        a1=ent_cycrho1.get()
        a2=ent_cycrho2.get()
        b1=ent_cycphi1.get()
        b2=ent_cycphi2.get()
        c1=ent_cycz1.get()
        c2=ent_cycz2.get()
        d1=ent_cx.get()
        d2=ent_cy.get()
        d3=ent_cz.get()        
        ti_cyc_main_func(ff,a1,a2,b1,b2,c1,c2,d1,d2,d3)
    else:
        print("Warning !! Unexpected Error !! Please Check your input again!!")
        #Label(text="Warning !! Unexpected Error !! Please Check your input again!!")
    
def call_reset():
    ent_func.delete(0, 'end')
    ent_cx1.delete(0, 'end')
    ent_cx2.insert(0, 'end')
    ent_cy1.delete(0, 'end')
    ent_cy2.delete(0, 'end')
    ent_cz1.delete(0, 'end')
    ent_cz2.delete(0, 'end')
    ent_sr1.delete(0, 'end')
    ent_sr2.delete(0, 'end')
    ent_stheta1.delete(0, 'end')
    ent_stheta2.delete(0, 'end')
    ent_sphi1.insert(0, 'end')
    ent_sphi2.insert(0, 'end')
    ent_er1.insert(0, 'end')
    ent_er2.insert(0, 'end')
    ent_etheta1.delete(0, 'end')
    ent_etheta2.delete(0, 'end')
    ent_ephi1.delete(0, 'end')
    ent_ephi2.delete(0, 'end')
    ent_cycrho1.delete(0, 'end')
    ent_cycrho2.delete(0, 'end')
    ent_cycphi1.delete(0, 'end')
    ent_cycphi2.delete(0, 'end')
    ent_cycz1.delete(0, 'end')
    ent_cycz2.delete(0, 'end')
    ent_cx.delete(0, 'end')
    ent_cy.delete(0, 'end')
    ent_cz.delete(0, 'end')
    ent_a.delete(0, 'end')
    ent_b.delete(0, 'end')
    ent_c.delete(0, 'end')
    ent_func.insert(0,"0")
    ent_cx1.insert(0,"0")
    ent_cx2.insert(0,"0")
    ent_cy1.insert(0,"0")
    ent_cy2.insert(0,"0")
    ent_cz1.insert(0,"0")
    ent_cz2.insert(0,"0")
    ent_sr1.insert(0,"0")
    ent_sr2.insert(0,"0")
    ent_stheta1.insert(0,"0")
    ent_stheta2.insert(0,"0")
    ent_sphi1.insert(0,"0")
    ent_sphi2.insert(0,"0")
    ent_er1.insert(0,"0")
    ent_er2.insert(0,"0")
    ent_etheta1.insert(0,"0")
    ent_etheta2.insert(0,"0")
    ent_ephi1.insert(0,"0")
    ent_ephi2.insert(0,"0")
    ent_cycrho1.insert(0,"0")
    ent_cycrho2.insert(0,"0")
    ent_cycphi1.insert(0,"0")
    ent_cycphi2.insert(0,"0")
    ent_cycz1.insert(0,"0")
    ent_cycz2.insert(0,"0")
    ent_cx.insert(0,"0")
    ent_cy.insert(0,"0")
    ent_cz.insert(0,"0")
    ent_a.insert(0,"1")
    ent_b.insert(0,"1")
    ent_c.insert(0,"1")


window = tk.Tk()
window.geometry("1000x600")
#window.configure(bg='#856ff8')
#window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='C:/Users/user/.spyder-py3/DI.png'))
window.title("Triple Integrals Calculator")
var_f = tk.StringVar()
var_cx1 = tk.StringVar()
var_cx2 = tk.StringVar()
var_cy1 = tk.StringVar()
var_cy2 = tk.StringVar()
var_cz1 = tk.StringVar()
var_cz2 = tk.StringVar()
var_sr1 = tk.StringVar()
var_sr2 = tk.StringVar()
var_stheta1 = tk.StringVar()
var_stheta2 = tk.StringVar()
var_sphi1 = tk.StringVar()
var_sphi2 = tk.StringVar()
var_er1 = tk.StringVar()
var_er2 = tk.StringVar()
var_etheta1 = tk.StringVar()
var_etheta2 = tk.StringVar()
var_ephi1 = tk.StringVar()
var_ephi2 = tk.StringVar()
var_cycrho1 = tk.StringVar()
var_cycrho2 = tk.StringVar()
var_cycphi1 = tk.StringVar()
var_cycphi2 = tk.StringVar()
var_cycz1 = tk.StringVar()
var_cycz2 = tk.StringVar()
var_cx = tk.StringVar()
var_cy = tk.StringVar()
var_cz = tk.StringVar()
var_a = tk.StringVar()
var_b = tk.StringVar()
var_c = tk.StringVar()

Label(window, text="Give the function f(x,y,z) for integration:",font=("Arial",10)).place(x=0,y=1)
ent_func = Entry(window, textvariable=var_f)
ent_func.place(x=230,y=2)

lbl_coor = Label(window, text="Choose type of coordinates:",font=("Arial",10)).place(x=0,y=50)
btn_cc = Button(window, text="Cartesian")
btn_cc.bind("<Button-1>", btn_di_cc)

btn_sc = Button(window, text="Spherical")
btn_sc.bind("<Button-1>", btn_di_sc)

btn_ec = Button(window, text="Ellipsoidal")
btn_ec.bind("<Button-1>", btn_di_ec)

btn_cyc = Button(window, text="Cylindrical")
btn_cyc.bind("<Button-1>", btn_di_cyc)

btn_cc.place(x=0,y=70)
btn_sc.place(x=60,y=70)
btn_ec.place(x=119,y=70)
btn_cyc.place(x=183,y=70)

a=100
Label(text="Insert Edges:",font=("Arial",10)).place(x=0,y=a)
Label(text="x1 =").place(x=0,y=a+20)
ent_cx1 = Entry(window, textvariable=var_cx1)
ent_cx1.place(x=30,y=a+20)
ent_cx1.insert(0,"0")
Label(text="x2 =").place(x=0,y=a+40)
ent_cx2 = Entry(window, textvariable=var_cx2)
ent_cx2.place(x=30,y=a+40)
ent_cx2.insert(0,"0")
Label(text="y1 =").place(x=150,y=a+20)
ent_cy1 = Entry(window, textvariable=var_cy1)
ent_cy1.place(x=180,y=a+20)
ent_cy1.insert(0,"0")
Label(text="y2 =").place(x=150,y=a+40)
ent_cy2 = Entry(window, textvariable=var_cy2)
ent_cy2.place(x=180,y=a+40)
ent_cy2.insert(0,"0")
Label(text="z1 =").place(x=300,y=a+20)
ent_cz1 = Entry(window, textvariable=var_cz1)
ent_cz1.place(x=330,y=a+20)
ent_cz1.insert(0,"0")
Label(text="z2 =").place(x=300,y=a+40)
ent_cz2 = Entry(window, textvariable=var_cz2)
ent_cz2.place(x=330,y=a+40)
ent_cz2.insert(0,"0")
a=a+60
Label(text="Insert Edges for spherical coordinnates:",font=("Arial",10)).place(x=0,y=a)
Label(text="r1 =").place(x=0,y=a+20)
ent_sr1 = Entry(window, textvariable=var_sr1)
ent_sr1.place(x=30,y=a+20)
ent_sr1.insert(0,"0")
Label(text="r2 =").place(x=0,y=a+40)
ent_sr2 = Entry(window, textvariable=var_sr2)
ent_sr2.place(x=30,y=a+40)
ent_sr2.insert(0,"0")
Label(text="θ1 =").place(x=150,y=a+20)
ent_stheta1 = Entry(window, textvariable=var_stheta1)
ent_stheta1.place(x=180,y=a+20)
ent_stheta1.insert(0,"0")
Label(text="θ2 =").place(x=150,y=a+40)
ent_stheta2 = Entry(window, textvariable=var_stheta2)
ent_stheta2.place(x=180,y=a+40)
ent_stheta2.insert(0,"0")
Label(text="φ1 =").place(x=300,y=a+20)
ent_sphi1 = Entry(window, textvariable=var_sphi1)
ent_sphi1.place(x=330,y=a+20)
ent_sphi1.insert(0,"0")
Label(text="φ2 =").place(x=300,y=a+40)
ent_sphi2 = Entry(window, textvariable=var_sphi2)
ent_sphi2.place(x=330,y=a+40)
ent_sphi2.insert(0,"0")
a=a+60
Label(text="Insert Edges for ellipsoidal coordinnates:",font=("Arial",10)).place(x=0,y=a)
Label(text="r1 =").place(x=0,y=a+20)
ent_er1 = Entry(window, textvariable=var_er1)
ent_er1.place(x=30,y=a+20)
ent_er1.insert(0,"0")
Label(text="r2 =").place(x=0,y=a+40)
ent_er2 = Entry(window, textvariable=var_er2)
ent_er2.place(x=30,y=a+40)
ent_er2.insert(0,"0")
Label(text="θ1 =").place(x=150,y=a+20)
ent_etheta1 = Entry(window, textvariable=var_etheta1)
ent_etheta1.place(x=180,y=a+20)
ent_etheta1.insert(0,"0")
Label(text="θ2 =").place(x=150,y=a+40)
ent_etheta2 = Entry(window, textvariable=var_etheta2)
ent_etheta2.place(x=180,y=a+40)
ent_etheta2.insert(0,"0")
Label(text="φ1 =").place(x=300,y=a+20)
ent_ephi1 = Entry(window, textvariable=var_ephi1)
ent_ephi1.place(x=330,y=a+20)
ent_ephi1.insert(0,"0")
Label(text="φ2 =").place(x=300,y=a+40)
ent_ephi2 = Entry(window, textvariable=var_ephi2)
ent_ephi2.place(x=330,y=a+40)
ent_ephi2.insert(0,"0")
a=a+60
Label(text="Insert Edges for cylindrical coordinnates:",font=("Arial",10)).place(x=0,y=a)
Label(text="ρ1 =").place(x=0,y=a+20)
ent_cycrho1 = Entry(window, textvariable=var_cycrho1)
ent_cycrho1.place(x=30,y=a+20)
ent_cycrho1.insert(0,"0")
Label(text="ρ2 =").place(x=0,y=a+40)
ent_cycrho2 = Entry(window, textvariable=var_cycrho2)
ent_cycrho2.place(x=30,y=a+40)
ent_cycrho2.insert(0,"0")
Label(text="φ1 =").place(x=150,y=a+20)
ent_cycphi1 = Entry(window, textvariable=var_cycphi1)
ent_cycphi1.place(x=180,y=a+20)
ent_cycphi1.insert(0,"0")
Label(text="φ2 =").place(x=150,y=a+40)
ent_cycphi2 = Entry(window, textvariable=var_cycphi2)
ent_cycphi2.place(x=180,y=a+40)
ent_cycphi2.insert(0,"0")
Label(text="z1 =").place(x=300,y=a+20)
ent_cycz1 = Entry(window, textvariable=var_cycz1)
ent_cycz1.place(x=330,y=a+20)
ent_cycz1.insert(0,"0")
Label(text="z2 =").place(x=300,y=a+40)
ent_cycz2 = Entry(window, textvariable=var_cycz2)
ent_cycz2.place(x=330,y=a+40)
ent_cycz2.insert(0,"0")
a=a+60
Label(text="Center of coordinate system (default is K(0,0,0)):",font=("Arial",10)).place(x=0,y=a)
Label(text="Kx =").place(x=0,y=a+20)
ent_cx = Entry(window,textvariable=var_cx)
ent_cx.place(x=30,y=a+20)
ent_cx.insert(0,"0")
Label(text="Ky =").place(x=150,y=a+20)
ent_cy = Entry(window,textvariable=var_cy)
ent_cy.place(x=180,y=a+20)
ent_cy.insert(0,"0")
Label(text="Kz =").place(x=300,y=a+20)
ent_cz = Entry(window,textvariable=var_cz)
ent_cz.place(x=330,y=a+20)
ent_cz.insert(0,"0")
a=a+60
Label(text="Length of axes for ellipsoidal coordinates (default (a=1,b=1,c=1)):",font=("Arial",10)).place(x=0,y=a)
Label(text="a =").place(x=0,y=a+20)
ent_a = Entry(window,textvariable=var_a)
ent_a.place(x=30,y=a+20)
ent_a.insert(0,"1")
Label(text="b =").place(x=150,y=a+20)
ent_b = Entry(window,textvariable=var_b)
ent_b.place(x=180,y=a+20)
ent_b.insert(0,"1")
Label(text="c =").place(x=300,y=a+20)
ent_c = Entry(window,textvariable=var_c)
ent_c.place(x=330,y=a+20)
ent_c.insert(0,"1")
a=a+60

Button(window, text="Compute",command=call_compute).place(x=0,y=a)

Button(window, text="Reset", command=call_reset).place(x=150, y=a)

Button(window, text="Exit", command=window.destroy).place(x=300,y=a)

#Button(window, text="Theory", command=call_theory).place(x=150,y=a+60)

window.mainloop()
