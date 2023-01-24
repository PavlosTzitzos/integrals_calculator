function [O] = ISIDI(DD,srf,el)
%DD is coordinates
% srf is z=z(x,y) or y=y(x,z) or x=x(y,z)
% el is "no" or "yes"
syms x y z theta phi R h
f = 1;
x1 = -1; x2 = 1; y1 = -sqrt(1 - x^2); y2 = sqrt(1 - x^2); z1 = 1; z2 = 2-x^2-y^2;
a = 1; b = 1; c = 1; k1 = 0; k2 = 0; k3 = 0; r1 = 0; r2 = 2;
theta1 = 0; theta2 = 2*pi; phi1 = 0; phi2 = pi/2;
zsrf = -2*(4 - x^2 - y^2);
ysrf = 1;
xsrf = y^2+z^2;
%xt = ;
%yt = ;
%zt = ;
if DD == "car"
    if srf == "z"
        ds = sqrt(1 + diff(zsrf,x)^2 + diff(zsrf,y)^2 );
        fnew = subs(f,z,zsrf)*ds;
        if el == "no"
            if (myhasSym(x1,x,y,z) == 0) || (myhasSym(x2,x,y,z) == 0)
                I1 = int(fnew, y, y1, y2);
                I2 = int(I1, x, x1, x2);
            elseif (myhasSym(y1,x,y,z) == 0) || (myhasSym(y2,x,y,z) == 0)
                I1 = int(fnew, x, x1, x2);
                I2 = int(I1, y, y1, y2);
            else
                fprintf("\nSomething went wrong!\n");
            end
            O = [I1 I2];
        elseif el == "yes"
            O = IDIEC(a,b,k1,k2,fnew,r1,r2,theta1,theta2);
        else
            fprintf("\nCheck your input\n");
        end
    elseif srf == "y"
        ds = sqrt(1 + diff(ysrf,x)^2 + diff(ysrf,z)^2 );
        fnew = subs(f,y,ysrf)*ds;
        if el == "no"
            if (myhasSym(x1,x,y,z) == 0) || (myhasSym(x2,x,y,z) == 0)
                I1 = int(fnew, z, z1, z2);
                I2 = int(I1, x, x1, x2);
            elseif (myhasSym(z1,x,y,z) == 0) || (myhasSym(z2,x,y,z) == 0)
                I1 = int(fnew, x, x1, x2);
                I2 = int(I1, z, z1, z2);
            else
                fprintf("\nSomething went wrong!\n");
            end
            O = [I1 I2];
        elseif el == "yes"
            O = IDIEC(a,b,k1,k2,fnew,r1,r2,theta1,theta2);
        else
            fprintf("\nCheck your input\n");
        end
    elseif srf == "x"
        ds = sqrt(1 + diff(xsrf,y)^2 + diff(xsrf,z)^2 );
        fnew = subs(f,x,xsrf)*ds;
        if el == "no"
            if (myhasSym(z1,x,y,z) == 0) || (myhasSym(z2,x,y,z) == 0)
                I1 = int(fnew, y, y1, y2);
                I2 = int(I1, z, z1, z2);
            elseif (myhasSym(y1,x,y,z) == 0) || (myhasSym(y2,x,y,z) == 0)
                I1 = int(fnew, z, z1, z2);
                I2 = int(I1, y, y1, y2);
            else
                fprintf("\nSomething went wrong!\n");
            end
            O = [I1 I2];
        elseif el == "yes"
            O = IDIEC(a,b,k1,k2,fnew,r1,r2,theta1,theta2);
        else
            fprintf("\nCheck your input\n");
        end
    else
        fprintf("\nWrong input!\n");
        O = "ERROR";
    end
elseif DD == "el"
    xel = a*r2*sin(theta)*cos(phi) + k1;
    yel = b*r2*sin(theta)*sin(phi) + k2;
    zel = c*r2*cos(theta) + k3;
    ds = a*b*r2^2*sin(theta);
    fnew = subs(f,[x y z], [xel yel zel]);
    I1 = int(fnew*ds, theta, theta1, theta2);
    I2 = int(I1, phi, phi1, phi2);
    O = [I1 I2];
elseif DD == "cyl"
    xcyl = r2*cos(phi) + k1;
    ycyl = r2*sin(phi) + k2;
    zcyl = z;
    ds = r2;
    fnew = subs(f,[x y z], [xcyl ycyl zcyl]);
    I1 = int(fnew*ds, phi, phi1, phi2);
    I2 = int(I1, z, z1, z2);
    O = [I1 I2];
elseif DD == "rt"
    if srf == "x"
       I = 2*pi*int(f*abs(yt)*sqrt(diff(xt,t)^2+diff(yt,t)^2));
    elseif srf == "y"
        I = 2*pi*int(f*abs(yt)*sqrt(diff(xt,t)^2+diff(yt,t)^2));
    elseif srf == "z"
        I = 2*pi*int(f*abs(yt)*sqrt(diff(xt,t)^2+diff(yt,t)^2));
    else
        fprintf("\nERROR\n");
    end
else
    fprintf("\n Warning 1 ! Check your DD variable.\n DD = car,el,cyl.\n");
    O = "ERROR";
end

end