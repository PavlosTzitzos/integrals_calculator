function [R] = ILIBG(G,F,DD,sf,cnt,trn)
syms t x y z xt(t) yt(t) zt(t)
%F = [x*y , -x^2, 0];
%cnt = "open";
%DD = "el"; sf = "xy";
%trn = "+"; % sign is + or -
O = [0 0 0];
A = [0 1 0];
B = [1 0 0];
C = [0 1 1];
D = [1 2];

a = G(1,1); b = G(1,2); c = G(1,3); d = G(1,4);
%1. Edges for Orthogonal C space D
c1 = G(2,1); c2 = G(2,2); k1 = G(2,3); k2 = G(2,4);
%2. EC - const - center
r1 = G(3,1); r2 = G(3,2); theta1 = G(3,3); theta2 = G(3,4);
%3. EC - radius - theta
k = isequal(simplify(diff(F(1),y)),simplify(diff(F(2),x)));
if (k == 1) && (F(3) == 0) && (cnt == "closed")&&(DD == "in")
    % If: closed curve , curl F = 0 and Dc in AF     Then: I = 0.
    fprintf("\nFunction is conservative.\n");
    R = 0;
elseif (cnt == "closed")
    % Use Green's Theorem
    fprintf("\nGreen Theorem\n");
    DF = diff(F(2),x) - diff(F(1),y);
    if DD == "cart"
        %Double Integral simple x and y space D
        I1 = int(DF, x, a, b);
        I2 = int(I1, y, c, d);
        R = I2;
    elseif DD == "el"
        %Double Integral in elliptical coordinates
        fprintf("\nDouble Integral in elliptical coordinates.\n");
        O = IDIEC(c1,c2,k1,k2,DF,r1,r2,theta1,theta2);
        R = O(2);
    else
        fprintf("\nCannot use Green Theorem\n");
        R = "ERROR";
    end
    if trn == "-"
        R = -R;
    end
elseif DD == "el"
    % The line of integration is an ellipsoid
    R = ILIEC(c1,c2,k1,k2,F,sf,A,B,trn);
elseif (DD == "xy") && (DD == "yx") && (DD == "xz") && (DD == "zx") && (DD == "zy") && (DD == "yz")
    if (DD == "xy") || (DD == "yx")
        y1 = A(1); y2 = B(1);
        x1 = A(1); x2 = B(1);
        
        if (myhasSym(y1,x) == -0.5)||(has(y2,x) == -0.5)
            I1 = int(F(1)+F(2)*diff(y,x), x, x1, x2);
            fprintf("wait");
        elseif has(y1,x) == 1
            fprintf("wait");
        end
    elseif (DD == "xz") && (DD == "zx")
        fprintf("wait");
        ...
    elseif (DD == "zy") && (DD == "zy")
    fprintf("wait");
        ...
    else
        fprintf("\nWrong surface, check DD\n");
    end
    R = I1;
elseif DD == "points"
    % Basic case
    fprintf("\nCalculate with the original forms.\n");
    R1 = ILIBK(F,O,B,"k");
    R2 = ILIBK(F,B,A,"k");
    R3 = ILIBK(F,A,O,"k");
%    R4 = ILIBK(F,D,A,"k");
    R = R1(1) + R2(1) + R3(1);% + R4(1);
else
    fprintf("\nSomething went wrong!\n");
end

end
