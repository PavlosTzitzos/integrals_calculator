function [O] = ITIEC(chs,a,b,c,k1,k2,k3)

syms x y z R R1 R2 k r rho m0 I0 L d sgm rho0 e0

f = 1;
% rho = k*sqrt(r); % density of charge , Q = int_A rho dV
% u = k/r^4; % density of energy , E = int_A u dV
% E = int_K u dV , where u = piecewise((0 <= rho)&(rho <= R), k*rho, rho> R, k*R^2/rho);
% u = piecewise((0 <= R1)&(R1<=R2),((m0*I0)/(2*pi*rho))^2/(2*m0));
% u = 0.5*sgm*(k*rho)^2;
% rho(r) = piecewise(r<=R,rho0*(1-(r/R)),r>R,0);

if (chs == "el")||(chs == "sph")
    
    syms r theta phi
    
    xel = a*r*sin(theta)*cos(phi)+k1;
    yel = b*r*sin(theta)*sin(phi)+k2;
    zel = c*r*cos(theta)+k3;
    
    fnew = subs(f,[x y z],[xel yel zel]);
    
    r1 = 0;
    r2 = R;
    theta1 = pi/2;
    theta2 = pi;
    phi1 = 0;
    phi2 = 2*pi;
    
    I1 = int(fnew*a*b*c*r^2*sin(theta), r, r1, r2);
    I2 = int(I1, theta, theta1, theta2);
    I3 = int(I2, phi, phi1, phi2);
    
elseif (chs == "cyl")||(chs == "par")||(chs == "cn")
    syms rho phi z
    
    xcyl = rho*cos(phi)+k1;
    ycyl = b*rho*sin(phi)+k2;
    zcyl = z;
    
    fnew = subs(f,[x y z],[xcyl ycyl zcyl]);
    
    rho1 = 0;
    rho2 = R;
    phi1 = 0;
    phi2 = 2*pi;
    z1 = 0;
    z2 = d;
    
    I1 = int(fnew*rho, rho, rho1, rho2);
    I2 = int(I1, phi, phi1, phi2);
    I3 = int(I2, z, z1, z2);
    
else
    fprintf("Wrong input!\n");
end
O = [I1, I2, I3];
end
