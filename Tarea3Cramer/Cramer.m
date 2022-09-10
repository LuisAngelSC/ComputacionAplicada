clear all
n=3;
a=[0.25 0.15 0; 0.45 0.5 0.75;0.3 0.35 0.25];
B=[1.5;5;3]

for i=1:n
    for j=1:n
        D(i,j)=a(i,j);
    end
end
delta=det(D)

A1=a;
A1(1:end,1)=B;
x1= det(A1)/delta;

A2=a;
A2(1:end,2)=B;
x2= det(A2)/delta;

A3=a;
A3(1:end,3)=B;
x3= det(A3)/delta;