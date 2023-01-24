clc; clear;
%Integrate Line Integral
syms x y z t
%f(x,y,z)
%Initializing the function :
F = [x*y x^2 0];
%initialize the parametrized curve and its limits t1 and t2:
if(F(2)~=0 || F(3)~=0)
    fprintf("Vector Function\n");
end

t1 = pi;
t2 = 0;
xt = cos(t);
yt = sin(t);
zt = 0;
%F is the function
%t1 <= t <= t2
%c:(xt,yt,zt)
%calls the ILIG file as many times as the non zero terms in F.
% vector of c:
ct = [xt yt zt];
%turn is + or -
%D1 is 
%D2 is ""
%D1 = "xy"; D2 = "no"; turn = "+";
if (F(2) == 0) && (F(3) == 0)
    % A kind Line Integral
    %function f(x,y,z)
    O = ILIG(F,ct,t1,t2,D1,D2,1);
else
    % B kind Line Integral
    %function: F(x,y,z) = (F1 , F2 , F3)
    mx = 2;
    %initialize at 2 compounts
    if F(3) ~= 0
        mx = 3;
    end
    %correction, if necessary, at 3 compounts
    % 1 integral breaks at 3 different integrals:
    for c =1:1:mx
        O(c) = ILIG(F(c),ct,t1,t2,D1,D2,2);
        display(O)
    end
end
%if the turn of the c is - then the result is:
if turn == "-"
    O = - O;
end
%printing the result:
display(O)
