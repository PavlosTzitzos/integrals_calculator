% Double Integral for a simple y space D
% D ={(x,y): a <= x <= b and g1(x) <= y <= g2(x)}
syms x y
f = 2 * x^2 * y^4;
%Lines: y = 1 + x^2 , y = x , x = 1 and x = 0.
y1 = x;
y2 = 1 + x^2;
% y1 <= y <= y2
I1 = int(f, y , y1 , y2);
x1 = 0;
x2 = 1;
% x1 <= x <= x2
I2 = int(I1, x , x1 , x2);
display(I2)
%%
syms x y z
h = x^2 + 2 * y^2 * z;
z1 = x^2 + y^2;
z2 = 1;
% z1 <= z <= z2
I1 = int(h, z , z1 , z2);
y1 = -sqrt(1-x^2);
y2 = -y1;
% y1 <= y <= y2
I2 = int(I1, y , y1 , y2);
x1 = -1;
x2 = -x1;
% x1 <= x <= x2
I3 = int(I2, x , x1 , x2)
%%
% Double Integral for a simple x space D
% D ={(x,y): a <= y <= b and g1(y) <= x <= g2(y)}
syms x y
f = x^2 - y^3;
%Lines: x = y^2 , x = 8 - y^2.
x1 = y^2;
x2 = 8 - y^2;
%x1 <= x <= x2
I1 = int(f, x, x1, x2);
y1 = -2;
y2 = 2;
% y1 <= y <= y2
I2 = int(I1, y, y1, y2);
display(I2)
%%
% Double Integral for a simple x and a simple y space D
syms x y
f = cos(3*x^2);
%Lines: y = x , x = 1 , x = 0 , y = 0.
%Simple x space D:
% D ={(x,y): a <= y <= b and g1(y) <= x <= g2(y)}
y1 = 0;
y2 = 1;
% y1 <= y <= y2
I1 = int(f, y, y1, y2);
x1 = y;
x2 = 1;
% x1 <= x <= x2
I2 = int(I1, x, x1,x2)
display(I2)
%Simple y space D:
% D ={(x,y): a <= x <= b and g1(x) <= y <= g2(x)}
x1 = 0;
x2 = 1;
%x1 <= x <= x2
I3 = int(f, x, x1, x2);
y1 = 0;
y2 = x;
% y1 <= y <= y2
I4 = int(I3, y, y1, y2);
display(I4)
%%
% Double Integral in polar coordinates
%The given cartesian space Dc is:
%Dc = {(x,y): a <= x^2 + y^2 <= b and g1(x) <= y <= g2(x)}
%or
%Dc = {(x,y): a <= x^2 + y^2 <= b and g1(y) <= x <= g2(y)}
%The polar space Dp will be:
%Dp = {(r,theta): r1 <= r <= r2 and theta1 <= theta <= theta2}
syms r theta
x = r * cos(theta);
y = r * sin(theta);
f = exp(-2 * (x^2 + y^2));
%Dc = {(x,y): 1 <= x^2 + y^2 <= 4 and -x <= y <= x}
%r = sqrt(x^2 + y^2) which gives: sqrt(a) <= r <= sqrt(b)
r1 = 1;
r2 = 2;
% r1 <= r <= r2
I1 = int(f*r, r, r1, r2);
%theta = atan(y / x) which gives: atan(-1) <= theta <= atan(1)
theta1 = atan(-1);
theta2 = atan(1);
% theta1 <= theta <= theta2
I2 = int(I1, theta, theta1, theta2);
display(I2)
%%
syms r th
x = r * cos(theta);%(i)
y = r * sin(theta);%(ii)
f = x*y;
%Line: x^2 + y^2 = 2*x (iii)
%This is a circle:
%x^2 - 2*x + 1 + y^2 = 1 => (x-1)^2 + y^2 = 1
%Put (i) and (ii) in (iii):
%r = 2*cos(theta)
r1 = 0;
r2 = 2*cos(theta);
% r1 <= r <= r2
I1 = int(f*r, r, r1, r2);
%theta = atan(y / x) which gives: atan(-1) <= theta <= atan(1)
theta1 = atan(-1);
theta2 = atan(1);
% theta1 <= theta <= theta2
I2 = int(I1, theta, theta1, theta2);
%%
% Triple Integral simple for a z space D
% up from a surface z = z1(x,y) and down from a surface z = z2(x,y)
% A = {(x,y,z): z1(x,y) <= z <= z2(x,y) , (x,y) in D}
% D = {(x,y): a <= x <= b and y1(x) <= y <= y2(x)}
% In this example:  int_x( int_y( int_z( f )dz )dy )dx
syms x y z
f = x^2 + 2*y^2 * z;
%Paraboloid: z = x^2 + y^2 and the surface(Level) z = 1.
%This gives: x^2 + y^2 <= z <= 1
%Then the projection of the A on xy plane is a circle centered in O(0,0)
%and with radius R = 1.
%This gives: - sqrt(1 - x^2) <= y <= sqrt(1 - x^2)
%And this gives: -1 <= x <= 1
z1 = 1;
z2 = x^2 + y^2;
% z1 <= z <= z2
I1 = int(f, z, z1, z2);
y1 = - sqrt(1 - x^2);
y2 = sqrt(1 - x^2);
% y1 <= y <= y2
I2 = int(I1, y, y1, y2);
x1 = -1;
x2 = 1;
% x1 <= x <= x2
I3 = int(I2, x, x1, x2);
display(I3)
%%
% Triple integral simple for a x space D
% In this example:  int_z( int_y( int_x( f )dx )dy )dz
syms x y z
f = x^2 + 2*y^2 * z;
% Cylinders: x^2 + z^2 = 1 (i) and y^2 + z^2 = 1 (ii)
% Solve (i) for x and : -sqrt(1 - z^2) <= x <= sqrt(1 - z^2)
% Solve (ii) for y and get: -sqrt(1 - z^2) <= y <= sqrt(1 - z^2)
% The projection of the enclosed surface on the yz plane is the unit circle.
% This gives the: -1 <= z <= 1
x1 = -sqrt(1 - z^2);
x2 = sqrt(1 - z^2);
% x1 <= x <= x2
I1 = int(f, x, x1, x2);
y1 = -sqrt(1 - z^2);
y2 = sqrt(1 - z^2);
% y1 <= y <= y2
I2 = int(I1, y, y1, y2);
z1 = -1;
z2 = 1;
% z1 <= z <= z2
I3 = int(I2, z, z1, z2);
display(I3)
%%
% Triple integral simple for a z space D
% In this example:  int_z( int_y( int_x( f )dx )dy )dz
syms x y z r theta
f = x^2 * y^2 + z^3;
% Surfaces: z = x^2 + y^2 , z = 1 , x^2 + y^2 = 1 , y = 2x , y = -2x , y>0
% For z we get:  1 <= z <= x^2 + y^2 we are under the paraboloid till z = 1
% On xy plane we are inside the unit circle and then we are on the upper
% half semi circle , y > 0.
% We will use polar coordinates cause we can easily see that : 0 <= r <= 1
% And theta1 <= theta <= theta2 , with theta = arctan( y / x )
% With y = 2*x and y = -2*x we get: -atan(2) <= theta <= atan(2)
z1 = x^2 + y^2;
z2 = 1;
% z1 <= z <= z2
I1 = int(f, z, z1, z2);
%Substitute x = r*cos(theta) and y = r*sin(theta)
I1new = subs(I1, [x y], [r*cos(theta) r*sin(theta)]);
r1 = 0;
r2 = 1;
% r1 <= r <= r2
I2 = int(I1new*r, r, r1, r2);
theta1 = -atan(2);
theta2 = atan(2);
% theta1 <= theta <= theta2
I3 = int(I2, theta, theta1, theta2);
display(I3)