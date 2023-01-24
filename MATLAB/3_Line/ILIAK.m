function [O] = ILIAK(ct,dct,f,t1,t2)
syms t x y z

ft = subs(f, {x, y, z}, [ct(1), ct(2), ct(3)]);

%t1 <= t <= t2
I = int(ft*sqrt(dct(1)^2 + dct(2)^2 + dct(3)^2), t, t1, t2);
L = int(sqrt(dct(1)^2 + dct(2)^2 + dct(3)^2), t, t1, t2);
MV = I/L;
O = [I L MV];
end
