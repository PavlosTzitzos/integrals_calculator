# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 20:11:43 2022

@author: user
"""
from sympy import symbols, diff, integrate, latex
from sympy.parsing.sympy_parser import parse_expr
from tkinter import Label
from tkinter import Button
from tkinter import Entry
import tkinter
import tkinter as tk
import matplotlib.pyplot as plt

global dc

def curve_integral_vf(funcx, funcy, funcz,c1,c2,c3,ta,tb,a1,a2,a3,b1,b2,b3):
    x, y, z, t, t1, t2 = symbols('x y z t t1 t2')
    fx, fy, fz = symbols('fx fy fz')
    cx, cy, cz, dcx, dcy, dcz = symbols('cx cy cz dcx dcy dcz')
    a=0
    b=0
    if a1!="" and a2!="" and a3!="":
        a = 1
        #print("Parametrize the line AB:")
        xa = parse_expr(a1)
        ya = parse_expr(a2)
        za = parse_expr(a3)
        xb = parse_expr(b1)
        yb = parse_expr(b2)
        zb = parse_expr(b3)
        cx = (1-t)*xa+t*xb
        cy = (1-t)*ya+t*yb
        cz = (1-t)*za+t*zb
        t1 = 0
        t2 = 1
        #print(" x(t)= ",cx,"\n","y(t)= ",cy,"\n","z(t)= ",cz,"\n","with t in [0,1] \n")
    else:
        a = 2
        cx = parse_expr(c1)
        cy = parse_expr(c2)
        cz = parse_expr(c3)
        t1 = parse_expr(ta)
        t2 = parse_expr(tb)
        
    fx = parse_expr(funcx)
    fy = parse_expr(funcy)
    fz = parse_expr(funcz)
    #print(fx, fy, fz)
    
    dcx = diff(cx,t)
    dcy = diff(cy,t)
    dcz = diff(cz,t)
    fx1 = fx.subs(x,cx)
    fx2 = fx1.subs(y,cy)
    fx3 = fx2.subs(z,cz)
    fy1 = fy.subs(x,cx)
    fy2 = fy1.subs(y,cy)
    fy3 = fy2.subs(z,cz)
    fz1 = fz.subs(x,cx)
    fz2 = fz1.subs(y,cy)
    fz3 = fz2.subs(z,cz)
    fnew = fx3*dcx+fy3*dcy+fz3*dcz
    #print("Check if the vector field is conservative or not")
    #print("Check if : curl(F) = 0")
    #checking if is conservative : curl x F = 0
    Gx = diff(fz,y) - diff(fy,z)
    Gy = diff(fx,z) - diff(fz,x)
    Gz = diff(fy,x) - diff(fx,y)
    if Gx == 0 and Gy == 0 and Gz == 0:
        b = 1
        #print("Conservative Vector Field: curl(F)=0 ")
        fix = integrate(fx,x)   #step 1
        fdy = diff(fix,y)       #step 2
        gdy = fy-fdy
        g = integrate(gdy,y)
        fixnew = fix + g           #step 3
        fdz = diff(fixnew,z)       #step 4
        hdz = fz-fdz
        h = integrate(hdz,z)
        fi = fixnew + h           #step 5
        f1 = fi.subs(x,cx)
        f2 = f1.subs(y,cy)
        f3 = f2.subs(z,cz)
        f4 = f3.subs(t,t2)-f3.subs(t,t1)
        #print("Result is: ")
        #pprint(f4)
    else:
        b = 2
        I = integrate(fnew,(t,t1,t2))
        """
        print("Not Conservative Vector Field: curl(F) not 0 ")
        print("Replace F(x,y,z) with f(t) dot c'(t)")
        print("Calculating Integral:")
        pprint(Integral(fnew,(t,t1,t2)))
        print("Result is: ")
        pprint(I)
        """
    
    if a==1 and b==1:
        mathtext_demos = {
            "Header demo":
                "",
            "Parametrize the line AB:":
                r"$x_{(t)} = (1-t) \cdot x_A + t \cdot x_B = "+latex(cx)+" $"
                "\n"
                r"$y_{(t)} = (1-t) \cdot y_A + t \cdot y_B = "+latex(cy)+" $"
                "\n"
                r"$z_{(t)} = (1-t) \cdot z_A + t \cdot z_B = "+latex(cz)+" $"
                "\n"
                "with "r"$ 0 \le t \le 1 $",
            "Checking if F is conservative:":
                r"$ \vec{\nabla} \times \vec{F} = [0,0,0] $",
            "Now ge can find a function f such that:":
                r"$ \nabla f(x,y,z) = \vec{F} (x,y,z) \newline $",
            "Step 1 - Integrate F1":
                r"$ f (x,y,z) = \int F_1 dx = \phi_1 + g(y,z) = "+latex(fix)+" + g(y,z) $",
            "Step 2 - Differentiate f : ":
                r"$ \frac{ \partial f (x,y,z) }{ \partial y } = \frac{ \partial \phi_1 }{ \partial y } + \frac{ \partial g }{ \partial y } = F_2$",
            "which gives the g function after integration with respect to y":
                r"$ g = "+latex(g)+" + h(z) $",
            "Now f becomes:":
                r"$ f(x,y,z) = \phi_1 + \phi_2 + h(z) = "+latex(fixnew)+" + h(z) $",
            "Step 3 - Differentiate f again : ":
                r"$ \frac{ \partial f (x,y,z) }{ \partial z } = \frac{ \partial \phi_1 }{ \partial z } + \frac{ \partial \phi_2 }{ \partial z } + \frac{ \partial h}{ \partial z}= F_3$",
            "which gives h after integration: ":
                r"$ h(z) = "+latex(h)+" + c $",
            "Finally f is: ":
                r"$f(x,y,z) = "+latex(f4)+" + c $",
        }
    elif a==1 and b==2:
        mathtext_demos = {
            "Header demo":
                "",
            "Parametrize the line AB:":
                r"$x_{(t)} = (1-t) \cdot x_A + t \cdot x_B = "+latex(cx)+" $"
                "\n"
                r"$y_{(t)} = (1-t) \cdot y_A + t \cdot y_B = "+latex(cy)+" $"
                "\n"
                r"$z_{(t)} = (1-t) \cdot z_A + t \cdot z_B = "+latex(cz)+" $"
                "\n"
                "with "r"$ 0 \le t \le 1 $",
            "Checking if F is conservative:":
                r"$ \vec{\nabla} \times \vec{F} \neq [0,0,0] $",
            "F is not conservative so we use the following:":
                "Replace: "r"$x$"+" with "+r"$x(t)$"+" , "+r"$y$"+" with "+r"$y(t)$"+" and "+r"$z$"+" with "+r"$z(t)$",
            "The new F(t) is: ":
                r"$F(t) = ["+latex(fx3)+" , "+latex(fy3)+" , "+latex(fz3)+"] $",
            "Differentiate the curve:":
                r"$ \dot{x}_{(t)} = "+latex(dcx)+" $"
                "\n"
                r"$ \dot{y}_{(t)} = "+latex(dcy)+" $"
                "\n"
                r"$ \dot{z}_{(t)} = "+latex(dcz)+" $",
            "The integral is":
                r"$ I = \int ^{"+latex(t2)+"} _{"+latex(t1)+"} "+latex(fnew)+" $",
            "which gives:":
                r"$I = "+latex(I)+"$"
        }
    elif a==2 and b==1:
        mathtext_demos = {
            "Header demo":
                "",
            "The curve is:":
                r"$x_{(t)} = "+latex(cx)+" $"
                "\n"
                r"$y_{(t)} = "+latex(cy)+" $"
                "\n"
                r"$z_{(t)} = "+latex(cz)+" $"
                "\n"
                "with "r"$ "+latex(t1)+" \le t \le "+latex(t1)+" $",
            "Checking if F is conservative:":
                r"$ \vec{\nabla} \times \vec{F} = [0,0,0] $",
            "Now ge can find a function f such that:":
                r"$ \nabla f(x,y,z) = \vec{F} (x,y,z) \newline $",
            "Step 1 - Integrate F1":
                r"$ f (x,y,z) = \int F_1 dx = \phi_1 + g(y,z) = "+latex(fix)+" + g(y,z) $",
            "Step 2 - Differentiate f : ":
                r"$ \frac{ \partial f (x,y,z) }{ \partial y } = \frac{ \partial \phi_1 }{ \partial y } + \frac{ \partial g }{ \partial y } = F_2$",
            "which gives the g function after integration with respect to y":
                r"$ g = "+latex(g)+" + h(z) $",
            "Now f becomes:":
                r"$ f(x,y,z) = \phi_1 + \phi_2 + h(z) = "+latex(fixnew)+" + h(z) $",
            "Step 3 - Differentiate f again : ":
                r"$ \frac{ \partial f (x,y,z) }{ \partial z } = \frac{ \partial \phi_1 }{ \partial z } + \frac{ \partial \phi_2 }{ \partial z } + \frac{ \partial h}{ \partial z}= F_3$",
            "which gives h after integration: ":
                r"$ h(z) = "+latex(h)+" + c $",
            "Finally f is: ":
                r"$f(x,y,z) = "+latex(f4)+" + c $",
        }
    elif a==2 and b==2:
        mathtext_demos = {
            "Header demo":
                "",
            "The curve is:":
                r"$x_{(t)} = "+latex(cx)+" $"
                "\n"
                r"$y_{(t)} = "+latex(cy)+" $"
                "\n"
                r"$z_{(t)} = "+latex(cz)+" $"
                "\n"
                "with "r"$ "+latex(t1)+" \le t \le "+latex(t1)+" $",
            "Checking if F is conservative:":
                r"$ \vec{\nabla} \times \vec{F} \neq [0,0,0] $",
            "F is not conservative so we use the following:":
                "Replace: "r"$x$"+" with "+r"$x(t)$"+" , "+r"$y$"+" with "+r"$y(t)$"+" and "+r"$z$"+" with "+r"$z(t)$",
            "The new F(t) is: ":
                r"$F(t) = ["+latex(fx3)+" , "+latex(fy3)+" , "+latex(fz3)+"] $",
            "Differentiate the curve:":
                r"$ \dot{x}_{(t)} = "+latex(dcx)+" $"
                "\n"
                r"$ \dot{y}_{(t)} = "+latex(dcy)+" $"
                "\n"
                r"$ \dot{z}_{(t)} = "+latex(dcz)+" $",
            "The integral is":
                r"$ I = \int ^{"+latex(t2)+"} _{"+latex(t1)+"} "+latex(fnew)+" $",
            "which gives:":
                r"$I = "+latex(I)+"$"
        }
    else:
        #error
        mathtext_demos = {
            "Header demo":
                "Error Wrong Input"
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
    ax.set_title("Calculating Line Integral ...",
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
    

def green_call():
    #print("Using Green's Theorem . . .")
    #Label(text="Using Green's Theorem . . .").place(x=320,y=0)
    if ent_func_z.get()=="0":
        #print("Cannot use Green's Theorem for 3D Vector Field.")
        #Label(text = "Cannot use Green's Theorem for 3D Vector Field.").place(x=320,y=30)
    else:
        #remember only for CLOSED curve c AND SIMPLE region D
        #call double integral with all possible inputs in a new window.
        #print("Calculating Double Integral")
    
    
def call_compute():
    ffx = ent_func_x.get()
    ffy = ent_func_y.get()
    ffz = ent_func_z.get()
    a=ent_curve_x.get()
    b=ent_curve_y.get()
    c=ent_curve_z.get()
    d = ent_t1.get()
    aa = ent_t2.get()
    bb = ent_xa.get()
    cc = ent_ya.get()
    dd = ent_za.get()
    ee = ent_xb.get()
    ff = ent_yb.get()
    gg = ent_zb.get()
    curve_integral_vf(ffx,ffy,ffz,a,b,c,d,aa,bb,cc,dd,ee,ff,gg)
    
def call_reset():
    ent_func_x.delete(0, 'end')
    ent_func_y.delete(0,'end')
    ent_func_z.delete(0,'end')
    ent_t1.delete(0,'end')
    ent_t2.delete(0,'end')
    ent_curve_x.delete(0,'end')
    ent_curve_y.delete(0,'end')
    ent_curve_z.delete(0,'end')
    ent_xa.delete(0,'end')
    ent_ya.delete(0,'end')
    ent_za.delete(0,'end')
    ent_func_x.insert(0,"0")
    ent_func_y.insert(0,"0")
    ent_func_z.insert(0,"0")
    ent_t1.insert(0,"0")
    ent_t2.insert(0,"0")
    ent_curve_x.insert(0,"0")
    ent_curve_y.insert(0,"0")
    ent_curve_z.insert(0,"0")
    

#main
window = tk.Tk()
window.geometry("480x550")
window.title("Line Integrals Calculator for Vector Functions")

var_fx = tk.StringVar()
var_fy = tk.StringVar()
var_fz = tk.StringVar()
var_t1 = tk.StringVar()
var_t2 = tk.StringVar()
var_cx = tk.StringVar()
var_cy = tk.StringVar()
var_cz = tk.StringVar()
var_kx = tk.StringVar()
var_ky = tk.StringVar()
var_kz = tk.StringVar()
var_xa = tk.StringVar()
var_ya = tk.StringVar()
var_za = tk.StringVar()
var_xb = tk.StringVar()
var_yb = tk.StringVar()
var_zb = tk.StringVar()

Label(window, text="Give the function F(x,y,z)=[F1 , F2 , F3] for integration:",font=("Arial",10)).place(x=0,y=1)
lbl_Fx = Label(text="F1(x,y,z)=").place(x=0,y=25)
ent_func_x = Entry(window, textvariable=var_fx)
ent_func_x.place(x=60,y=25)
lbl_Fx = Label(text="F2(x,y,z)=").place(x=0,y=50)
ent_func_y = Entry(window, textvariable=var_fy)
ent_func_y.place(x=60,y=50)
lbl_Fx = Label(text="F3(x,y,z)=").place(x=0,y=75)
ent_func_z = Entry(window, textvariable=var_fz)
ent_func_z.place(x=60,y=75)
ent_func_x.insert(0,"0")
ent_func_y.insert(0,"0")
ent_func_z.insert(0,"0")
Label(window, text="Give the curve c(t) = [x(t) , y(t) , z(t)] :",font=("Arial",10)).place(x=0,y=100)
lbl_cx = Label(text="x(t)=").place(x=0,y=125)
ent_curve_x = Entry(window, textvariable=var_cx)
ent_curve_x.place(x=30,y=125)
lbl_cy = Label(text="y(t)=").place(x=0,y=150)
ent_curve_y = Entry(window, textvariable=var_cy)
ent_curve_y.place(x=30,y=150)
lbl_cz = Label(text="z(t)=").place(x=0,y=175)
ent_curve_z = Entry(window, textvariable=var_cz)
ent_curve_z.place(x=30,y=175)

Label(window, text="Give the edges t1 and t2:",font=("Arial",10)).place(x=0,y=200)
lbl_cx = Label(text="t1 =").place(x=0,y=225)
ent_t1 = Entry(window, textvariable=var_t1)
ent_t1.place(x=30,y=225)
lbl_cy = Label(text="t2 =").place(x=0,y=250)
ent_t2 = Entry(window, textvariable=var_t2)
ent_t2.place(x=30,y=250)

Label(window, text="Or give the points of a line AB:",font=("Arial",10)).place(x=0,y=275)
lbl_xa = Label(text="xa =").place(x=0,y=300)
ent_xa = Entry(window, textvariable=var_xa)
ent_xa.place(x=30,y=300)
lbl_ya = Label(text="ya =").place(x=0,y=325)
ent_ya = Entry(window, textvariable=var_ya)
ent_ya.place(x=30,y=325)
lbl_za = Label(text="za =").place(x=0,y=350)
ent_za = Entry(window, textvariable=var_za)
ent_za.place(x=30,y=350)

lbl_xb = Label(text="xb =").place(x=200,y=300)
ent_xb = Entry(window, textvariable=var_xb)
ent_xb.place(x=230,y=300)
lbl_yb = Label(text="yb =").place(x=200,y=325)
ent_yb = Entry(window, textvariable=var_yb)
ent_yb.place(x=230,y=325)
lbl_zb = Label(text="zb =").place(x=200,y=350)
ent_zb = Entry(window, textvariable=var_zb)
ent_zb.place(x=230,y=350)

Label(text="If you have a circle centered in K(x0,y0,z0): (x-x0)^2 + (y-y0)^2 = r^2").place(x=0,y=370)
Label(text="then: c(t)=[r*cos(t)+x0 , r*sin(t)+y0 , z0] with t in [0,2π].").place(x=0,y=390)
Label(text="If you have an ellipse centered in K(x0,y0,z0): (x-x0/a)^2 + (y-y0/b)^2 = 1").place(x=0,y=410)
Label(text="then: c(t) = [a*cos(t) , b*sin(t), z0] with t in [0,2π].").place(x=0,y=430)
Label(text="Use Green's Theorem for any other curve that cannot be entered with above 2 ways.").place(x=0,y=450)
Button(window, text="Green's Thoerem", command=green_call).place(x=150,y=470)

Button(window, text="Compute",command=call_compute).place(x=30,y=500)

Button(window, text="Reset", command=call_reset).place(x=180, y=500)

Button(window, text="Exit", command=window.destroy).place(x=330,y=500)

window.mainloop()
