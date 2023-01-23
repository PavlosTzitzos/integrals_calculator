# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 20:13:30 2022

@author: user
"""
from sympy import sqrt, symbols, diff, integrate, latex
from sympy.parsing.sympy_parser import parse_expr
from tkinter import Label
from tkinter import Button
from tkinter import Entry
import tkinter
import tkinter as tk
import matplotlib.pyplot as plt

def curve_integral(func,c1,c2,c3,ta,tb):
    f, x, y, z, t, t1, t2 = symbols('f x y z t t1 t2')
    cx, cy, cz, dcx, dcy, dcz = symbols('cx cy cz dcx dcy dcz')
    f = parse_expr(func)
    cx = parse_expr(c1)
    cy = parse_expr(c2)
    cz = parse_expr(c3)
    t1 = parse_expr(ta)
    t2 = parse_expr(tb)
    dcx = diff(cx,t)
    dcy = diff(cy,t)
    dcz = diff(cz,t)
    f1 = f.subs(x,cx)
    f2 = f1.subs(y,cy)
    f3 = f2.subs(z,cz)
    fnew = f3*sqrt(dcx**2 + dcy**2 + dcz**2)
    I = integrate(fnew,(t,t1,t2))
    mathtext_demos = {
        "Header demo":
            r"$You~entered: \int ^{"+latex(t2)+"} _{"+latex(t1)+"} "+latex(f)+" dt $",
        "The curve is:":
            r"$ \vec{c} _{(t)} = ["+latex(cx)+" , "+latex(cy)+" , "+latex(cz)+" ]$",
        "Differentiate the curve:":
            r"$ \dot{ \vec{c} } _{(t)} = ["+latex(dcx)+" , "+latex(dcy)+" , "+latex(dcz)+" ]$",
        "The norm of the above vector is:":
            r"$ \parallel \dot{ \vec{c}} _{(t)} \parallel  = \sqrt{ ("+latex(dcx)+")^2 + ("+latex(dcy)+")^2 + ("+latex(dcz)+")^2 }$",
        "The function you entered is:":
            r"$f(x,y,z) = "+latex(f)+"$",
        "Replace:":
            r"$x$"+" with "+r"$x(t)$"+" , "+r"$y$"+" with "+r"$y(t)$"+" , and "+r"$z$"+" with "+r"$z(t)$",
        "which gives:":
            r"$ f(t) = "+latex(f3)+"$",
        "The Integral is: ":
            r"$I = \int^{"+latex(t2)+"}_{"+latex(t1)+"} "+latex(fnew)+" dt $",
        "which gives final result:":
            r"$I_2 = "+latex(I)+"$",
    }
    """
    print("Calculating Line Integral . . .")
    print("The new function f(t) is:")
    pprint(fnew)
    print("The integral is:")
    pprint(Integral(fnew,(t,t1,t2)))
    print("The result is:")
    pprint(I)
    """
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

def call_compute():
    ff = ent_func.get()
    a=ent_curve_x.get()
    b=ent_curve_y.get()
    c=ent_curve_z.get()
    d = ent_t1.get()
    aa = ent_t2.get()
    curve_integral(ff,a,b,c,d,aa)
    
def call_reset():
    ent_func.delete(0, 'end')
    ent_t1.delete(0,'end')
    ent_t2.delete(0,'end')
    ent_curve_x.delete(0,'end')
    ent_curve_y.delete(0,'end')
    ent_curve_z.delete(0,'end')
    ent_func.insert(0,"0")
    ent_t1.insert(0,"0")
    ent_t2.insert(0,"0")
    ent_curve_x.insert(0,"0")
    ent_curve_y.insert(0,"0")
    ent_curve_z.insert(0,"0")


#main
window = tk.Tk()
window.geometry("400x250")
window.title("Line Integrals Calculator")
Label(window, text="Give the function f(x,y,z) for integration:",font=("Arial",10)).place(x=0,y=1)
var_f = tk.StringVar()
var_t1 = tk.StringVar()
var_t2 = tk.StringVar()
var_cx = tk.StringVar()
var_cy = tk.StringVar()
var_cz = tk.StringVar()
var_kx = tk.StringVar()
var_ky = tk.StringVar()
var_kz = tk.StringVar()
var_a = tk.StringVar()
var_b = tk.StringVar()

ent_func = Entry(window, textvariable=var_f)
ent_func.place(x=230,y=2)

Label(window, text="Give the curve c(t) = [x(t) , y(t) , z(t)] :",font=("Arial",10)).place(x=0,y=25)

lbl_cx = Label(text="x(t)=").place(x=0,y=50)
ent_curve_x = Entry(window, textvariable=var_cx)
ent_curve_x.place(x=30,y=50)
lbl_cy = Label(text="y(t)=").place(x=0,y=75)
ent_curve_y = Entry(window, textvariable=var_cy)
ent_curve_y.place(x=30,y=75)
lbl_cz = Label(text="z(t)=").place(x=0,y=100)
ent_curve_z = Entry(window, textvariable=var_cz)
ent_curve_z.place(x=30,y=100)

Label(window, text="Give the edges t1 and t2:",font=("Arial",10)).place(x=0,y=125)
lbl_cx = Label(text="t1 =").place(x=0,y=150)
ent_t1 = Entry(window, textvariable=var_t1)
ent_t1.place(x=30,y=150)
lbl_cy = Label(text="t2 =").place(x=0,y=175)
ent_t2 = Entry(window, textvariable=var_t2)
ent_t2.place(x=30,y=175)

Button(window, text="Compute",command=call_compute).place(x=0,y=200)

Button(window, text="Reset", command=call_reset).place(x=150, y=200)

Button(window, text="Exit", command=window.destroy).place(x=300,y=200)

window.mainloop()
