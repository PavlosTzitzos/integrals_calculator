#import libraries :
from sympy import exp
from sympy import symbols
from sympy import integrate
from sympy import cos
from sympy import sin
from sympy.parsing.sympy_parser import parse_expr
from tkinter import Label
from tkinter import Button
from tkinter import Entry
import tkinter
import tkinter as tk
from sympy import latex
import matplotlib.pyplot as plt

#create the variable for cartesian or polar coordinates
global pc

def sym_compare(a,b):
    """
        compare two sympy symbols a b :
        return value : condition
        1 : a > b
        -1: a < b
        0 : a = b
    """
    d = a-b
    if d.is_positive:
        return 1
    elif d.is_negative:
        return -1
    else:
        return 0

def swap_values(a,b):
    """
        Swaps 2 values of variables a and b:
        a_new <-- b_old
        b_new <-- a_old
        returns new values of a and b
    """
    temp = a
    a = b
    b = temp
    return a, b

def warning_one(a,b):
    """
        A warning message appears when swap function is called
        when a and b are : a > b
        returns new values of a and b
    """
    if sym_compare(a,b) ==1:
        Label(window,text="Warning! Inverting Inputs ...").place(x=400,y=0)
        a,b = swap_values(a,b)
    else:
        Label(window,text="No errors detected").place(x=400,y=0)
    return a,b

def di_main_func(fnct,xa,xb,yc,yd,pc,ra,rb,tc,td,k1,k2,ax,by):
    """
    main function starts here:
    first declare symbols that the script requires
    then ask for input in terminal
    """
    x, y, r, theta = symbols('x y r theta')
    x1, x2, y1, y2 = symbols('x1 x2 y1 y2')
    kx, ky, a, b = symbols('k1 k2 ax by')
    """
        from strings convert to sympy objects:
    """
    f=parse_expr(fnct)
    x1=parse_expr(xa)
    x2=parse_expr(xb)
    y1=parse_expr(yc)
    y2=parse_expr(yd)
    r1=parse_expr(ra)
    r2=parse_expr(rb)
    theta1=parse_expr(tc)
    theta2=parse_expr(td)
    kx=parse_expr(k1)
    ky=parse_expr(k2)
    a=parse_expr(ax)
    b=parse_expr(by)
    csx=400
    csy=20
    Label(window, text="Calculating Double Integral ...").place(x=csx,y=csy)
    """
        Starting calculations:
         main idea is to check for the cases that are explained in readme.md file
         and then decide the series of integration
        
       Start with cartesian coordinates and then go to polar coordinates
    """
    if pc == 0: #cartesian coordinates
        if (x1.is_number==1 and x2.is_number==1 and y1.is_number==1 and y2.is_number==1):
            """
                case 1 from readme.md file
            """
            x1,x2 = warning_one(x1,x2)
            y1,y2 = warning_one(y1,y2)
            I1 = integrate(f,(x,x1,x2))
            I = integrate(I1,(y,y1,y2))
            """
                after calculating create the latex for the answer :
            """
            mathtext_demos = {
                "Header demo":
                    r"$You~entered: \int ^{"+latex(y2)+"} _{"+latex(y1)+"} \int ^{"+latex(x2)+"} _{"+latex(x1)+"} "+latex(f)+" dx dy$",
                "First Integral is:":
                    r"$I_1 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(f)+" dx $",
                "which gives:":
                    r"$I_1 = "+latex(I1)+"$",
                "Second Integral is: ":
                    r"$I_2 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(I1)+" dy $",
                "which gives final result:":
                    r"$I_2 = "+latex(I)+" $",
            }
            
        elif((x1.is_number==0 or x2.is_number==0) and y1.is_number==1 and y2.is_number==1):
            """
                case 2 or 3 from readme.md file
            """
            y1,y2 = warning_one(y1,y2)
            I1 = integrate(f,(x,x1,x2))
            I = integrate(I1,(y,y1,y2))
            """
                after calculating create the latex for the answer :
            """
            mathtext_demos = {
                "Header demo":
                    r"$You~entered: \int ^{"+latex(y2)+"} _{"+latex(y1)+"} \int ^{"+latex(x2)+"} _{"+latex(x1)+"} "+latex(f)+" dx dy$",
                "First Integral is:":
                    r"$I_1 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(f)+" dx $",
                "which gives:":
                    r"$I_1 = "+latex(I1)+"$",
                "Second Integral is: ":
                    r"$I_2 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(I1)+" dy $",
                "which gives final result:":
                    r"$I_2 = "+latex(I)+" $",
            }
            
        else:
            """
                case 4 or 5 from readme.md file
            """
            x1,x2 = warning_one(x1,x2)
            I1 = integrate(f,(y,y1,y2))
            I = integrate(I1,(x,x1,x2))
            """
                after calculating create the latex for the answer :
            """
            mathtext_demos = {
                "Header demo":
                    r"$You~entered: \int ^{"+latex(x2)+"} _{"+latex(x1)+"} \int ^{"+latex(y2)+"} _{"+latex(y1)+"} "+latex(f)+" dy dx$",
                "First Integral is:":
                    r"$I_1 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(f)+" dy $",
                "which gives:":
                    r"$I_1 = "+latex(I1)+"$",
                "Second Integral is: ":
                    r"$I_2 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(I1)+" dx $",
                "which gives final result:":
                    r"$I_2 = "+latex(I)+" $",
            }
            
    elif pc==1:
        """
            polar coordinates:
        """
        fp = f.subs([(x, r*cos(theta)+kx),(y, r*sin(theta)+ky)])
        I1 = integrate(fp*r,(r,r1,r2))
        I = integrate(I1,(theta,theta1,theta2))
        """
            after calculating create the latex for the answer :
        """
        mathtext_demos = {
            "Header demo":
                r"$You~entered: \int ^{"+latex(theta2)+"} _{"+latex(theta1)+"} \int ^{"+latex(r2)+"} _{"+latex(r1)+"} "+latex(fp)+" \cdot r dr d $"
                r"$ \theta$",
            "Change of variables, using polar coordinates:":
                "Replace: "
                r"$ x $"" with "r"$ r \cdot cos( \theta ) + K_x $"
                " and "r"$ y $"" with "r"$ r \cdot sin( \theta ) + K_y $",
            "The new function is: ":
                r"$ f(r, \theta) = "+latex(fp)+" $",
            "First Integral is:":
                r"$I_1 = \int^{"+latex(r2)+"}_{"+latex(r1)+"} "+latex(fp)+" \cdot r dr $",
            "which gives:":
                r"$I_1 = "+latex(I1)+"$",
            "Second Integral is: ":
                r"$I_2 = \int^{"+latex(theta2)+"}_{"+latex(theta1)+"} "+latex(I1)+" d$"
                r"$ \theta $",
            "which gives final result:":
                r"$I_2 = "+latex(I)+" $",
        }
        
    elif pc==2:
        """
            elliptical coordinates:
        """
        fp = f.subs([(x, a*r*cos(theta)+kx),(y, b*r*sin(theta)+ky)])
        I1 = integrate(fp*a*b*r,(r,r1,r2))
        I = integrate(I1,(theta,theta1,theta2))
        """
            after calculating create the latex for the answer :
        """
        mathtext_demos = {
            "Header demo":
                r"$You~entered: \int ^{"+latex(theta2)+"} _{"+latex(theta1)+"} \int ^{"+latex(r2)+"} _{"+latex(r1)+"} "+latex(f)+" \cdot a \cdot b \cdot r dr d $"
                r"$ \theta$",
            "Change of variables, using elliptical coordinates:":
                "Replace: "
                r"$ x $"" with "r"$ a \cdot r \cdot cos( \theta ) + K_x $"
                " and "r"$ y $"" with "r"$ b \cdot r \cdot sin( \theta ) + K_y $",
            "The new function is: ":
                r"$ f(r, \theta) = "+latex(fp)+" $",
            "First Integral is:":
                r"$I_1 = \int^{"+latex(r2)+"}_{"+latex(r1)+"} "+latex(fp)+" \cdot a \cdot b \cdot r dr $",
            "which gives:":
                r"$I_1 = "+latex(I1)+"$",
            "Second Integral is: ":
                r"$I_2 = \int^{"+latex(theta2)+"}_{"+latex(theta1)+"} "+latex(I1)+" d$"
                r"$ \theta $",
            "which gives final result:":
                r"$I_2 = "+latex(I)+" $",
        }
    """
        After the calculations print then image with latex using matplotlib
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
    ax.set_title("Calculating Double Integral ...",
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

def btn_di_ec(event):
    """
        event :
            button double integral elliptical coordinates is pressed last
        changes the global variable pc value to 2
    """
    global pc
    pc = 2

def btn_di_pc(event):
    """
        event :
            button double integral polar coordinates is pressed last
            changes the global variable pc value to 1
    """
    global pc
    pc = 1

def btn_di_cc(event):
    """
        event :
            button double integral cartesian coordinates is pressed last
        changes the global variable pc value to 0
    """
    global pc
    pc = 0
    
def call_compute():
    """After input arguments:
       > function f(x,y)
       > edges of integration: x1 <= x <= x2 , y1 <= y <= y2
       > edges of polar
       > edges of elliptical
       call the main function: di_main_func()   
    """
    ff = ent_func.get()
    a=ent_x1.get()
    b=ent_x2.get()
    c=ent_y1.get()
    d=ent_y2.get()
    aa=ent_r1.get()
    bb=ent_r2.get()
    cc=ent_theta1.get()
    dd=ent_theta2.get()
    aaa=ent_cx.get()
    bbb=ent_cy.get()
    ccc=ent_a.get()
    ddd=ent_b.get()
    global pc
    di_main_func(ff,a,b,c,d,pc,aa,bb,cc,dd,aaa,bbb,ccc,ddd)
    
    
def call_reset():
    """
        A reset function that makes all fields values 0.
        and length of axes of ellitical coordinates 1.
    """
    ent_func.delete(0, 'end')
    ent_x1.delete(0,'end')
    ent_x2.delete(0,'end')
    ent_y1.delete(0,'end')
    ent_y2.delete(0,'end')
    ent_r1.delete(0,'end')
    ent_r2.delete(0,'end')
    ent_theta1.delete(0,'end')
    ent_theta2.delete(0,'end')
    ent_cx.delete(0,'end')
    ent_cy.delete(0,'end')
    ent_a.delete(0,'end')
    ent_b.delete(0,'end')
    ent_func.insert(0,"0")
    ent_x1.insert(0,"0")
    ent_x2.insert(0,"0")
    ent_y1.insert(0,"0")
    ent_y2.insert(0,"0")
    ent_r1.insert(0,"0")
    ent_r2.insert(0,"0")
    ent_theta1.insert(0,"0")
    ent_theta2.insert(0,"0")
    ent_cx.insert(0,"0")
    ent_cy.insert(0,"0")
    ent_a.insert(0,"1")
    ent_b.insert(0,"1")

"""
    main function:
        create the window
        difine dimentions
        add title
"""
window = tk.Tk()
window.geometry("800x400")
window.title("Double Integrals Calculator")
"""
    create labels
    declare variables of tk
    create Entries
    place them inside the window
    add buttons for coordinates to change the global pc value
"""
Label(window, text="Give the function f(x,y) for integration:",font=("Arial",10)).place(x=0,y=1)
var_f = tk.StringVar()
var_x1 = tk.StringVar()
var_x2 = tk.StringVar()
var_y1 = tk.StringVar()
var_y2 = tk.StringVar()
var_r1 = tk.StringVar()
var_r2 = tk.StringVar()
var_theta1 = tk.StringVar()
var_theta2 = tk.StringVar()
var_cx = tk.StringVar()
var_cy = tk.StringVar()
var_a = tk.StringVar()
var_b = tk.StringVar()

ent_func = Entry(window, textvariable=var_f)
ent_func.place(x=200,y=2)

lbl_coor = Label(window, text="Choose type of coordinates:",font=("Arial",10)).place(x=0,y=50)
btn_cc = Button(window, text="Cartesian")
btn_cc.bind("<Button-1>", btn_di_cc)

btn_pc = Button(window, text="Polar")
btn_pc.bind("<Button-1>", btn_di_pc)

btn_ec = Button(window, text="Elliptical")
btn_ec.bind("<Button-1>", btn_di_ec)

btn_cc.place(x=0,y=70)
btn_pc.place(x=60,y=70)
btn_ec.place(x=98,y=70)

a=100
lbl_edges = Label(text="Insert Edges:",font=("Arial",10)).place(x=0,y=a)
lbl_x1 = Label(text="x1 =").place(x=0,y=a+20)
ent_x1 = Entry(window, textvariable=var_x1)
ent_x1.place(x=30,y=a+20)
ent_x1.insert(0,"0")
lbl_x2 = Label(text="x2 =").place(x=0,y=a+40)
ent_x2 = Entry(window, textvariable=var_x2)
ent_x2.place(x=30,y=a+40)
ent_x2.insert(0,"0")
lbl_y1 = Label(text="y1 =").place(x=150,y=a+20)
ent_y1 = Entry(window, textvariable=var_y1)
ent_y1.place(x=180,y=a+20)
ent_y1.insert(0,"0")
lbl_y2 = Label(text="y2 =").place(x=150,y=a+40)
ent_y2 = Entry(window, textvariable=var_y2)
ent_y2.place(x=180,y=a+40)
ent_y2.insert(0,"0")
a=a+60
lbl_edges = Label(text="Insert Edges for polar coordinates:",font=("Arial",10)).place(x=0,y=a)
lbl_r1 = Label(text="r1 =").place(x=0,y=a+20)
ent_r1 = Entry(window, textvariable=var_r1)
ent_r1.place(x=30,y=a+20)
ent_r1.insert(0,"0")
lbl_r2 = Label(text="r2 =").place(x=0,y=a+40)
ent_r2 = Entry(window, textvariable=var_r2)
ent_r2.place(x=30,y=a+40)
ent_r2.insert(0,"0")
lbl_theta1 = Label(text="θ1 =").place(x=150,y=a+20)
ent_theta1 = Entry(window, textvariable=var_theta1)
ent_theta1.place(x=180,y=a+20)
ent_theta1.insert(0,"0")
lbl_theta2 = Label(text="θ2 =").place(x=150,y=a+40)
ent_theta2 = Entry(window, textvariable=var_theta2)
ent_theta2.place(x=180,y=a+40)
ent_theta2.insert(0,"0")
a=a+60
lbl_center = Label(text="Center of coordinate system (default is K(0,0)):",font=("Arial",10)).place(x=0,y=a)
lbl_cx = Label(text="Kx =").place(x=0,y=a+20)
ent_cx = Entry(window,textvariable=var_cx)
ent_cx.place(x=30,y=a+20)
ent_cx.insert(0,"0")
lbl_cy = Label(text="Ky =").place(x=150,y=a+20)
ent_cy = Entry(window,textvariable=var_cy)
ent_cy.place(x=180,y=a+20)
ent_cy.insert(0,"0")
a=a+60
lbl_center = Label(text="Length of axes for elliptical coordinates (default (a=1,b=1,c=1)):",font=("Arial",10)).place(x=0,y=a)
lbl_a = Label(text="a =").place(x=0,y=a+20)
ent_a = Entry(window,textvariable=var_a)
ent_a.place(x=30,y=a+20)
ent_a.insert(0,"1")
lbl_b = Label(text="b =").place(x=150,y=a+20)
ent_b = Entry(window,textvariable=var_b)
ent_b.place(x=180,y=a+20)
ent_b.insert(0,"1")
a=a+60
"""
    final buttons:
        compute : to call compute function and start calculations
        reset   : to call reset function 
        exit    : to exit the application
"""
Button(window, text="Compute",command=call_compute).place(x=0,y=a)

Button(window, text="Reset", command=call_reset).place(x=150, y=a)

Button(window, text="Exit", command=window.destroy).place(x=300,y=a)

"""
    end the main loop :
"""
window.mainloop()
