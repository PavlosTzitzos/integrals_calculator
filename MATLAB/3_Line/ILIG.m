function [O] = ILIG(f,ct,t1,t2, DD,frm,p)
%Integrate Line Integral - General File
syms x y z t
%geting the derivatives of c:
dct(1) = diff(ct(1),t);
dct(2) = diff(ct(2),t);
dct(3) = diff(ct(3),t);
%a check for x, y, z in f.
DDD = myhasSym(f,x,y,z);
%creating f(t):
fnew = subs(f, [x y z], [ct(1) ct(2) ct(3)]);

if DDD == 0
    %No x,y,z
    fprintf("\nERROR\n");
    O = "ERROR";
elseif (DDD == 1) || (DDD == 0.5) || (DDD == -0.5)
    %...
    if frm == "x"
        Ix = int(fnew*dct(1), t, t1, t2);
        O = Ix;
    elseif frm == "y"
        Iy = int(fnew*dct(2), t, t1, t2);
        O = Iy;
    elseif frm == "z"
        Iz = int(fnew*dct(3), t, t1, t2);
        O = Iz;
    elseif frm == "no" && p==0
        
        if (DD == "xyz") && (DDD == 1)
            I = int(fnew*sqrt(dct(1)^2 + dct(2)^2 + dct(3)^2), t, t1, t2);
        elseif DD == "xy"
            I = int(fnew*sqrt(dct(1)^2 + dct(2)^2), t, t1, t2);
        elseif DD == "xz"
            I = int(fnew*sqrt(dct(1)^2 + dct(3)^2), t, t1, t2);
        elseif DD == "yz"
            I = int(fnew*sqrt(dct(2)^2 + dct(3)^2), t, t1, t2);
        else
            fprintf("\nWarning ! Wrong Input ! \n");
        end
        O = I;
    else
        fprintf("\nCheck your input DD\n");
    end
else
    fprintf("\nCannot calculate higher dimensions maximum 3!!\n");
end

end