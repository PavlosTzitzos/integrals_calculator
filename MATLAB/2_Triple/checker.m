function [c,p] = checker(A)

n = length(A);
c = zeros(1,4);

for i =1:n
    if A(i) == 1
        c(1) = c(1) + 1;
        p(i) = 0;
    elseif A(i) == 0.5
        c(2) = c(2) + 1;
        p(i) = 0;
    elseif A(i) == 0
        c(3) = c(3) + 1;
        p(i) = 1;
    elseif A(i) == -0.5
        c(4) = c(4) + 1;
        p(i) = 0;
    else
        fprintf("ERROR");
    end
end

end
