function [O,C] = IDISD()
syms x y k
sd = 1;
% sd = surface density
% p = pressure
f = 1/(x^2+y^2); % use f = sd; to calculate the mass and the center of mass of D.
x1 = -1;
x2 = 1;
y1 = -sqrt(1-x^2);
y2 = sqrt(1-x^2);
T1 = isnumeric(x1);
T2 = isnumeric(x2);
T3 = isnumeric(y1);
T4 = isnumeric(y2);
if ((T3 == 1)&&(T4 == 1))
    % Double Integral for a simple x space D:
    % D ={(x,y): a <= y <= b and g1(y) <= x <= g2(y)}
    %x1 <= x <= x2
    I1 = int(f, x, x1, x2);
    % y1 <= y <= y2
    I2 = int(I1, y, y1, y2);
    % Calculate the Area of the simple x space D:
    E1 = int(1, x, x1, x2);
    E2 = int(E1, y, y1, y2);
    % Calculate the Mean Value of the function in the simple x space D:
    MV = I2/E2;
    % Find the values of f for the MV:
    %sol = solve(f == MV,[x,y]);
    %display(sol.x);
    %display(sol.y);
    %xc = int(int(x*sd, x, x1, x2), y, y1, y2)/I2;
    %yc = int(int(y*sd, x, x1, x2), y, y1, y2)/I2; % here mass is I2
    %C=[xc,yc];
    O = [I1,I2,E1,E2,MV];
    hold on
    fplot(x1);
    fplot(x2);
    fplot(x,y1);
    fplot(x,y2);
    hold off
elseif ((T1 == 1)&&(T2 == 1))
    % Double Integral for a simple y space D
    % D ={(x,y): a <= x <= b and g1(x) <= y <= g2(x)}
    % y1 <= y <= y2
    I1 = int(f, y , y1 , y2);
    % x1 <= x <= x2
    I2 = int(I1, x , x1 , x2);
    % Calculate the Area of the simple x space D:
    E1 = int(1, y, y1, y2);
    E2 = int(E1, x, x1, x2);
    % Calculate the Mean Value of the function in the simple x space D:
    MV = I2/E2;
    % Find the values of f for the MV:
    %sol = solve(f == MV,[x,y]);
    %display(sol.x);
    %display(sol.y);
    %xc = int(int(x*f, y, y1, y2), x, x1, x2)/I2;
    %yc = int(int(y*f, y, y1, y2), x, x1, x2)/I2; % here mass is I2
    %C=[xc,yc];
    O = [I1,I2,E1,E2,MV];
    hold on
    fplot(x1,y);
    fplot(x2,y);
    fplot(y1);
    fplot(y2);
    hold off
else
    fprintf("Error, check your input!");
    O = "ERROR";
    C = O;
end
end
