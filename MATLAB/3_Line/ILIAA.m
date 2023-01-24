clc; clear;
syms x y z t
%Integrate Line Integral version AA
F = [x*y^2 , -y, 0];

% For A' kind:
t1 = 0;
t2 = 1;

% For B' kind:
a = 0; b = 1; c = 0; d = 0;
%1. Edges for Orthogonal C space D: a<=x<=b,c<=y<=d.
c1 = 1; c2 = 1; k1 = 0; k2 = 0;
%2. EC - const: [c1 c2] - center: [k1 k2]
r1 = 0; r2 = 1; theta1 = 0; theta2 = pi/2;
%3. EC - radius: [r1 r2] - theta: [theta1 theta2]
G = [a b c d;c1 c2 k1 k2;r1 r2 theta1 theta2];
cnt = "closed";   % control is "open" or "closed"
DD = "el";      % DD is "in" or "out" and "el" or "cart" or "points"
sf = "xy";      % sf is surface and is "xy","yx","xz","zx","zy","yz"
trn = "+";      % trn is the sign of the direction of the line or curve 
                % and is "+" or "-"
% In case you have specific points go to ILIBG

if (F(2) == 0) && (F(3) == 0)
    fprintf("\nLine Integral A' kind\n\n");
    
    f = F(1);
    
    xt = 2*cos(t);
    yt = 2*sin(t);
    zt = t;
    
    ct = [xt yt zt];
    
    dxt = diff(xt, t);
    dyt = diff(yt, t);
    dzt = diff(zt, t);
    
    dct = [dxt dyt dzt];
    O = ILIAK(ct,dct,f,t1,t2);
    display(O)
elseif (F(2) ~= 0) || (F(1) ~= 0) || (F(3) ~= 0)
    fprintf("\nLine Integral B' kind\n\n");
    O = ILIBG(G,F,DD,sf,cnt,trn);
    display(O)
else
    fprintf("\nERROR !! Check your function\n\n");
end
