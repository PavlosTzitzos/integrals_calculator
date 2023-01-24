function [O] = StokesTheorem(n,F,D)
%n =  1; or 2;
%F = [F1 F2 F3]; or G = div F
%D = "+" or "-";
syms x y z
if (n == 1)&&(D == "+")
    O = curl(F,[x y z]);
elseif (n == 2)&&(D == "+")
    O = vectorPotential(F,[x y z]);
else
    fprintf("\nWrong input\n");
end

end