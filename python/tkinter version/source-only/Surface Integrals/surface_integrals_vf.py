# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 13:53:19 2022

@author: user
"""
from sympy import symbols, diff, integrate, latex, sqrt
from sympy.parsing.sympy_parser import parse_expr
import tkinter as tk
from tkinter import Label , Entry , Button
import matplotlib.pyplot as plt
#import matplotlib
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#matplotlib.use('TkAgg')

global orient

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
        Label(window,text="Warning! Inverting Inputs ...").place(x=450,y=0)
        a,b = swap_values(a,b)
    else:
        Label(window,text="No errors detected").place(x=450,y=0)
    return a,b
"""
def graph_latex(str_a,str_b,str_f,str_var,csx,csy):
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
"""
def surface_integral_vf(funcx,funcy,funcz,s1,s2,s3,a,b,c,d,sfunc,xa,xb,ya,yb,za,zb):
    global orient
    fx, fy, fz, sx, sy, sz, g = symbols('fx fy fz sx sy sz g')
    u1, u2, v1, v2 = symbols('u1 u2 v1 v2')
    x, y, z, v, u = symbols('x y z v u')
    x1, x2, y1, y2, z1, z2 = symbols('x1 x2 y1 y2 z1 z2')
    #csx = 450
    #csy = 20
    #Label(window, text="Transforming Surface integral to Double integral").place(x=csx,y=csy)
    fx = parse_expr(funcx)
    fy = parse_expr(funcy)
    fz = parse_expr(funcz)
    if sfunc == "":
        sx = parse_expr(s1)
        sy = parse_expr(s2)
        sz = parse_expr(s3)
        u1 = parse_expr(a)
        u2 = parse_expr(b)
        v1 = parse_expr(c)
        v2 = parse_expr(d)
        #Label(window,text="Step 1 - Calculate ds/dv and ds/du").place(x=csx,y=csy+30)
        #step 1: ds/dv and ds/du =;
        dvsx = diff(sx,v)
        dvsy = diff(sy,v)
        dvsz = diff(sz,v)
        dusx = diff(sx,u)
        dusy = diff(sy,u)
        dusz = diff(sz,u)
        #Label(window,text="Step 2- Calculate the cross product of the above derivatives").place(x=csx,y=csy+60)
        #step 2: cross product ds/du x ds/dv = ;
        if orient == 1:
            #positive orientation Dus x Dvs
            va = dusy*dvsz - dvsy*dusz
            vb = dvsx*dusz - dusx*dvsz
            vc = dusx*dvsy - dvsx*dusy
        else:
            #negative orientation Dvs x Dus
            va = dvsy*dusz - dusy*dvsz
            vb = dusx*dvsz - dvsx*dusz
            vc = dvsx*dusy - dusx*dvsy
        #Label(window, text="Step 3 - Calclate the norm of the above vector").place(x=csx,y=csy+90)
        #step 3: norm of cross product
        #normv = sqrt(va**2 + vb**2 + vc**2)
        #Label(window, text="Step 4 - Replace x,y,z with x(u,v),y(u,v),z(u,v) ").place(x=csx,y=csy+120)
        #step 4: replace x,y,z with s
        fx1 = fx.subs(x,sx)
        fx2 = fx1.subs(y,sy)
        fx3 = fx2.subs(z,sz)
        fy1 = fy.subs(x,sx)
        fy2 = fy1.subs(y,sy)
        fy3 = fy2.subs(z,sz)
        fz1 = fz.subs(x,sx)
        fz2 = fz1.subs(y,sy)
        fz3 = fz2.subs(z,sz)
        #Label(window, text="Step 5 - The function f(u,v) is:").place(x=csx,y=csy+150)
        #step 5: new integral is double
        fnew = fx3*va + fy3*vb + fz3*vc
        #csy = csy + 150
        #Label(window, text="Calculating Double Integral ...").place(x=csx,y=csy)
        if (u1.is_number==1 and u2.is_number==1 and v1.is_number==1 and v2.is_number==1):
            u1,u2 = warning_one(u1,u2)
            v1,v2 = warning_one(v1,v2)
            #1.
            #Simple u and v
            I1 = integrate(fnew,(u,u1,u2))
            I = integrate(I1,(v,v1,v2))
            mathtext_demos = {
                "Header demo":
                    "",
                "From Surface Integral to Double Integral . . . :":
                    "",
                "Step 1 - Calculate "+r"$ \frac{ d s }{ d v }$"+" and "+r"$ \frac{ d s }{ d u }$"+":":
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(dvsx)+" , "+latex(dvsy)+" , "+latex(dvsz)+" ]$"
                    " and "
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(dusx)+" , "+latex(dusy)+" , "+latex(dusz)+" ]$",
                "Step 2 - Calculate the cross product (Hint 1) :":
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(va)+" , "+latex(vb)+" , "+latex(vc)+" ]$", 
                "Step 3 - Replacing in "+r"$\vec{F}(x,y,z)$"+":":
                    r"$ x $ "+" with "+r"$ x(u,v) $"+" , "+
                    r"$ y $ "+" with "+r"$ y(u,v) $"+" and "+
                    r"$ z $ "+" with "+r"$ z(u,v) $",
                "The new function is:":
                    r"$ \vec{F} (u,v) = [ "+latex(fx3)+" , "+latex(fy3)+" , "+latex(fz3)+" ] $",
                "Calculating Double Integral . . .":
                    "Region D is simple u and v",
                "First Integral is:":
                    r"$I_1 = \int^{"+latex(u2)+"}_{"+latex(u1)+"} "+latex(fnew)+" du $",
                "which gives:":
                    r"$I_1 = "+latex(I1)+"$",
                "Second Integral is: ":
                    r"$I_2 = \int^{"+latex(v2)+"}_{"+latex(v1)+"} "+latex(I1)+" dv $",
                "which gives final result:":
                    r"$I_2 = "+latex(I)+" $",
                "Hint 1":
                    "Positive orientation: "
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} \times \frac{ \partial \vec{s} (u,v) }{ \partial v} $"
                    " Negative orientation: "
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} $"
            }
            """
            Label(window, text="D is Simple u and v.").place(x=csx,y=csy+30)
            Label(window, text="First integral is:").place(x=csx,y=csy+50)
            graph_latex(latex(u1),latex(u2),latex(fnew),"u",csx,csy+80)
            Label(window, text="which gives:").place(x=csx,y=csy+130)
            graph_latex("0","0",latex(I1),"0",csx,csy+150)
            Label(window, text="Second integral is:").place(x=csx,y=csy+200)
            graph_latex(latex(v1),latex(v2),latex(I1),"v",csx,csy+220)
            Label(window, text="which gives:").place(x=csx,y=csy+270)
            graph_latex("0","0",latex(I),"0",csx,csy+290)
            """
        elif((u1.is_number==0 or u2.is_number==0) and v1.is_number==1 and v2.is_number==1):
            v1,v2 = warning_one(v1,v2)
            #2.
            #Simple u
            #display result...
            I1 = integrate(fnew,(u,u1,u2))
            I = integrate(I1,(v,v1,v2))
            mathtext_demos = {
                "Header demo":
                    "",
                "From Surface Integral to Double Integral . . . :":
                    "",
                "Step 1 - Calculate ds/dv and ds/du:":
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(dvsx)+" , "+latex(dvsy)+" , "+latex(dvsz)+" ]$"
                    " and "
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(dusx)+" , "+latex(dusy)+" , "+latex(dusz)+" ]$",
                "Step 2 - Calculate the cross product:":
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(va)+" , "+latex(vb)+" , "+latex(vc)+" ]$", 
                "Step 3 - Replacing in "+r"$\vec{F}(x,y,z)$"+":":
                    r"$ x $ "+" with "+r"$ x(u,v) $"+" , "+
                    r"$ y $ "+" with "+r"$ y(u,v) $"+" and "+
                    r"$ z $ "+" with "+r"$ z(u,v) $",
                "The new function is:":
                    r"$ \vec{F} (u,v) = [ "+latex(fx3)+" , "+latex(fy3)+" , "+latex(fz3)+" ] $",
                "Calculating Double Integral . . .":
                    "",
                "First Integral is:":
                    r"$I_1 = \int^{"+latex(u2)+"}_{"+latex(u1)+"} "+latex(fnew)+" du $",
                "which gives:":
                    r"$I_1 = "+latex(I1)+"$",
                "Second Integral is: ":
                    r"$I_2 = \int^{"+latex(v2)+"}_{"+latex(v1)+"} "+latex(I1)+" dv $",
                "which gives final result:":
                    r"$I_2 = "+latex(I)+" $",
                "Hint 1":
                    "Positive orientation: "
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} \times \frac{ \partial \vec{s} (u,v) }{ \partial v} $"
                    " Negative orientation: "
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} $"
            }
            """
            Label(window, text="D is Simple u.").place(x=csx,y=csy+30)
            Label(window, text="First integral is:").place(x=csx,y=csy+50)
            graph_latex(latex(u1),latex(u2),latex(fnew),"u",csx,csy+80)
            Label(window, text="which gives:").place(x=csx,y=csy+130)
            graph_latex("0","0",latex(I1),"0",csx,csy+150)
            Label(window, text="Second integral is:").place(x=csx,y=csy+200)
            graph_latex(latex(v1),latex(v2),latex(I1),"v",csx,csy+220)
            Label(window, text="which gives:").place(x=csx,y=csy+270)
            graph_latex("0","0",latex(I),"0",csx,csy+290)
            """
        else:
            u1,u2 = warning_one(u1,u2)
            #3.
            #Simple v
            #display result...
            I1 = integrate(fnew,(v,v1,v2))
            I = integrate(I1,(u,u1,u2))
            mathtext_demos = {
                "Header demo":
                    "",
                "From Surface Integral to Double Integral . . . :":
                    "",
                "Step 1 - Calculate ds/dv and ds/du:":
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(dvsx)+" , "+latex(dvsy)+" , "+latex(dvsz)+" ]$"
                    " and "
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(dusx)+" , "+latex(dusy)+" , "+latex(dusz)+" ]$",
                "Step 2 - Calculate the cross product:":
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(va)+" , "+latex(vb)+" , "+latex(vc)+" ]$", 
                "Step 3 - Replacing in "+r"$\vec{F}(x,y,z)$"+":":
                    r"$ x $ "+" with "+r"$ x(u,v) $"+" , "+
                    r"$ y $ "+" with "+r"$ y(u,v) $"+" and "+
                    r"$ z $ "+" with "+r"$ z(u,v) $",
                "The new function is:":
                    r"$ \vec{F} (u,v) = [ "+latex(fx3)+" , "+latex(fy3)+" , "+latex(fz3)+" ] $",
                "Calculating Double Integral . . .":
                    "",
                "First Integral is:":
                    r"$I_1 = \int^{"+latex(v2)+"}_{"+latex(v1)+"} "+latex(fnew)+" dv $",
                "which gives:":
                    r"$I_1 = "+latex(I1)+"$",
                "Second Integral is: ":
                    r"$I_2 = \int^{"+latex(u2)+"}_{"+latex(u1)+"} "+latex(I1)+" du $",
                "which gives final result:":
                    r"$I_2 = "+latex(I)+" $",
                "Hint 1":
                    "Positive orientation: "
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} \times \frac{ \partial \vec{s} (u,v) }{ \partial v} $"
                    " Negative orientation: "
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} $"
            }
            """
            Label(window, text="D is Simple y.").place(x=csx,y=csy+30)
            Label(window, text="First integral is:").place(x=csx,y=csy+50)
            graph_latex(latex(v1),latex(v2),latex(fnew),"v",csx,csy+80)
            Label(window, text="which gives:").place(x=csx,y=csy+130)
            graph_latex("0","0",latex(I1),"0",csx,csy+150)
            Label(window, text="Second integral is:").place(x=csx,y=csy+200)
            graph_latex(latex(u1),latex(u2),latex(I1),"u",csx,csy+220)
            Label(window, text="which gives:").place(x=csx,y=csy+270)
            graph_latex("0","0",latex(I),"0",csx,csy+290)
            """
        #end
    elif sfunc != "":
        g = parse_expr(sfunc)
        #step 1 - calculate the grad g
        if orient != 0:
            #positive orientation
            gradgx = -diff(g,x)
            gradgy = -diff(g,y)
            gradgz = diff(g,z)
        else:
            #neagtive orientation
            gradgx = diff(g,x)
            gradgy = diff(g,y)
            gradgz = -diff(g,z)
        #step 2 - find the norm of the grad g
        normg = sqrt(gradgx**2 + gradgy**2 + gradgz**2)
        #step 3 - find the vector n
        nvx = gradgx/normg
        nvy = gradgy/normg
        nvz = gradgz/normg
        #step 4 - claculate the dot product of the function with the n vector
        f2 = fx*nvx+fy*nvy+fz*nvz
        #step 5 - new function for double integral is:
        fnew = f2*normg
        
        if za == "" and zb == "":
            x1 = parse_expr(xa)
            x2 = parse_expr(xb)
            y1 = parse_expr(ya)
            y2 = parse_expr(yb)
            
            #z is empty
            #Label(window, text="Calculating Double Integral ...").place(x=csx,y=csy)
            if (x1.is_number==1 and x2.is_number==1 and y1.is_number==1 and y2.is_number==1):
                x1,x2 = warning_one(x1,x2)
                y1,y2 = warning_one(y1,y2)
                #1.
                #Simple x and y
                I1 = integrate(fnew,(x,x1,x2))
                I = integrate(I1,(y,y1,y2))
                mathtext_demos = {
                    "Header demo":
                        "",
                    "From Surface Integral to Double Integral . . . :":
                        "",
                    "Step 1 - Calculate "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                    "Step 2 - Find "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                        r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                    "Step 3 - Calculate "+r"$ \hat{n} $"+":":
                        r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                    "Step 4 - The new "+r"$\vec{F}(x,y,z)$"+" is":
                        r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                    "Calculating Double Integral . . .":
                        "",
                    "First Integral is:":
                        r"$I_1 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(fnew)+" dx $",
                    "which gives:":
                        r"$I_1 = "+latex(I1)+"$",
                    "Second Integral is: ":
                        r"$I_2 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(I1)+" dy $",
                    "which gives final result:":
                        r"$I_2 = "+latex(I)+" $",
                    "Hint 1":
                        "Positive orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ - \frac{ \partial g(x,y,z) }{ \partial x} , - \frac{ \partial g(x,y,z) }{ \partial y} , \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                        " Negative orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ \frac{ \partial g(x,y,z) }{ \partial x} , \frac{ \partial g(x,y,z) }{ \partial y} , - \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                }
                """
                Label(window, text="D is Simple x and y.").place(x=csx,y=csy+30)
                Label(window, text="First integral is:").place(x=csx,y=csy+50)
                graph_latex(latex(x1),latex(x2),latex(fnew),"x",csx,csy+80)
                Label(window, text="which gives:").place(x=csx,y=csy+130)
                graph_latex("0","0",latex(I1),"0",csx,csy+150)
                Label(window, text="Second integral is:").place(x=csx,y=csy+200)
                graph_latex(latex(y1),latex(y2),latex(I1),"y",csx,csy+220)
                Label(window, text="which gives:").place(x=csx,y=csy+270)
                graph_latex("0","0",latex(I),"0",csx,csy+290)
                """
            elif((x1.is_number==0 or x2.is_number==0) and y1.is_number==1 and y2.is_number==1):
                y1,y2 = warning_one(y1,y2)
                #2.
                #Simple x
                #display result...
                I1 = integrate(fnew,(x,x1,x2))
                I = integrate(I1,(y,y1,y2))
                mathtext_demos = {
                    "Header demo":
                        "",
                    "From Surface Integral to Double Integral . . . :":
                        "",
                    "Step 1 - Calculate "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                    "Step 2 - Find "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                        r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                    "Step 3 - Calculate "+r"$ \hat{n} $"+":":
                        r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                    "Step 4 - The new "+r"$\vec{F}(x,y,z)$"+" is":
                        r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                    "Calculating Double Integral . . .":
                        "",
                    "First Integral is:":
                        r"$I_1 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(fnew)+" dx $",
                    "which gives:":
                        r"$I_1 = "+latex(I1)+"$",
                    "Second Integral is: ":
                        r"$I_2 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(I1)+" dy $",
                    "which gives final result:":
                        r"$I_2 = "+latex(I)+" $",
                    "Hint 1":
                        "Positive orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ - \frac{ \partial g(x,y,z) }{ \partial x} , - \frac{ \partial g(x,y,z) }{ \partial y} , \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                        " Negative orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ \frac{ \partial g(x,y,z) }{ \partial x} , \frac{ \partial g(x,y,z) }{ \partial y} , - \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                }
                """
                Label(window, text="D is Simple x.").place(x=csx,y=csy+30)
                Label(window, text="First integral is:").place(x=csx,y=csy+50)
                graph_latex(latex(x1),latex(x2),latex(fnew),"x",csx,csy+80)
                Label(window, text="which gives:").place(x=csx,y=csy+130)
                graph_latex("0","0",latex(I1),"0",csx,csy+150)
                Label(window, text="Second integral is:").place(x=csx,y=csy+200)
                graph_latex(latex(y1),latex(y2),latex(I1),"y",csx,csy+220)
                Label(window, text="which gives:").place(x=csx,y=csy+270)
                graph_latex("0","0",latex(I),"0",csx,csy+290)
                """
            else:
                x1,x2 = warning_one(x1,x2)
                #3.
                #Simple y
                #display result...
                I1 = integrate(fnew,(y,y1,y2))
                I = integrate(I1,(x,x1,x2))
                mathtext_demos = {
                    "Header demo":
                        "",
                    "From Surface Integral to Double Integral . . . :":
                        "",
                    "Step 1 - Calculate "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                    "Step 2 - Find "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                        r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                    "Step 3 - Calculate "+r"$ \hat{n} $"+":":
                        r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                    "Step 4 - The new "+r"$\vec{F}(x,y,z)$"+" is":
                        r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                    "Calculating Double Integral . . .":
                        "",
                    "First Integral is:":
                        r"$I_1 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(fnew)+" dy $",
                    "which gives:":
                        r"$I_1 = "+latex(I1)+"$",
                    "Second Integral is: ":
                        r"$I_2 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(I1)+" dx $",
                    "which gives final result:":
                        r"$I_2 = "+latex(I)+" $",
                    "Hint 1":
                        "Positive orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ - \frac{ \partial g(x,y,z) }{ \partial x} , - \frac{ \partial g(x,y,z) }{ \partial y} , \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                        " Negative orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ \frac{ \partial g(x,y,z) }{ \partial x} , \frac{ \partial g(x,y,z) }{ \partial y} , - \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                }
                """
                Label(window, text="D is Simple y.").place(x=csx,y=csy+30)
                Label(window, text="First integral is:").place(x=csx,y=csy+50)
                graph_latex(latex(y1),latex(y2),latex(fnew),"y",csx,csy+80)
                Label(window, text="which gives:").place(x=csx,y=csy+130)
                graph_latex("0","0",latex(I1),"0",csx,csy+150)
                Label(window, text="Second integral is:").place(x=csx,y=csy+200)
                graph_latex(latex(x1),latex(x2),latex(I1),"x",csx,csy+220)
                Label(window, text="which gives:").place(x=csx,y=csy+270)
                graph_latex("0","0",latex(I),"0",csx,csy+290)
                """
            #end
        elif ya == "" and yb == "":
            x1 = parse_expr(xa)
            x2 = parse_expr(xb)
            z1 = parse_expr(za)
            z2 = parse_expr(zb)
            #y is empty
            
            #Label(window, text="Calculating Double Integral ...").place(x=csx,y=csy)
            
            if (x1.is_number==1 and x2.is_number==1 and z1.is_number==1 and z2.is_number==1):
                x1,x2 = warning_one(x1,x2)
                z1,z2 = warning_one(z1,z2)
                #1.
                #Simple x and z
                I1 = integrate(fnew,(x,x1,x2))
                I = integrate(I1,(z,z1,z2))
                mathtext_demos = {
                    "Header demo":
                        "",
                    "From Surface Integral to Double Integral . . . :":
                        "",
                    "Step 1 - Calculate "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                    "Step 2 - Find "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                        r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                    "Step 3 - Calculate "+r"$ \hat{n} $"+":":
                        r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                    "Step 4 - The new "+r"$\vec{F}(x,y,z)$"+" is":
                        r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                    "Calculating Double Integral . . .":
                        "",
                    "First Integral is:":
                        r"$I_1 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(fnew)+" dx $",
                    "which gives:":
                        r"$I_1 = "+latex(I1)+"$",
                    "Second Integral is: ":
                        r"$I_2 = \int^{"+latex(z2)+"}_{"+latex(z1)+"} "+latex(I1)+" dz $",
                    "which gives final result:":
                        r"$I_2 = "+latex(I)+" $",
                    "Hint 1":
                        "Positive orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ - \frac{ \partial g(x,y,z) }{ \partial x} , - \frac{ \partial g(x,y,z) }{ \partial y} , \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                        " Negative orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ \frac{ \partial g(x,y,z) }{ \partial x} , \frac{ \partial g(x,y,z) }{ \partial y} , - \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                }
                """
                Label(window, text="D is Simple x and z.").place(x=csx,y=csy+30)
                Label(window, text="First integral is:").place(x=csx,y=csy+50)
                graph_latex(latex(x1),latex(x2),latex(fnew),"x",csx,csy+80)
                Label(window, text="which gives:").place(x=csx,y=csy+130)
                graph_latex("0","0",latex(I1),"0",csx,csy+150)
                Label(window, text="Second integral is:").place(x=csx,y=csy+200)
                graph_latex(latex(z1),latex(z2),latex(I1),"z",csx,csy+220)
                Label(window, text="which gives:").place(x=csx,y=csy+270)
                graph_latex("0","0",latex(I),"0",csx,csy+290)
                """
            elif((x1.is_number==0 or x2.is_number==0) and z1.is_number==1 and z2.is_number==1):
                z1,z2 = warning_one(z1,z2)
                #2.
                #Simple x
                #display result...
                I1 = integrate(fnew,(x,x1,x2))
                I = integrate(I1,(z,z1,z2))
                mathtext_demos = {
                    "Header demo":
                        "",
                    "From Surface Integral to Double Integral . . . :":
                        "",
                    "Step 1 - Calculate "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                    "Step 2 - Find "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                        r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                    "Step 3 - Calculate "+r"$ \hat{n} $"+":":
                        r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                    "Step 4 - The new "+r"$\vec{F}(x,y,z)$"+" is":
                        r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                    "Calculating Double Integral . . .":
                        "",
                    "First Integral is:":
                        r"$I_1 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(fnew)+" dx $",
                    "which gives:":
                        r"$I_1 = "+latex(I1)+"$",
                    "Second Integral is: ":
                        r"$I_2 = \int^{"+latex(z2)+"}_{"+latex(z1)+"} "+latex(I1)+" dz $",
                    "which gives final result:":
                        r"$I_2 = "+latex(I)+" $",
                    "Hint 1":
                        "Positive orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ - \frac{ \partial g(x,y,z) }{ \partial x} , - \frac{ \partial g(x,y,z) }{ \partial y} , \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                        " Negative orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ \frac{ \partial g(x,y,z) }{ \partial x} , \frac{ \partial g(x,y,z) }{ \partial y} , - \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                }
                """
                Label(window, text="D is Simple x.").place(x=csx,y=csy+30)
                Label(window, text="First integral is:").place(x=csx,y=csy+50)
                graph_latex(latex(x1),latex(x2),latex(fnew),"x",csx,csy+80)
                Label(window, text="which gives:").place(x=csx,y=csy+130)
                graph_latex("0","0",latex(I1),"0",csx,csy+150)
                Label(window, text="Second integral is:").place(x=csx,y=csy+200)
                graph_latex(latex(z1),latex(z2),latex(I1),"z",csx,csy+220)
                Label(window, text="which gives:").place(x=csx,y=csy+270)
                graph_latex("0","0",latex(I),"0",csx,csy+290)
                """
            else:
                x1,x2 = warning_one(x1,x2)
                #3.
                #Simple z
                #display result...
                I1 = integrate(fnew,(z,z1,z2))
                I = integrate(I1,(x,x1,x2))
                mathtext_demos = {
                    "Header demo":
                        "",
                    "From Surface Integral to Double Integral . . . :":
                        "",
                    "Step 1 - Calculate "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                    "Step 2 - Find "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                        r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                    "Step 3 - Calculate "+r"$ \hat{n} $"+":":
                        r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                    "Step 4 - The new "+r"$\vec{F}(x,y,z)$"+" is":
                        r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                    "Calculating Double Integral . . .":
                        "",
                    "First Integral is:":
                        r"$I_1 = \int^{"+latex(z2)+"}_{"+latex(z1)+"} "+latex(fnew)+" dz $",
                    "which gives:":
                        r"$I_1 = "+latex(I1)+"$",
                    "Second Integral is: ":
                        r"$I_2 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(I1)+" dx $",
                    "which gives final result:":
                        r"$I_2 = "+latex(I)+" $",
                    "Hint 1":
                        "Positive orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ - \frac{ \partial g(x,y,z) }{ \partial x} , - \frac{ \partial g(x,y,z) }{ \partial y} , \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                        " Negative orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ \frac{ \partial g(x,y,z) }{ \partial x} , \frac{ \partial g(x,y,z) }{ \partial y} , - \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                }
                """
                Label(window, text="D is Simple z.").place(x=csx,y=csy+30)
                Label(window, text="First integral is:").place(x=csx,y=csy+50)
                graph_latex(latex(z1),latex(z2),latex(fnew),"z",csx,csy+80)
                Label(window, text="which gives:").place(x=csx,y=csy+130)
                graph_latex("0","0",latex(I1),"0",csx,csy+150)
                Label(window, text="Second integral is:").place(x=csx,y=csy+200)
                graph_latex(latex(x1),latex(x2),latex(I1),"x",csx,csy+220)
                Label(window, text="which gives:").place(x=csx,y=csy+270)
                graph_latex("0","0",latex(I),"0",csx,csy+290)
                """
            #end
        elif xa == "" and xb == "":
            y1 = parse_expr(ya)
            y2 = parse_expr(yb)
            z1 = parse_expr(za)
            z2 = parse_expr(zb)
            #x is empty
            #Label(window, text="Calculating Double Integral ...").place(x=csx,y=csy)
            
            if (y1.is_number==1 and y2.is_number==1 and z1.is_number==1 and z2.is_number==1):
                y1,y2 = warning_one(y1,y2)
                z1,z2 = warning_one(z1,z2)
                #1.
                #Simple y and z
                I1 = integrate(fnew,(y,y1,y2))
                I = integrate(I1,(z,z1,z2))
                mathtext_demos = {
                    "Header demo":
                        "",
                    "From Surface Integral to Double Integral . . . :":
                        "",
                    "Step 1 - Calculate "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                    "Step 2 - Find "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                        r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                    "Step 3 - Calculate "+r"$ \hat{n} $"+":":
                        r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                    "Step 4 - The new "+r"$\vec{F}(x,y,z)$"+" is":
                        r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                    "Calculating Double Integral . . .":
                        "",
                    "First Integral is:":
                        r"$I_1 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(fnew)+" dy $",
                    "which gives:":
                        r"$I_1 = "+latex(I1)+"$",
                    "Second Integral is: ":
                        r"$I_2 = \int^{"+latex(z2)+"}_{"+latex(z1)+"} "+latex(I1)+" dz $",
                    "which gives final result:":
                        r"$I_2 = "+latex(I)+" $",
                    "Hint 1":
                        "Positive orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ - \frac{ \partial g(x,y,z) }{ \partial x} , - \frac{ \partial g(x,y,z) }{ \partial y} , \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                        " Negative orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ \frac{ \partial g(x,y,z) }{ \partial x} , \frac{ \partial g(x,y,z) }{ \partial y} , - \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                }
                """
                Label(window, text="D is Simple y and z.").place(x=csx,y=csy+30)
                Label(window, text="First integral is:").place(x=csx,y=csy+50)
                graph_latex(latex(y1),latex(y2),latex(fnew),"y",csx,csy+80)
                Label(window, text="which gives:").place(x=csx,y=csy+130)
                graph_latex("0","0",latex(I1),"0",csx,csy+150)
                Label(window, text="Second integral is:").place(x=csx,y=csy+200)
                graph_latex(latex(z1),latex(z2),latex(I1),"z",csx,csy+220)
                Label(window, text="which gives:").place(x=csx,y=csy+270)
                graph_latex("0","0",latex(I),"0",csx,csy+290)
                """
            elif((y1.is_number==0 or y2.is_number==0) and z1.is_number==1 and z2.is_number==1):
                z1,z2 = warning_one(z1,z2)
                #2.
                #Simple y
                #display result...
                I1 = integrate(fnew,(y,y1,y2))
                I = integrate(I1,(z,z1,z2))
                mathtext_demos = {
                    "Header demo":
                        "",
                    "From Surface Integral to Double Integral . . . :":
                        "",
                    "Step 1 - Calculate "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                    "Step 2 - Find "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                        r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                    "Step 3 - Calculate "+r"$ \hat{n} $"+":":
                        r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                    "Step 4 - The new "+r"$\vec{F}(x,y,z)$"+" is":
                        r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                    "Calculating Double Integral . . .":
                        "",
                    "First Integral is:":
                        r"$I_1 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(fnew)+" dy $",
                    "which gives:":
                        r"$I_1 = "+latex(I1)+"$",
                    "Second Integral is: ":
                        r"$I_2 = \int^{"+latex(z2)+"}_{"+latex(z1)+"} "+latex(I1)+" dz $",
                    "which gives final result:":
                        r"$I_2 = "+latex(I)+" $",
                    "Hint 1":
                        "Positive orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ - \frac{ \partial g(x,y,z) }{ \partial x} , - \frac{ \partial g(x,y,z) }{ \partial y} , \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                        " Negative orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ \frac{ \partial g(x,y,z) }{ \partial x} , \frac{ \partial g(x,y,z) }{ \partial y} , - \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                }
                """
                Label(window, text="D is Simple y.").place(x=csx,y=csy+30)
                Label(window, text="First integral is:").place(x=csx,y=csy+50)
                graph_latex(latex(y1),latex(y2),latex(fnew),"y",csx,csy+80)
                Label(window, text="which gives:").place(x=csx,y=csy+130)
                graph_latex("0","0",latex(I1),"0",csx,csy+150)
                Label(window, text="Second integral is:").place(x=csx,y=csy+200)
                graph_latex(latex(z1),latex(z2),latex(I1),"z",csx,csy+220)
                Label(window, text="which gives:").place(x=csx,y=csy+270)
                graph_latex("0","0",latex(I),"0",csx,csy+290)
                """
            else:
                y1,y2 = warning_one(y1,y2)
                #3.
                #Simple z
                #display result...
                I1 = integrate(fnew,(z,z1,z2))
                I = integrate(I1,(y,y1,y2))
                mathtext_demos = {
                    "Header demo":
                        "",
                    "From Surface Integral to Double Integral . . . :":
                        "",
                    "Step 1 - Calculate "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                    "Step 2 - Find "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                        r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                    "Step 3 - Calculate "+r"$ \hat{n} $"+":":
                        r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                    "Step 4 - The new "+r"$\vec{F}(x,y,z)$"+" is":
                        r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                    "Calculating Double Integral . . .":
                        "",
                    "First Integral is:":
                        r"$I_1 = \int^{"+latex(z2)+"}_{"+latex(z1)+"} "+latex(fnew)+" dz $",
                    "which gives:":
                        r"$I_1 = "+latex(I1)+"$",
                    "Second Integral is: ":
                        r"$I_2 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(I1)+" dy $",
                    "which gives final result:":
                        r"$I_2 = "+latex(I)+" $",
                    "Hint 1":
                        "Positive orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ - \frac{ \partial g(x,y,z) }{ \partial x} , - \frac{ \partial g(x,y,z) }{ \partial y} , \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                        " Negative orientation: "
                        r"$ \vec{ \nabla } g(x,y,z) = [ \frac{ \partial g(x,y,z) }{ \partial x} , \frac{ \partial g(x,y,z) }{ \partial y} , - \frac{ \partial g(x,y,z) }{ \partial z} ] $"
                }
                """
                Label(window, text="D is Simple z.").place(x=csx,y=csy+30)
                Label(window, text="First integral is:").place(x=csx,y=csy+50)
                graph_latex(latex(z1),latex(z2),latex(fnew),"z",csx,csy+80)
                Label(window, text="which gives:").place(x=csx,y=csy+130)
                graph_latex("0","0",latex(I1),"0",csx,csy+150)
                Label(window, text="Second integral is:").place(x=csx,y=csy+200)
                graph_latex(latex(y1),latex(y2),latex(I1),"y",csx,csy+220)
                Label(window, text="which gives:").place(x=csx,y=csy+270)
                graph_latex("0","0",latex(I),"0",csx,csy+290)
                """
            #end
        else:
            mathtext_demos = {
                "Header demo":
                    "Error Cannot Calculate !!! ",
            }
            #Label(window, text = "Error Cannot Calculate !!!").place(x=csx,y=csy+100)
        #end
    #end
    n_lines = len(mathtext_demos)
    # Colors used in Matplotlib online documentation.
    mpl_grey_rgb = (51 / 255, 51 / 255, 51 / 255)

    # Creating figure and axis.
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.90],
                      facecolor="white", frameon=False)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Calculating Surface Integral ...",
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

def call_or_p():
    global orient
    #positive = 1
    orient = 1

def call_or_n():
    global orient
    #negative = 0
    orient = 0

def call_compute():
    fx = ent_func_x.get()
    fy = ent_func_y.get()
    fz = ent_func_z.get()
    a=ent_s_x.get()
    b=ent_s_y.get()
    c=ent_s_z.get()
    d = ent_u1.get()
    aa = ent_u2.get()
    bb = ent_v1.get()
    cc = ent_v2.get()
    dd = ent_sfunc.get()
    a1 = ent_x1.get()
    a2 = ent_x2.get()
    a3 = ent_y1.get()
    a4 = ent_y2.get()
    a5 = ent_z1.get()
    a6 = ent_z2.get()
    surface_integral_vf(fx,fy,fz,a,b,c,d,aa,bb,cc,dd,a1,a2,a3,a4,a5,a6)
    
def call_reset():
    ent_func_x.delete(0, 'end')
    ent_func_y.delete(0, 'end')
    ent_func_z.delete(0, 'end')
    ent_u1.delete(0,'end')
    ent_u2.delete(0,'end')
    ent_v1.delete(0,'end')
    ent_v2.delete(0,'end')
    ent_s_x.delete(0,'end')
    ent_s_y.delete(0,'end')
    ent_s_z.delete(0,'end')
    ent_sfunc.delete(0,'end')
    ent_x1.delete(0,'end')
    ent_x2.delete(0,'end')
    ent_y1.delete(0,'end')
    ent_y2.delete(0,'end')
    ent_z1.delete(0,'end')
    ent_z2.delete(0,'end')
    ent_func_x.insert(0,"0")
    ent_func_y.insert(0,"0")
    ent_func_z.insert(0,"0")
    ent_u1.insert(0,"0")
    ent_u2.insert(0,"0")
    ent_v1.insert(0,"0")
    ent_v2.insert(0,"0")
    ent_s_x.insert(0,"0")
    ent_s_y.insert(0,"0")
    ent_s_z.insert(0,"0")
    ent_sfunc.insert(0,"")
    ent_x1.insert(0,"0")
    ent_x2.insert(0,"0")
    ent_y1.insert(0,"0")
    ent_y2.insert(0,"0")
    ent_z1.insert(0,"0")
    ent_z2.insert(0,"0")

#main
window = tk.Tk()
window.geometry("800x700")
#window.configure(bg='#856ff8')
#window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='C:/Users/user/.spyder-py3/DI.png'))
window.title("Line Integrals Calculator")
Label(window, text="Give the function F(x,y,z)=[F1(x,y,z) , F2(x,y,z) , F3(x,y,z)] for integration:",font=("Arial",10)).place(x=0,y=1)
var_fx = tk.StringVar()
var_fy = tk.StringVar()
var_fz = tk.StringVar()
var_t1 = tk.StringVar()
var_t2 = tk.StringVar()
var_sx = tk.StringVar()
var_sy = tk.StringVar()
var_sz = tk.StringVar()
var_ua = tk.StringVar()
var_ub = tk.StringVar()
var_va = tk.StringVar()
var_vb = tk.StringVar()
var_sfunc = tk.StringVar()
var_x1 = tk.StringVar()
var_x2 = tk.StringVar()
var_y1 = tk.StringVar()
var_y2 = tk.StringVar()
var_z1 = tk.StringVar()
var_z2 = tk.StringVar()

Label(window, text="F1 = ").place(x=0,y=25)
ent_func_x = Entry(window, textvariable=var_fx)
ent_func_x.place(x=30,y=25)
Label(window, text="F2 = ").place(x=0,y=50)
ent_func_y = Entry(window, textvariable=var_fy)
ent_func_y.place(x=30,y=50)
Label(window, text="F3 = ").place(x=0,y=75)
ent_func_z = Entry(window, textvariable=var_fz)
ent_func_z.place(x=30,y=75)

Label(window, text="Orientation of surface is positive or negative?").place(x=0,y=100)
Button(window,text="Positive", command=call_or_p).place(x=0,y=125)
Button(window,text="Negative", command=call_or_n).place(x=100,y=125)
global orient
orient = 1
axy = 125
Label(window, text="Give the surface s(u,v) = [x(u,v) , y(u,v) , z(u,v)] :",font=("Arial",10)).place(x=0,y=axy+25)

Label(text="x(u,v) =").place(x=0,y=axy+50)
ent_s_x = Entry(window, textvariable=var_sx)
ent_s_x.place(x=45,y=axy+50)
Label(text="y(u,v) =").place(x=0,y=axy+75)
ent_s_y = Entry(window, textvariable=var_sy)
ent_s_y.place(x=45,y=axy+75)
lbl_cz = Label(text="z(u,v) =").place(x=0,y=axy+100)
ent_s_z = Entry(window, textvariable=var_sz)
ent_s_z.place(x=45,y=axy+100)

Label(window, text="Give the edges u1 and u2:",font=("Arial",10)).place(x=0,y=axy+125)
Label(text="u1 =").place(x=0,y=axy+150)
ent_u1 = Entry(window, textvariable=var_ua)
ent_u1.place(x=30,y=axy+150)
Label(text="u2 =").place(x=0,y=axy+175)
ent_u2 = Entry(window, textvariable=var_ub)
ent_u2.place(x=30,y=axy+175)

Label(window, text="Give the edges v1 and v2:",font=("Arial",10)).place(x=0,y=axy+200)
Label(text="v1 =").place(x=0,y=axy+225)
ent_v1 = Entry(window, textvariable=var_va)
ent_v1.place(x=30,y=axy+225)
Label(text="v2 =").place(x=0,y=axy+250)
ent_v2 = Entry(window, textvariable=var_vb)
ent_v2.place(x=30,y=axy+250)

Label(window, text="Or give the function s(x,y,z)=0 ,which describes the surface:").place(x=0,y=axy+275)
Label(text="s(x,y,z)=").place(x=0,y=axy+300)
ent_sfunc =Entry(window, textvariable=var_sfunc)
ent_sfunc.place(x=50,y=axy+300)
Label(text="=0").place(x=175,y=axy+300)

Label(window, text="Give the edges for x,y,z:").place(x=0,y=axy+325)
Label(window, text="x1=" ).place(x=0,y=axy+350)
ent_x1 = Entry(window,textvariable=var_x1)
ent_x1.place(x=30,y=axy+350)
Label(window, text="x2=" ).place(x=170,y=axy+350)
ent_x2 = Entry(window,textvariable=var_x2)
ent_x2.place(x=200,y=axy+350)
Label(window, text="y1=" ).place(x=0,y=axy+375)
ent_y1 = Entry(window,textvariable=var_y1)
ent_y1.place(x=30,y=axy+375)
Label(window, text="y2=" ).place(x=170,y=axy+375)
ent_y2 = Entry(window,textvariable=var_y2)
ent_y2.place(x=200,y=axy+375)
Label(window, text="z1=" ).place(x=0,y=axy+400)
ent_z1 = Entry(window,textvariable=var_z1)
ent_z1.place(x=30,y=axy+400)
Label(window, text="z2=" ).place(x=170,y=axy+400)
ent_z2 = Entry(window,textvariable=var_z2)
ent_z2.place(x=200,y=axy+400)

Button(window, text="Compute",command=call_compute).place(x=0,y=600)

Button(window, text="Reset", command=call_reset).place(x=150, y=600)

Button(window, text="Exit", command=window.destroy).place(x=300,y=600)

#Button(window, text="Theory", command=call_theory).place(x=150,y=a+60)

window.mainloop()
