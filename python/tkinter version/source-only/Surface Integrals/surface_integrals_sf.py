# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:18:22 2022

@author: user
"""
from sympy import symbols, diff, integrate, Integral, latex, sqrt, sin, cos, exp
from sympy.parsing.sympy_parser import parse_expr
import tkinter as tk
from tkinter import Label , Entry , Button
#import matplotlib
import matplotlib.pyplot as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#matplotlib.use('TkAgg')

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
        print("Warning! Inverting Inputs ...")
        #Label(window,text="Warning! Inverting Inputs ...").place(x=400,y=0)
        a,b = swap_values(a,b)
    else:
        print("No errors detected")
        #Label(window,text="No errors detected").place(x=400,y=0)
    return a,b
"""
def graph_latex(str_a,str_b,str_f,str_var,csx,csy):
    #if you use the console the you don't need this function
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
def surface_integral(func,s1,s2,s3,a,b,c,d):
    f, sx, sy, sz = symbols('f sx sy sz')
    u1, u2, v1, v2 = symbols('u1 u2 v1 v2')
    x, y, z, v, u = symbols('x y z v u')
    #csx = 450
    #csy = 20
    #Label(window, text="Transforming Surface integral to Double integral").place(x=csx,y=csy)
    #print("From Surface integral to Double Integral . . .")
    f = parse_expr(func)
    sx = parse_expr(s1)
    sy = parse_expr(s2)
    sz = parse_expr(s3)
    u1 = parse_expr(a)
    u2 = parse_expr(b)
    v1 = parse_expr(c)
    v2 = parse_expr(d)
    #print("Step 1 - Calculate ds/dv and ds/du")
    #Label(window,text="Step 1 - Calculate ds/dv and ds/du").place(x=csx,y=csy+30)
    #step 1: ds/dv and ds/du =;
    dvsx = diff(sx,v)
    dvsy = diff(sy,v)
    dvsz = diff(sz,v)
    dusx = diff(sx,u)
    dusy = diff(sy,u)
    dusz = diff(sz,u)
    #print("Step 2- Calculate the cross product of the above derivatives")
    #Label(window,text="Step 2- Calculate the cross product of the above derivatives").place(x=csx,y=csy+60)
    #step 2: cross product ds/du x ds/dv = ;
    va = dusy*dvsz-dvsy*dusz
    vb = dvsx*dusz-dusx*dvsz
    vc = dusx*dvsy-dvsx*dusy
    #print("Step 3 - Calculate the norm of the above vector")
    #Label(window, text="Step 3 - Calclate the norm of the above vector").place(x=csx,y=csy+90)
    #step 3: norm of cross product
    normv = sqrt(va**2 + vb**2 + vc**2)
    #pprint(normv)
    #print("Step 4 - Replace x,y,z with x(u,v),y(u,v),z(u,v) ")
    #Label(window, text="Step 4 - Replace x,y,z with x(u,v),y(u,v),z(u,v) ").place(x=csx,y=csy+120)
    #step 4: replace x,y,z with s
    f1 = f.subs(x,sx)
    f2 = f1.subs(y,sy)
    f3 = f2.subs(z,sz)
    #print("Step 5 - The function f(u,v) is:")
    #Label(window, text="Step 5 - The function f(u,v) is:").place(x=csx,y=csy+150)
    #step 5: new integral is double
    fnew = f3*normv
    #pprint(fnew)
    #csy = csy + 150
    #print("Calculating Double Integral ...")
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
            "Step 1 - Calculate ds/dv and ds/du:":
                r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(dvsx)+" , "+latex(dvsy)+" , "+latex(dvsz)+" ]$"
                "\n"
                r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(dusx)+" , "+latex(dusy)+" , "+latex(dusz)+" ]$",
            "Step 2 - Calculate the cross product:":
                r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(va)+" , "+latex(vb)+" , "+latex(vc)+" ]$", 
            "Step 3 - Calculate the norm of the above vector:":
                r"$ \parallel \frac{ \partial s(u,v) }{ \partial v} \times \frac{ \partial s(u,v) }{ \partial u} \parallel =  "+latex(normv)+" $", 
            "Step 4 - Replacing in f(x,y,z):":
                r"$ x$ "+" with "+" x(t) $"
                r"$ y$ "+" with "+" y(t) $"
                r"$ z$ "+" with "+" z(t) $",
            "The new f(t) is":
                r"$ f(t) = "+latex(f3)+" $",
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
        }
        """
        print("D is Simple u and v.")
        print("First integral is:")
        pprint(Integral(fnew,(u,u1,u2)))
        print("which gives:")
        pprint(I1)
        print("Second integral is:")
        pprint(Integral(I1,(v,v1,v2)))
        print("which gives the final result:")
        pprint(I)
        """
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
        I1 = integrate(f,(u,u1,u2))
        I = integrate(I1,(v,v1,v2))
        mathtext_demos = {
            "Header demo":
                "",
            "From Surface Integral to Double Integral . . . :":
                "",
            "Step 1 - Calculate ds/dv and ds/du:":
                r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(dvsx)+" , "+latex(dvsy)+" , "+latex(dvsz)+" ]$"
                "\n"
                r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(dusx)+" , "+latex(dusy)+" , "+latex(dusz)+" ]$",
            "Step 2 - Calculate the cross product:":
                r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(va)+" , "+latex(vb)+" , "+latex(vc)+" ]$", 
            "Step 3 - Calculate the norm of the above vector:":
                r"$ \parallel \frac{ \partial s(u,v) }{ \partial v} \times \frac{ \partial s(u,v) }{ \partial u} \parallel =  "+latex(normv)+" $", 
            "Step 4 - Replacing in f(x,y,z):":
                r"$ x$ "+" with "+" x(t) $"
                r"$ y$ "+" with "+" y(t) $"
                r"$ z$ "+" with "+" z(t) $",
            "The new f(t) is":
                r"$ f(t) = "+latex(f3)+" $",
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
        }
        """
        print("D is Simple u.")
        print("First integral is:")
        pprint(Integral(fnew,(u,u1,u2)))
        print("which gives:")
        pprint(I1)
        print("Second integral is:")
        pprint(Integral(I1,(v,v1,v2)))
        print("which gives the final result:")
        pprint(I)
        """
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
        I1 = integrate(f,(v,v1,v2))
        I = integrate(I1,(u,u1,u2))
        mathtext_demos = {
            "Header demo":
                "",
            "From Surface Integral to Double Integral . . . :":
                "",
            "Step 1 - Calculate ds/dv and ds/du:":
                r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(dvsx)+" , "+latex(dvsy)+" , "+latex(dvsz)+" ]$"
                "\n"
                r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(dusx)+" , "+latex(dusy)+" , "+latex(dusz)+" ]$",
            "Step 2 - Calculate the cross product:":
                r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(va)+" , "+latex(vb)+" , "+latex(vc)+" ]$", 
            "Step 3 - Calculate the norm of the above vector:":
                r"$ \parallel \frac{ \partial s(u,v) }{ \partial v} \times \frac{ \partial s(u,v) }{ \partial u} \parallel =  "+latex(normv)+" $", 
            "Step 4 - Replacing in f(x,y,z):":
                r"$ x$ "+" with "+" x(t) $"
                r"$ y$ "+" with "+" y(t) $"
                r"$ z$ "+" with "+" z(t) $",
            "The new f(t) is":
                r"$ f(t) = "+latex(f3)+" $",
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
        }
        """
        print("D is Simple v.")
        print("First integral is:")
        pprint(Integral(fnew,(v,v1,v2)))
        print("which gives:")
        pprint(I1)
        print("Second integral is:")
        pprint(Integral(I1,(u,u1,u2)))
        print("which gives the final result:")
        pprint(I)
        """
        """
        Label(window, text="D is Simple v.").place(x=csx,y=csy+30)
        Label(window, text="First integral is:").place(x=csx,y=csy+50)
        graph_latex(latex(v1),latex(v2),latex(fnew),"v",csx,csy+80)
        Label(window, text="which gives:").place(x=csx,y=csy+130)
        graph_latex("0","0",latex(I1),"0",csx,csy+150)
        Label(window, text="Second integral is:").place(x=csx,y=csy+200)
        graph_latex(latex(u1),latex(u2),latex(I1),"u",csx,csy+220)
        Label(window, text="which gives:").place(x=csx,y=csy+270)
        graph_latex("0","0",latex(I),"0",csx,csy+290)
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
    

def call_compute():
    ff = ent_func.get()
    a=ent_s_x.get()
    b=ent_s_y.get()
    c=ent_s_z.get()
    d = ent_u1.get()
    aa = ent_u2.get()
    bb = ent_v1.get()
    cc = ent_v2.get()
    surface_integral(ff,a,b,c,d,aa,bb,cc)
    
def call_reset():
    ent_func.delete(0, 'end')
    ent_u1.delete(0,'end')
    ent_u2.delete(0,'end')
    ent_v1.delete(0,'end')
    ent_v2.delete(0,'end')
    ent_s_x.delete(0,'end')
    ent_s_y.delete(0,'end')
    ent_s_z.delete(0,'end')
    ent_func.insert(0,"0")
    ent_u1.insert(0,"0")
    ent_u2.insert(0,"0")
    ent_v1.insert(0,"0")
    ent_v2.insert(0,"0")
    ent_s_x.insert(0,"0")
    ent_s_y.insert(0,"0")
    ent_s_z.insert(0,"0")


#main
window = tk.Tk()
window.geometry("800x400")
#window.configure(bg='#856ff8')
#window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='C:/Users/user/.spyder-py3/DI.png'))
window.title("Line Integrals Calculator")
Label(window, text="Give the function f(x,y,z) for integration:",font=("Arial",10)).place(x=0,y=1)
var_f = tk.StringVar()
var_t1 = tk.StringVar()
var_t2 = tk.StringVar()
var_sx = tk.StringVar()
var_sy = tk.StringVar()
var_sz = tk.StringVar()
var_ua = tk.StringVar()
var_ub = tk.StringVar()
var_va = tk.StringVar()
var_vb = tk.StringVar()
var_a = tk.StringVar()
var_b = tk.StringVar()

ent_func = Entry(window, textvariable=var_f)
ent_func.place(x=230,y=2)

Label(window, text="Give the surface s(u,v) = [x(u,v) , y(u,v) , z(u,v)] :",font=("Arial",10)).place(x=0,y=25)

Label(text="x(u,v) =").place(x=0,y=50)
ent_s_x = Entry(window, textvariable=var_sx)
ent_s_x.place(x=45,y=50)
Label(text="y(u,v) =").place(x=0,y=75)
ent_s_y = Entry(window, textvariable=var_sy)
ent_s_y.place(x=45,y=75)
lbl_cz = Label(text="z(u,v) =").place(x=0,y=100)
ent_s_z = Entry(window, textvariable=var_sz)
ent_s_z.place(x=45,y=100)

Label(window, text="Give the edges u1 and u2:",font=("Arial",10)).place(x=0,y=125)
Label(text="u1 =").place(x=0,y=150)
ent_u1 = Entry(window, textvariable=var_ua)
ent_u1.place(x=30,y=150)
Label(text="u2 =").place(x=0,y=175)
ent_u2 = Entry(window, textvariable=var_ub)
ent_u2.place(x=30,y=175)

Label(window, text="Give the edges v1 and v2:",font=("Arial",10)).place(x=0,y=200)
Label(text="v1 =").place(x=0,y=225)
ent_v1 = Entry(window, textvariable=var_va)
ent_v1.place(x=30,y=225)
Label(text="v2 =").place(x=0,y=250)
ent_v2 = Entry(window, textvariable=var_vb)
ent_v2.place(x=30,y=250)

Button(window, text="Compute",command=call_compute).place(x=0,y=300)

Button(window, text="Reset", command=call_reset).place(x=150, y=300)

Button(window, text="Exit", command=window.destroy).place(x=300,y=300)

#Button(window, text="Theory", command=call_theory).place(x=150,y=a+60)

window.mainloop()
