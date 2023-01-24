%Line Integrals
%A' kind

syms t a b
x = b;
dx = diff(x,t);
y = a*cos(t);
dy = diff(y,t);
z = a*sin(t);
dz = diff(z,t);

f = x*y*z^2;

t1 = 0;
t2 = pi/2;
%t1 <= t <= t2
I = int(f*sqrt(dx^2+dy^2+dz^2), t, t1, t2);
display(I)
%%
%B' kind
clc; clear;
syms t x y z
xt = sin(t);
dxt = diff(xt, t);
yt = cos(t);
dyt = diff(yt, t);
zt = 1;
dzt = diff(zt, t);
f = [ y*x^2+x*exp(z) , -x*(y^2)*exp(y) , (z^2)-2*x*y ];
ft = subs(f, {x, y, z}, [xt, yt, zt]);
t1 = 0;
t2 = 2*pi;
%t1 <= t <= t2
%Checking if f is conservative
if ( curl(f, [x y z]) == [0;0;0] )% ?????????
    U = potential(f, [ x y z ]);
    A = subs(ft, t, t1);
    B = subs(ft, t, t2);
    UA = subs(U, x, y, z, A);
    UB = subs(U, x, y, z, B);
    IAB = UB - UA;
    sprintf( 'IAB=%s' , char(IAB) )
else
    I = vpaintegral(ft(1)*dxt + ft(2)*dyt + ft(3)*dzt,t,t1,t2);
    display(I)
end
%%
% B' kind with 3 lines
%we can integrate its line seperately
clc; clear;
syms t x y z
% The 3 points are: O(0,0) , A(0,1) , B(1,0)
f = [ (x*y)^2 , 2*(y^3) ];

%OB
xtOB = t;
dxtOB = diff(xtOB, t);
ytOB = 0;
dytOB = diff(ytOB, t);
ztOB = 0;
dztOB = diff(ztOB, t);
t1OB = 0;
t2OB = 1;
%t1OB <= tOB <= t2OB
ftOB = subs(f, {x, y}, [xtOB, ytOB]);
IOB = int(ftOB(1)*dxtOB+ftOB(2)*dytOB,t,t1OB,t2OB);
display(IOB)
%BA
xtBA = t;
dxtBA = diff(xtBA, t);
ytBA = 1 - t;
dytBA = diff(ytBA, t);
ztBA = 0;
dztBA = diff(ztBA, t);
t1BA = 1;
t2BA = 0;
%t1BA <= tBA <= t2BA
ftBA = subs(f, {x, y}, [xtBA, ytBA]);
IBA = int(ftBA(1)*dxtBA+ftBA(2)*dytBA,t,t1BA,t2BA);
display(IBA)
%AO
xtAO = 0;
dxtAO = diff(xtAO, t);
ytAO = t;
dytAO = diff(ytAO, t);
ztAO = 0;
dztAO = diff(ztAO, t);
t1AO = 1;
t2AO = 0;
%t1AO <= tAO <= t2AO
ftAO = subs(f, {x, y}, [xtAO, ytAO]);
IAO = int(ftAO(1)*dxtAO+ftAO(2)*dytAO,t,t1AO,t2AO);
display(IAO)
%Sum of the 3 parts:
I = IOB + IBA + IAO;
display(I)
%%
% Surface Integrals
% Surface Integral A' kind
syms x y z
f = x^2 - y*z^2;
% S is: z = 1 , z = 2 - x^2 - y^2.
zp = 2 - x^2 - y^2;
ds = sqrt(1 + diff(zp,x)^2 + diff(zp,y)^2 );
% This gives ds = sqrt(1 + (-2x)^2 + (-2y)^2)dxdy.
% Place the z cartesian equation in the f and replace the ds.
% Now it is a double integral which we can solve as in integrals.m.
% D = {(x,y): -sqrt(1-x^2) <= y <= sqrt(1-x^2) and -1 <= x <= 1}
f = subs(f,z,zp);
x1 = -1;
x2 = 1;
%x1 <= x <= x2
y1 = -sqrt(1 - x^2);
y2 = sqrt(1 - x^2);
%y1 <= y <= y2
% 1st way:
I1 = vpaintegral(f*ds, y, y1, y2);
display(I1)
I2 = vpaintegral(I1, x, x1, x2);
display(I2)
% 2nd way:
syms r theta
xp = r*cos(theta);
yp = r*sin(theta);
dsp = subs(ds, {x,y}, {xp, yp});
fp = subs(f,{x,y}, {xp, yp});
r1 = 0;
r2 = 1;
%r1 <= r <= r2
theta1 = 0;
theta2 = 2*pi;
%theta1 <= theta <= theta2
I3 = int(fp*dsp*r, r, r1, r2);
display(I3)
I4 = int(I3, theta, theta1, theta2);
display(I4)
%%
syms x y z
f = x/(sqrt(1 + 4*(z^2 + y^2)));
% S is: x - y^2 - z^2 = 0 with x <= 1.
xs = y^2 + z^2;
ds = sqrt(1 + diff(xs,y)^2 + diff(xs,z)^2 );
fnew = subs(f,x,xs)
z1 = -1;
z2 = 1;
%z1 <= z <= z2
y1 = -sqrt(1 - z^2);
y2 = sqrt(1 - z^2);
%y1 <= y <= y2
% 1st way:
I1 = vpaintegral(fnew*ds, y, y1, y2);
display(I1)
I2 = vpaintegral(I1, z, z1, z2);
display(I2)
% 2nd way:
syms r theta
yp = r*cos(theta);
zp = r*sin(theta);
dsp = subs(ds, {y,z}, {yp, zp})
fp = subs(fnew,{y,z}, {yp, zp})
r1 = 0;
r2 = 1;
%r1 <= r <= r2
theta1 = 0;
theta2 = 2*pi;
%theta1 <= theta <= theta2
I3 = int(fp*dsp*r, r, r1, r2);
I4 = int(I3, theta, theta1, theta2);
display(I4)
%%
% Surface Integral B' kind
syms x y z
z = x^2 + y^2;
F = [x y z];
n = [diff(z,x) diff(z,y) -1];
% now the integral is a double integral and we will transform it in polar
% coordinates.
syms r theta
xp = r*cos(theta);
yp = r*sin(theta);
Fp = subs(F, {x,y}, {xp,yp});
np = subs(n, {x,y}, {xp,yp});
%Now we are ready to integrate
r1 = 0;
r2 = 1;
%r1 <= r <= r2
theta1 = 0;
theta2 = 2*pi;
%theta1 <= theta <= theta2
I1 = int(dot(Fp,np)*r, r, r1,r2);
I2 = int(I1, theta, theta1, theta2);
display(I2)
%%
% Surface Integral B' kind
% At this point go and see some basic theory before you continue
% nvector = nabla(g(x,y,z)) , where g=g(x,y,z) is the surface equation.
% Here: g(x,y,z) = x^2 + y^2 + z^2 - 4 , which is a semisphere for z <= 0.
% That's why we are going to use spherical coordinates:
% 0 <= phi <= 2*pi , pi/2 <= theta <= pi , 0 <= R <= 2.
% The rvector is : (came from hat n)
% rvector(theta, phi) = 2*sin(theta)*cos(phi)*ivector + ...
% ... 2*sin(theta)*sin(phi)*jvector + 2*cos(theta)*kvector
% The integral is:
% int_phi ( int_theta ( (Fvector dot rvector) * R^2 * sin(theta) )dtheta ) dphi

syms x y z
F = [y -y*z x];
g = x^2 + y^2 + z^2 - 4;
nvector = gradient(g);
normn = 4; % norm n = R^2 = 4
nhat = nvector / normn;
%Spherical Coordinates:
syms theta phi
R = 2;
xsp = R*sin(theta)*cos(phi);
ysp = R*sin(theta)*sin(phi);
zsp = R*cos(theta);

Fsp = subs(F, {x,y,z}, {xsp,ysp,zsp});
nhatsp = subs(nhat, {x,y,z}, {xsp,ysp,zsp});

theta1 = pi/2;
theta2 = pi;
%theta1 <= theta <= theta2
phi1 = 0;
phi2 = 2*pi;
%phi1 <= phi <= phi2

I1 = int(dot(Fsp,nhatsp)*R^2*sin(theta), theta, theta1, theta2);
I2 = int(I1, phi, phi1, phi2);
display(I2)
%%
% Surface Integral with Elliptical Coordinates
syms x y z
%Surface equation:
z = x^2 + 2*y^2; % with z<=1 and out -|-> in
% Fvector:
F = [2*y -x -z];
n = [-diff(z,x) -diff(z,y) 1];
syms r theta
xel = r*cos(theta);
yel = (1/sqrt(2))*r*sin(theta);
Fel = subs(F, {x,y}, {xel,yel});
nel = subs(n, {x,y}, {xel,yel});

r1 = 0;
r2 = 1;
%r1 <= r <= r2
theta1 = 0;
theta2 = 2*pi;
%theta1 <= theta <= theta2

I1 = int(dot(Fel,nel)*(1/sqrt(2))*r, r, r1, r2);
I2 = int(I1, theta, theta1, theta2);
display(I2)
