function[O] = myhasSym(A,B,C,D)

if isnumeric(A) == 0
    
T1 = has(A,B);
T2 = has(A,C);
T3 = has(A,D);

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
