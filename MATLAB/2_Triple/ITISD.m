function [O,C] = ITISD(v,sp)
syms x y z z1(x,y) z2(x,y) y1(x,z) y2(x,z) x1(y,z) x2(y,z) k
%rho = k*x; % rho = density
f = 1;
z1 = ;
z2 = ;
y1 = ;
y2 = ;
x1 = ;
x2 = ;
T(1) = myhasSym(z1,x,y,z);
T(2) = myhasSym(z2,x,y,z);
T(3) = myhasSym(y1,x,y,z);
T(4) = myhasSym(y2,x,y,z);
T(5) = myhasSym(x1,x,y,z);
T(6) = myhasSym(x2,x,y,z);
[chk,pivots] = checker(T);
flag = 1;
if chk(1) > 0
    fprintf("\t!!!WARNING!!!!\n");
    fprintf("Cannot calculate the gaven integral.\n");
    fprintf("Chkecker the z1,z2,y1,y2,x1,x2!!!\n");
    flag = 0;
elseif ((chk(2) > 0)&&(chk(1)==0)) && (flag == 1)
    if (((T(1) == 0.5)||(T(2) == 0.5))) && (flag == 1)
        % Triple Integral simple for a z space D
        % up from a surface z = z1(x,y) and down from a surface z = z2(x,y)
        % A = {(x,y,z): z1(x,y) <= z <= z2(x,y) , (x,y) in D}
        
        % z1 <= z <= z2
        I1 = int(f, z, z1, z2);
        % volume
        if v == 1
            V1 = int(1, z, z1, z2);
        end
        % special
        if sp == 1
            xc1 = int(rho*x, z, z1, z2);
            yc1 = int(rho*y, z, z1, z2);
            zc1 = int(rho*z, z, z1, z2);
        end
        if (((T(3) == 0)&&(T(4) == 0))) && (flag == 1)
            % Double Integral for a simple x space D:
            % D ={(x,y): a <= y <= b and g1(y) <= x <= g2(y)}
            
            % x1 <= x <= x2
            I2 = int(I1, x, x1, x2);
            % y1 <= y <= y2
            I3 = int(I2, y, y1, y2);
            % volume
            if v == 1
                V2 = int(V1, x, x1, x2);
                V3 = int(V2, y, y1, y2);
            end
            % special
            if sp == 1
                xc2 = int(int(xc1, x, x1, x2), y, y1, y2);
                yc2 = int(int(yc1, x, x1, x2), y, y1, y2);
                zc2 = int(int(zc1, x, x1, x2), y, y1, y2);
            end
            flag = 0;
        elseif (((T(5) == 0)&&(T(6) == 0))) && (flag == 1)
            % Double Integral for a simple y space D
            % D ={(x,y): a <= x <= b and g1(x) <= y <= g2(x)}
            
            % y1 <= y <= y2
            I2 = int(I1, y, y1, y2);
            % x1 <= x <= x2
            I3 = int(I2, x, x1, x2);
            % volume
            if v == 1
                V2 = int(V1, y, y1, y2);
                V3 = int(V2, x, x1, x2);
            end
            % special
            if sp == 1
                xc2 = int(int(xc1, y, y1, y2), x, x1, x2);
                yc2 = int(int(yc1, y, y1, y2), x, x1, x2);
                zc2 = int(int(zc1, y, y1, y2), x, x1, x2);
            end
            flag = 0;
        else
        fprintf("Error, check your input! 1 \n");
        O = "ERROR";
        C = O;
        end
        
    elseif (((T(3) == 0.5)||(T(4) == 0.5))) && (flag == 1)
        % Triple Integral simple for a y space D
        % up from a surface y = y1(x,z) and down from a surface y = y2(x,z)
        % A = {(x,y,z): y1(x,z) <= y <= y2(x,z) , (x,z) in D}
        
        % y1 <= y <= y2
        I1 = int(f, y, y1, y2);
        % volume
        if v == 1
            V1 = int(1, y, y1, y2);
        end
        % special
        if sp == 1
            xc1 = int(rho*x, y, y1, y2);
            yc1 = int(rho*y, y, y1, y2);
            zc1 = int(rho*z, y, y1, y2);
        end
        if (((T(1) == 0)&&(T(2) == 0))) && (flag == 1)
            % Double Integral for a simple x space D:
            % D ={(x,z): a <= z <= b and g1(z) <= x <= g2(z)}
            fprintf("hey");
            % x1 <= x <= x2
            I2 = int(I1, x, x1, x2);
            % z1 <= z <= z2
            I3 = int(I2, z, z1, z2);
            % volume
            if v == 1
                V2 = int(V1, x, x1, x2);
                V3 = int(V2, z, z1, z2);
            end
            % special
            if sp == 1
                xc2 = int(int(xc1, x, x1, x2), z, z1, z2);
                yc2 = int(int(yc1, x, x1, x2), z, z1, z2);
                zc2 = int(int(zc1, x, x1, x2), z, z1, z2);
            end
            flag = 0;
        elseif (((T(5) == 0)&&(T(6) == 0))) && (flag == 1)
            % Double Integral for a simple z space D
            % D ={(x,z): a <= x <= b and g1(x) <= z <= g2(x)}
            fprintf("hey");
            % z1 <= z <= z2
            I2 = int(I1, z, z1, z2);
            % x1 <= x <= x2
            I3 = int(I2, x, x1, x2);
            % volume
            if v == 1
                V2 = int(V1, z, z1, z2);
                V3 = int(V2, x, x1, x2);
            end
            % special
            if sp == 1
                xc2 = int(int(xc1, z, z1, z2), x, x1, x2);
                yc2 = int(int(yc1, z, z1, z2), x, x1, x2);
                zc2 = int(int(zc1, z, z1, z2), x, x1, x2);
            end
            flag = 0;
        else
        fprintf("Error, check your input! 2 \n");
        O = "ERROR";
        C = O;
        end
    elseif (((T(5) == 0.5)||(T(6) == 0.5))) && (flag == 1)
        % Triple Integral simple for a x space A
        % up from a surface x = x1(y,z) and down from a surface x = x2(y,z)
        % A = {(x,y,z): x1(y,z) <= x <= x2(y,z) , (y,z) in D}
        
        % x1 <= x <= x2
        I1 = int(f, x, x1, x2);
        % volume
        if v == 1
            V1 = int(1, x, x1, x2);
        end
        % special
        if sp == 1
            xc1 = int(rho*x, x, x1, x2);
            yc1 = int(rho*y, x, x1, x2);
            zc1 = int(rho*z, x, x1, x2);
        end
        if (((T(1) == 0)&&(T(2) == 0))) && (flag == 1)
            % Double Integral for a simple y space D:
            % D ={(x,z): a <= z <= b and g1(z) <= y <= g2(z)}
            
            % y1 <= y <= y2
            I2 = int(I1, y, y1, y2);
            % z1 <= z <= z2
            I3 = int(I2, z, z1, z2);
            % volume
            if v == 1
                V2 = int(V1, y, y1, y2);
                V3 = int(V2, z, z1, z2);
            end
            % special
            if sp == 1
                xc2 = int(int(xc1, y, y1, y2), z, z1, z2);
                yc2 = int(int(yc1, y, y1, y2), z, z1, z2);
                zc2 = int(int(zc1, y, y1, y2), z, z1, z2);
            end
            flag = 0;
        elseif (((T(3) == 0)&&(T(4) == 0))) && (flag == 1)
            % Double Integral for a simple z space D
            % D ={(x,z): a <= y <= b and g1(x) <= z <= g2(x)}
            
            % z1 <= z <= z2
            I2 = int(I1, z, z1, z2);
            % y1 <= y <= y2
            I3 = int(I2, y, y1, y2);
            % volume
            if v == 1
                V2 = int(V1, z, z1, z2);
                V3 = int(V2, y, y1, y2);
            end
            % special
            if sp == 1
                xc2 = int(int(xc1, z, z1, z2), y, y1, y2);
                yc2 = int(int(yc1, z, z1, z2), y, y1, y2);
                zc2 = int(int(zc1, z, z1, z2), y, y1, y2);
            end
            flag = 0;
        else
        fprintf("Error, check your input! 3 \n");
        O = "ERROR";
        C = O;
        end
    end
elseif ((chk(4) >= 1)&&(chk(1) == 0)&&(chk(2)==0)) && (flag == 1)
    % Triple Integral on a simple A
    % with the other two variables depend only on the simple one.
    if (pivots(1) == 1) && (pivots(2) == 1)
        if ((pivots(3) == 1) && (pivots(4) == 1))||((pivots(5) == 0) && (pivots(6) == 0))
            I1 = int(f, x, x1, x2);
            I2 = int(I1, y, y1, y2);
            flag = 0;
        elseif (((pivots(5) == 1) && (pivots(6) == 1))||((pivots(3) == 0) && (pivots(4) == 0))) && (flag == 1)
            I1 = int(f, y, y1, y2);
            I2 = int(I1, x, x1, x2);
            flag = 0;
        elseif (((pivots(3) == 1) || (pivots(4) == 1)&&((pivots(5) == 1) || (pivots(6) == 1)))) && (flag == 1)
            I1 = int(f, x, x1, x2);
            I2 = int(I1, y, y1, y2);
            flag = 0;
        else
            fprintf("\nERROR\n");
        end
        % Triple Integral simple for a y or x space D
        I3 = int(I2, z, z1, z2);
        % volume
        if v == 1
            V1 = int(1, y, y1, y2);
            V2 = int(V1, x, x1, x2);
            V3 = int(V2, z, z1, z2);
        end
        % special
        if sp == 1
            xc2 = int(int(int(rho*x, y, y1, y2), x, x1, x2), z, z1, z2);
            yc2 = int(int(int(rho*y, y, y1, y2), x, x1, x2), z, z1, z2);
            zc2 = int(int(int(rho*z, y, y1, y2), x, x1, x2), z, z1, z2);
        end
    elseif ((pivots(3) == 1) && (pivots(4) == 1)) && (flag == 1)
        % Triple Integral simple for a z or x space D
        if (pivots(5) == 1) && (pivots(6) == 1)
            flag = 0;
        elseif ((pivots(5) == 1) || (pivots(6) == 1)) && (flag == 1)
            
            flag = 0;
        elseif ((pivots(5) == 0) && (pivots(6) == 0)) && (flag == 1)
            
            flag = 0;
        else
            fprintf("\nERROR\n");
        end
        I1 = int(f, z, z1, z2);
        I2 = int(I1, x, x1, x2);
        I3 = int(I2, y, y1, y2);
        % volume
        if v == 1
            V1 = int(1, z, z1, z2);
            V2 = int(V1, x, x1, x2);
            V3 = int(V2, y, y1, y2);
        end
        % special
        if sp == 1
            xc2 = int(int(int(rho*x, z, z1, z2), x, x1, x2), y, y1, y2);
            yc2 = int(int(int(rho*y, z, z1, z2), x, x1, x2), y, y1, y2);
            zc2 = int(int(int(rho*z, z, z1, z2), x, x1, x2), y, y1, y2);
        end
    elseif (pivots(5) == 1) && (pivots(6) == 1)
        % Triple Integral simple for a z or y space D
        if (pivots(1) == 0) && (pivots(2) == 0)
            
        elseif (pivots(3) == 0) && (pivots(4) == 0)
            
        else
            
        end
        I1 = int(f, z, z1, z2);
        I2 = int(I1, y, y1, y2);
        I3 = int(I2, x, x1, x2);
        % volume
        if v == 1
            V1 = int(1, z, z1, z2);
            V2 = int(V1, y, y1, y2);
            V3 = int(V2, y, y1, y2);
        end
        % special
        if sp == 1
            xc2 = int(int(int(rho*x, z, z1, z2), y, y1, y2), x, x1, x2);
            yc2 = int(int(int(rho*y, z, z1, z2), y, y1, y2), x, x1, x2);
            zc2 = int(int(int(rho*z, z, z1, z2), y, y1, y2), x, x1, x2);
        end
    else
        fprintf("ERROR");
    end
    
elseif ((chk(3) == 6)) && (flag == 1)
    % Triple Integral on a rectangular parallelepiped Α
    % The order of integration does not matter.
    
    % z1 <= z <= z2
    I1 = int(f, z, z1, z2);
    % y1 <= y <= y2
    I2 = int(I1, y, y1, y2);
    % x1 <= x <= x2
    I3 = int(I2, x, x1, x2);
    % volume
    if v == 1
        V1 = int(1, z, z1, z2);
        V2 = int(V1, y, y1, y2);
        V3 = int(V2, x, x1, x2);
    end
    % special
    if sp == 1
        xc2 = int(int(int(rho*x, z, z1, z2), y, y1, y2), x, x1, x2);
        yc2 = int(int(int(rho*y, z, z1, z2), y, y1, y2), x, x1, x2);
        zc2 = int(int(int(rho*z, z, z1, z2), y, y1, y2), x, x1, x2);
    end
else
    fprintf("\n ! ERROR ! \n");
end
O = [I1,I2,I3];
if v == 1
    MV = I3 / V3;
    O = [I1,I2,I3,V1,V2,V3,MV];
end
if sp == 1
    C = [xc2/I3, yc2/I3, zc2/I3];
end
disp(flag);
end
