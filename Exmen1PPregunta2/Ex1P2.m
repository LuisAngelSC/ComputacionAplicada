prom_E=mean(Estatura); %Promedio Estatura
desv_est_E=std(Estatura); %Desv. Estan. de Estatura
b=prom_E;
c=var(Estatura);
a=(1/(desv_est_E*sqrt(2*pi())));
for i=1:200
    gauss(i)=a*exp(-((i-b)^2)/(2*c));
end
plot(gauss);

hist_E=histogram(Estatura)




% prom_T=mean(Talla);%Promedio Talla
% desv_est_T=std(Talla); %Desv. Estan. de Talla
% % hist_T=histogram(Talla)