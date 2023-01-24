function [O] = GaussTheorem(n,F,D1,D2)
syms x y z
%n =  1; or 2;
%F = [F1 F2 F3]; or G = div F
%D1 = "closed" or "open";
%D2 = "inout" or outin;
if (n == 1)&&(D1 == "closed")
    O = divergence(F);
elseif (n == 2)&&(D1 == "closed")
    O = potential(F);
else
    fprintf("\nWrong input\n");
end

end
