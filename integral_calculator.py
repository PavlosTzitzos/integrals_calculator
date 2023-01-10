# -*- coding: utf-8 -*-
"""
Created on Sun May  8 15:27:36 2022

@author: vnavr
"""

import PySimpleGUI as sg
from sympy import latex
from sympy import symbols, diff, integrate, sqrt, sympify
from sympy import cos
from sympy import sin
from sympy.parsing.sympy_parser import parse_expr
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from sympy.plotting import plot3d, PlotGrid, plot
from sympy import plot_implicit, And

global language
language=1


sg.theme('LightGreen3')


help_int = ['ΑΠΛΟ ΟΛΟΚΛΗΡΩΜΑ','ΔΙΠΛΟ ΟΛΟΚΛΗΡΩΜΑ','ΤΡΠΛΟ ΟΛΟΚΛΗΡΩΜΑ','ΕΠΙΚΑΜΠΥΛΙΟ','ΕΠΙΦΑΝΕΙΑΚΟ','___________________','ΠΛΗΡΟΦΟΡΙΕΣ']


help_info = {help_int[0] :1,
             help_int[1] :2, 
             help_int[2] :3, 
             help_int[3] :4,
             help_int[4] :5,
             help_int[5] :6,
             help_int[6] :7
             }
#ΛΙΣΤΕΣ ΜΕΝΟΥ

text_frame = ['ΥΠΟΛΟΓΙΣΜΟΣ ΟΛΟΚΛΗΡΩΜΑΤΩΝ', 'ΔΙΠΛΟ ΟΛΟΚΛΗΡΩΜΑ - ΚΑΡΤΕΣΙΑΝΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ','ΔΙΠΛΟ ΟΛΟΚΛΗΡΩΜΑ - ΠΟΛΙΚΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ','ΤΡΙΠΛΟ ΟΛΟΚΛΗΡΩΜΑ - ΚΑΡΤΕΣΙΑΝΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ','ΤΡΙΠΛΟ ΟΛΟΚΛΗΡΩΜΑ - ΣΦΑΙΡΙΚΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ','ΤΡΙΠΛΟ ΟΛΟΚΛΗΡΩΜΑ - ΕΛΛΕΙΠΤΙΚΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ','ΤΡΙΠΛΟ ΟΛΟΚΛΗΡΩΜΑ - ΚΥΛΙΝΔΡΙΚΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ','ΕΠΙΚΑΜΠΥΛΙΟ ΟΛΟΚΛΗΡΩΜΑ - ΒΑΘΜΩΤΗ ΣΥΝΑΡΤΗΣΗ','ΕΠΙΚΑΜΠΥΛΙΟ ΟΛΟΚΛΗΡΩΜΑ - ΔΙΑΝΥΣΜΑΤΙΚΗ ΣΥΝΑΡΤΗΣΗ','ΕΠΙΦΑΝΕΙΑΚΟ ΟΛΟΚΛΗΡΩΜΑ - ΒΑΘΜΩΤΗ ΣΥΝΑΡΤΗΣΗ','ΕΠΙΦΑΝΕΙΑΚΟ ΟΛΟΚΛΗΡΩΜΑ - ΔΙΑΝΥΣΜΑΤΙΚΗ ΣΥΝΑΡΤΗΣΗ']
menu_kindf = ['ΒΑΘΜΩΤΗ','ΔΙΑΝΥΣΜΑΤΙΚΗ']
menu_kind_int = ['ΔΙΠΛΑ','ΤΡΙΠΛΑ','ΕΠΙΚΑΜΠΥΛΙΑ','ΕΠΙΦΑΝΕΙΑΚΑ']
menu_kind_coordinate = ['ΚΑΡΤΕΣΙΑΝΕΣ','ΠΟΛΙΚΕΣ','ΣΦΑΙΡΙΚΕΣ','ΕΛΛΕΙΠΤΙΚΕΣ','ΚΥΛΙΝΔΡΙΚΕΣ']

double_inputs1= ['doublef','doublex1','doublex2','doubley1','doubley2']
double_inputs2= ['doublef2','doubler1','doubler2','doubleth1','doubleth2']
triple_inputs1= ['triplef','triplex1','triplex2','tripley1','tripley2','triplez1','triplez2']
triple_inputs2= ['triplef2','tripler1','tripler2','tripleθ1','tripleθ2','tripleφ1','tripleφ2']
triple_inputs3= ['triplef3','3tripler1','3tripler2','3tripleθ1','3tripleθ2','3tripleφ1','3tripleφ2']
triple_inputs4= ['triplef4','4triplex1','4triplex2','4tripley1','4tripley2','4triplez1','4triplez2']
line_inputs1= ['linef','linext','lineyt','linezt','linet1','linet2']
line_inputs2= ['linef1','linef2','linef3','linext2','lineyt2','linezt2','2linet1','2linet2','linexa','linexb','lineya','lineyb','lineza','linezb']
surface_inputs1 = ['surfacef','surfacex','surfacey','surfacez','surfaceu1','surfaceu2','surfacev1','surfacev2']
surface_inputs2 = ['2surfacef1','2surfacef2','2surfacef3','2surfacex','2surfacey','2surfacez','2surfaceu1','2surfaceu2','2surfacev1','2surfacev2','2surfacefs','2surfacex1','2surfacex2','2surfacey1','2surfacey2','2surfacez1','2surfacez2']

keys = [double_inputs1, double_inputs2, triple_inputs1, triple_inputs2, triple_inputs3, triple_inputs4, line_inputs1, line_inputs2, surface_inputs1,surface_inputs2]
calculate = ['1a','2a','3a','4a','5a','6a','7a','8a','9a','10a']
clear = ['clear1','clear2','clear3','clear4','clear5','clear6','clear7','clear8','clear9','clear10']


#ΑΓΓΛΙΚΑ
help_int2 = ['SIMPLE INTEGRAL', 'DOUBLE INTEGRAL', 'TRIPLE INTEGRAL', 'LINE INTEGRAL', 'SURFACE INTEGRAL', '___________________','INFORMATIONS']
help_info2 = {help_int2[0] : 1,
             help_int2[1] :2, 
             help_int2[2] :3, 
             help_int2[3] :4,
             help_int2[4] :5,
             help_int2[5] :6,
             help_int2[6] :7
             }

text_frame2=['INTEGRAL CALCULATOR', 'DOUBLE INTEGRAL - CARTESIAN COORDINATES','DOUBLE INTEGRAL - POLAR COORDINATES','TRIPLE INTEGRAL - CARTESIAN COORDINATES','TRIPLE INTEGRAL - SPHERICAL COORDINATES','TRIPLE INTEGRAL - ELEPTIC COORDINATES','TRIPLE INTEGRAL - CYLINDRICAL COORDINATES','LINE INTEGRAL - GRADE FUNCTION','LINE INTEGRAL - VECTOR FUNCTION','SURFACE INTEGRAL - GRADE FUNCTION','SURFACE INTEGRAL - VECTOR FUNCTION' ]
menu_kindf2 = ['GRADE','VECTOR']
menu_kind_int2 = ['DOUBLE','TRIPLE','LINE','SURFACE']
menu_kind_coordinate2 = ['CARTESIAN','POLAR','SPHERICAL','ELEPTIC','CYLINDRICAL']

ΕΝ_double_inputs1= ['2doublef','2doublex1','2doublex2','2doubley1','2doubley2']
ΕΝ_double_inputs2= ['2doublef2','2doubler1','2doubler2','2doubleth1','2doubleth2']
ΕΝ_triple_inputs1= ['2triplef','2triplex1','2triplex2','2tripley1','2tripley2','2triplez1','2triplez2']
ΕΝ_triple_inputs2= ['2triplef2','2tripler1','2tripler2','2ripleθ1','2tripleθ2','2tripleφ1','2tripleφ2']
ΕΝ_triple_inputs3= ['2triplef3','23tripler1','23tripler2','23tripleθ1','23tripleθ2','23tripleφ1','23tripleφ2']
ΕΝ_triple_inputs4= ['2triplef4','24triplex1','24triplex2','24tripley1','24tripley2','24triplez1','24triplez2']
ΕΝ_line_inputs1= ['2linef','2linext','2lineyt','2linezt','2linet1','2linet2']
ΕΝ_line_inputs2= ['2linef1','2linef2','2linef3','2linext2','2lineyt2','2linezt2','22linet1','22linet2','2linexa','2linexb','2lineya','2lineyb','2lineza','2linezb']
ΕΝ_surface_inputs1 = ['2surfacef','2surfacex','2surfacey','2surfacez','2surfaceu1','2surfaceu2','2surfacev1','2surfacev2']
ΕΝ_surface_inputs2 = ['22surfacef1','22surfacef2','22surfacef3','22surfacex','22surfacey','22surfacez','22surfaceu1','22surfaceu2','22surfacev1','22surfacev2','22surfacefs','22surfacex1','22surfacex2','22surfacey1','22surfacey2','22surfacez1','22surfacez2']

keys2 = [ΕΝ_double_inputs1, ΕΝ_double_inputs2, ΕΝ_triple_inputs1, ΕΝ_triple_inputs2, ΕΝ_triple_inputs3, ΕΝ_triple_inputs4, ΕΝ_line_inputs1, ΕΝ_line_inputs2, ΕΝ_surface_inputs1, ΕΝ_surface_inputs2]
calculate2 = ['1b','2b','3b','4b','5b','6b','7b','8b','9b','10b']

clear2 = ['2clear1','2clear2','2clear3','2clear4','2clear5','2clear6','2clear7','2clear8','2clear9','2clear10']




def popuphelp(filename,filename2,filename3,num):
    
    col1=[ [sg.Text('',size=(15, 1),background_color='light blue')], [sg.Text('',size=(15, 1),background_color='light blue')], [sg.Text('',size=(15, 1),background_color='light blue')], [sg.Text('',size=(15, 1),background_color='light blue')], [sg.Text('',size=(15, 1),background_color='light blue')], [sg.Text('',size=(15, 1),background_color='light blue')],[sg.Text('',size=(15, 1),background_color='light blue')],[sg.Text('',size=(15, 1),background_color='light blue')],[sg.Text('',size=(15, 1),background_color='light blue')],[sg.Text('',size=(15, 1),background_color='light blue')],[sg.Text('',size=(15, 1),background_color='light blue')],[sg.Text('',size=(15, 1),background_color='light blue')],[sg.Text('',size=(15, 1),background_color='light blue')],[sg.Text('',size=(15, 1),background_color='light blue')],[sg.Text('',size=(15, 1),background_color='light blue')],[sg.Text('',size=(15, 1),background_color='light blue')],[sg.Text('',size=(15, 1),background_color='light blue')],[sg.Text('',size=(15, 1),background_color='light blue')],[sg.Text('',size=(15, 1),background_color='light blue')],[sg.Text('',size=(15, 1),background_color='light blue')],
        [sg.Button('ΠΡΟΗΓΟΥΜΕΝΟ', key='PREVIUS', expand_x=True,size=(20,1))],
           [sg.Button('ΕΠΟΜΕΝΟ', key='ΝΕΧΤ', expand_x=True,size=(20,1))]]
    
    layout = [[sg.Image(filename=filename,key='-IMGBOX-',background_color=('white'), expand_x=True, expand_y=True),sg.Column(col1,key='im1',visible=True,background_color='light blue',size=(230,700)),]]
    window = sg.Window('ΒΟΗΘΕΙΑ', layout, border_depth=2, resizable=True, finalize=True, size=(700, 650))



    counter=0
    
    while True:
        event, values = window.read()
        # print(event, values)
        if (event == sg.WIN_CLOSED):
            break
        if num==0:
            window['im1'].update(visible=False)
        elif num==1:
            window['im1'].update(visible=True)
            if event == 'ΝΕΧΤ':
                if counter==0:
                    window['-IMGBOX-'].update(filename2)
                    counter=counter+1

                    
        elif num==2:
            window['im1'].update(visible=True)
            if event == 'ΝΕΧΤ':
                if counter==0:
                    window['-IMGBOX-'].update(filename2)
                    counter=counter+1
                elif counter==1:
                    window['-IMGBOX-'].update(filename3)
                    counter=counter+1

         
        if num==1:
             window['im1'].update(visible=True)
             if event == 'PREVIUS':
                 if counter==1:
                     window['-IMGBOX-'].update(filename)
                     counter=counter-1
                     
        elif num==2:
             window['im1'].update(visible=True)
             if event == 'PREVIUS':
                 if counter==2:
                     window['-IMGBOX-'].update(filename2)
                     counter=counter-1
                 elif counter==1:
                     window['-IMGBOX-'].update(filename)
                     counter=counter-1

    window.close()
    
    
def help_DEF(x):
    if x == 1:
        popuphelp('integral.png','','',0)

    elif x ==2 :
        popuphelp('double1.png','double2.png','',1)
    elif x ==3 :
        popuphelp('triple1.png','triple2.png','',1)
    elif x ==4 :
        popuphelp('line1.png','line2.png','line3.png',2)
    elif x ==5 :
         popuphelp('surface1.png','surface2.png','',1)
    elif x ==6 :
        print('')    
    elif x ==7 :
        popuphelp('info.png','','',0)
            

#ΕΛΕΓΧΟΣ ΑΝ ΕΚΑΝΕ ΕΙΣΑΓΩΓΗ Ο ΧΡΗΣΤΗΣ
def check_inputs(array):
    counter = 0
    for x in array:
        if x == '':
            counter = counter+1
    return counter
#end

def correction(a,language):
    c=0
    d=0
    
    for i in range(len(a)):
        if a[i] == "(":
            c+=1
        elif a[i] == ")":
            d+=1
    if c!=d and language==0:
        sg.Popup("There is a missing parenthesis.",title='ΕΙΔΟΠΟΙΗΣΗ !!!')
        return 0
    elif c!=d and language==1:
        sg.Popup("Λείπει μια παρένθεση.",title='ΕΙΔΟΠΟΙΗΣΗ !!!')
        return 0
    flag=0
    for i in range(len(a)):
        if a[i]=="e" and a[i+1]!="^":
            a=a[:i]+"exp("+a[i+1]+")"+a[i:]
        if a[i]=="e" and a[i+1]=="^" and a[i+2]!="(":
            for j in range(i+2,len(a)):
                if a[j] in "+*/-":
                    a=a[:i+2]+"("+a[i+2:j]+")"+a[j:]
                    flag = 1
                    break
            if flag==1:
                break
#   print(a)
    if "e^(" in a:
        a = a.replace("e^" , "exp")
    return a



def initialize(array):
    i=0
    print(array)
    for x in array:
       array[i]=0
       i=i+1
    return array
#end

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
#ΔΙΠΛΑ ΚΑΡΤΕΣΙΑΝΕΣ
#ΜΕΤΑΤΡΟΠΗ ΑΛΦΑΡΙΘΜΗΤΙΚΩΝ ΤΙΜΩΝ ΣΕ ΣΥΜΒΟΛΙΚΕΣ
def inputs_call(array_inputs):
    f = sympify(array_inputs[0])
    #f = inputs_request(f,"Give the function f(x,y)")
    x1 = sympify(array_inputs[1])
    #x1 = inputs_request(f,"Give x1")
    x2 = sympify(array_inputs[2])
    #x2 = inputs_request(f,"Give x2")
    y1 = sympify(array_inputs[3])
    #y1 = inputs_request(f,"Give y1")
    y2 = sympify(array_inputs[4])
    #y2 = inputs_request(f,"Give y2")
    return f, x1, x2, y1, y2
    #end
    
#ΔΙΠΛΑ ΠΟΛΙΚΕΣ
#ΜΕΤΑΤΡΟΠΗ ΑΛΦΑΡΙΘΜΗΤΙΚΩΝ ΤΙΜΩΝ ΣΕ ΣΥΜΒΟΛΙΚΕΣ    
def inputs_polar(array_polar):
    f = sympify(array_polar[0])
    r1 = sympify(array_polar[1])
    r2 = sympify(array_polar[2])
    theta1 = sympify(array_polar[3])
    theta2 = sympify(array_polar[4])
    return f,r1,r2,theta1,theta2
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

#ΥΠΟΛΟΓΙΣΜΟΣ ΔΙΠΛΩΝ ΟΛΟΚΛΗΡΩΜΑΤΩΝ
def double_integral(array_inputs,pc,language):
    
    #ΔΗΛΩΣΗ ΣΥΜΒΟΛΙΚΩΝ ΜΕΤΑΒΛΗΤΩΝ
    x, y, r, theta = symbols('x y r theta') 
    x1, x2, y1, y2 = symbols('x1 x2 y1 y2')
    f,r1,r2,theta1,theta2 = symbols('f r1 r2 theta1 theta2')
    
    #ΜΕΤΑΤΡΟΠΗ ΑΛΦΑΡΙΘΜΗΤΙΚΩΝ ΤΙΜΩΝ ΑΠΟ ΤΟΝ ΧΡΗΣΤΗ ΣΕ ΣΥΜΒΟΛΙΚΕΣ
    
    if (pc==0):
        f,x1,x2,y1,y2 = inputs_call(array_inputs)
    elif pc==1:
        f,r1,r2,theta1,theta2 = inputs_polar(array_inputs)
    
    #end
    #ΥΠΟΛΟΓΙΣΜΟΣ ΟΛΟΚΛΗΡΩΜΑΤΟΣ  
    if (x1.is_number==1 and x2.is_number==1 and y1.is_number==1 and y2.is_number==1 and pc==0):
            x1,x2 = warning_one(x1,x2)
            y1,y2 = warning_one(y1,y2)
            #1.
            #Simple x and y
            I1 = integrate(f,(x,x1,x2))
            I = integrate(I1,(y,y1,y2))
            if language == 1:
                mathtext_demos = {
                    "Header demo":
                        "Εισαγάγατε:"+r"$  \int ^{"+latex(y2)+"} _{"+latex(y1)+"} \int ^{"+latex(x2)+"} _{"+latex(x1)+"} "+latex(f)+" dx dy$",
                    "Το πρώτο ολοκλήρωμα είναι:":
                        r"$I_1 = "
                        r"\int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(f)+" dx $",
                    "Το οποίο μας δίνει:":
                        r"$I_1 = "+latex(I1)+"$",
                    "Το δεύτερο ολοκλήρωμα είναι: ":
                        r"$I_2 = "
                        r"\int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(I1)+" dy $",
                    "Το οποίο μας δίνει το τελικό αποτέλεσμα:":
                        r"$I_2 = "+latex(I)+"$",
                }
                
            elif language == 0 :
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
            
    elif((x1.is_number==0 or x2.is_number==0) and y1.is_number==1 and y2.is_number==1 and pc==0):
            y1,y2 = warning_one(y1,y2)
            #2.
            #Simple x
            #display result...
            I1 = integrate(f,(x,x1,x2))
            I = integrate(I1,(y,y1,y2))
            if language == 1:
                mathtext_demos = {
                    "Header demo":
                        "Εισαγάγατε:"+r"$  \int ^{"+latex(y2)+"} _{"+latex(y1)+"} \int ^{"+latex(x2)+"} _{"+latex(x1)+"} "+latex(f)+" dx dy$",
                    "Το πρώτο ολοκλήρωμα είναι:":
                        r"$I_1 = "
                        r"\int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(f)+" dx $",
                    "Το οποίο μας δίνει:":
                        r"$I_1 = "+latex(I1)+"$",
                    "Το δεύτερο ολοκλήρωμα είναι: ":
                        r"$I_2 = "
                        r"\int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(I1)+" dy $",
                    "Το οποίο μας δίνει το τελικό αποτέλεσμα:":
                        r"$I_2 = "+latex(I)+"$",
                }
            elif language == 0:
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
    elif(pc==0):
            x1,x2 = warning_one(x1,x2)
            #3.
            #Simple y
            #display result...
            I1 = integrate(f,(y,y1,y2))
            I = integrate(I1,(x,x1,x2))
            if language == 1:
                mathtext_demos = {
                    "Header demo":
                        "Εισαγάγατε:"+r"$  \int ^{"+latex(x2)+"} _{"+latex(x1)+"} \int ^{"+latex(y2)+"} _{"+latex(y1)+"} "+latex(f)+" dy dx$",
                    "Το πρώτο ολοκλήρωμα είναι:":
                        r"$I_1 = "
                        r"\int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(f)+" dy $",
                    "Το οποίο μας δίνει:":
                        r"$I_1 = "+latex(I1)+"$",
                    "Το δεύτερο ολοκλήρωμα είναι: ":
                        r"$I_2 = "
                        r"\int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(I1)+" dx $",
                    "Το οποίο μας δίνει το τελικό αποτέλεσμα:":
                        r"$I_2 = "+latex(I)+"$",
                }
            elif language == 0:
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
    elif(pc==1):
            fp = f.subs([(x, r*cos(theta)),(y, r*sin(theta))])
            I1 = integrate(fp*r,(r,r1,r2))
            I = integrate(I1,(theta,theta1,theta2))
            if language == 1:

                mathtext_demos = {
                    "Header demo":
                        "Εισαγάγατε:"+r"$  \int ^{"+latex(x2)+"} _{"+latex(x1)+"} \int ^{"+latex(y2)+"} _{"+latex(y1)+"} "+latex(f)+" dy dx$",
                    "Αλλαγή μεταβλητών, με χρήση πολικών συντεταγμένων.":
                        "Αντικαθιστώ "r"$x$"" με "r"$r \cdot cos( \theta)$"" και "r"$y$"" με "r"$r \cdot sin( \theta)$",
                    "Η νέα συνάρτηση είναι: ":
                        r"$ f(r , \theta) = "+latex(fp)+"$",
                    "Το πρώτο ολοκλήρωμα είναι:":
                        r"$I_1 = "
                        r"\int^{"+latex(r2)+"} _{"+latex(r1)+"} "+latex(fp)+" dr $",
                    "Το οποίο μας δίνει:":
                        r"$I_1 = "+latex(I1)+"$",
                    "Το δεύτερο ολοκλήρωμα είναι: ":
                        r"$I_2 = "
                        r"\int^{"+latex(theta2)+"}_{"+latex(theta1)+"} "+latex(I)+" d $"
                        r"$ \theta $",
                    "Το οποίο μας δίνει το τελικό αποτέλεσμα:":
                        r"$I_2 = "+latex(I)+"$",
                }
            
            elif language == 0:
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
                     
    
    n_lines = len(mathtext_demos)

    # Colors used in Matplotlib online documentation.
    mpl_grey_rgb = (51 / 255, 51 / 255, 51 / 255)

    # Creating figure and axis.
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.90],
                      facecolor="white", frameon=False)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    if language == 1:
        title= "Υπολογισμός διπλού ολοκληρώματος..."
    elif language == 0:
        title = "Double integral calculation ..."
    ax.set_title(title,color=mpl_grey_rgb, fontsize=14, weight='bold')
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
    plt.show(block=False)
    #"Γραφική παράσταση της"+ 
    """
    fig, axs = plt.subplots(1, 2)
    axs[0].p1 = plot3d(f,show=False)
    axs[0].set_title('Γραφική παράσταση της f(x,y)')
    
    fig.suptitle('Γραφικές παραστάσεις!', fontsize=16)
    
    axs[1].p8 = plot_implicit(And( x > x1, x < x2, y >y1, y < y2),show=False)
    axs[1].set_title('Γραφική παράσταση του χωρίου ολοκλήρωσης D')
    
    
    
    p2 = plot(x1,show=False)
    p3 = plot(x2,show=False)
    p2.extend(p3)
    p4 = plot(y1,show=False)
    p2.extend(p4):
    p5 = plot(y2,show=False)
    p2.extend(p5)
    """
    p1 = plot3d(f,show=False)
    #plt.p1
    #p1.set_title('Γραφική παράσταση της f(x,y)')
    p2 = plot_implicit(And( x > x1, x < x2, y >y1, y < y2),show=False,adaptive=True)
    #plt.set_title('Γραφική παράσταση του χωρίου ολοκλήρωσης D')
      
    #plt.show() ,(x, x1-2, x2+2), (y, y1-2, y2+2)
    PlotGrid(1, 2, p1, p2)
    

#end

#ΥΠΟΛΟΓΙΣΜΟΣ ΤΡΙΠΛΩΝ ΟΛΟΚΛΗΡΩΜΑΤΩΝ
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
            sg.Popup("Error! Something whent wrong!")
           #Label(window,text="Error! Something whent wrong!").place(x=0,y=0)
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
            sg.Popup("ERROR")
            #Label(window,text="ERROR").place(x=1,y=1)
        #end
    #end
    return c,p
#end

#ΤΡΙΠΛΑ ΚΑΡΤΕΣΙΑΝΕΣ
def ti_cc_main_func(array,language):
    
    x, y, z = symbols('x y z')
    x1, x2, y1, y2, z1, z2 = symbols('x1 x2 y1 y2 z1 z2')
    f=sympify(array[0])
    x1=sympify(array[1])
    x2=sympify(array[2])
    y1=sympify(array[3])
    y2=sympify(array[4])
    z1=sympify(array[5])
    z2=sympify(array[6])
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
        if language == 1:
            mathtext_demos = {
                "Header demo":
                    "Εισαγάγατε:"+r"$  \int ^{"+latex(z2)+"} _{"+latex(z1)+"} \int ^{"+latex(y2)+"} _{"+latex(y1)+"} \int ^{"+latex(x2)+"} _{"+latex(x1)+"} "+latex(f)+" dx dy dz$",
                "Το πρώτο ολοκλήρωμα είναι:":
                    r"$I_1 = \int^{"+latex(x2)+"} _{"+latex(x1)+"} "+latex(f)+" dx $",
                "Το οποίο δίνει το I1:":
                    r"$I_1 = "+latex(I1)+"$",
                "Το δεύτερο ολοκλήρωμα είναι:":
                    r"$I_2 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(I1)+" dy $",
                "Το οποίο δίνει το I2:":
                    r"$I_2 = "+latex(I2)+"$",
                "Το τρίτο ολοκλήρωμα είναι:":
                    r"$I_3 = \int ^{"+latex(z2)+"} _{"+latex(z1)+"} "+latex(I2)+"dz $",
                "Το οποίο δίνει το I3, το τελικό αποτέλεσμα:":
                    r"$I_3 = "+latex(I3)+"$"
            }
        elif language == 0:
            
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
       
        
    elif g =="dx dz dy":
        if language == 1:

            mathtext_demos = {
                "Header demo":
                    "Εισαγάγατε:"+r"$  \int ^{"+latex(y2)+"} _{"+latex(y1)+"} \int ^{"+latex(z2)+"} _{"+latex(z1)+"} \int ^{"+latex(x2)+"} _{"+latex(x1)+"} "+latex(f)+" dx dz dy$",
                "Το πρώτο ολοκλήρωμα είναι:":
                    r"$I_1 = \int^{"+latex(x2)+"} _{"+latex(x1)+"} "+latex(f)+" dx $",
                "Το οποίο δίνει το I1:":
                    r"$I_1 = "+latex(I1)+"$",
                "Το δεύτερο ολοκλήρωμα είναι:":
                    r"$I_2 = \int^{"+latex(z2)+"}_{"+latex(z1)+"} "+latex(I1)+" dz $",
                "Το οποίο δίνει το I2:":
                    r"$I_2 = "+latex(I2)+"$",
                "Το τρίτο ολοκλήρωμα είναι:":
                    r"$I_3 = \int ^{"+latex(y2)+"} _{"+latex(y1)+"} "+latex(I2)+"dy $",
                "Το οποίο δίνει το I3, το τελικό αποτέλεσμα:":
                    r"$I_3 = "+latex(I3)+"$"
            }
        elif language == 1:
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

        
        
    elif g =="dy dx dz":
        if language == 1:
            mathtext_demos = {
                "Header demo":
                    "Εισαγάγατε:"+r"$  \int ^{"+latex(z2)+"} _{"+latex(z1)+"} \int ^{"+latex(x2)+"} _{"+latex(x1)+"} \int ^{"+latex(y2)+"} _{"+latex(y1)+"} "+latex(f)+" dy dx dz$",
                "Το πρώτο ολοκλήρωμα είναι:":
                    r"$I_1 = \int^{"+latex(y2)+"} _{"+latex(y1)+"} "+latex(f)+" dy $",
                "Το οποίο δίνει το I1:":
                    r"$I_1 = "+latex(I1)+"$",
                "Το δεύτερο ολοκλήρωμα είναι:":
                    r"$I_2 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(I1)+" dx $",
                "Το οποίο δίνει το I2:":
                    r"$I_2 = "+latex(I2)+"$",
                "Το τρίτο ολοκλήρωμα είναι:":
                    r"$I_3 = \int ^{"+latex(z2)+"} _{"+latex(z1)+"} "+latex(I2)+"dz $",
                "Το οποίο δίνει το I3, το τελικό αποτέλεσμα:":
                    r"$I_3 = "+latex(I3)+"$"
            }
        elif language == 0:
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
       
        
    elif g =="dy dz dx":
        if language == 1:
            mathtext_demos = {
                "Header demo":
                    "Εισαγάγατε:"+r"$  \int ^{"+latex(x2)+"} _{"+latex(x1)+"} \int ^{"+latex(z2)+"} _{"+latex(z1)+"} \int ^{"+latex(y2)+"} _{"+latex(y1)+"} "+latex(f)+" dy dz dx$",
                "Το πρώτο ολοκλήρωμα είναι:":
                    r"$I_1 = \int^{"+latex(y2)+"} _{"+latex(y1)+"} "+latex(f)+" dy $",
                "Το οποίο δίνει το I1:":
                    r"$I_1 = "+latex(I1)+"$",
                "Το δεύτερο ολοκλήρωμα είναι:":
                    r"$I_2 = \int^{"+latex(z2)+"}_{"+latex(z1)+"} "+latex(I1)+" dz $",
                "Το οποίο δίνει το I2:":
                    r"$I_2 = "+latex(I2)+"$",
                "Το τρίτο ολοκλήρωμα είναι:":
                    r"$I_3 = \int ^{"+latex(x2)+"} _{"+latex(x1)+"} "+latex(I2)+"dx $",
                "Το οποίο δίνει το I3, το τελικό αποτέλεσμα:":
                    r"$I_3 = "+latex(I3)+"$"
            }
        elif language == 0:
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
        
        
    elif g =="dz dx dy":
        if language ==1:
            mathtext_demos = {
                "Header demo":
                    "Εισαγάγατε:"+r"$  \int ^{"+latex(y2)+"} _{"+latex(y1)+"} \int ^{"+latex(x2)+"} _{"+latex(x1)+"} \int ^{"+latex(z2)+"} _{"+latex(z1)+"} "+latex(f)+" dz dx dy$",
                "Το πρώτο ολοκλήρωμα είναι:":
                    r"$I_1 = \int^{"+latex(z2)+"} _{"+latex(z1)+"} "+latex(f)+" dz $",
                "Το οποίο δίνει το I1:":
                    r"$I_1 = "+latex(I1)+"$",
                "Το δεύτερο ολοκλήρωμα είναι:":
                    r"$I_2 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(I1)+" dx $",
                "Το οποίο δίνει το I2:":
                    r"$I_2 = "+latex(I2)+"$",
                "Το τρίτο ολοκλήρωμα είναι:":
                    r"$I_3 = \int ^{"+latex(y2)+"} _{"+latex(y1)+"} "+latex(I2)+"dy $",
                "Το οποίο δίνει το I3, το τελικό αποτέλεσμα:":
                    r"$I_3 = "+latex(I3)+"$"
            }
        elif language == 0:
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
        
        
    elif g =="dz dy dx":
        if language == 1:
            mathtext_demos = {
                "Header demo":
                    "Εισαγάγατε:"+r"$  \int ^{"+latex(x2)+"} _{"+latex(x1)+"} \int ^{"+latex(y2)+"} _{"+latex(y1)+"} \int ^{"+latex(z2)+"} _{"+latex(z1)+"} "+latex(f)+" dz dy dx$",
                "Το πρώτο ολοκλήρωμα είναι:":
                    r"$I_1 = \int^{"+latex(z2)+"} _{"+latex(z1)+"} "+latex(f)+" dz $",
                "Το οποίο δίνει το I1:":
                    r"$I_1 = "+latex(I1)+"$",
                "Το δεύτερο ολοκλήρωμα είναι: ":
                    r"$I_2 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(I1)+" dy $",
                "Το οποίο δίνει το I2:":
                    r"$I_2 = "+latex(I2)+"$",
                "Το τρίτο ολοκλήρωμα είναι:":
                    r"$I_3 = \int ^{"+latex(x2)+"} _{"+latex(x1)+"} "+latex(I2)+"dx $",
                "Το οποίο δίνει το I3, το τελικό αποτέλεσμα:":
                    r"$I_3 = "+latex(I3)+"$"
            }
        elif language == 0:
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
    if language ==1:
        title = "Υπολογισμός τριπλού ολοκληρώματος..."
    elif language== 0:
        title = "Calculation of triple integral ..."
    ax.set_title(title,
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

    plt.show(block=False)
    
    
    #end
    
#ΤΡΙΠΛΑ ΣΦΑΙΡΙΚΕΣ
def ti_sc_main_func(array,language):
    
    x, y, z, r, theta, phi = symbols('x y z r theta phi')
    x1, x2, y1, y2, z1, z2 = symbols('r1 r2 theta1 theta2 phi1 phi2')
    
    f=sympify(array[0])
    r1=sympify(array[1])
    r2=sympify(array[2])
    theta1=sympify(array[3])
    theta2=sympify(array[4])
    phi1=sympify(array[5])
    phi2=sympify(array[6])
    k1=sympify("0")
    k2=sympify("0")
    k3=sympify("0")
    #Input Arguments:
    # function f(x,y,z)
    
    fp = f.subs(x, r*sin(theta)*cos(phi)+k1)
    fpp = fp.subs(y, r*sin(theta)*sin(phi)+k2)
    fppp = fpp.subs(z,r*cos(theta)+k3)
    fnew = fppp*r**2*sin(theta)
    I1 = integrate(fnew, (r, r1, r2))
    I2 = integrate(I1, (theta, theta1, theta2))
    I3 = integrate(I2, (phi, phi1, phi2))
    
    if language == 1:

        mathtext_demos = {
            "Header demo":
                "Εισαγάγατε:"+r"$  \int ^{"+latex(phi2)+"} _{"+latex(phi1)+"} \int ^{"+latex(theta2)
                +"} _{"+latex(theta1)+"} \int ^{"+latex(r2)+"} _{"+latex(r1)+"} $"
                r"$f( x( r , $"+
                r"$ \theta , \phi ) , y( r , $"+
                r"$ \theta , \phi ) ) \cdot r^2 \cdot sin( $"+
                r"$ \theta ) dr d $"+
                r"$ \theta d $"+
                r"$\phi $",
            "Αλλαγή μεταβλητών, χρησιμοποιώντας σφαιρικές συντεταγμένες:":
                "Αντικαθιστώ: "+r"$x$"+" με "+r"$r \cdot sin( \theta ) \cdot cos( \phi ) + Κ_x $"
                " και: "+r"$y$"+" με "+r"$r \cdot sin( \theta ) \cdot sin( \phi ) + Κ_y $"
                " και: "+r"$z$"+" με "+r"$r \cdot cos( \theta ) + Κ_z $",
            "Η νέα συνάρτηση είναι:":
                r"$f(r, \theta , \phi ) = "+latex(fnew)+" $",
            "Το πρώτο ολοκλήρωμα είναι:":
                r"$I_1 = \int^{"+latex(r2)+"} _{"+latex(r1)+"} "+latex(fnew)+" dr $",
            "Το οποίο δίνει το I1:":
                r"$I_1 = "+latex(I1)+"$",
            "Το δεύτερο ολοκλήρωμα είναι:":
                r"$I_2 = \int^{"+latex(theta2)+"}_{"+latex(theta1)+"} "+latex(I1)+" d $"+
                r"$ \theta $",
            "Το οποίο δίνει I2:":
                r"$I_2 = "+latex(I2)+"$",
            "Το τρίτο ολοκλήρωμα είναι:":
                r"$I_3 = \int ^{"+latex(phi2)+"} _{"+latex(phi1)+"} "+latex(I2)+" d"
                " \phi $",
            "Το οποίο δίνει το I3, το τελικό αποτέλεσμα:":
                r"$I_3 = "+latex(I3)+"$"
        }
    elif language== 0:
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
    if language == 1:
        title = "Υπολογισμός τριπλού ολοκληρώματος - σφαιρικές συντεταγμένες"
    elif language == 0:
        title = "Triple Integer Calculation - Spherical Coordinates"
    ax.set_title(title,
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

    plt.show(block=False)
    
    #end
#ΤΡΙΠΛΑ ΕΛΛΕΙΠΤΙΚΕΣ
def ti_ec_main_func(array,language):
    x, y, z, r, theta, phi = symbols('x y z r theta phi')
    x1, x2, y1, y2, z1, z2 = symbols('r1 r2 theta1 theta2 phi1 phi2')
    f=sympify(array[0])
    r1=sympify(array[1])
    r2=sympify(array[2])
    theta1=sympify(array[3])
    theta2=sympify(array[4])
    phi1=sympify(array[5])
    phi2=sympify(array[6])
    k1=sympify("0")
    k2=sympify("0")
    k3=sympify("0")
    a=sympify("1")
    b=sympify("1")
    c=sympify("1")
    
    #Input Arguments:
    # function f(x,y,z)
    
    fp = f.subs(x, a*r*sin(theta)*cos(phi)+k1)
    fpp = fp.subs(y, b*r*sin(theta)*sin(phi)+k2)
    fppp = fpp.subs(z,c*r*cos(theta)+k3)
    fnew = fppp*a*b*c*r**2*sin(theta)
    I1 = integrate(fnew, (r, r1, r2))
    I2 = integrate(I1, (theta, theta1, theta2))
    I3 = integrate(I2, (phi, phi1, phi2))
    if language ==1 :
        
        mathtext_demos = {
            "Header demo":
                "Εισαγάγατε:"+r"$ \int ^{"+latex(phi2)+"} _{"+latex(phi1)+"} \int ^{"+latex(theta2)+
                "} _{"+latex(theta1)+"} \int ^{"+latex(r2)+"} _{"+latex(r1)+"} $"
                r"$ f( x( r , \theta , \phi ) , y( r , \theta , \phi ) ) \cdot a \cdot b \cdot c \cdot r^2 \cdot sin( \theta ) dr d $"
                r"$\theta d $"
                r"$\phi $",
            "Αλλαγή μεταβλητών, χρησιμοποιώντας ελλειψοειδείς συντεταγμένες:":
                "Αντικαθιστώ: "+r"$x$"+" με "+r"$a \cdot r \cdot sin( \theta ) \cdot cos( \phi ) + Κ_x $"
                " και: "+r"$y$"+" με "+r"$b \cdot r \cdot sin( \theta ) \cdot sin( \phi ) + Κ_y $"
                " και: "+r"$z$"+" με "+r"$c \cdot r \cdot cos( \theta ) + Κ_z $",
            "Η νέα συνάρτηση είναι:":
                r"$f(r, \theta , \phi ) = "+latex(fnew)+" $",
            "Το πρώτο ολοκλήρωμα είναι:":
                r"$I_1 = \int^{"+latex(r2)+"} _{"+latex(r1)+"} "+latex(fnew)+" dr $",
            "Το οποίο δίνει το I1:":
                r"$I_1 = "+latex(I1)+"$",
            "Το δεύτερο ολοκλήρωμα είναι: ":
                r"$I_2 = \int^{"+latex(theta2)+"}_{"+latex(theta1)+"} "+latex(I1)+" d$"
                r"$ \theta $",
            "Το οποίο δίνει το I2:":
                r"$I_2 = "+latex(I2)+"$",
            "Το τρίτο ολοκλήρωμα είναι:":
                r"$I_3 = \int ^{"+latex(phi2)+"} _{"+latex(phi1)+"} "+latex(I2)+" d"
                " \phi $",
            "Το οποίο δίνει το I3, το τελικό αποτέλεσμα:":
                r"$I_3 = "+latex(I3)+"$"
        }
    elif language == 0:
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
    if language ==1 :
        title = "Υπολογισμός τριπλού ολοκληρώματος - ελλειπτικές συντεταγμένες"
    elif language==0:
        title ="Triple Integer Calculation - Elliptic Coordinates"
    ax.set_title(title,
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

    plt.show(block=False)
    
    #end


#ΤΡΙΠΛΑ ΚΥΛΙΝΔΡΙΚΕΣ
def ti_cyc_main_func(array,language):
    x, y, z, r, phi, rho = symbols('x y z r phi rho')
    x1, x2, y1, y2, z1, z2 = symbols('rho1 rho2 phi1 phi2 z1 z2')
    f=sympify(array[0])
    rho1=sympify(array[1])
    rho2=sympify(array[2])
    phi1=sympify(array[3])
    phi2=sympify(array[4])
    z1=sympify(array[5])
    z2=sympify(array[6])
    k1=sympify("0")
    k2=sympify("0")
    k3=sympify("0")
    
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
    if language == 1:
        mathtext_demos = {
            "Header demo":
                "Εισαγάγατε:"+r"$ \int ^{"+latex(z2)+"} _{"+latex(z1)+"} \int ^{"+latex(phi2)+
                "} _{"+latex(phi1)+"} \int ^{"+latex(rho2)+"} _{"+latex(rho1)+"} $"
                r"$f( x( \rho , \phi , z ) , y( \rho , \phi , z ) ) \cdot \rho d $"
                r"$\rho d $"
                r"$\phi d z $",
            "Αλλαγή μεταβλητών, χρησιμοποιώντας κυλινδρικές συντεταγμένες::":
                "Αντικαθιστώ: "+r"$x$"+" με "+r"$a \cdot r \cdot sin( \theta ) \cdot cos( \phi ) + Κ_x $"
                " και: "+r"$y$"+" με "+r"$b \cdot r \cdot sin( \theta ) \cdot sin( \phi ) + Κ_y $"
                " και: "+r"$z$"+" με "+r"$c \cdot r \cdot cos( \theta ) + Κ_z $",
            "The new function is:":
                r"$f(r, \theta , \phi ) = "+latex(fnew)+" $",
            "Το πρώτο ολοκλήρωμα είναι:":
                r"$I_1 = \int^{"+latex(rho2)+"} _{"+latex(rho1)+"} "+latex(fnew)+" d$"
                r"$ \rho $",
            "Το οποίο μας δίνει I1:":
                r"$I_1 = "+latex(I1)+"$",
            "Το δεύτερο ολοκλήρωμα είναι: ":
                r"$I_2 = \int^{"+latex(phi2)+"}_{"+latex(phi1)+"} "+latex(I1)+" d $"
                r"$ \phi $",
            "Το οποίο μας δίνει I2:":
                r"$I_2 = "+latex(I2)+"$",
            "Το τρίτο ολοκλήρωμα είναι:":
                r"$I_3 = \int ^{"+latex(z2)+"} _{"+latex(z1)+"} "+latex(I2)+" d z $",
            "Το οποίο δίνει το I3, το τελικό αποτέλεσμα:":
                r"$I_3 = "+latex(I3)+"$"
        }
    elif language == 0:
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
    if language ==1 :
        title = "Υπολογισμός τριπλού ολοκληρώματος - κυλινδρικές συντεταγμένες"
    elif language == 0:
        title = "Triple integral calculation - cylindrical coordinates"

    ax.set_title(title,
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

    plt.show(block=False)
    
    #end

   

#ΥΠΟΛΟΓΙΣΜΟΣ ΕΠΙΚΑΜΠΥΛΙΩΝ ΟΛΟΚΛΗΡΩΜΑΤΩΝ

#ΕΠΙΚΑΜΠΥΛΙΟ ΒΑΘΜΩΤΗ
def curve_integral(array,language):
    f, x, y, z, t, t1, t2 = symbols('f x y z t t1 t2')
    cx, cy, cz, dcx, dcy, dcz = symbols('cx cy cz dcx dcy dcz')
    f = sympify(array[0])
    cx = sympify(array[1])
    cy = sympify(array[2])
    cz = sympify(array[3])
    t1 = sympify(array[4])
    t2 = sympify(array[5])
    dcx = diff(cx,t)
    dcy = diff(cy,t)
    dcz = diff(cz,t)
    f1 = f.subs(x,cx)
    f2 = f1.subs(y,cy)
    f3 = f2.subs(z,cz)
    fnew = f3*sqrt(dcx**2 + dcy**2 + dcz**2)
    I = integrate(fnew,(t,t1,t2))
    if language ==1 :
        mathtext_demos = {
            "Header demo":
                "Εισαγάγατε: "+r"$  \int ^{"+latex(t2)+"} _{"+latex(t1)+"} "+latex(f)+" dt $",
            "Η καμπύλη είναι:":
                r"$ \vec{c} _{(t)} = ["+latex(cx)+" , "+latex(cy)+" , "+latex(cz)+" ]$",
            "Διαφοροποίηση της καμπύλης:":
                r"$ \dot{ \vec{c} } _{(t)} = ["+latex(dcx)+" , "+latex(dcy)+" , "+latex(dcz)+" ]$",
            "Η norm του παραπάνω διανύσματος είναι:":
                r"$ \parallel \dot{ \vec{c}} _{(t)} \parallel  = \sqrt{ ("+latex(dcx)+")^2 + ("+latex(dcy)+")^2 + ("+latex(dcz)+")^2 }$",
            "Η συνάρτηση που εισαγάγατε είναι:":
                r"$f(x,y,z) = "+latex(f)+"$",
            "Αντικαθιστώ:":
                r"$x$"+"  με  "+r"$x(t)$"+" , "+r"$y$"+"  με  "+r"$y(t)$"+" , και "+r"$z$"+"  με  "+r"$z(t)$",
            "Το οποίο δίνει:":
                r"$ f(t) = "+latex(f3)+"$",
            "Το ολοκλήρωμα είναι:":
                r"$I = \int^{"+latex(t2)+"}_{"+latex(t1)+"} "+latex(fnew)+" dt $",
            "Το οποίο δίνει το τελικό αποτέλεσμα:":
                r"$I_2 = "+latex(I)+"$",
        }
    elif language ==0:
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
    if language == 1:
        title = "Υπολογισμός επικαμπύλιου ολοκληρώματος"
    elif language == 0:
        title = "Calculation of a line integral"

    ax.set_title(title,
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

    plt.show(block=False)
#end

#ΕΠΙΚΑΜΠΥΛΙΟ ΔΙΑΝΥΣΜΑΤΙΚΗ
def curve_integral_vf(array1,array2,language):
    x, y, z, t, t1, t2 = symbols('x y z t t1 t2')
    fx, fy, fz = symbols('fx fy fz')
    cx, cy, cz, dcx, dcy, dcz = symbols('cx cy cz dcx dcy dcz')
    a=0
    b=0
    print("Hi")
    if array2[0] !="" and array2[2] !="" and array2[4] !="":
        a = 1
        #print("Parametrize the line AB:")
        xa = sympify(array2[0])
        ya = sympify(array2[2])
        za = sympify(array2[4])
        xb = sympify(array2[1])
        yb = sympify(array2[3])
        zb = sympify(array2[5])
        cx = (1-t)*xa+t*xb
        cy = (1-t)*ya+t*yb
        cz = (1-t)*za+t*zb
        t1 = 0
        t2 = 1
        #print(" x(t)= ",cx,"\n","y(t)= ",cy,"\n","z(t)= ",cz,"\n","with t in [0,1] \n")
    else:
        a = 2
        cx = sympify(array1[3])
        cy = sympify(array1[4])
        cz = sympify(array1[5])
        t1 = sympify(array1[6])
        t2 = sympify(array1[7])
        
    fx = sympify(array1[0])
    fy = sympify(array1[1])
    fz = sympify(array1[2])
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
        if language ==1:
            mathtext_demos = {
                "Header demo":
                    "",
                "Παραμετροποιήστε τη γραμμή AB:":
                    r"$x_{(t)} = (1-t) \cdot x_A + t \cdot x_B = "+latex(cx)+" $"
                    "\n"
                    r"$y_{(t)} = (1-t) \cdot y_A + t \cdot y_B = "+latex(cy)+" $"
                    "\n"
                    r"$z_{(t)} = (1-t) \cdot z_A + t \cdot z_B = "+latex(cz)+" $"
                    "\n"
                    "with "r"$ 0 \leq t \leq 1 $",
                "Έλεγχος εάν το F είναι συντηρητικό:":
                    r"$ \vec{\nabla} \times \vec{F} = [0,0,0] $",
                "Τώρα η g μπορεί να βρει μια συνάρτηση f τέτοια ώστε:":
                    r"$ \nabla f(x,y,z) = \vec{F} (x,y,z) $",
                "Βήμα 1 - oλοκληρώστε το F1":
                    r"$ f (x,y,z) = \int F_1 dx = \phi_1 + g(y,z) = "+latex(fix)+" + g(y,z) $",
                "Βήμα 2 - Διαφοροποίηση f :":
                    r"$ \frac{ \partial f (x,y,z) }{ \partial y } = \frac{ \partial \phi_1 }{ \partial y } + \frac{ \partial g }{ \partial y } = F_2$",
                "Που δίνει τη συνάρτηση g μετά την ολοκλήρωση ως προς το y":
                    r"$ g = "+latex(g)+" + h(z) $",
                "Τώρα το f γίνεται:":
                    r"$ f(x,y,z) = \phi_1 + \phi_2 + h(z) = "+latex(fixnew)+" + h(z) $",
                "Βήμα 3 - Διαφοροποιήστε ξανά το f:":
                    r"$ \frac{ \partial f (x,y,z) }{ \partial z } = \frac{ \partial \phi_1 }{ \partial z } + \frac{ \partial \phi_2 }{ \partial z } + \frac{ \partial h}{ \partial z}= F_3$",
                "που δίνει μετά την ολοκλήρωση: ":
                    r"$ h(z) = "+latex(h)+" + c $",
                "Τελικά το f είναι: ":
                    r"$f(x,y,z) = "+latex(f4)+" + c $",
            }
        
        elif language ==0:
            
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
                    "with "r"$ 0 \leq t \leq 1 $",
                "Checking if F is conservative:":
                    r"$ \vec{\nabla} \times \vec{F} = [0,0,0] $",
                "Now ge can find a function f such that:":
                    r"$ \nabla f(x,y,z) = \vec{F} (x,y,z) $",
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
        if language ==1:
            mathtext_demos = {
                "Header demo":
                    "",
                "Παραμετροποιήστε τη γραμμή AB:":
                    r"$x_{(t)} = (1-t) \cdot x_A + t \cdot x_B = "+latex(cx)+" $"
                    "\n"
                    r"$y_{(t)} = (1-t) \cdot y_A + t \cdot y_B = "+latex(cy)+" $"
                    "\n"
                    r"$z_{(t)} = (1-t) \cdot z_A + t \cdot z_B = "+latex(cz)+" $"
                    "\n"
                    "with "r"$ 0 \leq t \leq 1 $",
                "Έλεγχος εάν το F είναι συντηρητικό:":
                    r"$ \vec{\nabla} \times \vec{F} \neq [0,0,0] $",
                "Το F δεν είναι συντηρητικό, επομένως χρησιμοποιούμε τα ακόλουθα:":
                    "Replace: "r"$x$"+" with "+r"$x(t)$"+" , "+r"$y$"+" with "+r"$y(t)$"+" and "+r"$z$"+" with "+r"$z(t)$",
                "Το νέο F(t) είναι:":
                    r"$F(t) = ["+latex(fx3)+" , "+latex(fy3)+" , "+latex(fz3)+"] $",
                "Διαφοροποιήστε την καμπύλη:":
                    r"$ \dot{x}_{(t)} = "+latex(dcx)+" $"
                    "\n"
                    r"$ \dot{y}_{(t)} = "+latex(dcy)+" $"
                    "\n"
                    r"$ \dot{z}_{(t)} = "+latex(dcz)+" $",
                "Το ολοκλήρωμα είναι :":
                    r"$ I = \int ^{"+latex(t2)+"} _{"+latex(t1)+"} "+latex(fnew)+" $",
                "Που δίνει:":
                    r"$I = "+latex(I)+"$"
            }
        elif language ==0: 
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
                    "with "r"$ 0 \leq t \leq 1 $",
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
        if language ==1 :
            mathtext_demos = {
                "Header demo":
                    "",
                "Η καμπύλη είναι:":
                    r"$x_{(t)} = "+latex(cx)+" $"
                    "\n"
                    r"$y_{(t)} = "+latex(cy)+" $"
                    "\n"
                    r"$z_{(t)} = "+latex(cz)+" $"
                    "\n"
                    "with "r"$ "+latex(t1)+" \leq t \leq "+latex(t1)+" $",
                "Έλεγχος εάν το F είναι συντηρητικό":
                    r"$ \vec{\nabla} \times \vec{F} = [0,0,0] $",
                "Τώρα η g μπορεί να βρει μια συνάρτηση f τέτοια ώστε:":
                    r"$ \nabla f(x,y,z) = \vec{F} (x,y,z) $",
                "Βήμα 1 - Ενσωματώστε το F1":
                    r"$ f (x,y,z) = \int F_1 dx = \phi_1 + g(y,z) = "+latex(fix)+" + g(y,z) $",
                "Βήμα 2 - Διαφοροποίηση f : ":
                    r"$ \frac{ \partial f (x,y,z) }{ \partial y } = \frac{ \partial \phi_1 }{ \partial y } + \frac{ \partial g }{ \partial y } = F_2$",
                "Που δίνει τη συνάρτηση g μετά την ολοκλήρωση ως προς το y":
                    r"$ g = "+latex(g)+" + h(z) $",
                "Τώρα το f γίνεται:":
                    r"$ f(x,y,z) = \phi_1 + \phi_2 + h(z) = "+latex(fixnew)+" + h(z) $",
                "Βήμα 3 - Διαφοροποιήστε ξανά το f:":
                    r"$ \frac{ \partial f (x,y,z) }{ \partial z } = \frac{ \partial \phi_1 }{ \partial z } + \frac{ \partial \phi_2 }{ \partial z } + \frac{ \partial h}{ \partial z}= F_3$",
                "Που δίνει μετά την ολοκλήρωση:":
                    r"$ h(z) = "+latex(h)+" + c $",
                "Τελικά το f είναι: ":
                    r"$f(x,y,z) = "+latex(f4)+" + c $",
            }
        elif language ==0:
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
                    "with "r"$ "+latex(t1)+" \leq t \leq "+latex(t1)+" $",
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
        if language == 1:
            
            mathtext_demos = {
                "Header demo":
                    "",
                "Η καμπύλη είναι:":
                    r"$x_{(t)} = "+latex(cx)+" $"
                    "\n"
                    r"$y_{(t)} = "+latex(cy)+" $"
                    "\n"
                    r"$z_{(t)} = "+latex(cz)+" $"
                    "\n"
                    "with "r"$ "+latex(t1)+" \leq t \leq "+latex(t1)+" $",
                "Έλεγχος εάν το F είναι συντηρητικό:":
                    r"$ \vec{\nabla} \times \vec{F} \neq [0,0,0] $",
                "Το F δεν είναι συντηρητικό, επομένως χρησιμοποιούμε τα ακόλουθα:":
                    "Αντικαθιστώ: "r"$x$"+" με "+r"$x(t)$"+" , "+r"$y$"+" με "+r"$y(t)$"+" και "+r"$z$"+" με "+r"$z(t)$",
                "Το νέο F(t) είναι:":
                    r"$F(t) = ["+latex(fx3)+" , "+latex(fy3)+" , "+latex(fz3)+"] $",
                "Διαφοροποιήστε την καμπύλη:":
                    r"$ \dot{x}_{(t)} = "+latex(dcx)+" $"
                    "\n"
                    r"$ \dot{y}_{(t)} = "+latex(dcy)+" $"
                    "\n"
                    r"$ \dot{z}_{(t)} = "+latex(dcz)+" $",
                "Το ολοκλήρωμα είναι":
                    r"$ I = \int ^{"+latex(t2)+"} _{"+latex(t1)+"} "+latex(fnew)+" $",
                "που δίνει:":
                    r"$I = "+latex(I)+"$"
            }
        elif language == 0:
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
                    "with "r"$ "+latex(t1)+" \leq t \leq "+latex(t1)+" $",
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
    if language ==1:
        title = "Υπολογισμός επικαμπύλιου ολοκληρώματος ..."

    elif language == 0:
        title= "Calculating Line Integral ..."
    ax.set_title(title ,
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

    plt.show(block=False)
 #end   

#ΥΠΟΛΟΓΙΣΜΟΣ ΕΠΙΦΑΝΕΙΑΚΩΝ ΟΛΟΚΛΗΡΩΜΑΤΩΝ
def surface_integral(array,language):
    f, sx, sy, sz = symbols('f sx sy sz')
    u1, u2, v1, v2 = symbols('u1 u2 v1 v2')
    x, y, z, v, u = symbols('x y z v u')
    #csx = 450
    #csy = 20
    #Label(window, text="Transforming Surface integral to Double integral").place(x=csx,y=csy)
    #print("From Surface integral to Double Integral . . .")
    f = sympify(array[0])
    sx = sympify(array[1])
    sy = sympify(array[2])
    sz = sympify(array[3])
    u1 = sympify(array[4])
    u2 = sympify(array[5])
    v1 = sympify(array[6])
    v2 = sympify(array[7])
    #print("Step 1 - Calculate ds/dv and ds/du")
    #Label(window,text="Step 1 - Calculate ds/dv and ds/du").place(x=csx,y=csy+30)
    #step 1: ds/dv and ds/du =;
    dvsx = diff(sx,v)
    dvsy = diff(sy,v)
    dvsz = diff(sz,v)
    dusx = diff(sx,u)
    dusy = diff(sy,u)
    dusz = diff(sz,u)
    
    #step 2: cross product ds/du x ds/dv = ;
    va = dusy*dvsz-dvsy*dusz
    vb = dvsx*dusz-dusx*dvsz
    vc = dusx*dvsy-dvsx*dusy
    
    #step 3: norm of cross product
    normv = sqrt(va**2 + vb**2 + vc**2)
    
    #step 4: replace x,y,z with s
    f1 = f.subs(x,sx)
    f2 = f1.subs(y,sy)
    f3 = f2.subs(z,sz)
    
    #step 5: new integral is double
    fnew = f3*normv
    
    if (u1.is_number==1 and u2.is_number==1 and v1.is_number==1 and v2.is_number==1):
        
        u1,u2 = warning_one(u1,u2)
        v1,v2 = warning_one(v1,v2)
        #1.
        #Simple u and v
        I1 = integrate(fnew,(u,u1,u2))
        I = integrate(I1,(v,v1,v2))
        if language ==1 :
            mathtext_demos = {
                "Header demo":
                    "",
                "Από Επιφανειακό Ολοκλήρωμα σε Διπλό Ολοκλήρωμα :":
                    "",
                "Βήμα 1 - Υπολογισμός ds/dv και ds/du:":
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(dvsx)+" , "+latex(dvsy)+" , "+latex(dvsz)+" ]$"
                    "\n"
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(dusx)+" , "+latex(dusy)+" , "+latex(dusz)+" ]$",
                "Βήμα 2 - Υπολογισμός του διασταυρούμενου γινομένου:":
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(va)+" , "+latex(vb)+" , "+latex(vc)+" ]$", 
                "Βήμα 3 - Υπολογισμός της norm του παραπάνω διανύσματος:":
                    r"$ \parallel \frac{ \partial s(u,v) }{ \partial v} \times \frac{ \partial s(u,v) }{ \partial u} \parallel =  "+latex(normv)+" $", 
                "Βήμα 4 - Αντικατάσταση σε f(x,y,z):":
                    r" x"+" με "+" x(t) "
                    r" y "+" με "+" y(t) "
                    r" z "+" με "+" z(t) ",
                "Το νέο f(t) είναι:":
                    r"$ f(t) = "+latex(f3)+" $",
                "Το πρώτο ολοκλήρωμα είναι:":
                    r"$I_1 = \int^{"+latex(u2)+"}_{"+latex(u1)+"} "+latex(fnew)+" du $",
                "Το οποίο δίνει:":
                    r"$I_1 = "+latex(I1)+"$",
                "Το δεύτερο ολοκλήρωμα είναι: ":
                    r"$I_2 = \int^{"+latex(v2)+"}_{"+latex(v1)+"} "+latex(I1)+" dv $",
                "Το οποίο δίνει το τελικό αποτέλεσμα:":
                    r"$I_2 = "+latex(I)+" $",
            }
        elif language == 0:
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
                "First Integral is:":
                    r"$I_1 = \int^{"+latex(u2)+"}_{"+latex(u1)+"} "+latex(fnew)+" du $",
                "which gives:":
                    r"$I_1 = "+latex(I1)+"$",
                "Second Integral is: ":
                    r"$I_2 = \int^{"+latex(v2)+"}_{"+latex(v1)+"} "+latex(I1)+" dv $",
                "which gives final result:":
                    r"$I_2 = "+latex(I)+" $",
            }
            
            
        
        
    elif((u1.is_number==0 or u2.is_number==0) and v1.is_number==1 and v2.is_number==1):
        v1,v2 = warning_one(v1,v2)
        #2.
        #Simple u
        #display result...
        I1 = integrate(f,(u,u1,u2))
        I = integrate(I1,(v,v1,v2))
        if language == 1:
            mathtext_demos = {
                "Header demo":
                    "",
                "Από Επιφανειακό Ολοκλήρωμα σε Διπλό Ολοκλήρωμα :":
                    "",
                "Βήμα 1 - Υπολογισμός ds/dv και ds/du:":
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(dvsx)+" , "+latex(dvsy)+" , "+latex(dvsz)+" ]$"
                    "\n"
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(dusx)+" , "+latex(dusy)+" , "+latex(dusz)+" ]$",
                "Βήμα 2 - Υπολογισμός του διασταυρούμενου γινομένου:":
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(va)+" , "+latex(vb)+" , "+latex(vc)+" ]$", 
                "Βήμα 3 - Υπολογισμός της norm του παραπάνω διανύσματος:":
                    r"$ \parallel \frac{ \partial s(u,v) }{ \partial v} \times \frac{ \partial s(u,v) }{ \partial u} \parallel =  "+latex(normv)+" $", 
                "Βήμα 4 - Αντικατάσταση σε f(x,y,z):":
                    r" x "+" με "+" x(t) "
                    r"y "+" με "+" y(t) "
                    r" z "+" με "+" z(t) ",
                "Tο νέο f(t) είναι:":
                    r"$ f(t) = "+latex(f3)+" $",
                "Το πρώτο ολοκλήρωμα είναι:":
                    r"$I_1 = \int^{"+latex(u2)+"}_{"+latex(u1)+"} "+latex(fnew)+" du $",
                "Το οποίο δίνει:":
                    r"$I_1 = "+latex(I1)+"$",
                "Το δεύτερο ολοκλήρωμα είναι: ":
                    r"$I_2 = \int^{"+latex(v2)+"}_{"+latex(v1)+"} "+latex(I1)+" dv $",
                "Το οποίο δίνει το τελικό αποτέλεσμα:":
                    r"$I_2 = "+latex(I)+" $",
            }
        elif language == 0:
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
                "First Integral is:":
                    r"$I_1 = \int^{"+latex(u2)+"}_{"+latex(u1)+"} "+latex(fnew)+" du $",
                "which gives:":
                    r"$I_1 = "+latex(I1)+"$",
                "Second Integral is: ":
                    r"$I_2 = \int^{"+latex(v2)+"}_{"+latex(v1)+"} "+latex(I1)+" dv $",
                "which gives final result:":
                    r"$I_2 = "+latex(I)+" $",
            }
            
       
    else:
        u1,u2 = warning_one(u1,u2)
        #3.
        #Simple v
        #display result...
        I1 = integrate(f,(v,v1,v2))
        I = integrate(I1,(u,u1,u2))
        if language ==1 :
            
            mathtext_demos = {
                "Header demo":
                    "",
                "Από Επιφανειακό Ολοκλήρωμα σε Διπλό Ολοκλήρωμα :":
                    "",
                "Βήμα 1 - Υπολογισμός ds/dv και ds/du:":
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(dvsx)+" , "+latex(dvsy)+" , "+latex(dvsz)+" ]$"
                    "\n"
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(dusx)+" , "+latex(dusy)+" , "+latex(dusz)+" ]$",
                "Βήμα 2 - Υπολογισμός του διασταυρούμενου γινομένου:":
                    r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(va)+" , "+latex(vb)+" , "+latex(vc)+" ]$", 
                "Βήμα 3 - Υπολογισμός της norm του παραπάνω διανύσματος:":
                    r"$ \parallel \frac{ \partial s(u,v) }{ \partial v} \times \frac{ \partial s(u,v) }{ \partial u} \parallel =  "+latex(normv)+" $", 
                "Βήμα 4 - Αντικατάσταση σε f(x,y,z):":
                    r" x "+" με "+" x(t) "
                    r" y "+" με "+" y(t) "
                    r" z "+" με "+" z(t) ",
                "Tο νέο f(t) είναι:":
                    r"$ f(t) = "+latex(f3)+" $",
                "Το πρώτο ολοκλήρωμα είναι:":
                    r"$I_1 = \int^{"+latex(v2)+"}_{"+latex(v1)+"} "+latex(fnew)+" dv $",
                "Το οποίο δίνει:":
                    r"$I_1 = "+latex(I1)+"$",
                "Το δεύτερο ολοκλήρωμα είναι:":
                    r"$I_2 = \int^{"+latex(u2)+"}_{"+latex(u1)+"} "+latex(I1)+" du $",
                "Το οποίο δίνει το τελικό αποτέλεσμα:":
                    r"$I_2 = "+latex(I)+" $",
            }
        elif language ==0:
            
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
                "First Integral is:":
                    r"$I_1 = \int^{"+latex(v2)+"}_{"+latex(v1)+"} "+latex(fnew)+" dv $",
                "which gives:":
                    r"$I_1 = "+latex(I1)+"$",
                "Second Integral is: ":
                    r"$I_2 = \int^{"+latex(u2)+"}_{"+latex(u1)+"} "+latex(I1)+" du $",
                "which gives final result:":
                    r"$I_2 = "+latex(I)+" $",
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
    if language ==1:
        title = "Υπολογισμός επιφανειακού ολοκληρώματος "
    elif language == 0:
        title = "Surface integral calculation"

    ax.set_title(title,
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


# ΕΠΙΦΑΝΕΙΑΚΑ ΟΛΟΚΛΗΡΩΜΑΤΑ ΔΙΑΝΥΣΜΑΤΙΚΗ
def surface_integral_vf(array1,array2,orient,language):
    
    fx, fy, fz, sx, sy, sz, g = symbols('fx fy fz sx sy sz g')
    u1, u2, v1, v2 = symbols('u1 u2 v1 v2')
    x, y, z, v, u = symbols('x y z v u')
    x1, x2, y1, y2, z1, z2 = symbols('x1 x2 y1 y2 z1 z2')
    #csx = 450
    #csy = 20
    #Label(window, text="Transforming Surface integral to Double integral").place(x=csx,y=csy)
    fx = sympify(array1[0])
    fy = sympify(array1[1])
    fz = sympify(array1[2])
    if array2[0] == "":
        sx = sympify(array1[3])
        sy = sympify(array1[4])
        sz = sympify(array1[5])
        u1 = sympify(array1[6])
        u2 = sympify(array1[7])
        v1 = sympify(array1[8])
        v2 = sympify(array1[9])
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
            if language ==1:
                mathtext_demos = {
                    "Header demo":
                        "",
                    "Από Επιφανειακό Ολοκλήρωμa σε Διπλό Ολοκλήρωμa. . :":
                        "",
                    "Βήμα 1 - Υπολογίστε "+r"$ \frac{ d s }{ d v }$"+" and "+r"$ \frac{ d s }{ d u }$"+":":
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(dvsx)+" , "+latex(dvsy)+" , "+latex(dvsz)+" ]$"
                        " and "
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(dusx)+" , "+latex(dusy)+" , "+latex(dusz)+" ]$",
                    "Βήμα 2 - Υπολογίστε το διασταυρούμενο γινόμενο (Συμβουλή 1):":
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(va)+" , "+latex(vb)+" , "+latex(vc)+" ]$", 
                    "Βήμα 3 - Αντικατάσταση "+r"$\vec{F}(x,y,z)$"+":":
                        r"$ x $ "+" με "+r"$ x(u,v) $"+" , "+
                        r"$ y $ "+" με "+r"$ y(u,v) $"+" και "+
                        r"$ z $ "+" με "+r"$ z(u,v) $",
                    "Η νέα συνάρτηση είναι:":
                        r"$ \vec{F} (u,v) = [ "+latex(fx3)+" , "+latex(fy3)+" , "+latex(fz3)+" ] $",
                    "Υπολογισμός Διπλού Ολοκληρώματος . . .":
                        "Η περιοχή D είναι απλή ως προς u και v",
                    "Το πρώτο ολοκλήρωμα είναι:":
                        r"$I_1 = \int^{"+latex(u2)+"}_{"+latex(u1)+"} "+latex(fnew)+" du $",
                    "Που δίνει:":
                        r"$I_1 = "+latex(I1)+"$",
                    "Το δεύτερο ολοκλήρωμα είναι:":
                        r"$I_2 = \int^{"+latex(v2)+"}_{"+latex(v1)+"} "+latex(I1)+" dv $",
                    "που δίνει το τελικό αποτέλεσμα:":
                        r"$I_2 = "+latex(I)+" $",
                    "Υπόδειξη 1":
                        "Θετικός προσανατολισμός: "
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} \times \frac{ \partial \vec{s} (u,v) }{ \partial v} $"
                        " Αρνητικός προσανατολισμός: "
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} $"
                }
            elif language ==0:
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
            
        elif((u1.is_number==0 or u2.is_number==0) and v1.is_number==1 and v2.is_number==1):
            v1,v2 = warning_one(v1,v2)
            #2.
            #Simple u
            #display result...
            I1 = integrate(fnew,(u,u1,u2))
            I = integrate(I1,(v,v1,v2))
            if language == 1:
                mathtext_demos = {
                    "Header demo":
                        "",
                    "Από Επιφανειακό Ολοκλήρωμa σε Διπλό Ολοκλήρωμa. . :":
                        "",
                    "Βήμα 1 - Υπολογίστε τα ds/dv και ds/du:":
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(dvsx)+" , "+latex(dvsy)+" , "+latex(dvsz)+" ]$"
                        " και "
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(dusx)+" , "+latex(dusy)+" , "+latex(dusz)+" ]$",
                    "Βήμα 2 - Υπολογίστε το διασταυρούμενο γινόμενο:":
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(va)+" , "+latex(vb)+" , "+latex(vc)+" ]$", 
                    "Βήμα 3 - Αντικατάσταση "+r"$\vec{F}(x,y,z)$"+":":
                        r"$ x $ "+" με "+r"$ x(u,v) $"+" , "+
                        r"$ y $ "+" με "+r"$ y(u,v) $"+" και "+
                        r"$ z $ "+" με "+r"$ z(u,v) $",
                    "Η νέα συνάρτηση είναι:":
                        r"$ \vec{F} (u,v) = [ "+latex(fx3)+" , "+latex(fy3)+" , "+latex(fz3)+" ] $",
                    "Υπολογισμός Διπλού Ολοκληρώματος . . .":
                        "",
                    "Το πρώτο ολοκλήρωμα είναι:":
                        r"$I_1 = \int^{"+latex(u2)+"}_{"+latex(u1)+"} "+latex(fnew)+" du $",
                    "Που δίνει:":
                        r"$I_1 = "+latex(I1)+"$",
                    "Το δεύτερο ολοκλήρωμα είναι:":
                        r"$I_2 = \int^{"+latex(v2)+"}_{"+latex(v1)+"} "+latex(I1)+" dv $",
                    "που δίνει το τελικό αποτέλεσμα:":
                        r"$I_2 = "+latex(I)+" $",
                    "Υπόδειξη 1":
                        "Θετικός προσανατολισμός: "
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} \times \frac{ \partial \vec{s} (u,v) }{ \partial v} $"
                        " Αρνητικός προσανατολισμός: "
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} $"
                
                }
            elif language == 0:
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
            
        else:
            u1,u2 = warning_one(u1,u2)
            #3.
            #Simple v
            #display result...
            I1 = integrate(fnew,(v,v1,v2))
            I = integrate(I1,(u,u1,u2))
            if language == 1:
                mathtext_demos = {
                    "Header demo":
                        "",
                    "Από Επιφανειακό Ολοκλήρωμa σε Διπλό Ολοκλήρωμa. . :":
                        "",
                    "Βήμα 1 - Υπολογίστε τα ds/dv και ds/du:":
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(dvsx)+" , "+latex(dvsy)+" , "+latex(dvsz)+" ]$"
                        " και "
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(dusx)+" , "+latex(dusy)+" , "+latex(dusz)+" ]$",
                    "Βήμα 2 - Υπολογίστε το διασταυρούμενο γινόμενο:":
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} =  [ "+latex(va)+" , "+latex(vb)+" , "+latex(vc)+" ]$", 
                    "Βήμα 3 - Αντικατάσταση "+r"$\vec{F}(x,y,z)$"+":":
                        r"$ x $ "+" με "+r"$ x(u,v) $"+" , "+
                        r"$ y $ "+" με "+r"$ y(u,v) $"+" και "+
                        r"$ z $ "+" με "+r"$ z(u,v) $",
                    "Η νέα συνάρτηση είναι:":
                        r"$ \vec{F} (u,v) = [ "+latex(fx3)+" , "+latex(fy3)+" , "+latex(fz3)+" ] $",
                    "Υπολογισμός Διπλού Ολοκληρώματος . . .":
                        "",
                    "Το πρώτο ολοκλήρωμα είναι:":
                        r"$I_1 = \int^{"+latex(u2)+"}_{"+latex(u1)+"} "+latex(fnew)+" du $",
                    "Που δίνει:":
                        r"$I_1 = "+latex(I1)+"$",
                    "Το δεύτερο ολοκλήρωμα είναι:":
                        r"$I_2 = \int^{"+latex(v2)+"}_{"+latex(v1)+"} "+latex(I1)+" dv $",
                    "που δίνει το τελικό αποτέλεσμα:":
                        r"$I_2 = "+latex(I)+" $",
                    "Υπόδειξη 1":
                        "Θετικός προσανατολισμός: "
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} \times \frac{ \partial \vec{s} (u,v) }{ \partial v} $"
                        " Αρνητικός προσανατολισμός: "
                        r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} $"
                
                }
                
            elif language == 0:
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
        #end
    elif array2[0] != "":
        g = sympify(array2[0])
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
        
        if array2[5] == "" and array2[6] == "":
            x1 = sympify(array2[1])
            x2 = sympify(array2[2])
            y1 = sympify(array2[3])
            y2 = sympify(array2[4])
            
            #z is empty
            #Label(window, text="Calculating Double Integral ...").place(x=csx,y=csy)
            if (x1.is_number==1 and x2.is_number==1 and y1.is_number==1 and y2.is_number==1):
                x1,x2 = warning_one(x1,x2)
                y1,y2 = warning_one(y1,y2)
                #1.
                #Simple x and y
                I1 = integrate(fnew,(x,x1,x2))
                I = integrate(I1,(y,y1,y2))
                if language ==1:
                    mathtext_demos = {
                        "Header demo":
                            "",
                        "Από Επιφανειακό Ολοκλήρωμa σε Διπλό Ολοκλήρωμα . . .:":
                            "",
                        "Βήμα 1 - Υπολογίστε "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                        "Βήμα 2 - Εύρεση "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                            r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                        "Βήμα 3 - Υπολογίστε "+r"$ \hat{n} $"+":":
                            r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                        "Βήμα 4 - Το νέο "+r"$\vec{F}(x,y,z)$"+"  είναι":
                            r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                        "Υπολογισμός Διπλού Ολοκληρώματος . . .":
                            "",
                        "Το πρώτο ολοκλήρωμα είναι:":
                            r"$I_1 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(fnew)+" dx $",
                        "Που δίνει":
                            r"$I_1 = "+latex(I1)+"$",
                        "Το δεύτερο ολοκλήρωμα είναι:":
                            r"$I_2 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(I1)+" dy $",
                        "που δίνει το τελικό αποτέλεσμα:":
                            r"$I_2 = "+latex(I)+" $",
                        "Υπόδειξη 1":
                            "Θετικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} \times \frac{ \partial \vec{s} (u,v) }{ \partial v} $"
                            " Αρνητικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} $"
                    }
                        
                elif language == 0:
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
            elif((x1.is_number==0 or x2.is_number==0) and y1.is_number==1 and y2.is_number==1):
                y1,y2 = warning_one(y1,y2)
                #2.
                #Simple x
                #display result...
                I1 = integrate(fnew,(x,x1,x2))
                I = integrate(I1,(y,y1,y2))
                if language ==1 :
                    mathtext_demos = {
                        "Header demo":
                            "",
                        "Από Επιφανειακό Ολοκλήρωμa σε Διπλό Ολοκλήρωμα . . .:":
                            "",
                        "Βήμα 1 - Υπολογίστε "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                        "Βήμα 2 - Εύρεση "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                            r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                        "Βήμα 3 - Υπολογίστε "+r"$ \hat{n} $"+":":
                            r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                        "Βήμα 4 - Το νέο "+r"$\vec{F}(x,y,z)$"+"  είναι":
                            r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                        "Υπολογισμός Διπλού Ολοκληρώματος . . .":
                            "",
                        "Το πρώτο ολοκλήρωμα είναι:":
                            r"$I_1 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(fnew)+" dx $",
                        "Που δίνει":
                            r"$I_1 = "+latex(I1)+"$",
                        "Το δεύτερο ολοκλήρωμα είναι:":
                            r"$I_2 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(I1)+" dy $",
                        "που δίνει το τελικό αποτέλεσμα:":
                            r"$I_2 = "+latex(I)+" $",
                        "Υπόδειξη 1":
                            "Θετικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} \times \frac{ \partial \vec{s} (u,v) }{ \partial v} $"
                            " Αρνητικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} $"
                    }
                   
                elif language == 0:
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
            else:
                x1,x2 = warning_one(x1,x2)
                #3.
                #Simple y
                #display result...
                I1 = integrate(fnew,(y,y1,y2))
                I = integrate(I1,(x,x1,x2))
                if language == 1:
                    mathtext_demos = {
                        "Header demo":
                            "",
                        "Από Επιφανειακό Ολοκλήρωμa σε Διπλό Ολοκλήρωμα . . .:":
                            "",
                        "Βήμα 1 - Υπολογίστε "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                        "Βήμα 2 - Εύρεση "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                            r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                        "Βήμα 3 - Υπολογίστε "+r"$ \hat{n} $"+":":
                            r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                        "Βήμα 4 - Το νέο "+r"$\vec{F}(x,y,z)$"+"  είναι":
                            r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                        "Υπολογισμός Διπλού Ολοκληρώματος . . .":
                            "",
                        "Το πρώτο ολοκλήρωμα είναι:":
                            r"$I_1 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(fnew)+" dy $",
                        "Που δίνει:":
                            r"$I_1 = "+latex(I1)+"$",
                        "Τ δεύτερο ολοκλήρωμα είναι ":
                            r"$I_2 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(I1)+" dx $",
                        "Που δίνει το τελικό αποτέλεσμα:":
                            r"$I_2 = "+latex(I)+" $",
                        "Υπόδειξη 1":
                            "Θετικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} \times \frac{ \partial \vec{s} (u,v) }{ \partial v} $"
                            " Αρνητικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} $"
                   }
                elif language == 0:
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
            #end
        elif array2[3] == "" and array2[4] == "":
            x1 = sympify(array2[1])
            x2 = sympify(array2[2])
            z1 = sympify(array2[5])
            z2 = sympify(array2[6])
            #y is empty
            
            #Label(window, text="Calculating Double Integral ...").place(x=csx,y=csy)
            
            if (x1.is_number==1 and x2.is_number==1 and z1.is_number==1 and z2.is_number==1):
                x1,x2 = warning_one(x1,x2)
                z1,z2 = warning_one(z1,z2)
                #1.
                #Simple x and z
                I1 = integrate(fnew,(x,x1,x2))
                I = integrate(I1,(z,z1,z2))
                if language == 1:
                    
                    mathtext_demos = {
                        "Header demo":
                            "",
                        "Από Επιφανειακό Ολοκλήρωμa σε Διπλό Ολοκλήρωμα . . .:":
                            "",
                        "Βήμα 1 - Υπολογίστε "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                        "Βήμα 2 - Εύρεση "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                            r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                        "Βήμα 3 - Υπολογίστε "+r"$ \hat{n} $"+":":
                            r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                        "Βήμα 4 - Το νέο "+r"$\vec{F}(x,y,z)$"+"  είναι":
                            r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                        "Υπολογισμός Διπλού Ολοκληρώματος . . .":
                            "",
                        "Το πρώτο ολοκλήρωμα είναι:":
                            r"$I_1 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(fnew)+" dx $",
                        "Που δίνει :":
                            r"$I_1 = "+latex(I1)+"$",
                        "Το δεύτερο ολοκλήρωμα είναι:":
                            r"$I_2 = \int^{"+latex(z2)+"}_{"+latex(z1)+"} "+latex(I1)+" dz $",
                        "που δίνει το τελικό αποτέλεσμα:":
                            r"$I_2 = "+latex(I)+" $",
                        "Υπόδειξη 1":
                            "Θετικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} \times \frac{ \partial \vec{s} (u,v) }{ \partial v} $"
                            " Αρνητικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} $"
                   }
                elif language == 0:
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
            elif((x1.is_number==0 or x2.is_number==0) and z1.is_number==1 and z2.is_number==1):
                z1,z2 = warning_one(z1,z2)
                #2.
                #Simple x
                #display result...
                I1 = integrate(fnew,(x,x1,x2))
                I = integrate(I1,(z,z1,z2))
                if language == 1:
                    
                    mathtext_demos = {
                        "Header demo":
                            "",
                        "Από Επιφανειακό Ολοκλήρωμa σε Διπλό Ολοκλήρωμα . . .:":
                            "",
                        "Βήμα 1 - Υπολογίστε "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                        "Βήμα 2 - Εύρεση "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                            r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                        "Βήμα 3 - Υπολογίστε "+r"$ \hat{n} $"+":":
                            r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                        "Βήμα 4 - Το νέο "+r"$\vec{F}(x,y,z)$"+"  είναι":
                            r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                        "Υπολογισμός Διπλού Ολοκληρώματος . . .":
                            "",
                        "Το πρώτο ολοκλήρωμα είναι:":
                            r"$I_1 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(fnew)+" dx $",
                        "Που δίνει :":
                            r"$I_1 = "+latex(I1)+"$",
                        "Το δεύτερο ολοκλήρωμα είναι:":
                            r"$I_2 = \int^{"+latex(z2)+"}_{"+latex(z1)+"} "+latex(I1)+" dz $",
                        "που δίνει το τελικό αποτέλεσμα:":
                            r"$I_2 = "+latex(I)+" $",
                        "Υπόδειξη 1":
                            "Θετικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} \times \frac{ \partial \vec{s} (u,v) }{ \partial v} $"
                            " Αρνητικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} $"
                   }
                elif language == 0:
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
                
            else:
                x1,x2 = warning_one(x1,x2)
                #3.
                #Simple z
                #display result...
                I1 = integrate(fnew,(z,z1,z2))
                I = integrate(I1,(x,x1,x2))
                if language == 1:
                    mathtext_demos = {
                        "Header demo":
                            "",
                        "Από Επιφανειακό Ολοκλήρωμa σε Διπλό Ολοκλήρωμα . . .:":
                            "",
                        "Βήμα 1 - Υπολογίστε "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                        "Βήμα 2 - Εύρεση "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                            r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                        "Βήμα 3 - Υπολογίστε "+r"$ \hat{n} $"+":":
                            r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                        "Βήμα 4 - Το νέο "+r"$\vec{F}(x,y,z)$"+"  είναι":
                            r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                        "Υπολογισμός Διπλού Ολοκληρώματος . . .":
                            "",
                        "Το πρώτο ολοκλήρωμα είναι:":
                            r"$I_1 = \int^{"+latex(z2)+"}_{"+latex(z1)+"} "+latex(fnew)+" dz $",
                        "Που δίνει":
                            r"$I_1 = "+latex(I1)+"$",
                        "Το δεύτερο ολοκλήρωμα είναι:":
                            r"$I_2 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(I1)+" dx $",
                        "που δίνει το τελικό αποτέλεσμα:":
                            r"$I_2 = "+latex(I)+" $",
                        "Υπόδειξη 1":
                            "Θετικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} \times \frac{ \partial \vec{s} (u,v) }{ \partial v} $"
                            " Αρνητικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} $"
                   }
                elif language == 0:
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
                
            #end
        elif array2[1] == "" and array2[2] == "":
            y1 = sympify(array2[3])
            y2 = sympify(array2[4])
            z1 = sympify(array2[5])
            z2 = sympify(array2[6])
            #x is empty
            #Label(window, text="Calculating Double Integral ...").place(x=csx,y=csy)
            
            if (y1.is_number==1 and y2.is_number==1 and z1.is_number==1 and z2.is_number==1):
                y1,y2 = warning_one(y1,y2)
                z1,z2 = warning_one(z1,z2)
                #1.
                #Simple y and z
                I1 = integrate(fnew,(y,y1,y2))
                I = integrate(I1,(z,z1,z2))
                if language == 1:
                    
                    mathtext_demos = {
                        "Header demo":
                            "",
                        "Από Επιφανειακό Ολοκλήρωμa σε Διπλό Ολοκλήρωμα . . .:":
                            "",
                        "Βήμα 1 - Υπολογίστε "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                        "Βήμα 2 - Εύρεση "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                            r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                        "Βήμα 3 - Υπολογίστε "+r"$ \hat{n} $"+":":
                            r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                        "Βήμα 4 - Το νέο "+r"$\vec{F}(x,y,z)$"+"  είναι":
                            r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                        "Υπολογισμός Διπλού Ολοκληρώματος . . .":
                            "",
                        "Το πρώτο ολοκλήρωμα είναι:":
                            r"$I_1 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(fnew)+" dy $",
                        "Που δίνει":
                            r"$I_1 = "+latex(I1)+"$",
                        "Το δεύτερο ολοκλήρωμα είναι:":
                            r"$I_2 = \int^{"+latex(z2)+"}_{"+latex(z1)+"} "+latex(I1)+" dz $",
                        "που δίνει το τελικό αποτέλεσμα:":
                            r"$I_2 = "+latex(I)+" $",
                        "Υπόδειξη 1":
                            "Θετικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} \times \frac{ \partial \vec{s} (u,v) }{ \partial v} $"
                            " Αρνητικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} $"
                   }
                elif language ==0:
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
            elif((y1.is_number==0 or y2.is_number==0) and z1.is_number==1 and z2.is_number==1):
                z1,z2 = warning_one(z1,z2)
                #2.
                #Simple y
                #display result...
                I1 = integrate(fnew,(y,y1,y2))
                I = integrate(I1,(z,z1,z2))
                if language == 1:
                    
                    mathtext_demos = {
                        "Header demo":
                            "",
                        "Από Επιφανειακό Ολοκλήρωμa σε Διπλό Ολοκλήρωμα . . .:":
                            "",
                        "Βήμα 1 - Υπολογίστε "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                        "Βήμα 2 - Εύρεση "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                            r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                        "Βήμα 3 - Υπολογίστε "+r"$ \hat{n} $"+":":
                            r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                        "Βήμα 4 - Το νέο "+r"$\vec{F}(x,y,z)$"+"  είναι":
                            r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                        "Υπολογισμός Διπλού Ολοκληρώματος . . .":
                            "",
                        "Το πρώτο ολοκλήρωμα είναι:":
                            r"$I_1 = \int^{"+latex(y2)+"}_{"+latex(y1)+"} "+latex(fnew)+" dy $",
                        "Που δίνει":
                            r"$I_1 = "+latex(I1)+"$",
                        "Το δεύτερο ολοκλήρωμα είναι:":
                            r"$I_2 = \int^{"+latex(z2)+"}_{"+latex(z1)+"} "+latex(I1)+" dz $",
                        "που δίνει το τελικό αποτέλεσμα:":
                            r"$I_2 = "+latex(I)+" $",
                        "Υπόδειξη 1":
                            "Θετικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} \times \frac{ \partial \vec{s} (u,v) }{ \partial v} $"
                            " Αρνητικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} $"
                   }
                elif language == 0:
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
                
            else:
                y1,y2 = warning_one(y1,y2)
                #3.
                #Simple z
                #display result...
                I1 = integrate(fnew,(z,z1,z2))
                I = integrate(I1,(y,y1,y2))
                if language ==1 :
                    mathtext_demos = {
                        "Header demo":
                            "",
                        "Από Επιφανειακό Ολοκλήρωμa σε Διπλό Ολοκλήρωμα . . .:":
                            "",
                        "Βήμα 1 - Υπολογίστε "+r"$ \vec{ \nabla } g(x,y,z) $"+":":
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} =  [ "+latex(gradgx)+" , "+latex(gradgy)+" , "+latex(gradgz)+" ]$",
                        "Βήμα 2 - Εύρεση "+r"$\parallel \nabla g(x,y,z) \parallel $"+":":
                            r"$ \parallel \vec{ \nabla } g(x,y,z) \parallel =  "+latex(normg)+" $", 
                        "Βήμα 3 - Υπολογίστε "+r"$ \hat{n} $"+":":
                            r"$ \hat{n} = \frac{ \vec{ \nabla } g(x,y,z) }{ \parallel \vec{ \nabla } g(x,y,z) \parallel } = [ "+latex(nvx)+" , "+latex(nvy)+" , "+latex(nvz)+" ] $",
                        "Βήμα 4 - Το νέο "+r"$\vec{F}(x,y,z)$"+"  είναι":
                            r"$ \vec{F}_{(x,y,z)} = ( \vec{F} \cdot \hat{n} )~\parallel \vec{ \nabla } g(x,y,z) \parallel = [ "+latex(fnew)+" $",
                        "Υπολογισμός Διπλού Ολοκληρώματος . . .":
                            "",
                        "Το πρώτο ολοκλήρωμα είναι:":
                            r"$I_1 = \int^{"+latex(z2)+"}_{"+latex(z1)+"} "+latex(fnew)+" dz $",
                        "Που δίνει":
                            r"$I_1 = "+latex(I1)+"$",
                        "Το δεύτερο ολοκλήρωμα είναι:":
                            r"$I_2 = \int^{"+latex(x2)+"}_{"+latex(x1)+"} "+latex(I1)+" dx $",
                        "που δίνει το τελικό αποτέλεσμα:":
                            r"$I_2 = "+latex(I)+" $",
                        "Υπόδειξη 1":
                            "Θετικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial u} \times \frac{ \partial \vec{s} (u,v) }{ \partial v} $"
                            " Αρνητικός προσανατολισμός: "
                            r"$ \frac{ \partial \vec{s} (u,v) }{ \partial v} \times \frac{ \partial \vec{s} (u,v) }{ \partial u} $"
                   }
                    
                elif language == 0:
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
    if language == 1:
        title = "Υπολογισμός επιφανειακού ολοκληρώματος  ..."
    elif language == 0:
        title = "Calculating Surface Integral ..."
    ax.set_title(title,
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
    
    plt.show(block=False)
#end



#ΚΕΝΤΡΙΚΟ ΜΕΝΟΥ 

#menu1_def,menu1_def_2, menu2_def, menu2_def_2= form['menu1_def'],form['menu1_def_2'],form['menu2_def'],form['menu2_def_2']
def open_window():
    menu1_def_2 = [ ['LANGUAGE',['GREEK','ENGLISH']],['HELP', help_int2]]
    #ΑΓΓΛΙΚΑ
    title_frame_2 = [
                [sg.Text("", key='text_frame2',size=(125,1),justification='center',font=('Helvetica', 24, 'bold'),background_color='light blue',text_color='black')]
                ]
    #ΑΓΓΛΙΚΑ
    col1_2 = [ [sg.Text('',size=(35, 1),background_color='light blue')], 
            [sg.Text('Choose a function type:',size=(35, 1), font=('Helvetica', 13, 'bold'))],
            [sg.InputCombo(menu_kindf2 , key ='menu_kindf2', default_value='GRADE',size=(20, 1))],
            [sg.Text('',size=(35, 1), background_color='light blue')],
                  
            [sg.Text('Choose the type of integral:',size=(35, 1), font=('Helvetica', 13, 'bold'))],
            [sg.InputCombo(menu_kind_int2 , key = 'menu_kind_int2' , default_value='DOUBLE',size=(20, 1))],
            [sg.Text('',size=(35, 1),background_color='light blue')], 
            
            [sg.Text('Choose coordinates:',size=(35, 1), font=('Helvetica', 13, 'bold'))],
            [sg.InputCombo(menu_kind_coordinate2, key='menu_kind_coordinate2', default_value='CARTESIAN',size=(20, 1))],
            
            
            [sg.Text('',size=(35, 1),background_color='light blue')],
            [sg.Text('',size=(35, 1),background_color='light blue')], [sg.Text('',size=(35, 1),background_color='light blue')],
            
            ]

    #ΑΓΓΛΙΚΑ
    frame1_2 = [[sg.Frame('',col1_2,background_color='light blue'),sg.Image('integral2.png',size=(650,320))] ]
    #end
    #ΑΓΓΛΙΚΑ
    col2_2 = [   [sg.Text('',size=(125, 1),background_color='light blue')],
               [sg.Text('',size=(63, 1),background_color='light blue'),sg.Button('PREVIOUS',button_color=('black', '')),
               sg.Text('',size=(5, 1),background_color='light blue'),sg.Button('NEXT',button_color=('black', '')),
               sg.Text('',size=(5, 1),background_color='light blue'),sg.Button('EXIT',button_color=('black', '')),
               sg.Text('',size=(5, 1),background_color='light blue')], 
            ]

    menu2_def_2 = [
            [sg.Column(col2_2, background_color='light blue')],
            ]

    #ΑΓΓΛΙΚΑ
    frame2_col1_2 = [
            [sg.Text('DATA INPUT', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='l')],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Give the function f (x, y):',size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=ΕΝ_double_inputs1[0],size =(50, 1))],
            [sg.Text('Give x1:', size =(35, 1), font=('Helvetica', 13, 'bold'))], [ sg.InputText(key=ΕΝ_double_inputs1[1],size =(50, 1))],
            [sg.Text('Give x2:', size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=ΕΝ_double_inputs1[2],size =(50, 1))],
            [sg.Text('Give y1:', size =(35, 1), font=('Helvetica', 13, 'bold'))], [ sg.InputText(key=ΕΝ_double_inputs1[3],size =(50, 1))],
            [sg.Text('Give y2:', size =(35, 1), font=('Helvetica', 13, 'bold'))], [ sg.InputText(key=ΕΝ_double_inputs1[4],size =(50, 1))],    
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('CALCULATION', key =calculate2[0] ,button_color=('black', '')),
            sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('CLEANING', key =clear2[0]  ,button_color=('black', ''))],
            
        ]

    frame2_2 = [ [sg.Column(frame2_col1_2, background_color='light blue'),sg.Image('integral2.png',size=(650,320))] ]

    #ΑΓΓΛΙΚΑ
    frame3_col1_2 = [
            [sg.Text('DATA INPUT', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='l')],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Give the function f (x, y):',size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=ΕΝ_double_inputs2[0],size =(50, 1))],
            [sg.Text('Give ρ1:', size =(35, 1), font=('Helvetica', 13, 'bold'))], [ sg.InputText(key=ΕΝ_double_inputs2[1],size =(50, 1))],
            [sg.Text('Give ρ2:', size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=ΕΝ_double_inputs2[2],size =(50, 1))],
            [sg.Text('Give θ1:', size =(35, 1), font=('Helvetica', 13, 'bold'))], [ sg.InputText(key=ΕΝ_double_inputs2[3],size =(50, 1))],
            [sg.Text('Give θ2:', size =(35, 1), font=('Helvetica', 13, 'bold'))], [ sg.InputText(key=ΕΝ_double_inputs2[4],size =(50, 1))],    
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('CALCULATION', key =calculate2[1] ,button_color=('black', '')),
            sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('CLEANING', key =clear2[1]  ,button_color=('black', ''))],
            
        ]

    frame3_2 = [ [sg.Column(frame3_col1_2, background_color='light blue'),sg.Image('integral2.png',size=(650,320))] ]

    #ΑΓΓΛΙΚΑ
    frame4_col1_2 = [
                [sg.Text('DATA INPUT', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='l')],
                [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
                [sg.Text('Give the function f (x, y):',size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=ΕΝ_triple_inputs1[0],size =(50, 1))],
                [sg.Text('Give the edge x1:', size =(17, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=ΕΝ_triple_inputs1[1],size =(23, 1))],
                [sg.Text('Give the edge x2:', size =(17, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=ΕΝ_triple_inputs1[2],size =(23, 1))],
                [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
                [sg.Text('Give the edge y1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_triple_inputs1[3],size =(23, 1))],
                [sg.Text('Give the edge y2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_triple_inputs1[4],size =(23, 1))],
                [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
                [sg.Text('Give the edge z1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_triple_inputs1[5],size =(23, 1))], 
                [sg.Text('Give the edge z2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_triple_inputs1[6],size =(23, 1))],    
                [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
                [sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('CALCULATION', key =calculate2[2] ,button_color=('black', '')),
                sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('CLEANING', key =clear2[2]  ,button_color=('black', '')),
                  ],       
            ]
    frame4_2 = [ [sg.Column(frame4_col1_2, background_color='light blue'),sg.Image('integral2.png',size=(650,320))] ]
    #end
    
    #ΑΓΓΛΙΚΑ
    frame5_col1_2 = [
            [sg.Text('DATA INPUT', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='l')],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Give the function f(x,y,z):',size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=ΕΝ_triple_inputs2[0],size =(50, 1))],
            [sg.Text('Give the edge r1:', size =(17, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=ΕΝ_triple_inputs2[1],size =(23, 1))],
            [sg.Text('Give the edge r2:', size =(17, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=ΕΝ_triple_inputs2[2],size =(23, 1))],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Give the edge θ1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_triple_inputs2[3],size =(23, 1))],
            [sg.Text('Give the edge θ2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_triple_inputs2[4],size =(23, 1))],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Give the edge φ1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_triple_inputs2[5],size =(23, 1))], 
            [sg.Text('Give the edge φ2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_triple_inputs2[6],size =(23, 1))],    
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('CALCULATION', key =calculate2[3] ,button_color=('black', '')),
            sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('CLEANING', key =clear2[3]  ,button_color=('black', '')),
              ],
            ]

    frame5_2 = [[sg.Column(frame5_col1_2, background_color='light blue'),sg.Image('integral2.png',size=(650,320))]]
    #end
    #ΑΓΓΛΙΚΑ
    frame6_col1_2 = [
        [sg.Text('DATA INPUT', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='l')],
        [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
        [sg.Text('Give the function f(x,y,z):',size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=ΕΝ_triple_inputs3[0],size =(50, 1))],
        [sg.Text('Give the edge r1:', size =(17, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=ΕΝ_triple_inputs3[1],size =(23, 1))],
        [sg.Text('Give the edge r2:', size =(17, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=ΕΝ_triple_inputs3[2],size =(23, 1))],
        [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
        [sg.Text('Give the edge θ1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_triple_inputs3[3],size =(23, 1))],
        [sg.Text('Give the edge θ2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_triple_inputs3[4],size =(23, 1))],
        [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
        [sg.Text('Give the edge φ1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_triple_inputs3[5],size =(23, 1))], 
        [sg.Text('Give the edge φ2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_triple_inputs3[6],size =(23, 1))],    
        [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
        [sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('CALCULATION', key =calculate2[4] ,button_color=('black', '')),
        sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('CLEANING', key =clear2[4]  ,button_color=('black', '')),
          ],
        ]
    frame6_2 = [[sg.Column(frame6_col1_2, background_color='light blue'),sg.Image('integral2.png',size=(650,320))]]
    #end
    #ΑΓΓΛΙΚΑ
    frame7_col1_2 = [
            [sg.Text('DATA INPUT', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='l')],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Give the function f(x,y,z):',size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=ΕΝ_triple_inputs4[0],size =(50, 1))],
            [sg.Text('Give the edge ρ1:', size =(17, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=ΕΝ_triple_inputs4[1],size =(23, 1))],
            [sg.Text('Give the edge ρ2:', size =(17, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=ΕΝ_triple_inputs4[2],size =(23, 1))],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Give the edge φ1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_triple_inputs4[3],size =(23, 1))],
            [sg.Text('Give the edge φ2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_triple_inputs4[4],size =(23, 1))],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Give the edge ζ1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_triple_inputs4[5],size =(23, 1))], 
            [sg.Text('Give the edge ζ2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_triple_inputs4[6],size =(23, 1))],    
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('CALCULATION', key =calculate2[5] ,button_color=('black', '')),
            sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('CLEANING', key =clear2[5]  ,button_color=('black', '')),
              ],
            ]
    frame7_2 = [[sg.Column(frame7_col1_2, background_color='light blue'),sg.Image('integral2.png',size=(650,320))]]
    #end

    #ΑΓΓΛΙΚΑ
    frame8_col1_2 = [
            [sg.Text('DATA INPUT', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='l')],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Give the function f(x,y,z):',size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=ΕΝ_line_inputs1[0],size =(32, 1))],
            [sg.Text('Give the curve c(t) = [x(t), y(t), z(t)]:', size =(35, 1), font=('Helvetica', 13, 'bold'))],
            [sg.Text('x(t)=', size =(5, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=ΕΝ_line_inputs1[1],size =(23, 1))],
            [sg.Text('y(t)=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_line_inputs1[2],size =(23, 1))],
            [sg.Text('z(t)=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_line_inputs1[3],size =(23, 1))],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Give the edges t1 and t2:',size =(35, 1), font=('Helvetica', 13, 'bold'))], 
            [sg.Text('t1=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_line_inputs1[4],size =(23, 1))], 
            [sg.Text('t2=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_line_inputs1[5],size =(23, 1))],    
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('CALCULATION', key =calculate2[6] ,button_color=('black', '')),
            sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('CLEANING', key =clear2[6]  ,button_color=('black', '')),
              ],
            ]
    frame8_2 = [[sg.Column(frame8_col1_2, background_color='light blue'),sg.Image('integral2.png',size=(650,320))]]
    #end 

    #ΑΓΓΛΙΚΑ
    frame9_col1_2 = [
            [sg.Text('DATA INPUT', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='l')],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Give the function F(x,y,z)= [F1, F2, F3]:',size =(36, 1), font=('Helvetica', 13, 'bold'))], 
            [sg.Text('F1(x,y,z)=', size =(8, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=ΕΝ_line_inputs2[0],size =(23, 1))],
            [sg.Text('F2(x,y,z)=',size =(8, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_line_inputs2[1],size =(23, 1))],
            [sg.Text('F3(x,y,z)=',size =(8, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_line_inputs2[2],size =(23, 1))],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Give the curve c(t) = [x(t), y(t), z(t)]:', size =(36, 1), font=('Helvetica', 13, 'bold'))],
            [sg.Text('x(t)=', size =(5, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=ΕΝ_line_inputs2[3],size =(23, 1))],
            [sg.Text('y(t)=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_line_inputs2[4],size =(23, 1))],
            [sg.Text('z(t)=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_line_inputs2[5],size =(23, 1))],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            
            ]
    frame9_col2_col1_2 = [
         [sg.Text('',size=(15, 1),background_color='light steel blue')],
         [sg.Text('',size=(1, 1),background_color='light steel blue'),sg.Button('CALCULATION',size=(13, 1),key = calculate2[7],button_color=('black', ''))],
         [sg.Text('',size=(1, 1),background_color='light steel blue'),sg.Button('CLEANING',size=(13, 1),key = clear2[7] ,button_color=('black', ''))],
         [sg.Text('',size=(1, 1),background_color='light steel blue'),sg.Button('THEOREM Green ',size=(13, 1),key = 'green2' ,button_color=('black', ''))]

        ] 
    frame9_col2_col2_2 = [
        [sg.Text('Give the edges t1 and t2:',size =(25, 1), font=('Helvetica', 13, 'bold'))], 
        [sg.Text('t1=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_line_inputs2[6],size =(23, 1))], 
        [sg.Text('t2=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_line_inputs2[7],size =(23, 1))],    
        [sg.Text('_'*100,size=(55, 1),background_color='light blue')],
        [sg.Text('Second import method:',size =(35, 1),background_color='light coral', font=('Helvetica', 15, 'bold'))], 
        ]
    frame9_col2_col3_2 = [
        [sg.Text('If you have a circle centered in K(x0,y0,z0): (x-x0)^2 + (y-y0)^2 = r^2',size=(70, 1),background_color='light steel blue')],
        [sg.Text('then: c(t)=[r*cos(t)+x0 , r*sin(t)+y0 , z0] with t in [0,2π].',size=(70, 1),background_color='light steel blue')],
        [sg.Text('If you have an ellipse centered in K(x0,y0,z0): (x-x0/a)^2 + (y-y0/b)^2 = 1',size=(70, 1),background_color='light steel blue')],
        [sg.Text('then: c(t) = [a*cos(t) , b*sin(t), z0] with t in [0,2π].',size=(70, 1),background_color='light steel blue')],
        [sg.Text("Use Green's Theorem for any other curve that cannot be entered with above 2 ways.",size=(70, 1),background_color='light steel blue')],
        ]
    frame9_col2_col4_2 = [
        [sg.Text('Give the points of a line AB:',size =(60, 1), font=('Helvetica', 13, 'bold'))], 
        [sg.Text('xa=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_line_inputs2[8],size =(23, 1)),
        sg.Text('',size=(12, 1),background_color='light blue'), sg.Text('xb=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_line_inputs2[9],size =(23, 1))], 
        [sg.Text('ya=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_line_inputs2[10],size =(23, 1)),
        sg.Text('',size=(12, 1),background_color='light blue'),  sg.Text('yb=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_line_inputs2[11],size =(23, 1))], 
        [sg.Text('za=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_line_inputs2[12],size =(23, 1)),
         sg.Text('',size=(12, 1),background_color='light blue'), sg.Text('zb=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_line_inputs2[13],size =(23, 1))], 
        ]
    frame9_col2_2 = [
        [sg.Column(frame9_col2_col2_2, size=(400,145), background_color='light blue'),sg.Frame('',layout=frame9_col2_col1_2, size=(220,145), background_color='light steel blue')],
        [sg.Column(frame9_col2_col4_2, size=(620,115), background_color='light blue')],
        [sg.Column(frame9_col2_col3_2, size=(620,150), background_color='light steel blue')]
        ]

    frame9_2 = [[sg.Column(frame9_col1_2, background_color='light blue'),sg.Column(frame9_col2_2, background_color='light blue')]]
    #end  
    #ΑΓΓΛΙΚΑ
    frame10_col1_2 = [
            [sg.Text('DATA INPUT', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='center')],
            [sg.Text('_'*100,size=(54, 1),background_color='light blue')],
            [sg.Text('Give the function f(x,y,z):',size =(40, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=ΕΝ_surface_inputs1[0],size =(35, 1))],
            [sg.Text('Give the surface s(u,v)=[x(u,v), y(u,v), z(u,v)]:', size =(40, 1), font=('Helvetica', 13, 'bold'))],
            [sg.Text('x(u,v)=', size =(7, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=ΕΝ_surface_inputs1[1],size =(23, 1))],
            [sg.Text('y(u,v)=',size =(7, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs1[2],size =(23, 1))],
            [sg.Text('z(u,v)=',size =(7, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs1[3],size =(23, 1))],
            [sg.Text('_'*100,size=(54, 1),background_color='light blue')],
            [sg.Text('Give the edge u1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs1[4],size =(23, 1))], 
            [sg.Text('Give the edge u2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs1[5],size =(23, 1))],    
            [sg.Text('Give the edge v1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs1[6],size =(23, 1))], 
            [sg.Text('Give the edge v2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs1[7],size =(23, 1))],    
            [sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('CALCULATION',size=(13, 1),key = calculate2[8],button_color=('black', '')),
             sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('CLEANING',size=(13, 1),key = clear2[8] ,button_color=('black', ''))],
            ]

    frame10_2 = [[sg.Column(frame10_col1_2, background_color='light blue'),sg.Image('integral2.png',size=(650,320))]]
    #end

    #ΑΓΓΛΙΚΑ
    frame11_col1_2 =[
        [sg.Text('DATA INPUT', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='center')],
        [sg.Text('_'*100,size=(54, 1),background_color='light blue')],
        [sg.Text('Give the function F(x,y,z)= [F1, F2, F3]:',size =(40, 1), font=('Helvetica', 13, 'bold'))], 
        [sg.Text('F1(x,y,z)=', size =(9, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=ΕΝ_surface_inputs2[0],size =(23, 1))],
        [sg.Text('F2(x,y,z)=',size =(9, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs2[1],size =(23, 1))],
        [sg.Text('F3(x,y,z)=',size =(9, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs2[2],size =(23, 1))],
        
        [sg.Text('Give the surface s(u,v)=[x(u,v), y(u,v), z(u,v)]:', size =(40, 1), font=('Helvetica', 13, 'bold'))],
        [sg.Text('x(u,v)=', size =(9, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=ΕΝ_surface_inputs2[3],size =(23, 1))],
        [sg.Text('y(u,v)=',size =(9, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs2[4],size =(23, 1))],
        [sg.Text('z(u,v)=',size =(9, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs2[5],size =(23, 1))],
        [sg.Text('_'*100,size=(54, 1),background_color='light blue')],
        [sg.Text('Surface orientation:', size =(40, 1), font=('Helvetica', 13, 'bold'))],
        [sg.Button('Positive',size=(13, 1),key = 'positive',button_color=('black', '')),sg.Button('negative',size=(13, 1),key = 'negative',button_color=('black', ''))]
        
        ]   
    frame11_col2_col1_2 = [
         [sg.Text('',size=(15, 1),background_color='light steel blue')],
         [sg.Text('',size=(1, 1),background_color='light steel blue'),sg.Button('CALCULATION',size=(13, 1),key = calculate2[9],button_color=('black', ''))],
         [sg.Text('',size=(15, 1),background_color='light steel blue')],

         [sg.Text('',size=(1, 1),background_color='light steel blue'),sg.Button('CLEANING',size=(13, 1),key = clear2[9] ,button_color=('black', ''))]

        ] 
    frame11_col2_col2_2 = [
        [sg.Text('Give the edges u1 and u2:',size =(23, 1), font=('Helvetica', 13, 'bold'))],
        [sg.Text('u1=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs2[6],size =(23, 1))], 
        [sg.Text('u2=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs2[7],size =(23, 1))],    
        [sg.Text('Give the edges v1 and v2:',size =(23, 1), font=('Helvetica', 13, 'bold'))], 
        [sg.Text('v1=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs2[8],size =(23, 1))], 
        [sg.Text('v2=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs2[9],size =(23, 1))],    
        
        ]
    frame11_col2_2 = [
         [sg.Column(frame11_col2_col2_2, size=(400,180), background_color='light blue'),sg.Frame('',layout=frame11_col2_col1_2, size=(220,180), background_color='light steel blue')

         ], 
        [sg.Text('Second import method:',size =(60, 1),background_color='light coral', font=('Helvetica', 15, 'bold'))], 
        [sg.Text('Give the function s(x,y,z)=0,  η οποία περιγράφει την επιφάνεια:',size =(60, 1), font=('Helvetica', 13, 'bold'))], 
        [sg.Text('s(x,y,z)= 0 =', size =(7, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=surface_inputs2[10],size =(23, 1))],
        [sg.Text('Give the edges for x,y,z:',size =(46, 1), font=('Helvetica', 13, 'bold'))], 
        [sg.Text('x1=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs2[11],size =(23, 1)),
         sg.Text('x2=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs2[12],size =(23, 1))], 
        [sg.Text('y1=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs2[13],size =(23, 1)),
         sg.Text('y2=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs2[14],size =(23, 1))], 
        [sg.Text('z1=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs2[15],size =(23, 1)),
         sg.Text('z2=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=ΕΝ_surface_inputs2[16],size =(23, 1))], 

        ]
    frame11_2 = [
            [sg.Column(frame11_col1_2, background_color='light blue'),
                sg.Column(layout=frame11_col2_2,size=(625,420), background_color='light blue')]]
    
    #ΑΓΓΛΙΚΑ       
    frame_2 = [
         

        [sg.Frame("", layout=frame1_2, size=(1070,420), visible=True,   key='Frame1_2', element_justification='center', background_color='light blue'),
        sg.Frame("", layout=frame2_2, size=(1070,420), visible=False,   key='Frame2_2' , element_justification='left' ,background_color='light blue'),
        sg.Frame("", layout=frame3_2,  size=(1070,420),visible=False,   key='Frame3_2' , element_justification='left' , background_color='light blue'),
        sg.Frame("", layout=frame4_2,  size=(1070,420),visible=False,   key='Frame4_2' , element_justification='left' , background_color='light blue'),
        sg.Frame("", layout=frame5_2,  size=(1070,420),visible=False,   key='Frame5_2' , element_justification='left' , background_color='light blue'),
        sg.Frame("", layout=frame6_2,  size=(1070,420),visible=False,   key='Frame6_2' , element_justification='left' , background_color='light blue'),
        sg.Frame("", layout=frame7_2,  size=(1070,420),visible=False,   key='Frame7_2' , element_justification='left' , background_color='light blue'),
        sg.Frame("", layout=frame8_2,  size=(1070,420),visible=False,   key='Frame8_2' , element_justification='left' , background_color='light blue'),
        sg.Frame("", layout=frame9_2,  size=(1070,420),visible=False,   key='Frame9_2' , element_justification='left' , background_color='light blue'),
        sg.Frame("", layout=frame10_2,  size=(1070,425),visible=False,   key='Frame10_2' , element_justification='left' , background_color='light blue'),
        sg.Frame("", layout=frame11_2,  size=(1070,425),visible=False,   key='Frame11_2' , element_justification='left' , background_color='light blue')],
        ]
        
    # ------ GUI Defintion ------ #
    
    layout2 = [ [sg.Menu(menu1_def_2 )],
              [sg.Frame("", layout=title_frame_2, size=(1070,80), element_justification='center', background_color='light blue')],
              [sg.Column( frame_2,  key='frame',element_justification='center')],
              [sg.Frame("", layout=menu2_def_2, size=(1070,80), background_color='light blue')]
              
              ]  
    window = sg.Window("INTEGRAL CALCULATOR", layout2, modal=True).Finalize()
    #form.Layout(layout).Finalize()

    frame1_2,frame2_2,frame3_2,frame4_2, frame5_2 , frame6_2, frame7_2, frame8_2, frame9_2, frame10_2, frame11_2 = window['Frame1_2'], window['Frame2_2'],window['Frame3_2'], window['Frame4_2'], window['Frame5_2'], window['Frame6_2'], window['Frame7_2'], window['Frame8_2'], window['Frame9_2'], window['Frame10_2'], window['Frame11_2']

    window['text_frame2'].update(text_frame2[0])
    page=0
    orient=1
    language = 0
    counter1,counter2,counter=0,0,0
    key=keys[0]
    array_inputs = ['','','','','','','']
    while True:
        event, times = window.read()
        if event == "EXIT" or event == sg.WIN_CLOSED:
            break
        elif event == 'positive':
            orient = 1
        elif event == 'negative':
            orient = 2
        if event == 'ENGLISH':
            language = 0
        elif event == 'GREEK':
            language = 1
            window.close()
            first_window()
 

            
        #ΔΙΠΛΑ ΚΑΡΤΕΣΙΑΝΕΣ    
        if event == calculate2[0] :
            counter=0
            pc=0
            key = keys2[0]
            array_inputs=[times[ΕΝ_double_inputs1[0]],times[ΕΝ_double_inputs1[1]],times[ΕΝ_double_inputs1[2]],times[ΕΝ_double_inputs1[3]],times[ΕΝ_double_inputs1[4]]]
            print(array_inputs)
            counter = check_inputs(array_inputs)
            for x in range(len(array_inputs)):
                array_inputs[x] = correction(array_inputs[x],language)

            if counter >= 1:
                sg.Popup('You do not enter all the data! \nFill in all the input fields to do the calculation!!',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                double_integral(array_inputs,pc,language)
        #ΔΙΠΛΑ ΠΟΛΙΚΕΣ        
        elif event == calculate2[1] :
            counter=0
            pc=1
            key = keys2[1]
            array_inputs=[times[ΕΝ_double_inputs2[0]],times[ΕΝ_double_inputs2[1]],times[ΕΝ_double_inputs2[2]],times[ΕΝ_double_inputs2[3]],times[ΕΝ_double_inputs2[4]]]
            counter = check_inputs(array_inputs)
            for x in range(len(array_inputs)):
                array_inputs[x] = correction(array_inputs[x],language)

            if counter >= 1:
                sg.Popup('You do not enter all the data! \nFill in all the input fields to do the calculation!!',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                double_integral(array_inputs,pc,language)
        #ΤΡΙΠΛΑ ΚΑΡΤΕΣΙΑΝΕΣ
        elif event == calculate2[2] :
            counter=0
            key = keys2[2]
            array_inputs=[times[ΕΝ_triple_inputs1[0]],times[ΕΝ_triple_inputs1[1]],times[ΕΝ_triple_inputs1[2]],times[ΕΝ_triple_inputs1[3]],times[ΕΝ_triple_inputs1[4]],times[ΕΝ_triple_inputs1[5]],times[ΕΝ_triple_inputs1[6]]]
            counter = check_inputs(array_inputs)
            for x in range(len(array_inputs)):
                array_inputs[x] = correction(array_inputs[x],language)

            if counter >= 1:
                sg.Popup('You do not enter all the data! \nFill in all the input fields to do the calculation!!',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                print('ihfud')
                ti_cc_main_func(array_inputs,language)
                
        #ΤΡΙΠΛΑ ΣΦΑΙΡΙΚΕΣ
        elif event == calculate2[3] :
            counter=0
            key = keys2[3]
            array_inputs=[times[ΕΝ_triple_inputs2[0]],times[ΕΝ_triple_inputs2[1]],times[ΕΝ_triple_inputs2[2]],times[ΕΝ_triple_inputs2[3]],times[ΕΝ_triple_inputs2[4]],times[ΕΝ_triple_inputs2[5]],times[ΕΝ_triple_inputs2[6]]]
            counter = check_inputs(array_inputs)
            for x in range(len(array_inputs)):
                array_inputs[x] = correction(array_inputs[x],language)

            if counter >= 1:
                sg.Popup('You do not enter all the data! \nFill in all the input fields to do the calculation!!',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                print('ihfud')
                ti_sc_main_func(array_inputs,language)
        
        #ΤΡΙΠΛΑ ΕΛΛΕΙΠΤΙΚΕΣ
        elif event == calculate2[4] :
            counter=0
            key = keys2[4]
            array_inputs=[times[ΕΝ_triple_inputs3[0]],times[ΕΝ_triple_inputs3[1]],times[ΕΝ_triple_inputs3[2]],times[ΕΝ_triple_inputs3[3]],times[ΕΝ_triple_inputs3[4]],times[ΕΝ_triple_inputs3[5]],times[ΕΝ_triple_inputs3[6]]]
            counter = check_inputs(array_inputs)
            for x in range(len(array_inputs)):
                array_inputs[x] = correction(array_inputs[x],language)

            if counter >= 1:
                sg.Popup('You do not enter all the data! \nFill in all the input fields to do the calculation!!',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                ti_ec_main_func(array_inputs,language)
        
        #ΤΡΙΠΛΑ ΚΥΛΙΝΔΡΙΚΕΣ
        elif event == calculate2[5] :
            counter=0
            pc=4
            key = keys2[5]
            array_inputs=[times[ΕΝ_triple_inputs4[0]],times[ΕΝ_triple_inputs4[1]],times[ΕΝ_triple_inputs4[2]],times[ΕΝ_triple_inputs4[3]],times[ΕΝ_triple_inputs4[4]],times[ΕΝ_triple_inputs4[5]],times[ΕΝ_triple_inputs4[6]]]
            counter = check_inputs(array_inputs)
            for x in range(len(array_inputs)):
                array_inputs[x] = correction(array_inputs[x],language)

            if counter >= 1:
                sg.Popup('You do not enter all the data! \nFill in all the input fields to do the calculation!!',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                ti_cyc_main_func(array_inputs,language)
        
                
        #ΕΠΙΚΑΜΠΥΛΙΑ ΒΑΘΜΩΤΗ
        elif event == calculate2[6]:
            counter=0
            key = keys2[6]
            array_inputs=[times[ΕΝ_line_inputs1[0]],times[ΕΝ_line_inputs1[1]],times[ΕΝ_line_inputs1[2]],times[ΕΝ_line_inputs1[3]],times[ΕΝ_line_inputs1[4]],times[ΕΝ_line_inputs1[5]]]
            counter = check_inputs(array_inputs)
            for x in range(len(array_inputs)):
                array_inputs[x] = correction(array_inputs[x],language)

            if counter >= 1:
                sg.Popup('You do not enter all the data! \nFill in all the input fields to do the calculation!!',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                curve_integral(array_inputs,language)
        
        #ΕΠΙΚΑΜΠΥΛΙΑ ΔΙΑΝΥΣΜΑΤΙΚΗ 
        elif event == calculate2[7]:
            counter=0
            key = keys2[7]
            array_inputs=[times[ΕΝ_line_inputs2[0]],times[ΕΝ_line_inputs2[1]],times[ΕΝ_line_inputs2[2]],times[ΕΝ_line_inputs2[3]],times[ΕΝ_line_inputs2[4]],times[ΕΝ_line_inputs2[5]],times[ΕΝ_line_inputs2[6]],times[ΕΝ_line_inputs2[7]],times[ΕΝ_line_inputs2[8]],times[ΕΝ_line_inputs2[9]],times[ΕΝ_line_inputs2[10]],times[ΕΝ_line_inputs2[11]],times[ΕΝ_line_inputs2[12]],times[ΕΝ_line_inputs2[13]]]
            if array_inputs[8] == "" and array_inputs[9] == "" and array_inputs[10] == "":
                counter=0
                i=0
                array1=['','','','','','','','']
                array2=['','','','','','']
                while i<8:
                    array1[i]=array_inputs[i]
                    i=i+1
                counter = check_inputs(array1)
                for x in range(len(array1)):
                    array_inputs[x] = correction(array1[x],language)

            elif array_inputs[8] != "" and array_inputs[9] != "" and array_inputs[10] != "":
                counter1,counter2,counter=0,0,0
                i=0
                array1=['','','']
                array2=['','','','','','']
                while i<3:
                    array1[i]=array_inputs[i]
                    i=i+1
                
                counter1 = check_inputs(array1)
                for x in range(len(array1)):
                    array_inputs[x] = correction(array1[x],language)

                i=8
                j=0
                while i<14:
                    array2[j]=array_inputs[i]
                    j=j+1
                    i=i+1
                counter2 = check_inputs(array2)
                for x in range(len(array2)):
                    array_inputs[x] = correction(array2[x],language)

                counter = counter1 + counter2
            if counter >= 1:
                sg.Popup('You do not enter all the data! \nFill in all the input fields to do the calculation!!',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                curve_integral_vf(array1,array2,language)
                
        #ΒΑΘΜΩΤΗ ΕΠΙΦΑΝΕΙΑΚA          
        elif event == calculate2[8]:
            counter=0
            key = keys2[8]
            array_inputs=[times[ΕΝ_surface_inputs1[0]],times[ΕΝ_surface_inputs1[1]],times[ΕΝ_surface_inputs1[2]],times[ΕΝ_surface_inputs1[3]],times[ΕΝ_surface_inputs1[4]],times[ΕΝ_surface_inputs1[5]],times[ΕΝ_surface_inputs1[6]],times[ΕΝ_surface_inputs1[7]]]
            counter = check_inputs(array_inputs)
            for x in range(len(array_inputs)):
                array_inputs[x] = correction(array_inputs[x],language)

            if counter >= 1:
                sg.Popup('You do not enter all the data! \nFill in all the input fields to do the calculation!!',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                surface_integral(array_inputs,language)
         
        #ΔΙΑΝΥΣΜΑΤΙΚΗ ΕΠΙΦΑΝΕΙΑΚA          
        elif event == calculate2[9]:
            key = keys2[9]
            array_inputs=[times[ΕΝ_surface_inputs2[0]],times[ΕΝ_surface_inputs2[1]],times[ΕΝ_surface_inputs2[2]],times[ΕΝ_surface_inputs2[3]],times[ΕΝ_surface_inputs2[4]],times[ΕΝ_surface_inputs2[5]],times[ΕΝ_surface_inputs2[6]],times[ΕΝ_surface_inputs2[7]],times[ΕΝ_surface_inputs2[8]],times[ΕΝ_surface_inputs2[9]],times[ΕΝ_surface_inputs2[10]],times[ΕΝ_surface_inputs2[11]],times[ΕΝ_surface_inputs2[12]],times[ΕΝ_surface_inputs2[13]],times[ΕΝ_surface_inputs2[14]],times[ΕΝ_surface_inputs2[15]],times[ΕΝ_surface_inputs2[16]]]
            if array_inputs[10] == "":
                counter=0
                i=0
                array1=['','','','','','','','','','']
                array2=['','','','','','','']
                while i<10:
                    array1[i]=array_inputs[i]
                    i=i+1
                counter = check_inputs(array1)
                for x in range(len(array1)):
                    array_inputs[x] = correction(array1[x],language)

            elif array_inputs[10] != "":
                counter1,counter2,counter=0,0,0
                i=0
                array1=['','','']
                array2=['','','','','','','',]
                while i<3:
                    array1[i]=array_inputs[i]
                    i=i+1
                
                counter1 = check_inputs(array1)
                for x in range(len(array1)):
                    array_inputs[x] = correction(array1[x],language)

                i=10
                j=0
                while i<17:
                    array2[j]=array_inputs[i]
                    j=j+1
                    i=i+1
                counter2 = check_inputs(array2)
                for x in range(len(array2)):
                    array_inputs[x] = correction(array2[x],language)

                counter = counter1 + counter2
            if (orient < 1 and orient>2):
                  sg.Popup('You have not entered all the data! \n\nChoose a surface orientation to do the calculation!',title='ΕΙΔΟΠΟΙΗΣΗ !!!') 
            if counter >= 1:
                sg.Popup('You do not enter all the data! \nFill in all the input fields to do the calculation!!',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            
            elif counter == 0:
                surface_integral_vf(array1,array2,orient,language)
        
        for x in clear2:
            if event == x:
                array_out = array_inputs
                i=0
                for x in array_inputs:
                    x =''
                    array_out[i] = x
                    i=i+1
                for x in key:
                    window[x]('')
                    
        
         
        
        for x in help_int2:
                if event == x:
                   help_DEF(help_info2[x])
                    
        if event == 'NEXT':
                print('khsafudbuj')
                for x in menu_kindf2:
                    if x == times['menu_kindf2']:
                        temp2 = x
                for x in menu_kind_int2:
                     if x == times['menu_kind_int2']:
                         temp3 = x
                      
                for x in menu_kind_coordinate2:
                     if x == times['menu_kind_coordinate2']:
                         temp4 = x
                         #sg.Popup(x)

                #ΒΑΘΜΩΤΗ ΔΙΠΛΑ ΚΑΡΤΕΣΙΑΝΕΣ
                if  temp2==menu_kindf2[0] and temp3==menu_kind_int2[0] and temp4==menu_kind_coordinate2[0]:
                     page=1
                     key=keys2[0]
                     window['text_frame2'].update(text_frame2[1])
                     window['Frame3_2'].update(visible=False)
                     window['Frame4_2'].update(visible= False)
                     window['Frame5_2'].update(visible= False)
                     window['Frame6_2'].update(visible= False)
                     window['Frame7_2'].update(visible= False)
                     window['Frame8_2'].update(visible= False)
                     window['Frame9_2'].update(visible= False)
                     window['Frame10_2'].update(visible= False)
                     window['Frame11_2'].update(visible= False)
                     window['Frame1_2'].update(visible=False)
                     window['Frame2_2'].update(visible=True)
                #end
                
                #ΒΑΘΜΩΤΗ ΔΙΠΛΑ ΠΟΛΙΚΕΣ
                elif temp2==menu_kindf2[0] and temp3 == menu_kind_int2[0] and temp4 == menu_kind_coordinate2[1]:
                     page=2
                     key=keys2[1]
                     window['text_frame2'].update(text_frame2[2])
                     
                     window['Frame4_2'].update(visible= False)
                     window['Frame5_2'].update(visible= False)
                     window['Frame6_2'].update(visible= False)
                     window['Frame7_2'].update(visible= False)
                     window['Frame8_2'].update(visible= False)
                     window['Frame9_2'].update(visible= False)
                     window['Frame10_2'].update(visible= False)
                     window['Frame11_2'].update(visible= False)
                     window['Frame1_2'].update(visible=False)
                     window['Frame3_2'].update(visible=True)
                #end
                
                #ΒΑΘΜΩΤΗ ΤΡΙΠΛΑ ΚΑΡΤΕΣΙΑΝΕΣ
                elif temp2==menu_kindf2[0] and temp3 == menu_kind_int2[1] and temp4 == menu_kind_coordinate2[0]:
                     page=3
                     key=keys2[2]
                     window['text_frame2'].update(text_frame2[3])
                     window['Frame2_2'].update(visible= False)
                     window['Frame3_2'].update(visible=False)
                     window['Frame5_2'].update(visible= False)
                     window['Frame6_2'].update(visible= False)
                     window['Frame7_2'].update(visible= False)
                     window['Frame8_2'].update(visible= False)
                     window['Frame9_2'].update(visible= False)
                     window['Frame10_2'].update(visible= False)
                     window['Frame11_2'].update(visible= False)
                     window['Frame1_2'].update(visible=False)
                     window['Frame4_2'].update(visible=True)
                     
                    # output.update(visible=True)
                     #end
                #ΒΑΘΜΩΤΗ ΤΡΙΠΛΑ ΣΦΑΙΡΙΚΕΣ
                elif temp2==menu_kindf2[0] and temp3 == menu_kind_int2[1] and temp4 == menu_kind_coordinate2[2]:
                     page=4
                     key=keys2[3]
                     window['text_frame2'].update(text_frame2[4])
                     window['Frame2_2'].update(visible= False)
                     window['Frame3_2'].update(visible=False)
                     window['Frame4_2'].update(visible= False)
                     window['Frame6_2'].update(visible= False)
                     window['Frame7_2'].update(visible= False)
                     window['Frame8_2'].update(visible= False)
                     window['Frame9_2'].update(visible= False)
                     window['Frame10_2'].update(visible= False)
                     window['Frame11_2'].update(visible= False)
                     window['Frame1_2'].update(visible=False)
                     window['Frame5_2'].update(visible=True)
                    #end
                #ΒΑΘΜΩΤΗ ΤΡΙΠΛΑ ΕΛΛΕΙΠΤΙΚΕΣ
                elif temp2==menu_kindf2[0] and temp3 == menu_kind_int2[1] and temp4 == menu_kind_coordinate2[3]:
                     page=5
                     key=keys2[4]
                     window['text_frame2'].update(text_frame2[5])
                     window['Frame2_2'].update(visible= False)
                     window['Frame3_2'].update(visible=False)
                     window['Frame4_2'].update(visible= False)
                     window['Frame5_2'].update(visible= False)
                     window['Frame7_2'].update(visible= False)
                     window['Frame8_2'].update(visible= False)
                     window['Frame9_2'].update(visible= False)
                     window['Frame10_2'].update(visible= False)
                     window['Frame11_2'].update(visible= False)
                     window['Frame1_2'].update(visible=False)
                     window['Frame6_2'].update(visible=True)
                     #output.update(visible=True)
                     #end
                     
                #ΒΑΘΜΩΤΗ ΤΡΙΠΛΑ ΚΥΛΙΝΔΡΙΚΕΣ
                elif temp2==menu_kindf2[0] and temp3 == menu_kind_int2[1] and temp4 == menu_kind_coordinate2[4]:
                     page=6
                     key=keys2[5]
                     window['text_frame2'].update(text_frame2[6])
                     window['Frame2_2'].update(visible= False)
                     window['Frame3_2'].update(visible=False)
                     window['Frame4_2'].update(visible= False)
                     window['Frame5_2'].update(visible= False)
                     window['Frame6_2'].update(visible= False)
                     window['Frame8_2'].update(visible= False)
                     window['Frame9_2'].update(visible= False)
                     window['Frame10_2'].update(visible= False)
                     window['Frame11_2'].update(visible= False)
                     window['Frame1_2'].update(visible=False)
                     window['Frame7_2'].update(visible=True)
                     #end
                #ΒΑΘΜΩΤΗ ΕΠΙΚΑΜΠΥΛΙΑ
                elif temp2==menu_kindf2[0] and temp3 == menu_kind_int2[2]:
                     page=7
                     key=keys2[6]    
                     window['text_frame2'].update(text_frame2[7])
                     window['Frame2_2'].update(visible= False)
                     window['Frame3_2'].update(visible=False)
                     window['Frame4_2'].update(visible= False)
                     window['Frame5_2'].update(visible= False)
                     window['Frame6_2'].update(visible= False)
                     window['Frame7_2'].update(visible= False)
                     window['Frame9_2'].update(visible= False)
                     window['Frame10_2'].update(visible= False)
                     window['Frame11_2'].update(visible= False)
                     window['Frame1_2'].update(visible=False)
                     window['Frame8_2'].update(visible=True)
                     #end
                #ΔΙΑΝΥΣΜΑΤΙΚΗ ΕΠΙΚΑΜΠΥΛΙΑ
                elif temp2==menu_kindf2[1] and temp3 == menu_kind_int2[2]:
                     page=8
                     key=keys2[7]
                     window['text_frame2'].update(text_frame2[7])
                     window['Frame2_2'].update(visible= False)
                     window['Frame3_2'].update(visible=False)
                     window['Frame4_2'].update(visible= False)
                     window['Frame5_2'].update(visible= False)
                     window['Frame6_2'].update(visible= False)
                     window['Frame7_2'].update(visible= False)
                     window['Frame8_2'].update(visible= False)
                     window['Frame10_2'].update(visible= False)
                     window['Frame11_2'].update(visible= False)
                     window['Frame1_2'].update(visible=False)
                     window['Frame9_2'].update(visible=True)
                     #end
                #ΒΑΘΜΩΤΗ ΕΠΙΦΑΝΕΙΑΚA      
                elif temp2==menu_kindf2[0] and temp3 == menu_kind_int2[3]:
                    page=10
                    key=keys2[8]
                    window['text_frame2'].update(text_frame2[9])
                    window['Frame2_2'].update(visible= False)
                    window['Frame3_2'].update(visible=False)
                    window['Frame4_2'].update(visible= False)
                    window['Frame5_2'].update(visible= False)
                    window['Frame6_2'].update(visible= False)
                    window['Frame7_2'].update(visible= False)
                    window['Frame8_2'].update(visible= False)
                    window['Frame9_2'].update(visible= False)
                    window['Frame11_2'].update(visible= False)
                    window['Frame1_2'].update(visible=False)
                    window['Frame10_2'].update(visible=True)
                #end
                #ΔΙΑΝΥΣΜΑΤΙΚΗ ΕΠΙΦΑΝΕΙΑΚA      
                elif temp2==menu_kindf2[1] and temp3 == menu_kind_int2[3]:
                    page=11
                    key=keys2[9]
                    window['text_frame2'].update(text_frame2[10])
                    window['Frame2_2'].update(visible= False)
                    window['Frame3_2'].update(visible=False)
                    window['Frame4_2'].update(visible= False)
                    window['Frame5_2'].update(visible= False)
                    window['Frame6_2'].update(visible= False)
                    window['Frame7_2'].update(visible= False)
                    window['Frame8_2'].update(visible= False)
                    window['Frame9_2'].update(visible= False)
                    window['Frame10_2'].update(visible= False)
                    window['Frame1_2'].update(visible=False)
                    window['Frame11_2'].update(visible=True)
                   # output.update(visible=True)
                #end
        elif event == 'PREVIOUS':
                 if page==0:
                     print('')
                 elif page!=0:
                     counter=0
                     for x in array_inputs:
                         counter
                         if x == '':
                             counter=counter+1
                     
                     if counter >=1:
                         print('kl')
                         window['text_frame2'].update(text_frame2[0])
                         window['Frame2_2'].update(visible= False)
                         window['Frame3_2'].update(visible=False)
                         window['Frame4_2'].update(visible= False)
                         window['Frame5_2'].update(visible= False)
                         window['Frame6_2'].update(visible= False)
                         window['Frame7_2'].update(visible= False)
                         window['Frame8_2'].update(visible= False)
                         window['Frame9_2'].update(visible= False)
                         window['Frame10_2'].update(visible= False)
                         window['Frame11_2'].update(visible= False)
                         window['Frame1_2'].update(visible=True)
                         continue
                     elif counter == 0:
                         click = sg.popup_ok_cancel('Your data will be lost do you want to continue?',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
                         if click == 'OK':
                             #ΚΑΘΑΡΙΣΜΟΣ inputs
                             #array_inputs = clear_inputs(array_inputs,key)
                             
                             array_out = array_inputs
                             i=0
                             for x in array_inputs:
                                 x =''
                                 array_out[i] = x
                                 i=i+1
                             for x in key:
                                 window[x]('')
                                 
                             #end
                             page=0
                             window['text_frame2'].update(text_frame2[0])
                             window['Frame2_2'].update(visible= False)
                             window['Frame3_2'].update(visible=False)
                             window['Frame4_2'].update(visible= False)
                             window['Frame5_2'].update(visible= False)
                             window['Frame6_2'].update(visible= False)
                             window['Frame7_2'].update(visible= False)
                             window['Frame8_2'].update(visible= False)
                             window['Frame9_2'].update(visible= False)
                             window['Frame10_2'].update(visible= False)
                             window['Frame11_2'].update(visible= False)
                             window['Frame1_2'].update(visible=True)
                         elif click == 'Cancel':
                             print('')
        
        
    window.close()

def first_window():  
    menu1_def = [ ['ΓΛΩΣΣΑ',['ΕΛΛΗΝΙΚΑ','ΑΓΓΛΙΚΑ']],['ΒΟΗΘΕΙΑ', help_int]]


    #ΤΙΤΛΟΙ ΣΕΛΙΔΩΝ
    title_frame = [
                [sg.Text("", key='text_frame',size=(125,1),justification='center',font=('Helvetica', 24, 'bold'),background_color='light blue',text_color='black')]
                ]

    #1ο ΣΚΕΛΟΣ ΑΠΟ ΑΡΧΙΚΗ ΣΕΛΙΔΑ
    col1 = [ [sg.Text('',size=(35, 1),background_color='light blue')], 
            [sg.Text('Διάλεξτε είδος συνάρτησης:',size=(35, 1), font=('Helvetica', 13, 'bold'))],
            [sg.InputCombo(menu_kindf , key ='menu_kindf', default_value='ΒΑΘΜΩΤΗ',size=(20, 1))],
            [sg.Text('',size=(35, 1), background_color='light blue')],
                  
            [sg.Text('Διάλεξτε είδος ολοκληρώματος:',size=(35, 1), font=('Helvetica', 13, 'bold'))],
            [sg.InputCombo(menu_kind_int , key = 'menu_kind_int' , default_value='ΔΙΠΛΑ',size=(20, 1))],
            [sg.Text('',size=(35, 1),background_color='light blue')], 
            
            [sg.Text('Διάλεξτε συντεταγμένες:',size=(35, 1), font=('Helvetica', 13, 'bold'))],
            [sg.InputCombo(menu_kind_coordinate, key='menu_kind_coordinate', default_value='ΚΑΡΤΕΣΙΑΝΕΣ',size=(20, 1))],
            
            
            [sg.Text('',size=(35, 1),background_color='light blue')],
            [sg.Text('',size=(35, 1),background_color='light blue')], 
            
            
            ]

    #2ο ΣΚΕΛΟΣ ΑΠΟ ΑΡΧΙΚΗ ΣΕΛΙΔΑ
    col2 = [   [sg.Text('',size=(125, 1),background_color='light blue')],
               [sg.Text('',size=(63, 1),background_color='light blue'),sg.Button('ΠΡΟΗΓΟΥΜΕΝΟ',button_color=('black', '')),
               sg.Text('',size=(5, 1),background_color='light blue'),sg.Button('ΕΠΟΜΕΝΟ',button_color=('black', '')),
               sg.Text('',size=(5, 1),background_color='light blue'),sg.Button('ΕΞΟΔΟΣ',button_color=('black', '')),
               sg.Text('',size=(5, 1),background_color='light blue')], 
            ]


    #ΔΕΥΤΕΡΟ ΜΕΝΟΥ ΚΑΤΩ (ΥΠΟΣΕΛΙΔΟ)
    menu2_def = [
            [sg.Column(col2, background_color='light blue')],
            ]

    #ΑΡΧΙΚΗ ΣΕΛΙΔΑ
    frame1 = [[sg.Frame('',col1,background_color='light blue'),sg.Image('integral2.png',size=(650,320))] ]
    #end

    #ΔΕΥΤΕΡΕΥΟΥΣΕΣ ΣΕΛΙΔΕΣ


    #ΔΙΠΛΑ ΚΑΡΤΕΣΙΑΝΕΣ
    frame2_col1 = [
            [sg.Text('ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='l')],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Δώστε την συνάρτηση f(x,y):', size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=double_inputs1[0] ,size =(50, 1))],
            [sg.Text('Δώστε τo άκρο x1:', size =(35, 1),font=('Helvetica', 13, 'bold'))], [sg.InputText(key=double_inputs1[1] ,size =(50, 1))],
            [sg.Text('Δώστε τo άκρο x2:', size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=double_inputs1[2] ,size =(50, 1))],
            [sg.Text('Δώστε τo άκρο y1:', size =(35, 1),font=('Helvetica', 13, 'bold'))], [sg.InputText(key=double_inputs1[3] ,size =(50, 1))],
            [sg.Text('Δώστε τo άκρο y2:', size =(35, 1),font=('Helvetica', 13, 'bold'))], [sg.InputText(key=double_inputs1[4] ,size =(50, 1))],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('ΥΠΟΛΟΓΙΣΜΟΣ', key =calculate[0] ,button_color=('black', '')),
            sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('ΚΑΘΑΡΙΣΜΟΣ', key =clear[0] ,button_color=('black', '')),
              ],

        
            ]

    frame2 = [ [sg.Column(frame2_col1, background_color='light blue'),sg.Image('integral2.png',size=(650,320))] ]

    #ΔΙΠΛΑ ΠΟΛΙΚΕΣ
    frame3_col1 = [
            [sg.Text('ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='l')],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Δώστε την συνάρτηση f(x,y):',size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=double_inputs2[0],size =(50, 1))],
            [sg.Text('Δώστε τo ρ1:', size =(35, 1), font=('Helvetica', 13, 'bold'))], [ sg.InputText(key=double_inputs2[1],size =(50, 1))],
            [sg.Text('Δώστε τo ρ2:', size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=double_inputs2[2],size =(50, 1))],
            [sg.Text('Δώστε τo θ1:', size =(35, 1), font=('Helvetica', 13, 'bold'))], [ sg.InputText(key=double_inputs2[3],size =(50, 1))],
            [sg.Text('Δώστε τo θ2:', size =(35, 1), font=('Helvetica', 13, 'bold'))], [ sg.InputText(key=double_inputs2[4],size =(50, 1))],    
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('ΥΠΟΛΟΓΙΣΜΟΣ', key =calculate[1] ,button_color=('black', '')),
            sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('ΚΑΘΑΡΙΣΜΟΣ', key =clear[1]  ,button_color=('black', ''))],
            
        ]

    frame3 = [ [sg.Column(frame3_col1, background_color='light blue'),sg.Image('integral2.png',size=(650,320))] ]

    #ΤΡΙΠΛΑ 
    #ΚΑΡΤΕΣΙΑΝΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ
    frame4_col1 = [
                [sg.Text('ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='l')],
                [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
                [sg.Text('Δώστε την συνάρτηση f(x,y,z):',size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=triple_inputs1[0],size =(50, 1))],
                [sg.Text('Δώστε τo άκρο x1:', size =(17, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=triple_inputs1[1],size =(23, 1))],
                [sg.Text('Δώστε τo άκρο x2:', size =(17, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=triple_inputs1[2],size =(23, 1))],
                [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
                [sg.Text('Δώστε τo άκρο y1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=triple_inputs1[3],size =(23, 1))],
                [sg.Text('Δώστε τo άκρο y2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=triple_inputs1[4],size =(23, 1))],
                [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
                [sg.Text('Δώστε τo άκρο z1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=triple_inputs1[5],size =(23, 1))], 
                [sg.Text('Δώστε τo άκρο z2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=triple_inputs1[6],size =(23, 1))],    
                [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
                [sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('ΥΠΟΛΟΓΙΣΜΟΣ', key =calculate[2] ,button_color=('black', '')),
                sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('ΚΑΘΑΡΙΣΜΟΣ', key =clear[2]  ,button_color=('black', '')),
                  ],       
            ]
    frame4 = [ [sg.Column(frame4_col1, background_color='light blue'),sg.Image('integral2.png',size=(650,320))] ]
    #end

    #ΣΦΑΙΡΙΚΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ
    frame5_col1 = [
            [sg.Text('ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='l')],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Δώστε την συνάρτηση f(x,y,z):',size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=triple_inputs2[0],size =(50, 1))],
            [sg.Text('Δώστε τo άκρο r1:', size =(17, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=triple_inputs2[1],size =(23, 1))],
            [sg.Text('Δώστε τo άκρο r2:', size =(17, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=triple_inputs2[2],size =(23, 1))],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Δώστε τo άκρο θ1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=triple_inputs2[3],size =(23, 1))],
            [sg.Text('Δώστε τo άκρο θ2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=triple_inputs2[4],size =(23, 1))],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Δώστε τo άκρο φ1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=triple_inputs2[5],size =(23, 1))], 
            [sg.Text('Δώστε τo άκρο φ2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=triple_inputs2[6],size =(23, 1))],    
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('ΥΠΟΛΟΓΙΣΜΟΣ', key =calculate[3] ,button_color=('black', '')),
            sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('ΚΑΘΑΡΙΣΜΟΣ', key =clear[3]  ,button_color=('black', '')),
              ],
            ]

    frame5 = [[sg.Column(frame5_col1, background_color='light blue'),sg.Image('integral2.png',size=(650,320))]]
    #end

    #ΤΡΙΠΛΑ ΕΛΛΕΙΠΤΙΚΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ
    frame6_col1 = [
        [sg.Text('ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='l')],
        [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
        [sg.Text('Δώστε την συνάρτηση f(x,y,z):',size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=triple_inputs3[0],size =(50, 1))],
        [sg.Text('Δώστε τo άκρο r1:', size =(17, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=triple_inputs3[1],size =(23, 1))],
        [sg.Text('Δώστε τo άκρο r2:', size =(17, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=triple_inputs3[2],size =(23, 1))],
        [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
        [sg.Text('Δώστε τo άκρο θ1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=triple_inputs3[3],size =(23, 1))],
        [sg.Text('Δώστε τo άκρο θ2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=triple_inputs3[4],size =(23, 1))],
        [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
        [sg.Text('Δώστε τo άκρο φ1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=triple_inputs3[5],size =(23, 1))], 
        [sg.Text('Δώστε τo άκρο φ2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=triple_inputs3[6],size =(23, 1))],    
        [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
        [sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('ΥΠΟΛΟΓΙΣΜΟΣ', key =calculate[4] ,button_color=('black', '')),
        sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('ΚΑΘΑΡΙΣΜΟΣ', key =clear[4]  ,button_color=('black', '')),
          ],
        ]
    frame6 = [[sg.Column(frame6_col1, background_color='light blue'),sg.Image('integral2.png',size=(650,320))]]
    #end

    #ΤΡΙΠΛΑ ΚΥΛΙΝΔΡΙΚΕΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ
    frame7_col1 = [
            [sg.Text('ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='l')],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Δώστε την συνάρτηση f(x,y,z):',size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=triple_inputs4[0],size =(50, 1))],
            [sg.Text('Δώστε τo άκρο ρ1:', size =(17, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=triple_inputs4[1],size =(23, 1))],
            [sg.Text('Δώστε τo άκρο ρ2:', size =(17, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=triple_inputs4[2],size =(23, 1))],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Δώστε τo άκρο φ1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=triple_inputs4[3],size =(23, 1))],
            [sg.Text('Δώστε τo άκρο φ2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=triple_inputs4[4],size =(23, 1))],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Δώστε τo άκρο ζ1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=triple_inputs4[5],size =(23, 1))], 
            [sg.Text('Δώστε τo άκρο ζ2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=triple_inputs4[6],size =(23, 1))],    
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('ΥΠΟΛΟΓΙΣΜΟΣ', key =calculate[5] ,button_color=('black', '')),
            sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('ΚΑΘΑΡΙΣΜΟΣ', key =clear[5]  ,button_color=('black', '')),
              ],
            ]
    frame7 = [[sg.Column(frame7_col1, background_color='light blue'),sg.Image('integral2.png',size=(650,320))]]
    #end

    #ΒΑΘΜΩΤΗ ΕΠΙΚΑΜΠΥΛΙΑ
    frame8_col1 = [
            [sg.Text('ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='l')],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Δώστε την συνάρτηση f(x,y,z):',size =(35, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=line_inputs1[0],size =(32, 1))],
            [sg.Text('Δώστε την καμπύλη c(t) = [x(t), y(t), z(t)]:', size =(35, 1), font=('Helvetica', 13, 'bold'))],
            [sg.Text('x(t)=', size =(5, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=line_inputs1[1],size =(23, 1))],
            [sg.Text('y(t)=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=line_inputs1[2],size =(23, 1))],
            [sg.Text('z(t)=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=line_inputs1[3],size =(23, 1))],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Δώστε τα άκροα t1 και t2:',size =(35, 1), font=('Helvetica', 13, 'bold'))], 
            [sg.Text('t1=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=line_inputs1[4],size =(23, 1))], 
            [sg.Text('t2=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=line_inputs1[5],size =(23, 1))],    
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('ΥΠΟΛΟΓΙΣΜΟΣ', key =calculate[6] ,button_color=('black', '')),
            sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('ΚΑΘΑΡΙΣΜΟΣ', key =clear[6]  ,button_color=('black', '')),
              ],
            ]
    frame8 = [[sg.Column(frame8_col1, background_color='light blue'),sg.Image('integral2.png',size=(650,320))]]
    #end     

    #ΔΙΑΝΥΣΜΑΤΙΚΗ ΕΠΙΚΑΜΠΥΛΙΑ
    frame9_col1 = [
            [sg.Text('ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='l')],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Δώστε την συνάρτηση F(x,y,z)= [F1, F2, F3]:',size =(36, 1), font=('Helvetica', 13, 'bold'))], 
            [sg.Text('F1(x,y,z)=', size =(8, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=line_inputs2[0],size =(23, 1))],
            [sg.Text('F2(x,y,z)=',size =(8, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=line_inputs2[1],size =(23, 1))],
            [sg.Text('F3(x,y,z)=',size =(8, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=line_inputs2[2],size =(23, 1))],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            [sg.Text('Δώστε την καμπύλη c(t) = [x(t), y(t), z(t)]:', size =(36, 1), font=('Helvetica', 13, 'bold'))],
            [sg.Text('x(t)=', size =(5, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=line_inputs2[3],size =(23, 1))],
            [sg.Text('y(t)=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=line_inputs2[4],size =(23, 1))],
            [sg.Text('z(t)=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=line_inputs2[5],size =(23, 1))],
            [sg.Text('_'*100,size=(44, 1),background_color='light blue')],
            
            ]
    frame9_col2_col1 = [
         [sg.Text('',size=(15, 1),background_color='light steel blue')],
         [sg.Text('',size=(1, 1),background_color='light steel blue'),sg.Button('ΥΠΟΛΟΓΙΣΜΟΣ',size=(13, 1),key = calculate[7],button_color=('black', ''))],
         [sg.Text('',size=(1, 1),background_color='light steel blue'),sg.Button('ΚΑΘΑΡΙΣΜΟΣ',size=(13, 1),key = clear[7] ,button_color=('black', ''))],
         [sg.Text('',size=(1, 1),background_color='light steel blue'),sg.Button('Θεώρημα Green ',size=(13, 1),key = 'green' ,button_color=('black', ''))]

        ] 
    frame9_col2_col2 = [
        [sg.Text('Δώστε τα άκρα t1 και t2:',size =(25, 1), font=('Helvetica', 13, 'bold'))], 
        [sg.Text('t1=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=line_inputs2[6],size =(23, 1))], 
        [sg.Text('t2=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=line_inputs2[7],size =(23, 1))],    
        [sg.Text('_'*100,size=(55, 1),background_color='light blue')],
        [sg.Text('Δεύτερος τρόπος εισαγωγής:',size =(35, 1),background_color='light coral', font=('Helvetica', 15, 'bold'))], 
        ]
    frame9_col2_col3 = [
        [sg.Text('Εάν έχετε έναν κύκλο με κέντρο K(x0,y0,z0): (x-x0)^2 + (y-y0)^2 = r^2',size=(70, 1),background_color='light steel blue')],
        [sg.Text('Τότε: c(t)=[r*cos(t)+x0 , r*sin(t)+y0 , z0] with t in [0,2π].',size=(70, 1),background_color='light steel blue')],
        [sg.Text('Εάν έχετε μια έλλειψη με κέντρο K(x0,y0,z0): (x-x0/a)^2 + (y-y0/b)^2 = 1',size=(70, 1),background_color='light steel blue')],
        [sg.Text('Τότε: c(t) = [a*cos(t) , b*sin(t), z0] with t in [0,2π].',size=(70, 1),background_color='light steel blue')],
        [sg.Text("Χρησιμοποιήστε το Θεώρημα του Green για οποιαδήποτε άλλη καμπύλη που δεν μπορεί να εισαχθεί με παραπάνω 2 τρόπους.",size=(70, 1),background_color='light steel blue')],
        ]
    frame9_col2_col4 = [
        [sg.Text('Δώστε τα σημεία μιας ευθείας AB:',size =(60, 1), font=('Helvetica', 13, 'bold'))], 
        [sg.Text('xa=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=line_inputs2[8],size =(23, 1)),
        sg.Text('',size=(12, 1),background_color='light blue'), sg.Text('xb=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=line_inputs2[9],size =(23, 1))], 
        [sg.Text('ya=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=line_inputs2[10],size =(23, 1)),
        sg.Text('',size=(12, 1),background_color='light blue'),  sg.Text('yb=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=line_inputs2[11],size =(23, 1))], 
        [sg.Text('za=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=line_inputs2[12],size =(23, 1)),
         sg.Text('',size=(12, 1),background_color='light blue'), sg.Text('zb=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=line_inputs2[13],size =(23, 1))], 
        ]
    frame9_col2 = [
        [sg.Column(frame9_col2_col2, size=(400,145), background_color='light blue'),sg.Frame('',layout=frame9_col2_col1, size=(220,145), background_color='light steel blue')],
        [sg.Column(frame9_col2_col4, size=(620,115), background_color='light blue')],
        [sg.Column(frame9_col2_col3, size=(620,150), background_color='light steel blue')]
        ]

    frame9 = [[sg.Column(frame9_col1, background_color='light blue'),sg.Column(frame9_col2, background_color='light blue')]]
    #end  


    #ΒΑΘΜΩΤΗ ΕΠΙΦΑΝΕΙΑΚA      
    frame10_col1 = [
            [sg.Text('ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='center')],
            [sg.Text('_'*100,size=(54, 1),background_color='light blue')],
            [sg.Text('Δώστε την συνάρτηση f(x,y,z):',size =(40, 1), font=('Helvetica', 13, 'bold'))], [sg.InputText(key=surface_inputs1[0],size =(35, 1))],
            [sg.Text('Δώστε την επιφάνεια s(u,v)=[x(u,v), y(u,v), z(u,v)]:', size =(40, 1), font=('Helvetica', 13, 'bold'))],
            [sg.Text('x(u,v)=', size =(7, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=surface_inputs1[1],size =(23, 1))],
            [sg.Text('y(u,v)=',size =(7, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs1[2],size =(23, 1))],
            [sg.Text('z(u,v)=',size =(7, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs1[3],size =(23, 1))],
            [sg.Text('_'*100,size=(54, 1),background_color='light blue')],
            [sg.Text('Δώστε τo άκρο u1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs1[4],size =(23, 1))], 
            [sg.Text('Δώστε τo άκρο u2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs1[5],size =(23, 1))],    
            [sg.Text('Δώστε τo άκρο v1:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs1[6],size =(23, 1))], 
            [sg.Text('Δώστε τo άκρο v2:',size =(17, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs1[7],size =(23, 1))],    
            [sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('ΥΠΟΛΟΓΙΣΜΟΣ',size=(13, 1),key = calculate[8],button_color=('black', '')),
             sg.Text('',size=(3, 1),background_color='light blue'),sg.Button('ΚΑΘΑΡΙΣΜΟΣ',size=(13, 1),key = clear[8] ,button_color=('black', ''))],
            ]

    frame10 = [[sg.Column(frame10_col1, background_color='light blue'),sg.Image('integral2.png',size=(650,320))]]
    #end

    #ΔΙΑΝΥΣΜΑΤΙΚΗ ΕΠΙΦΑΝΕΙΑΚA  
    frame11_col1 =[
        [sg.Text('ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ', size =(35, 1), font=('Helvetica', 15, 'bold'),background_color='light blue',justification='center')],
        [sg.Text('_'*100,size=(54, 1),background_color='light blue')],
        [sg.Text('Δώστε την συνάρτηση F(x,y,z)= [F1, F2, F3]:',size =(40, 1), font=('Helvetica', 13, 'bold'))], 
        [sg.Text('F1(x,y,z)=', size =(9, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=surface_inputs2[0],size =(23, 1))],
        [sg.Text('F2(x,y,z)=',size =(9, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs2[1],size =(23, 1))],
        [sg.Text('F3(x,y,z)=',size =(9, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs2[2],size =(23, 1))],
        
        [sg.Text('Δώστε την επιφάνεια s(u,v)=[x(u,v), y(u,v), z(u,v)]:', size =(40, 1), font=('Helvetica', 13, 'bold'))],
        [sg.Text('x(u,v)=', size =(9, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=surface_inputs2[3],size =(23, 1))],
        [sg.Text('y(u,v)=',size =(9, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs2[4],size =(23, 1))],
        [sg.Text('z(u,v)=',size =(9, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs2[5],size =(23, 1))],
        [sg.Text('_'*100,size=(54, 1),background_color='light blue')],
        [sg.Text('Προσανατολισμός της επιφάνειας:', size =(40, 1), font=('Helvetica', 13, 'bold'))],
        [sg.Button('Θετικός',size=(13, 1),key = 'positive',button_color=('black', '')),sg.Button('Αρνητικός',size=(13, 1),key = 'negative',button_color=('black', ''))]
        
        ]   
    frame11_col2_col1 = [
         [sg.Text('',size=(15, 1),background_color='light steel blue')],
         [sg.Text('',size=(1, 1),background_color='light steel blue'),sg.Button('ΥΠΟΛΟΓΙΣΜΟΣ',size=(13, 1),key = calculate[9],button_color=('black', ''))],
         [sg.Text('',size=(15, 1),background_color='light steel blue')],

         [sg.Text('',size=(1, 1),background_color='light steel blue'),sg.Button('ΚΑΘΑΡΙΣΜΟΣ',size=(13, 1),key = clear[9] ,button_color=('black', ''))]

        ] 
    frame11_col2_col2 = [
        [sg.Text('Δώστε τα άκρα u1 και u2:',size =(23, 1), font=('Helvetica', 13, 'bold'))],
        [sg.Text('u1=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs2[6],size =(23, 1))], 
        [sg.Text('u2=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs2[7],size =(23, 1))],    
        [sg.Text('Δώστε τα άκρα v1 και v2:',size =(23, 1), font=('Helvetica', 13, 'bold'))], 
        [sg.Text('v1=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs2[8],size =(23, 1))], 
        [sg.Text('v2=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs2[9],size =(23, 1))],    
        
        ]
    frame11_col2 = [
         [sg.Column(frame11_col2_col2, size=(400,180), background_color='light blue'),sg.Frame('',layout=frame11_col2_col1, size=(220,180), background_color='light steel blue')
    
         ], 
        [sg.Text('Δεύτερος τρόπος εισαγωγής:',size =(60, 1),background_color='light coral', font=('Helvetica', 15, 'bold'))], 
        [sg.Text('Δώστε την συνάρτηση s(x,y,z)=0,  η οποία περιγράφει την επιφάνεια:',size =(60, 1), font=('Helvetica', 13, 'bold'))], 
        [sg.Text('s(x,y,z)= 0 =', size =(7, 1), font=('Helvetica', 13, 'bold')),sg.InputText(key=surface_inputs2[10],size =(23, 1))],
        [sg.Text('Δώστε τα άκρα για x,y,z:',size =(46, 1), font=('Helvetica', 13, 'bold'))], 
        [sg.Text('x1=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs2[11],size =(23, 1)),
         sg.Text('x2=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs2[12],size =(23, 1))], 
        [sg.Text('y1=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs2[13],size =(23, 1)),
         sg.Text('y2=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs2[14],size =(23, 1))], 
        [sg.Text('z1=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs2[15],size =(23, 1)),
         sg.Text('z2=',size =(5, 1), font=('Helvetica', 13, 'bold')), sg.InputText(key=surface_inputs2[16],size =(23, 1))], 

        ]
    frame11 = [
            [sg.Column(frame11_col1, background_color='light blue'),
                sg.Column(layout=frame11_col2,size=(625,420), background_color='light blue')]]

    #end
    
    #frame_gr_par = []

    frame = [
            [sg.Frame("", layout=frame1, size=(1070,420), visible=True,   key='Frame1', element_justification='center', background_color='light blue'),
            sg.Frame("", layout=frame2, size=(1070,420), visible=False,   key='Frame2' , element_justification='left' ,background_color='light blue'),
            sg.Frame("", layout=frame3,  size=(1070,420),visible=False,   key='Frame3' , element_justification='left' , background_color='light blue'),
            sg.Frame("", layout=frame4,  size=(1070,420),visible=False,   key='Frame4' , element_justification='left' , background_color='light blue'),
            sg.Frame("", layout=frame5,  size=(1070,420),visible=False,   key='Frame5' , element_justification='left' , background_color='light blue'),
            sg.Frame("", layout=frame6,  size=(1070,420),visible=False,   key='Frame6' , element_justification='left' , background_color='light blue'),
            sg.Frame("", layout=frame7,  size=(1070,420),visible=False,   key='Frame7' , element_justification='left' , background_color='light blue'),
            sg.Frame("", layout=frame8,  size=(1070,420),visible=False,   key='Frame8' , element_justification='left' , background_color='light blue'),
            sg.Frame("", layout=frame9,  size=(1070,420),visible=False,   key='Frame9' , element_justification='left' , background_color='light blue'),
            sg.Frame("", layout=frame10,  size=(1070,425),visible=False,   key='Frame10' , element_justification='left' , background_color='light blue'),
            sg.Frame("", layout=frame11,  size=(1070,425),visible=False,   key='Frame11' , element_justification='left' , background_color='light blue'),
            ]
            ]
       
        
    # ------ GUI Defintion ------ #
    layout = [ [sg.Menu(menu1_def)],
              [sg.Frame("", layout=title_frame, size=(1070,80), element_justification='center', background_color='light blue')],
              [sg.Column( frame,  key='frame',element_justification='center')],
               #sg.Frame('', layout=output, size=(625,425), visible=False, key='output'  ,element_justification='right', background_color='light blue')],
              [sg.Frame("", layout=menu2_def, size=(1070,80),background_color='light blue'),]
              
              ]  



    form = sg.FlexForm("ΥΠΟΛΟΓΙΣΜΟΣ ΟΛΟΚΛΗΡΩΜΑΤΩΝ",size=(1100, 635), element_justification='center', auto_size_text=False, auto_size_buttons=False,
                           default_button_element_size=(12, 1))
    form.Layout(layout).Finalize()
     
    frame, frame1,frame2,frame3,frame4, frame5 , frame6, frame7, frame8, frame9, frame10, frame11= form['frame'], form['Frame1'], form['Frame2'],form['Frame3'], form['Frame4'], form['Frame5'], form['Frame6'], form['Frame7'], form['Frame8'], form['Frame9'], form['Frame10'], form['Frame11']

    form['text_frame'].update(text_frame[0])
    page=0
    orient=1
    language = 1
    counter1,counter2,counter=0,0,0
    key=keys[0]
    array_inputs = ['','','','','','','']
    while True:
        button, values = form.Read()
        
        if button is None or button == 'ΕΞΟΔΟΣ':
            break
        #print('Button = ', button)
       
        elif button == 'positive':
            orient = 1
        elif button == 'negative':
            orient = 2
        if button == 'ΑΓΓΛΙΚΑ':
            language = 0
            form.close()
            open_window()
        elif button == 'ΕΛΛΗΝΙΚΑ':
            language = 1
        #ΔΙΠΛΑ ΚΑΡΤΕΣΙΑΝΕΣ    
        if button == calculate[0] :
            counter=0
            pc=0
            key = keys[0]
            array_inputs=[values[double_inputs1[0]],values[double_inputs1[1]],values[double_inputs1[2]],values[double_inputs1[3]],values[double_inputs1[4]]]
            counter = check_inputs(array_inputs)
            for x in range(len(array_inputs)):
                array_inputs[x] = correction(array_inputs[x],language)
            if counter >= 1:
                sg.Popup('Δεν έχετε εισάγει όλα τα δεδομένα!\nΣυμπληρώστε όλα τα πεδία εισαγωγής για να γίνει ο υπολογισμός !',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                double_integral(array_inputs,pc,language)
        #ΔΙΠΛΑ ΠΟΛΙΚΕΣ        
        elif button == calculate[1] :
            counter=0
            pc=1
            key = keys[1]
            array_inputs=[values[double_inputs2[0]],values[double_inputs2[1]],values[double_inputs2[2]],values[double_inputs2[3]],values[double_inputs2[4]]]
            counter = check_inputs(array_inputs)
            for x in range(len(array_inputs)):
                array_inputs[x] = correction(array_inputs[x],language)

            if counter >= 1:
                sg.Popup('Δεν έχετε εισάγει όλα τα δεδομένα!\nΣυμπληρώστε όλα τα πεδία εισαγωγής για να γίνει ο υπολογισμός !',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                double_integral(array_inputs,pc,language)
        #ΤΡΙΠΛΑ ΚΑΡΤΕΣΙΑΝΕΣ
        elif button == calculate[2] :
            counter=0
            key = keys[2]
            array_inputs=[values[triple_inputs1[0]],values[triple_inputs1[1]],values[triple_inputs1[2]],values[triple_inputs1[3]],values[triple_inputs1[4]],values[triple_inputs1[5]],values[triple_inputs1[6]]]
            counter = check_inputs(array_inputs)
            for x in range(len(array_inputs)):
                array_inputs[x] = correction(array_inputs[x],language)

            if counter >= 1:
                sg.Popup('Δεν έχετε εισάγει όλα τα δεδομένα!\nΣυμπληρώστε όλα τα πεδία εισαγωγής για να γίνει ο υπολογισμός !',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                ti_cc_main_func(array_inputs,language)
                
        #ΤΡΙΠΛΑ ΣΦΑΙΡΙΚΕΣ
        elif button == calculate[3] :
            counter=0
            key = keys[3]
            array_inputs=[values[triple_inputs2[0]],values[triple_inputs2[1]],values[triple_inputs2[2]],values[triple_inputs2[3]],values[triple_inputs2[4]],values[triple_inputs2[5]],values[triple_inputs2[6]]]
            counter = check_inputs(array_inputs)
            for x in range(len(array_inputs)):
                array_inputs[x] = correction(array_inputs[x],language)

            if counter >= 1:
                sg.Popup('Δεν έχετε εισάγει όλα τα δεδομένα!\nΣυμπληρώστε όλα τα πεδία εισαγωγής για να γίνει ο υπολογισμός !',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                ti_sc_main_func(array_inputs,language)
        
        #ΤΡΙΠΛΑ ΕΛΛΕΙΠΤΙΚΕΣ
        elif button == calculate[4] :
            counter=0
            key = keys[4]
            array_inputs=[values[triple_inputs3[0]],values[triple_inputs3[1]],values[triple_inputs3[2]],values[triple_inputs3[3]],values[triple_inputs3[4]],values[triple_inputs3[5]],values[triple_inputs3[6]]]
            counter = check_inputs(array_inputs)
            for x in range(len(array_inputs)):
                array_inputs[x] = correction(array_inputs[x],language)

            if counter >= 1:
                sg.Popup('Δεν έχετε εισάγει όλα τα δεδομένα!\nΣυμπληρώστε όλα τα πεδία εισαγωγής για να γίνει ο υπολογισμός !',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                ti_ec_main_func(array_inputs,language)
        
        #ΤΡΙΠΛΑ ΚΥΛΙΝΔΡΙΚΕΣ
        elif button == calculate[5] :
            counter=0
            pc=4
            key = keys[5]
            array_inputs=[values[triple_inputs4[0]],values[triple_inputs4[1]],values[triple_inputs4[2]],values[triple_inputs4[3]],values[triple_inputs4[4]],values[triple_inputs4[5]],values[triple_inputs4[6]]]
            counter = check_inputs(array_inputs)
            for x in range(len(array_inputs)):
                array_inputs[x] = correction(array_inputs[x],language)

            if counter >= 1:
                sg.Popup('Δεν έχετε εισάγει όλα τα δεδομένα!\nΣυμπληρώστε όλα τα πεδία εισαγωγής για να γίνει ο υπολογισμός !',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                ti_cyc_main_func(array_inputs,language)
        
                
        #ΕΠΙΚΑΜΠΥΛΙΑ ΒΑΘΜΩΤΗ
        elif button == calculate[6]:
            counter=0
            key = keys[6]
            array_inputs=[values[line_inputs1[0]],values[line_inputs1[1]],values[line_inputs1[2]],values[line_inputs1[3]],values[line_inputs1[4]],values[line_inputs1[5]]]
            counter = check_inputs(array_inputs)
            for x in range(len(array_inputs)):
                array_inputs[x] = correction(array_inputs[x],language)

            if counter >= 1:
                sg.Popup('Δεν έχετε εισάγει όλα τα δεδομένα!\nΣυμπληρώστε όλα τα πεδία εισαγωγής για να γίνει ο υπολογισμός !',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                curve_integral(array_inputs,language)
        
        #ΕΠΙΚΑΜΠΥΛΙΑ ΔΙΑΝΥΣΜΑΤΙΚΗ 
        elif button == calculate[7]:
            counter=0
            key = keys[7]
            array_inputs=[values[line_inputs2[0]],values[line_inputs2[1]],values[line_inputs2[2]],values[line_inputs2[3]],values[line_inputs2[4]],values[line_inputs2[5]],values[line_inputs2[6]],values[line_inputs2[7]],values[line_inputs2[8]],values[line_inputs2[9]],values[line_inputs2[10]],values[line_inputs2[11]],values[line_inputs2[12]],values[line_inputs2[13]]]
            if array_inputs[8] == "" and array_inputs[9] == "" and array_inputs[10] == "":
                counter=0
                i=0
                array1=['','','','','','','','']
                array2=['','','','','','']
                while i<8:
                    array1[i]=array_inputs[i]
                    i=i+1
                counter = check_inputs(array1)
                for x in range(len(array1)):
                    array_inputs[x] = correction(array1[x],language)

            elif array_inputs[8] != "" and array_inputs[9] != "" and array_inputs[10] != "":
                counter1,counter2,counter=0,0,0
                i=0
                array1=['','','']
                array2=['','','','','','']
                while i<3:
                    array1[i]=array_inputs[i]
                    i=i+1
                
                counter1 = check_inputs(array1)
                for x in range(len(array1)):
                    array_inputs[x] = correction(array1[x],language)
                i=8
                j=0
                while i<14:
                    array2[j]=array_inputs[i]
                    j=j+1
                    i=i+1
                counter2 = check_inputs(array2)
                for x in range(len(array2)):
                    array_inputs[x] = correction(array2[x],language)

                counter = counter1 + counter2
            if counter >= 1:
                sg.Popup('Δεν έχετε εισάγει όλα τα δεδομένα!\nΣυμπληρώστε όλα τα πεδία εισαγωγής για να γίνει ο υπολογισμός !',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                curve_integral_vf(array1,array2,language)
                
        #ΒΑΘΜΩΤΗ ΕΠΙΦΑΝΕΙΑΚA          
        elif button == calculate[8]:
            counter=0
            key = keys[8]
            array_inputs=[values[surface_inputs1[0]],values[surface_inputs1[1]],values[surface_inputs1[2]],values[surface_inputs1[3]],values[surface_inputs1[4]],values[surface_inputs1[5]],values[surface_inputs1[6]],values[surface_inputs1[7]]]
            counter = check_inputs(array_inputs)
            for x in range(len(array_inputs)):
                array_inputs[x] = correction(array_inputs[x],language)
            

            if counter >= 1:
                sg.Popup('Δεν έχετε εισάγει όλα τα δεδομένα!\nΣυμπληρώστε όλα τα πεδία εισαγωγής για να γίνει ο υπολογισμός !',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            elif counter == 0:
                surface_integral(array_inputs,language)
        
        #ΔΙΑΝΥΣΜΑΤΙΚΗ ΕΠΙΦΑΝΕΙΑΚA          
        elif button == calculate[9]:
            key = keys[9]
            array_inputs=[values[surface_inputs2[0]],values[surface_inputs2[1]],values[surface_inputs2[2]],values[surface_inputs2[3]],values[surface_inputs2[4]],values[surface_inputs2[5]],values[surface_inputs2[6]],values[surface_inputs2[7]],values[surface_inputs2[8]],values[surface_inputs2[9]],values[surface_inputs2[10]],values[surface_inputs2[11]],values[surface_inputs2[12]],values[surface_inputs2[13]],values[surface_inputs2[14]],values[surface_inputs2[15]],values[surface_inputs2[16]]]
            if array_inputs[10] == "":
                counter=0
                i=0
                array1=['','','','','','','','','','']
                array2=['','','','','','','']
                while i<10:
                    array1[i]=array_inputs[i]
                    i=i+1
                counter = check_inputs(array1)
                for x in range(len(array1)):
                    array_inputs[x] = correction(array1[x],language)

            elif array_inputs[10] != "":
                counter1,counter2,counter=0,0,0
                i=0
                array1=['','','']
                array2=['','','','','','','',]
                while i<3:
                    array1[i]=array_inputs[i]
                    i=i+1
                
                counter1 = check_inputs(array1)
                for x in range(len(array1)):
                    array_inputs[x] = correction(array1[x],language)

                i=10
                j=0
                while i<17:
                    array2[j]=array_inputs[i]
                    j=j+1
                    i=i+1
                counter2 = check_inputs(array2)
                for x in range(len(array2)):
                    array_inputs[x] = correction(array2[x],language)

                counter = counter1 + counter2
            if (orient < 1 and orient>2):
                  sg.Popup('Δεν έχετε εισάγει όλα τα δεδομένα!\n\nΔιαλέξτε προσανατολισμό επιφάνειας για να γίνει ο υπολογισμός !',title='ΕΙΔΟΠΟΙΗΣΗ !!!') 
            if counter >= 1:
                sg.Popup('Δεν έχετε εισάγει όλα τα δεδομένα!\nΣυμπληρώστε όλα τα πεδία εισαγωγής για να γίνει ο υπολογισμός !',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
            
            elif counter == 0:
                surface_integral_vf(array1,array2,orient,language)
        
        for x in clear:
            if button == x:
                array_out = array_inputs
                i=0
                for x in array_inputs:
                    x =''
                    array_out[i] = x
                    i=i+1
                for x in key:
                    form[x]('')
                
            
        
        #ΣΥΝΑΡΤΗΣΗ ΓΙΑ ΜΕΝΟΥ ΒΟΗΘΕΙΑΣ
        for x in help_int:
                if button == x:
                   help_DEF(help_info[x])
                   # sg.Popup(help_info[x])
                    
                
        #end
               
        if button == 'ΕΠΟΜΕΝΟ':
                for x in menu_kindf:
                    if x == values['menu_kindf']:
                        temp2 = x
                #end
 
                for x in menu_kind_int:
                    if x == values['menu_kind_int']:
                            #sg.Popup(x)
                            temp3 = x
                #end

                for x in menu_kind_coordinate:
                    if x == values['menu_kind_coordinate']:
                        temp4 = x
                        #sg.Popup(x)
                        
                #end
                #ΒΑΘΜΩΤΗ ΔΙΠΛΑ ΚΑΡΤΕΣΙΑΝΕΣ
                if language == 1 and temp2==menu_kindf[0] and temp3==menu_kind_int[0] and temp4==menu_kind_coordinate[0]:
                     page=1
                     key=keys[0]
                     form['text_frame'].update(text_frame[1])
                     form['Frame1'].update(visible=False)
                     form['Frame3'].update(visible= False)
                     form['Frame4'].update(visible= False)
                     form['Frame5'].update(visible= False)
                     form['Frame6'].update(visible= False)
                     form['Frame7'].update(visible= False)
                     form['Frame8'].update(visible= False)
                     form['Frame9'].update(visible= False)
                     form['Frame10'].update(visible= False)
                     form['Frame11'].update(visible= False)
                     form['Frame2'].update(visible=True)
                     
                     #output.update(visible=True)     
                #end
                
                #ΒΑΘΜΩΤΗ ΔΙΠΛΑ ΠΟΛΙΚΕΣ
                elif language == 1 and temp2==menu_kindf[0] and temp3 == menu_kind_int[0] and temp4 == menu_kind_coordinate[1]:
                     page=2
                     key=keys[1]
                     form['text_frame'].update(text_frame[2])
                     form['Frame1'].update(visible=False)
                     form['Frame2'].update(visible= False)
                     form['Frame4'].update(visible= False)
                     form['Frame5'].update(visible= False)
                     form['Frame6'].update(visible= False)
                     form['Frame7'].update(visible= False)
                     form['Frame8'].update(visible= False)
                     form['Frame9'].update(visible= False)
                     form['Frame10'].update(visible= False)
                     form['Frame11'].update(visible= False)
                     form['Frame3'].update(visible=True)
                     
                     #output.update(visible=True)
                #end
                
                #ΒΑΘΜΩΤΗ ΤΡΙΠΛΑ ΚΑΡΤΕΣΙΑΝΕΣ
                elif language == 1 and temp2==menu_kindf[0] and temp3 == menu_kind_int[1] and temp4 == menu_kind_coordinate[0]:
                     page=3
                     key=keys[2]
                     form['text_frame'].update(text_frame[3])
                     form['Frame1'].update(visible=False)
                     form['Frame2'].update(visible= False)
                     form['Frame3'].update(visible= False)
                     form['Frame5'].update(visible= False)
                     form['Frame6'].update(visible= False)
                     form['Frame7'].update(visible= False)
                     form['Frame8'].update(visible= False)
                     form['Frame9'].update(visible= False)
                     form['Frame10'].update(visible= False)
                     form['Frame11'].update(visible= False)
                     form['Frame4'].update(visible=True)
                     
                    # output.update(visible=True)
                     #end
                #ΒΑΘΜΩΤΗ ΤΡΙΠΛΑ ΣΦΑΙΡΙΚΕΣ
                elif language == 1 and temp2==menu_kindf[0] and temp3 == menu_kind_int[1] and temp4 == menu_kind_coordinate[2]:
                     page=4
                     form['text_frame'].update(text_frame[4])
                     form['Frame1'].update(visible=False)
                     form['Frame2'].update(visible= False)
                     form['Frame3'].update(visible= False)
                     form['Frame4'].update(visible= False)
                     form['Frame6'].update(visible= False)
                     form['Frame7'].update(visible= False)
                     form['Frame8'].update(visible= False)
                     form['Frame9'].update(visible= False)
                     form['Frame10'].update(visible= False)
                     form['Frame11'].update(visible= False)
                     
                     form['Frame5'].update(visible=True)
                     
                    #output.update(visible=True)
                    #end
                #ΒΑΘΜΩΤΗ ΤΡΙΠΛΑ ΕΛΛΕΙΠΤΙΚΕΣ
                elif language == 1 and temp2==menu_kindf[0] and temp3 == menu_kind_int[1] and temp4 == menu_kind_coordinate[3]:
                     page=5
                     form['text_frame'].update(text_frame[5])
                     form['Frame1'].update(visible=False)
                     form['Frame2'].update(visible= False)
                     form['Frame3'].update(visible= False)
                     form['Frame4'].update(visible= False)
                     form['Frame5'].update(visible= False)
                     form['Frame7'].update(visible= False)
                     form['Frame8'].update(visible= False)
                     form['Frame9'].update(visible= False)
                     form['Frame10'].update(visible= False)
                     form['Frame11'].update(visible= False)
                     
                     form['Frame6'].update(visible=True)
                     
                     #output.update(visible=True)
                     #end
                     
                #ΒΑΘΜΩΤΗ ΤΡΙΠΛΑ ΚΥΛΙΝΔΡΙΚΕΣ
                elif language == 1 and temp2==menu_kindf[0] and temp3 == menu_kind_int[1] and temp4 == menu_kind_coordinate[4]:
                     page=6
                     form['text_frame'].update(text_frame[6])
                     form['Frame1'].update(visible=False)
                     form['Frame2'].update(visible= False)
                     form['Frame3'].update(visible= False)
                     form['Frame4'].update(visible= False)
                     form['Frame5'].update(visible= False)
                     form['Frame6'].update(visible= False)
                     form['Frame8'].update(visible= False)
                     form['Frame9'].update(visible= False)
                     form['Frame10'].update(visible= False)
                     form['Frame11'].update(visible= False)
                     
                     form['Frame7'].update(visible=True)
                     
                     #output.update(visible=True)
                     #end
                #ΒΑΘΜΩΤΗ ΕΠΙΚΑΜΠΥΛΙΑ
                elif language == 1 and temp2==menu_kindf[0] and temp3 == menu_kind_int[2]:
                     page=7
                     key=keys[3]
                     form['text_frame'].update(text_frame[7])
                     form['Frame1'].update(visible=False)
                     form['Frame2'].update(visible= False)
                     form['Frame3'].update(visible= False)
                     form['Frame4'].update(visible= False)
                     form['Frame5'].update(visible= False)
                     form['Frame6'].update(visible= False)
                     form['Frame7'].update(visible= False)
                     form['Frame9'].update(visible= False)
                     form['Frame10'].update(visible= False)
                     form['Frame11'].update(visible= False)
                     
                     form['Frame8'].update(visible=True)
                     
                     #output.update(visible=True)
                     #end
                #ΔΙΑΝΥΣΜΑΤΙΚΗ ΕΠΙΚΑΜΠΥΛΙΑ
                elif language == 1 and temp2==menu_kindf[1] and temp3 == menu_kind_int[2]:
                     page=8
                     key=keys[3]
                     form['text_frame'].update(text_frame[7])
                     form['Frame1'].update(visible=False)
                     form['Frame2'].update(visible= False)
                     form['Frame3'].update(visible= False)
                     form['Frame4'].update(visible= False)
                     form['Frame5'].update(visible= False)
                     form['Frame6'].update(visible= False)
                     form['Frame7'].update(visible= False)
                     form['Frame8'].update(visible= False)
                     form['Frame10'].update(visible= False)
                     form['Frame11'].update(visible= False)
                     
                     form['Frame9'].update(visible=True)
                     
                     #output.update(visible=True)
                     #end
                #ΒΑΘΜΩΤΗ ΕΠΙΦΑΝΕΙΑΚA      
                elif language == 1 and temp2==menu_kindf[0] and temp3 == menu_kind_int[3]:
                    page=10
                    key=keys[4]
                    form['text_frame'].update(text_frame[9])
                    form['Frame1'].update(visible=False)
                    form['Frame2'].update(visible= False)
                    form['Frame3'].update(visible= False)
                    form['Frame4'].update(visible= False)
                    form['Frame5'].update(visible= False)
                    form['Frame6'].update(visible= False)
                    form['Frame7'].update(visible= False)
                    form['Frame8'].update(visible= False)
                    form['Frame9'].update(visible= False)
                    form['Frame11'].update(visible= False)
                    
                    form['Frame10'].update(visible=True)
                    
                    #output.update(visible=True)
                #end
                #ΔΙΑΝΥΣΜΑΤΙΚΗ ΕΠΙΦΑΝΕΙΑΚA      
                elif language == 1 and temp2==menu_kindf[1] and temp3 == menu_kind_int[3]:
                    page=11
                    key=keys[3]
                    form['text_frame'].update(text_frame[10])
                    form['Frame1'].update(visible=False)
                    form['Frame2'].update(visible= False)
                    form['Frame3'].update(visible= False)
                    form['Frame4'].update(visible= False)
                    form['Frame5'].update(visible= False)
                    form['Frame6'].update(visible= False)
                    form['Frame7'].update(visible= False)
                    form['Frame8'].update(visible= False)
                    form['Frame9'].update(visible= False)
                    form['Frame10'].update(visible= False)
                    form['Frame11'].update(visible=True)
                    
                   # output.update(visible=True)
                #end
        elif button == 'ΠΡΟΗΓΟΥΜΕΝΟ':
            if page==0:
                print('')
            elif page!=0:
                counter=0
                for x in array_inputs:
                    counter
                    if x == '':
                        counter=counter+1
                
                if counter >=1:
                    print('kl')
                    form['text_frame'].update(text_frame[0])
                    form['Frame2'].update(visible= False)
                    form['Frame3'].update(visible=False)
                    form['Frame4'].update(visible= False)
                    form['Frame5'].update(visible= False)
                    form['Frame6'].update(visible= False)
                    form['Frame7'].update(visible= False)
                    form['Frame8'].update(visible= False)
                    form['Frame9'].update(visible= False)
                    form['Frame10'].update(visible= False)
                    form['Frame11'].update(visible= False)
                    form['Frame1'].update(visible=True)
                    
                    continue
                elif counter == 0:
                    click = sg.popup_ok_cancel('Τα δεδομένα σας θα χαθούν θέλετε να συνεχίσετε;',title='ΕΙΔΟΠΟΙΗΣΗ !!!')
                    if click == 'OK':
                        #ΚΑΘΑΡΙΣΜΟΣ inputs
                        array_out = array_inputs
                        i=0
                        for x in array_inputs:
                            x =''
                            array_out[i] = x
                            i=i+1
                        for x in key:
                            form[x]('')
                        
                        #end
                        page=0
                        form['text_frame'].update(text_frame[0])
                      #  form['-OUT-'].update(value='')
                       # output.update(visible=False)
                        form['Frame2'].update(visible= False)
                        form['Frame3'].update(visible=False)
                        form['Frame4'].update(visible= False)
                        form['Frame5'].update(visible= False)
                        form['Frame6'].update(visible= False)
                        form['Frame7'].update(visible= False)
                        form['Frame8'].update(visible= False)
                        form['Frame9'].update(visible= False)
                        form['Frame10'].update(visible= False)
                        form['Frame11'].update(visible= False)
                        form['Frame1'].update(visible=True)
                    elif click == 'Cancel':
                        print('')
                
                        
    
    
        
    form.close()
def main():    
    if language == 1:
        first_window()
    elif language == 0:
        open_window()
        

if __name__ == "__main__":
    main()