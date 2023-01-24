function [I] = ILIEC(a,b,c1,c2,F,srf,A,B,turn)
% turn is positive "+" or negative "-"
% srf = "xy";
syms t x y z
% parametrize
if (srf == "xy") || (srf == "yx")
    xel = a*cos(t) + c1;    dxel = diff(xel,t);
    yel = b*sin(t) + c2;    dyel = diff(yel,t);
    zel = 1;                dzel = diff(zel,t);
elseif (srf == "xz") || (srf == "zx")
    xel = a*cos(t) + c1;    dxel = diff(xel,t);
    yel = 1;                dyel = diff(yel,t);
    zel = b*sin(t) + c2;    dzel = diff(zel,t);
elseif (srf == "yz") || (srf == "zy")
    xel = 1;                dxel = diff(xel,t);
    yel = a*cos(t) + c1;    dyel = diff(yel,t);
    zel = b*sin(t) + c2;    dzel = diff(zel,t);
else
    fprintf("\n Check your input!\n");
end
if (length(A) == 3) && (length(B) == 3)
    % turn and t1 <= t <= t2
    ang1 = createline([0 0 0],A);
    ang2 = createline([0 0 0],B);
    if turn == "+"
        t1 = ang1(1);
        t2 = ang2(1);
        if t1 == t2
            t1 = 0;
            t2 = 2*pi;
        end
    elseif turn == "-"
        t1 = ang2(1);
        t2 = ang1(1);
        if t1 == t2
            t1 = 2*pi;
            t2 = 0;
        end
    else
        fprintf("\n Check yor input\n");
    end
else
    fprintf("\nERROR\n\tA and B must be of length 3!\n");
end
Pnew = subs(F(1),[x y z], [xel yel zel])*dxel;
Qnew = subs(F(2),[x y z], [xel yel zel])*dyel;
Rnew = subs(F(3),[x y z], [xel yel zel])*dzel;
I = vpaintegral(Pnew+Qnew+Rnew,t, t1, t2);

end
