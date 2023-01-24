clc; clear;
syms x y z s t real
A = [0 0 0; 0 1 0; 0 0 1];
B = [1 0 0]';
c = -2;
X = [x y z]';
fprintf("\nThe general equation of a B' and A' degree Surface is:\n");
fprintf("\n%d *x^2 + %d *y^2 + %d *z^2 + %d *x*y + %d *x*z + %d *y*z + %d *x + %d *y + %d *z + %d = 0\n\n",A(1,1),A(2,2),A(3,3),2*A(1,2),2*A(1,3),2*A(2,3),B,c);

[P,D] = eig(A);

S = X'*D*X + B'*P*X + c == 0;
S = simplify(S);
display(S)
H = B'*P;

coef = [D(1,1) D(2,2) D(3,3) H c];
%coef = [1 1 0 0 0 1 -2];
if (D(1,1) ~= 1)&&(D(1,1) ~= 0)
    coef = coef./D(1,1);
end
display(coef)
if (coef(1) == 0)&&(coef(2) == 0)&&(coef(3) == 0)
    %Plane
    if B(3) ~= 0
        P = [0, 0, -c/B(3)];
    elseif B(3) == 0
        P = [0, 0, 1];
    else
        fprintf("\nERROR\n");
    end
    if B(2) ~= 0
        Q = [0, -c/B(2), 0];
    elseif B(2) == 0
        Q = [0, 1, 0];
    else
        fprintf("\nERROR\n");
    end
    if B(1) ~= 0
        R = [-c/B(1), 0, 0];
    elseif B(1) == 0
        R = [1, 0, 0];
    else
        fprintf("\nERROR\n");
    end
    display(P)
    display(Q)
    display(R)
    u = Q - P;
    v = R - P;
    display(u)
    display(v)
    r = [P(1) + s*v(1) + t*u(1); P(2) + s*v(2) + t*u(2); P(3) + s*v(3) + t*u(3)];
    display(r)
elseif (coef(1) == 1)&&(coef(2) == 1)&&(coef(3) == 1)&&(coef(7) ~= 0)
    chk1 = coef(4)^2+coef(5)^2+coef(6)^2 - 4*coef(7);
    if chk1 > 0
        %Sphere
        K = [-coef(4)/2,-coef(5)/2,-coef(6)/2];
        R = 0.5*sqrt(chk1);
        xt = K(1) + R*cos(s)*sin(t);
        yt = K(2) + R*sin(s)*sin(t);
        zt = K(3) + R*cos(t);
        r = [xt yt zt];
        display(r)
    else
        fprintf("\nCannot calculate.\n");
    end
    
elseif (coef(1) < 0)||(coef(2) < 0)||(coef(3) < 0)
    %Hyperboloid
    ah = sqrt(c/coef(1));
    bh = sqrt(c/coef(2));
    ch = sqrt(c/coef(3));
    xt = ah*cosh(s)*cos(t);
    yt = bh*cosh(s)*sin(t);
    zt = ch*sinh(t);
    r = [xt yt zt];
    
elseif (coef(1) < 0)||(coef(2) < 0)||(coef(3) < 0)
    %Ellipsoid
    ae = sqrt(c/coef(1));
    be = sqrt(c/coef(2));
    ce = sqrt(c/coef(3));
    xt = ae*cos(s)*sin(t);
    yt = be*sin(s)*sin(t);
    zt = ce*cos(t);
    r = [xt yt zt];
elseif ((coef(1) < 1)||(coef(2) < 1)||(coef(3) < 1))&&(coef(7) == 0)
    %R*r*cos()/h
    if (coef(1) < 0)&&(coef(2) > 0)&&(coef(3) > 0)
        xt = s;
        yt = s*cos(t);
        zt = s*sin(t);
    elseif (coef(2) < 0)&&(coef(1) > 0)&&(coef(3) > 0)
        xt = s*sin(t);
        yt = s;
        zt = s*cos(t);
    elseif (coef(3) < 0)&&(coef(2) > 0)&&(coef(1) > 0)
        xt = s*cos(t);
        yt = s*sin(t);
        zt = s;
    %elseif 
        
    else
        fprintf("\nOops...\n");
    end
    r = [xt yt zt];
else
    fprintf("\nCannot calculate integral.\n");
    fprintf("\nUsing other ways...\n");
    r = 0;
end

if r == 0
    %z = g(x,y) or y = g(x,z) or x = g(y,z)
    if (coef(3) == 0)&&(coef(2) ~= 0)&&(coef(1) ~= 0)
        xt = u;
        yt = v;
        zt = g;
    elseif (coef(2) == 0)&&(coef(3) ~= 0)&&(coef(1) ~= 0)
        xt = u;
        yt = g;
        zt = v;
    elseif (coef(1) == 0)&&(coef(2) ~= 0)&&(coef(3) ~= 0)
        xt = g;
        yt = u;
        zt = v;
    else
        fprintf("\nCannot calculate.\n");
        fprintf("\nUsing other methods...\n");
        r = 0;
    end
end

if r == 0
    %Surface of Revolution
    [r,flag] = SurfacefromRotation();
end
if flag == 1
    %Using simplified forms
    R = ISIDI();
    stop = 1;
end
if stop == 1
    r = 0;
    O = R;
elseif stop == 0
    
    
end
%S1 = x^2 + y^2 -1;
%S2 = x + z - 2;
%assume(z == 0)
%SD = simplify(S1 == S2)
%fplot(x^2+y^2-x+1)