clc; clear;
syms x y r
%Volume
M = x;
P = 2*sqrt(9-x^2);
A = M*P;
a = 0;
b = 3;
V = int(A,x,a,b);
fprintf("\nVolume is %d m^3\n",V);

%Rotation with disks
R = sqrt(x)-1;
ang = pi;
A = ang*R^2;
a = 1;
b = 4;
V = int(A,x,a,b);
fprintf("\nVolume is ");
display(V)
fprintf("m^3\n");

%Rotation with rings
R1 = x^2+1;% Inner radius
R2 = -x+3;%Outer radius
ang = pi;
A = ang*(R2^2-R1^2);
a = -2;
b = 1;
V = int(A,x,a,b);
fprintf("\nVolume is ");
display(V)
fprintf("m^3\n");

%Rotation with floios
R = x; %Radius
H = sqrt(x); %High
ang = 2*pi;
A = ang*R*H;
a = 0;
b = 4;
V = int(A,x,a,b);
fprintf("\nVolume is ");
display(V)
fprintf("m^3\n");

%Surface of rotation at x
f = 2*sqrt(x);
ang = 2*pi;
A = ang*f*sqrt(1+diff(f,x)^2);
a = 1;
b = 2;
S = int(A,x,a,b);
vv = vpa(S);
display(S)
fprintf("\nSurface is %d m^2\n",vv);

%Surface of rotation at y
f = 1-y;
ang = 2*pi;
A = ang*f*sqrt(1+diff(f,y)^2);
a = 0;
b = 1;
S = int(A,y,a,b);
vv = vpa(S);
display(S)
fprintf("\nSurface is %d m^2\n",vv);
