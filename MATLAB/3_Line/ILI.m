clc; clear;
%Integrate Line Integral
syms x y z t
%f(x,y,z)
%Initializing the function :
F = [y*x*z 0 0];
%initialize the parametrized curve and its limits t1 and t2:
t1 = 0;
t2 = 2;
xt = t;
yt = t^2;
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
D1 = "xy"; D2 = "no"; turn = "+";

if (F(2) == 0) && (F(3) == 0)
    % A kind Line Integral
    %function f(x,y,z)
    R = ILIG(F(1),ct,t1,t2,D1,D2,0);
else
    % B kind Line Integral
    %function: F(x,y,z) = (F1 , F2 , F3)
    mx = 2;
    con=0;
    %initialize at 2 compounts
    if F(3) ~= 0
        mx = 3;
    end
    
    %CF = curl(F,[x y z]);
    %if CF ==[0 0 0]
    %    fprintf("Conservative function");
    %    con=1;
    %end
    if con==1
        R=0;
    else
        %correction, if necessary, at 3 compounts
        % 1 integral breaks at 3 different integrals:
        D2 = ["x","y","z"];
        for c =1:1:mx
            O(c) = ILIG(F(c),ct,t1,t2,D1,D2(c),c);
        end
        R=0;
        for i=1:mx
            R=R+O(i);
        end
    end
end
%if the turn of the c is - then the result is:
if turn == "-"
    R = - R;
end
%printing the result:
%display(O);
display(R);
