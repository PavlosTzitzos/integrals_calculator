function [F,Duv] = Changeofvariables(fxy,oldxy,newuv,xuv,yuv,Dxy)
syms x y u v
fuv = subs(fxy,oldxy,newuv);
DJD = [diff(xuv,newuv(1)) diff(xuv,newuv(2));diff(yuv,newuv(1)) diff(yuv,newuv(2))];
F = fuv*DJD;
s1 = solve(Dxy(1,1) == xuv, Dxy(1,2) == xuv, [u v]);
s2 = solve(Dxy(2,1) == yuv, Dxy(2,2) == yuv, [u v]);
u1 = s1.u; v1 = s1.v;
u2 = s2.u; v2 = s2.v;
Duv = [u1 u2;v1 v2];
end
