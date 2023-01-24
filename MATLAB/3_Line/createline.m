function [R] = createline(A,B)

if length(A) ~= length(B)
    fprintf("\nERROR\n Points must be same length\n");
elseif length(B) == 2
    C = [A(1) 1; B(1) 1];
    D = [A(2);B(2)];
    R = C\D;% R = [a;b] : y = a*x + b
elseif length(B) == 3
    AB = B - A;% AB = OB - OA
    R = [AB(1) A(1);AB(2) A(2);AB(3) A(3)];
else
    fprintf("\nERROR\n");
end

end
