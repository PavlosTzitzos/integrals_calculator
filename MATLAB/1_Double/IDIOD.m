function [I2] = IDIOD()
prompt = 'Enter function: ';
ff = input(prompt,'s');
printf("Enter a: ");
a = input('f');
printf("Enter b: ");
b = input('f');
printf("Enter c: ");
c = input('f');
printf("Enter d: ");
d = input('f');
%a = 0;
%b = 1;
%c = -1;
%d = 0;
syms x y
%f = x - 2*y;
%f = y*x^2;
f = str2sym(ff)
I1 = int(f, x, a, b);
I2 = int(I1, y, c, d);

display(I1);
display(I2);

hold on
fplot(a,y);
fplot(b,y);
fplot(c);
fplot(d);
hold off
end
