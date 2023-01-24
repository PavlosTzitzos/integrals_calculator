function [O] = ISIVF(DD)
syms x y z theta phi aa bb cc
F = [x y z];
g = x^2 + y^2 - z;
nvector = gradient(g);

a = 1; b = 1; c = 1; k1 = 0; k2 = 0; k3 = 0;
R = 1; theta1 = 0; theta2 = pi; phi1 = 0; phi2 = 2*pi; z1 = 0; z2 = 1;
x1 = -1; x2 = 1; y1 = -sqrt(1-x^2); y2 = sqrt(1-x^2); z1 = 0; z2 = 1;
T1 = isnumeric(x1);
T2 = isnumeric(x2);
T3 = isnumeric(y1);
T4 = isnumeric(y2);
T5 = isnumeric(z1);
T6 = isnumeric(z2);
if DD == "car"
    if myhasSym(g,x^2,y^2,z) == 1
        %Double Integral xy
        zs = solve(g == 0,z);
        Fnew = subs(F,z,zs);
        AF = -Fnew(1)*diff(zs,x)-Fnew(2)*diff(zs,y)+Fnew(3);
        if ((T3 == 1)&&(T4 == 1))
            I1 = int(AF, x, x1, x2);
            I2 = int(I1, y, y1, y2);
        elseif ((T1 == 1)&&(T2 == 1))
            I1 = int(AF, y, y1, y2);
            I2 = int(I1, x, x1, x2);
        else
            fprintf("\nCannot calculate\n");
        end
    elseif myhasSym(g,x^2,y,z^2) == 1
        %Double Integral xz
        ys = solve(g == 0,y);
        Fnew = subs(F,y,ys);
        AF = -Fnew(1)*diff(ys,x)+Fnew(2)-Fnew(3)*diff(ys,z);
        if ((T5 == 1)&&(T6 == 1))
            I1 = int(AF, x, x1, x2);
            I2 = int(I1, z, z1, z2);
        elseif ((T1 == 1)&&(T2 == 1))
            I1 = int(AF, z, z1, z2);
            I2 = int(I1, x, x1, x2);
        else
            fprintf("\nCannot calculate\n");
        end
    elseif myhasSym(g,x,y^2,z^2) == 1
        %Double Integral yz
        xs = solve(g == 0,x);
        Fnew = subs(F,x,xs);
        AF = Fnew(1)-Fnew(2)*diff(xs,y)-Fnew(3)*diff(xs,z);
        if ((T3 == 1)&&(T4 == 1))
            I1 = int(AF, z, z1, z2);
            I2 = int(I1, y, y1, y2);
        elseif ((T5 == 1)&&(T6 == 1))
            I1 = int(AF, y, y1, y2);
            I2 = int(I1, z, z1, z2);
        else
            fprintf("\nCannot calculate\n");
        end
    else
        fprintf("\nCannot calculate\n");
    end
elseif DD == "el"
    xel = a*R*sin(theta)*cos(phi) + k1;
    yel = b*R*sin(theta)*sin(phi) + k2;
    zel = c*R*cos(theta) + k3;
    Fnew = subs(F,{x y z}, {xel yel zel});
    nvectornew = subs(nvector,{x y z}, {xel yel zel});
    nhat = nvectornew/norm(nvectornew);
    I1 = int(dot(Fnew,nhat)*a*b*c*R^2*sin(theta),theta, theta1, theta2);
    I2 = int(I1, phi, phi1, phi2);
elseif DD == "cyl"
    xcyl = a*R*cos(phi) + k1;
    ycyl = b*R*sin(phi) + k2;
    zcyl = c*z + k3;
    Fnew = subs(F,{x y z}, {xcyl ycyl zcyl});
    nvectornew = subs(nvector,{x y z}, {xcyl ycyl zcyl});
    nhat = nvectornew/norm(nvectornew);
    I1 = int(dot(Fnew,nhat)*a*b*c*R, phi, phi1, phi2);
    I2 = int(I1, z, z1, z2);
else
    fprintf("\nWrong input\n");
end
O = [I1 I2];
end
