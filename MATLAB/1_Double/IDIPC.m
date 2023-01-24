function [O] = IDIPC()
% Integrate Double Integral in Polar Coordinates

%The given cartesian space Dc is:
%Dc = {(x,y): a <= x^2 + y^2 <= b and g1(x) <= y <= g2(x)}
%or
%Dc = {(x,y): a <= x^2 + y^2 <= b and g1(y) <= x <= g2(y)}
%The polar space Dp will be:
%Dp = {(r,theta): r1 <= r <= r2 and theta1 <= theta <= theta2}
syms r theta
x = r * cos(theta);
y = r * sin(theta);

f = log(1+x^2+y^2);
%r = sqrt(x^2 + y^2)
%theta = atan(y / x)
r1 = 0;
r2 = 1;
theta1 = 0;
theta2 = 2*pi;
f*r
% r1 <= r <= r2
I1 = int(f*r, r, r1, r2);
% theta1 <= theta <= theta2
I2 = int(I1, theta, theta1, theta2);
% Calculate the Area of the simple x space D:
E1 = int(1, r, r1, r2);
E2 = int(E1, theta, theta1, theta2);
% Calculate the Mean Value of the function in the simple x space D:
MV = I2/E2;
O = [I1,I2,E1,E2,MV];

end
