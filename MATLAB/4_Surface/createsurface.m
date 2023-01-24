function [] = createsurface(chs,G,nn)
syms x y z
if chs == 1
    A = G;
    n = nn;
    srf = dot(n,[x y z]-A);
    display(srf);
elseif chs == 2
    A = G;
    b = nn(1,:);
    c = nn(2,:);
    n = cross(b,c);
    srf = dot(n,[x y z]-A);
    display(srf);
elseif chs == 3
    A = G(1,:);
    B = G(2,:);
    C = G(3,:);
    AB = B-A;
    BC = C-B;
    n = cross(AB,BC);
    srf = dot(n,[x y z]-C);
    display(srf);
else
    
end

end
