function [] = SurfacefromRotation(ct,DD)

if DD == "xy"
    xt = x*sin(phi);
    yt = y;
    zt = x*cos(phi);
    st = [xt yt zt];
elseif DD == "xz"
    xt = x*cos(phi);
    yt = x*sin(phi);
    zt = z;
    st = [xt yt zt];
elseif DD == "yx"
    xt = x;
    yt = y*cos(phi);
    zt = y*sin(phi);
    st = [xt yt zt];
elseif DD == "yz"
    xt = y*cos(phi);
    yt = y*sin(phi);
    zt = z;
    st = [xt yt zt];
elseif DD == "zx"
    xt = x;
    yt = z*cos(phi);
    zt = z*sin(phi);
    st = [xt yt zt];
elseif DD == "zy"
    xt = z*sin(phi);
    yt = y;
    zt = z*cos(phi);
    st = [xt yt zt];
else
    fprintf("\nERROR\n");
end

end

