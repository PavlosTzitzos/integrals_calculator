function [O,E,C] = ITIDIEC(a,b,c1,c2,v,sp,ar)
syms x y z z1(x,y) z2(x,y) y1(x,z) y2(x,z) x1(y,z) x2(y,z) k r theta
%rho = k*x; % rho = density
f = 1;
z1 = x^2+y^2;
z2 = sqrt(1 - y^2 - x^2) + 1;
y1 = -sqrt(1-x^2);
y2 = sqrt(1-x^2);
x1 = -1;
x2 = 1;
r1 = 0;
r2 = 1;
theta1 = 0;
theta2 = 2*pi;
T(1) = myhasSym(z1,x,y,z);
T(2) = myhasSym(z2,x,y,z);
T(3) = myhasSym(y1,x,y,z);
T(4) = myhasSym(y2,x,y,z);
T(5) = myhasSym(x1,x,y,z);
T(6) = myhasSym(x2,x,y,z);

[chk,pivots] = checker(T);

if ((T(1) == 0.5)||(T(2) == 0.5))
    % Triple Integral simple for a z space D
    % up from a surface z = z1(x,y) and down from a surface z = z2(x,y)
    % A = {(x,y,z): z1(x,y) <= z <= z2(x,y) , (x,y) in D}
    
    % z1 <= z <= z2
    I1 = int(f, z, z1, z2)
    % volume
    if v == 1
        V1 = int(1, z, z1, z2);
    end
    % special
    if sp == 1
        xc1 = int(rho*x, z, z1, z2);
        yc1 = int(rho*y, z, z1, z2);
        zc1 = int(rho*z, z, z1, z2);
    end
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
    xe = a*r*cos(theta)+c1;
    ye = b*r*sin(theta)+c2;
    I1new = subs(I1,[x y], [xe ye])
    % r1 <= r <= r2
    I2 = int(I1new*a*b*r, r, r1, r2)
    % theta1 <= theta <= theta2
    I3 = int(I2, theta, theta1, theta2);
    % Calculate the Area of the space D:
    if ar == 1
        E1 = int(a*b*r, r, r1, r2);
        E2 = int(E1, theta, theta1, theta2); %E = pi*a*b
    end
    %Volume
    if v == 1
        V1new = subs(V1, [x y], [xe ye]);
        V2 = int(V1new*a*b*r, r, r1, r2);
        V3 = int(V2, theta, theta1, theta2); %E = pi*a*b
    end
    % special
    if sp == 1
        xc2 = int(int(xc1*a*b*r, r, r1, r2), theta, theta1, theta2);
        yc2 = int(int(yc1*a*b*r, r, r1, r2), theta, theta1, theta2); % here mass is I3
        zc2 = int(int(zc1*a*b*r, r, r1, r2), theta, theta1, theta2);
    end
    
elseif ((T(3) == 0.5)&&(T(4) == 0.5))
    % Triple Integral simple for a y space D
    % up from a surface y = y1(x,z) and down from a surface y = y2(x,z)
    % A = {(x,y,z): y1(x,z) <= y <= y2(x,z) , (x,z) in D}
    
    % y1 <= y <= y2
    I1 = int(f, y, y1, y2);
    % volume
    if v == 1
        V1 = int(1, y, y1, y2);
    end
    % special
    if sp == 1
        xc1 = int(rho*x, y, y1, y2);
        yc1 = int(rho*y, y, y1, y2);
        zc1 = int(rho*z, y, y1, y2);
    end
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
    xe = a*r*cos(theta)+c1;
    ze = b*r*sin(theta)+c2;
    I1new = subs(I1,[x z], [xe ze]);
    % r1 <= r <= r2
    I2 = int(I1new*a*b*r, r, r1, r2);
    % theta1 <= theta <= theta2
    I3 = int(I2, theta, theta1, theta2);
    % Calculate the Area of the space D:
    if ar == 1
        E1 = int(a*b*r, r, r1, r2);
        E2 = int(E1, theta, theta1, theta2); %E = pi*a*b
    end
    %Volume
    if v == 1
        V1new = subs(V1, [x z], [xe ze]);
        V2 = int(V1new*a*b*r, r, r1, r2);
        V3 = int(V2, theta, theta1, theta2); %E = pi*a*b
    end
    % special
    if sp == 1
        xc2 = int(int(xc1*a*b*r, r, r1, r2), theta, theta1, theta2);
        yc2 = int(int(yc1*a*b*r, r, r1, r2), theta, theta1, theta2); % here mass is I3
        zc2 = int(int(zc1*a*b*r, r, r1, r2), theta, theta1, theta2);
    end
    
elseif ((T(5) == 0.5)&&(T(6) == 0.5))
    % Triple Integral simple for a x space D
    % up from a surface x = x1(y,z) and down from a surface x = x2(y,z)
    % A = {(x,y,z): x1(y,z) <= x <= x2(y,z) , (y,z) in D}
    
    % x1 <= x <= x2
    I1 = int(f, x, x1, x2);
    % volume
    if v == 1
        V1 = int(1, x, x1, x2);
    end
    % special
    if sp == 1
        xc1 = int(rho*x, x, x1, x2);
        yc1 = int(rho*y, x, x1, x2);
        zc1 = int(rho*z, x, x1, x2);
    end
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
    ye = a*r*cos(theta)+c1;
    ze = b*r*sin(theta)+c2;
    I1new = subs(I1,[x y], [ye ze]);
    % r1 <= r <= r2
    I2 = int(I1new*a*b*r, r, r1, r2);
    % theta1 <= theta <= theta2
    I3 = int(I2, theta, theta1, theta2);
    % Calculate the Area of the space D:
    if ar == 1
        E1 = int(a*b*r, r, r1, r2);
        E2 = int(E1, theta, theta1, theta2); %E = pi*a*b
    end
    %Volume
    if v == 1
        V1new = subs(V1, [y z], [ye ze]);
        V2 = int(V1new*a*b*r, r, r1, r2);
        V3 = int(V2, theta, theta1, theta2); %E = pi*a*b
    end
    % special
    if sp == 1
        xc2 = int(int(xc1*a*b*r, r, r1, r2), theta, theta1, theta2);
        yc2 = int(int(yc1*a*b*r, r, r1, r2), theta, theta1, theta2); % here mass is I3
        zc2 = int(int(zc1*a*b*r, r, r1, r2), theta, theta1, theta2);
    end
    
elseif (chk(4) == 4)
    % Triple Integral on a simple A
    % with the other two variables depend only on the simple one.
    if (pivots(1) == 1) && (pivots(2) == 1)
        % Triple Integral simple for a y or x space D
        I1 = int(f, y, y1, y2);
        I2 = int(I1, x, x1, x2);
        I3 = int(I2, z, z1, z2);
        % volume
        if v == 1
            V1 = int(1, y, y1, y2);
            V2 = int(V1, x, x1, x2);
            V3 = int(V2, z, z1, z2);
        end
        % special
        if sp == 1
            xc2 = int(int(int(rho*x, y, y1, y2), x, x1, x2), z, z1, z2);
            yc2 = int(int(int(rho*y, y, y1, y2), x, x1, x2), z, z1, z2);
            zc2 = int(int(int(rho*z, y, y1, y2), x, x1, x2), z, z1, z2);
        end
    elseif (pivots(3) == 1) && (pivots(4) == 1)
        % Triple Integral simple for a z or x space D
        I1 = int(f, z, z1, z2);
        I2 = int(I1, x, x1, x2);
        I3 = int(I2, y, y1, y2);
        % volume
        if v == 1
            V1 = int(1, z, z1, z2);
            V2 = int(V1, x, x1, x2);
            V3 = int(V2, y, y1, y2);
        end
        % special
        if sp == 1
            xc2 = int(int(int(rho*x, z, z1, z2), x, x1, x2), y, y1, y2);
            yc2 = int(int(int(rho*y, z, z1, z2), x, x1, x2), y, y1, y2);
            zc2 = int(int(int(rho*z, z, z1, z2), x, x1, x2), y, y1, y2);
        end
    elseif (pivots(5) == 1) && (pivots(6) == 1)
        % Triple Integral simple for a z or y space D
        I1 = int(f, z, z1, z2);
        I2 = int(I1, y, y1, y2);
        I3 = int(I2, x, x1, x2);
        % volume
        if v == 1
            V1 = int(1, z, z1, z2);
            V2 = int(V1, y, y1, y2);
            V3 = int(V2, y, y1, y2);
        end
        % special
        if sp == 1
            xc2 = int(int(int(rho*x, z, z1, z2), y, y1, y2), x, x1, x2);
            yc2 = int(int(int(rho*y, z, z1, z2), y, y1, y2), x, x1, x2);
            zc2 = int(int(int(rho*z, z, z1, z2), y, y1, y2), x, x1, x2);
        end
    else
        fprintf("ERROR");
    end
    
elseif (chk(3) == 6)
    % Triple Integral on a rectangular parallelepiped Α
    % The order of integration does not matter.
    
    % z1 <= z <= z2
    I1 = int(f, z, z1, z2);
    % y1 <= y <= y2
    I2 = int(I1, y, y1, y2);
    % x1 <= x <= x2
    I3 = int(I2, x, x1, x2);
    % volume
    if v == 1
        V1 = int(1, z, z1, z2);
        V2 = int(V1, y, y1, y2);
        V3 = int(V2, x, x1, x2);
    end
    % special
    if sp == 1
        xc2 = int(int(int(rho*x, z, z1, z2), y, y1, y2), x, x1, x2);
        yc2 = int(int(int(rho*y, z, z1, z2), y, y1, y2), x, x1, x2);
        zc2 = int(int(int(rho*z, z, z1, z2), y, y1, y2), x, x1, x2);
    end
end
O = [I1,I2,I3];
if v == 1
    MV = I3 / V3;
    O = [I1,I2,I3,V1,V2,V3,MV];
end
if ar == 1
    E = E2;
if sp == 1
    C = [xc2/I3, yc2/I3, zc2/I3];
end

end
