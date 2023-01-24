syms x y z
f = ;
choose = ;
%1 2 3 4 5

switch(choose)
    case 1
        %Siple Integral
    case 2
        Result = IDOD()
        if myhasSym(Result,x,y,z) ~= 0
            Result = IDISD
            if myhasSym(Result,x,y,z) ~= 0
                Result = IDIEC
                if myhasSym(Result,x,y,z) ~= 0
                    fprintf("\nERROR Check your input\n");
                end
            end
        end
        
    case 3
    case 4
    case 5
    otherwise
        fprintf("\nWrong Input\n");
end
