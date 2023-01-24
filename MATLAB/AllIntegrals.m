syms x y z

F = [y*x 0 0];
INTEGRAL = "D";
%Double = "D" , Triple = "T" , Line = "L" , Surface = "S" , General = "G"
COORDINATES = "car";
%Cartesian = "car" , "plr" , "el" , "cyl"

g = x^2 + y^2 - 1;%g(x,y,z) = 0


Folder = 'C:\Users\user\Documents\FILES_OCTAVE\Mathematics\Integrals\1_Double';
FileList = dir(fullfile(Folder, '*.m'));
for iFile = 1:numel(FileList)
    File = fullfile(FileList(iFile).folder, FileList(iFile).name);
    % Do what you want with this file, e.g.:
    if INTEGRAL = "D"
        if (myhasSym(F(2)) == 0)&&(myhasSym(F(3)) == 0)
            if COORDINATES == "car"
                O = IDISD(F(1));
            elseif COORDINATES == "el"
                O = IDIEC(F(1));
            else
                fprintf("\nWarning! D.1\n");
            end
        elseif (myhasSym(F(2)) ~= 0)||(myhasSym(F(3)) ~= 0)
            for j = 1:3
                if COORDINATES == "car"
                    O(j) = IDISD(F(j));
                elseif COORDINATES == "el"
                    O(j) = IDIEC(F(j));
                elseif myhasSym(F(j)) == 0
                    O(j) = NaN;
                else
                    fprintf("\nWarning! D.3\n");
                end
            end
        else
            fprintf("");
        end
    elseif INTEGRAL == "T"
        
    elseif INTEGRAL == "L"
        
        
    elseif INTEGRAL == "S"
        
    elseif INTEGRAL == "G"
        
    else
        fprintf("\nCannot calculate\n");
    end
end

