function [r1,r2,theta1,theta2] = limitsofintegration(a,b,c,d,flag)
syms x y 
x1=a;
x2=b;
y1=c;
y2=d;
switch (flag)
    case 0
        %Simple x and y
        r1=sqrt(x1^2+y1^2);
        r2=sqrt(x2^2+y2^2);
        theta1 = atan(y1/x2);
        theta2 = atan(y2/x1);
    case 1
        %Simple x
        A(1)=x1;
        B(1)=x1;
        C(1)=x2;
        D(1)=x2;
        A(2)=simplify(subs(y1,x,A(1)));
        B(2)=subs(y2,x,B(1));
        C(2)=subs(y1,x,C(1));
        D(2)=subs(y2,x,D(1));
        rA=sqrt(A(1)^2+A(2)^2);
        thetaA = atan(A(2)/A(1));
        rB=sqrt(B(1)^2+B(2)^2);
        thetaB = atan(B(2)/B(1));
        rC=sqrt(C(1)^2+C(2)^2);
        thetaC = atan(C(2)/C(1));
        rD=sqrt(D(1)^2+D(2)^2);
        thetaD = atan(D(2)/D(1));
        r1 = min([rA,rB,rC,rD]);
        r2 = max([rA,rB,rC,rD]);
        theta1 = min([thetaA,thetaB,thetaC,thetaD]);
        theta2 = max([thetaA,thetaB,thetaC,thetaD]);
    case 2
        %Simple y
        A(1)=x1;
        B(1)=x1;
        C(1)=x2;
        D(1)=x2;
        A(2)=simplify(subs(y1,x,A(1)));
        B(2)=subs(y2,x,B(1));
        C(2)=subs(y1,x,C(1));
        D(2)=subs(y2,x,D(1));
        rA=sqrt(A(1)^2+A(2)^2);
        thetaA = atan(A(2)/A(1));
        rB=sqrt(B(1)^2+B(2)^2);
        thetaB = atan(B(2)/B(1));
        rC=sqrt(C(1)^2+C(2)^2);
        thetaC = atan(C(2)/C(1));
        rD=sqrt(D(1)^2+D(2)^2);
        thetaD = atan(D(2)/D(1));
        r1 = min([rA,rB,rC,rD]);
        r2 = max([rA,rB,rC,rD]);
        theta1 = min([thetaA,thetaB,thetaC,thetaD]);
        theta2 = max([thetaA,thetaB,thetaC,thetaD]);
    otherwise
        fprintf("ERROR at limits of integration");
end

end