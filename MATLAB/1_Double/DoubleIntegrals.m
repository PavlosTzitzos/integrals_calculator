function [I] = DoubleIntegrals(f,x1,x2,y1,y2,pc)
% 
% f = f(x,y)
% x1 <= x <= x2
% y1 <= y <= y2
% pc = 1, for polar coordinates
% pc = 0, for cartesian -//-
% 
% I = Inetgral result
% 
syms x y r theta

while(isa(f,'double') == 0 && isa(f,'float') == 0 && isa(f,'sym') == 0)
    %Check if f is symbolic
    %Not symbolic
    f=str2sym(input("Give function f again: ",'s'));
    if (f=="exit")
        break;
    end
end

if(x1>x2)
    fprintf("\nWarning! x1 > x2\n\n");
    check = input("Do you want to invert them?\nType y for yes, n for no: ",'s');
    if(check=='y')
        temp = x1;
        x1 = x2;
        x2 = temp;
    end
end

if(y1>y2)
    fprintf("\nWarning! y1 > y2\n\n");
    check = input("Do you want to invert them?\nType y for yes, n for no: ",'s');
    if(check=='y')
        temp = y1;
        y1 = y2;
        y2 = temp;
    end
end

%Input Arguments:
% function f(x,y)
% x1 <= x <= x2 , y1 <= y <= y2
fprintf("Calculating Double Integral ... \n")
if (isnumeric(x1)==1 && isnumeric(x2)==1 && isnumeric(y1)==1 && isnumeric(y2)==1)
    %1.
    %Simple x and y
    fprintf("D is Simple x and y.\n");
    I = int(int(f,x,x1,x2),y,y1,y2);
    %I = integral(integral(f,y1,y2),x1,x2);
    %display result...
elseif((isnumeric(x1)==0 || isnumeric(x2)==0) && isnumeric(y1)==1 && isnumeric(y2)==1)
    %2.
    %Simple x
    fprintf("D is Simple x.\n");
    %display result...
    I = int(int(f,x1,x2),y1,y2);
else
    %3.
    %Simple y
    fprintf("D is Simple y.\n");
    %display result...
    I = int(int(f,y,y1,y2),x,x1,x2);
end

%.....what happens when we want polar coordinates ????.... (3)
if (pc==1)
    fprintf("");
    fprintf("Change of variables, using polar coordinates.\n");
    fprintf("Replace x with r*cos(theta) and y with r*sin(theta):");
    fp = subs(f,[x y], [r*cos(theta)+0 r*sin(theta)+0]);
    disp(fp);
    fprintf("Integrate with r variable first and theta second.");
    I = int(int(fp*r,r1,r2),theta1,theta2);
end
%......polar coordinates......

end