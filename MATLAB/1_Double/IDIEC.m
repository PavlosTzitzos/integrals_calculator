function [O,C] = IDIEC(a,b,c1,c2,ff,r1,r2,theta1,theta2)
% Integrate Double Integral in Elliptical Coordinates
%The given cartesian space Dc is:
%Dc = {(x,y): a <= x^2 + y^2 <= b and g1(x) <= y <= g2(x)}
%or
%Dc = {(x,y): a <= x^2 + y^2 <= b and g1(y) <= x <= g2(y)}
%The elliptical space Del will be:
%Del = {(r,theta): r1 <= r <= r2 and theta1 <= theta <= theta2}
%Equation of ellipse:
% (x / a)^2 + (y / b)^2 = 1  or  c * x^2 + d * y^2 = e 
% where c = (sqrt(e) / a)^2 and d = (sqrt(e) / b)^2.
syms r theta k R s0 z x y
xel = a*r*cos(theta)+c1;
yel = b*r*sin(theta)+c2;
sdec = s0*(1-(r/R));
% sdm = surface density of mass
% p = pressure
% sdec = surface density of electric charge
f = ff;
if myhasSym(ff,x,y,z) ~= 0
    if (has(ff,x) == 1) && (has(ff,y) == 1)
        f = subs(ff,[x y], [xel yel]);
    elseif (has(ff,y) == 1) && (has(ff,z) == 1)
        f = subs(ff,[y z], [xel yel]);
    elseif (has(ff,x) == 1) && (has(ff,z) == 1)
        f = subs(ff,[x z], [xel yel]);
    else
        fprintf("\ncannot calculate\n");
    end
end
if (r1 == 0)&&(r2 == 0)&&(theta1 == 0)&&(theta2 == 0) 
    r1 = 0;
    r2 = R;
    theta1 = 0;
    theta2 = 2*pi;
end

% r1 <= r <= r2
I1 = int(f*a*b*r, r, r1, r2);
% theta1 <= theta <= theta2
I2 = int(I1, theta, theta1, theta2);
% Calculate the Area of the simple x space D:
E1 = int(a*b*r, r, r1, r2);
E2 = int(E1, theta, theta1, theta2); %E = pi*a*b
% Calculate the Mean Value of the function in the simple x space D:
MV = I2/E2;
xc = int(int(x*f*a*b*r, r, r1, r2), theta, theta1, theta2)/I2;
yc = int(int(y*f*a*b*r, r, r1, r2), theta, theta1, theta2)/I2; % here mass is I2
C=[xc,yc];
O = [I1,I2,E1,E2,MV];
end
