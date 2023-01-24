function [O,flag] = ILIBK(F,A,B,cnt)
syms t x y z xt(t) yt(t) zt(t)
%cnt = "k";

LL = createline(A,B);
if length(A) == 2
    xt = t;
    yt = LL(1)*t+LL(2);
    zt = 0;
    if LL(1) == Inf
        xt = 0;
        yt = t;
    end
    if A(1) ~= B(1)
        t1 = A(1);
        t2 = B(1);
    elseif A(2) ~= B(2)
        t1 = A(2);
        t2 = B(2);
    else
        fprintf("\nCannot calculate\n");
    end
    
elseif length(A) == 3
    flag = 1;
    xt = LL(1,1)*t + LL(1,2);
    yt = LL(2,1)*t + LL(2,2);
    zt = LL(3,1)*t + LL(3,2);
    if has(xt,t) == 1
        t1 = solve(xt==A(1),t);
        t2 = solve(xt==B(1),t);
        flag = 0;
    elseif (has(yt,t) == 1) && (flag == 1)
        t1 = solve(yt==A(2),t);
        t2 = solve(yt==B(2),t);
        flag = 0;
    elseif (has(zt,t) == 1) && (flag == 1)
        t1 = solve(zt==A(3),t);
        t2 = solve(zt==B(3),t);
        flag = 0;
    else
        fprintf("ERROR");
    end
    
end
ct = [xt yt zt];

dxt = diff(xt, t);
dyt = diff(yt, t);
dzt = diff(zt, t);
dct = [dxt dyt dzt];

Ft = subs(F, {x, y, z}, [xt, yt, zt]);
%t1 <= t <= t2
%L = int(sqrt(dxt^2+dyt^2+dzt^2), t, t1, t2);
%display(L)

%Checking if f is conservative
if ( curl(F, [x y z]) == zeros(3,1) )  % nabla x F = 0
    fprintf("\nFunction is conservative.\n Calcualte with potential.\n");
    U = potential(F, [ x y z ]);    % F = nabla U
    if cnt == "p"
        A = subs(Ft, t, t1);            % A = F(t1)
        B = subs(Ft, t, t2);            % B = F(t2)
    end
        UA = subs(U, [x, y, z], A);       % UA = U(A)
        UB = subs(U, [x, y, z], B);       % UB = U(B)
    IAB = UB - UA;                  % IAB = int_AB F dr = U(B) - U(A)
    sprintf( 'IAB=%s' , char(IAB) )
    %MV = IAB/L;
    I = IAB;
else
    I = vpaintegral(Ft(1)*dxt + Ft(2)*dyt + Ft(3)*dzt,t,t1,t2);
    display(I)
    %MV = I/L;
    %display(MV)
end
L = 1;
MV = 1;
O = [I,L,MV];
end
