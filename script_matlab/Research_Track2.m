clc
clear all
close all
%% Solution of prof. Recchiuto 

Trial_1 = ["Trial_01";"Trial_02";"Trial_03";"Trial_04";"Trial_05";"Trial_06";"Trial_07";"Trial_08";"Trial_09";"Trial_10";"Trial_11";"Trial_12";"Trial_13";"Trial_14";"Trial_15"];
Time_1 = [185.55;190.21;187.80;199.1;201.22;220.1;185.24;194.39;197.81;171.30;177.2;181.1;241.59;198.76;200.1];
Colision_1 = [0;0;0;0;0;2;0;0;0;0;0;0;5;0;0];
Wrong_way_1 = [2;4;1;4;5;9;1;3;4;0;1;3;11;2;5];
Crash_1 = ['No';'No';'No';'No';'No';'No';'No';'No';'No';'No';'No';'No';'No';'No';'No'];
your_solution = table(Trial_1,Time_1,Colision_1,Wrong_way_1,Crash_1)

%% Solution of Haji Hosseini 

Trial_2 = ["Trial_01";"Trial_02";"Trial_03";"Trial_04";"Trial_05";"Trial_06";"Trial_07";"Trial_08";"Trial_09";"Trial_10";"Trial_11";"Trial_12";"Trial_13";"Trial_14";"Trial_15"];
Time_2 = [187.02;196.01;192.76;200.47;209.91;0;191.4;202.8;222.12;172.06;181.67;199.6;0;216.82;211.6];
Colision_2 = [0;2;1;3;5;0;1;2;7;0;1;3;0;6;3];
Wrong_way_2 = [5;6;4;5;6;0;4;5;9;3;4;6;0;9;8];
Crash_2 = ['No';'No';'No';'No';'No';'Ys';'No';'No';'No';'No';'No';'No';'Ys';'No';'No'];
my_solution = table(Trial_2,Time_2,Colision_2,Wrong_way_2,Crash_2)

%% Data analaysis
%============================= Bar_chart ================================== 
x = [1:15];
center_1 = [185.55;190.21;187.80;199.1;201.22;220.1;185.24;194.39;197.81;171.30;177.2;181.1;241.59;198.76;200.1];
center_2 = [187.02;196.01;192.76;200.47;209.91;0;191.4;202.8;222.12;172.06;181.67;199.6;0;216.82;211.6];
T1 = Time_1';
T2 = Time_2';
vals = [T1;T2];
hold all
b = bar(x,vals);
p1 = plot(x,center_1,'b','LineWidth',1);
p2 = plot(x,center_2,'r','LineWidth',1);
hold off
ylim([170 250])
title('Time') 
legend('your_solution','my_solution','Line of your_solution','Line of my_solution')
xlabel('Trial')
ylabel('Seconds')

figure 
subplot(1,2,1) 
b1= bar(x,T1);
ylim([170 250])
title('Bar chart') 
legend('my_solution')
xlabel('Trial')
ylabel('Seconds')
subplot(1,2,2) 
b2= bar(x,T2,'r');
ylim([170 250])
title('Bar chart') 
legend('your_solution')
xlabel('Trial')
ylabel('Seconds')

figure 
W12 = abs(Wrong_way_2 - Wrong_way_1);
W12([6,13],:)= 0;
W = [Wrong_way_1,W12]; 
b1= barh(x,W,'stacked');
title('Wrong way') 
legend('your_solution','my_solution')
xlabel('Times')
ylabel('Trial')


%============================== Pie_chart =================================
labels = {'Success','Crash'};
figure 
data_1 = [1 0];
subplot (1,2,1) 
pie(data_1)
title('your_solution')
data_2 = [0.87 0.13];
subplot (1,2,2)
pie(data_2)
title('my_solution') 
lgd = legend(labels);
%========================= Media & Mediana & sdt ==========================

Media_1 = mean(Time_1)
Median_1 = median(Time_1)
Std_1 = std(Time_1)
Min_1 = min(Time_1)
Max_1 = max(Time_1)

Time_2([6,13],:)= []; %remove zero lines
Media_2 = mean(Time_2)
Median_2 = median(Time_2)
Std_2 = std(Time_2)
Min_2 = min(Time_2)
Max_2 = max(Time_2)

figure
subplot(2,1,1)
hold all
plot(Time_1,'b','LineWidth',1)
plot(Time_1+Std_1,'c','LineWidth',6)
plot(Time_1-Std_1,'c','LineWidth',6)
xlim([1 15])
title('your_solution') 
legend('Time','std(sup-inf)')
xlabel('Trials')
ylabel('Second')
hold off

subplot(2,1,2)
hold all
plot(Time_2,'b','LineWidth',1)
plot(Time_2+Std_2,'c','LineWidth',6)
plot(Time_2-Std_2,'c','LineWidth',6)
xlim([1 13])
title('my_solution') 
legend('Time','std(sup-inf)')
xlabel('Trials')
ylabel('Second')
hold off

%============================== ttest =====================================

load alpha005
%hypothesis H0 : Time_1 > Time_2
%hypothesis H1 : Time_2 > Time_1 
t_test = (Media_2-Media_1)/ ((Std_2/sqrt(length(Std_2)))+(Std_1/sqrt(length(Std_1))));
alpha = 0.05;
[date,camp] = size(vals);
lunghezza_campioni = (length(Time_2) + length(Time_1)) - camp;
[i,j] = size(unnamed);
for e = 1:size(unnamed)
    i = lunghezza_campioni;
    t_tabella = unnamed(i);
end
abs(t_tabella)
abs(t_test)
if abs(t_tabella) == abs(t_test)
   disp('hypothesis H0: Time_1 > Time_2 verified')
else abs(t_tabella) < abs(t_test)
   disp('hypothesis H1: Time_2 > Time_1 verified')
    disp(abs(t_tabella) < abs(t_test))
end