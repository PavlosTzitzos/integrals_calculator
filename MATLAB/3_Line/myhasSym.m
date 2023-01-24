function[O] = myhasSym(A,B,C,D)
%A is a symbolic function.
%B,C,D are the variables in A.
if isnumeric(A) == 0
    T1 = has(A,B);
    % T1 is 1 if A contains B , 0 if not.
    T2 = has(A,C);
    % T2 is 1 if A contains C , 0 if not.
    T3 = has(A,D);
    % T3 is 1 if A contains D , 0 if not.
    if ((T1==1) && (T2==1) && (T3==1))
        O = 1;
    elseif ((T1==1) && (T2==1) && (T3==0))
        O = 0.5;
    elseif ((T1==1) && (T2==0) && (T3==1))
        O = 0.5;
    elseif ((T1==0) && (T2==1) && (T3==1))
        O = 0.5;
    elseif ((T1==1) && (T2==0) && (T3==0))
        O = -0.5;
    elseif ((T1==0) && (T2==1) && (T3==0))
        O = -0.5;
    elseif ((T1==0) && (T2==0) && (T3==1))
        O = -0.5;
    elseif ((T1==0) && (T2==0) && (T3==0))
        O = -1;
    else
        fprintf("Error! Something whent wrong!");
        O = NaN;
    end
elseif isnumeric(A) == 1
    O = 0;
end
