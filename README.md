# Assignment-Research Track 2 (statistic analysis)

Introduction
================================

Statistical analysis between two solutions; _YOUR SOLUTION_ (created by Prof. Recchiuto) and _MY SOLUTION_ (created by me). Analysis is based on 15 different mapping modes that basically Roboto has to find the silver tokens and take it. There are 7 silver tokens across the map. The time it takes Robot to make a complete turn is collected in a matrix to compare between two solutions; over time I took into account, colision number, wrong way number and if there was crash during mission. The purpose of the analysis is to compare two solutions through the data collected above, inside a matrix and making different analyzes such as analyzing in Bar chart, Pie chart, level of accuracy through standard deviation and T student test to verify hypotheses.

Hypothesis
================================

Assumption considered that _YOUR SOLUTION_ has less time than _MY SOLUTION_ to complete a lap in map, but _MY SOLUTION_ has more accurate time compare to _YOUR SOLUTION_. The following hypotheses can be verified through various analyzes

Running 
--------

To start the simulator you have to proceed with

```   
 $ python2 run.py your_solution.py
 $ python2 run.py my_solution.py
```

Resualt & Verify hypothesis
----------------------------

To load the data matrix and analyze it, I used __MATLAB__ to accomplish this.

The data was collected in two separate matrixes with the following names:
![image](https://user-images.githubusercontent.com/80394968/170829630-c5ee13db-9dd0-4210-b80f-d3adde3fcac4.png)
![image](https://user-images.githubusercontent.com/80394968/170829645-b27caffe-bc14-452f-a079-3443d5af484d.png)

First analysis done on [Bar chart](https://it.mathworks.com/help/matlab/ref/bar.html). As you can see height of the blue bars are lower than the red ones, this means that _YOUR SOLUTION_ takes less time to complete the lap. Also there are significant lines that pass from the maximum value of each bar. Therefore, looking at the hypothesis, the red line must always be above the blue line in this case the fact occurs that the time it takes _YOUR SOLUTION_ less than _MY SOLUTION_, but in two points these lines cross and change places, i.e. blue goes above the red . Because in _MY SOLUTION_ there have been two crash in trial 6° and 13° for this no time has been recorded. Therefore they are not important to note and hypothesis occurs.

![image](https://user-images.githubusercontent.com/80394968/170829711-571d7449-8fe0-4698-9eec-f3d3207394b7.png)

Separate view:

![image](https://user-images.githubusercontent.com/80394968/170830265-7499f386-f797-42fe-a0f5-6f44a7250bf1.png)

According to the analysis done on [horizontal Bar chart](https://it.mathworks.com/help/matlab/ref/barh.html) to compare the number of times that robot choose the wrong way and had to change the way. Again, as you can see in the chart, the numbers regarding  _MY SOLUTION_  are greater than _YOUR SOLUTION_ so for this reason robot takes more time to do a complete turn.

![image](https://user-images.githubusercontent.com/80394968/170830314-9424f7f4-d92b-4430-a0d0-19249fb20c93.png)

Third analysis done on [Pie chart](https://it.mathworks.com/help/matlab/ref/pie.html) to understand percentage of success between the two programs. In _YOUR SOLUTION_ there were no cases of crash instead in _MY SOLUTION_ there were two crash.

![image](https://user-images.githubusercontent.com/80394968/170830526-6418dfb7-4be7-4593-abd4-d57bbb552c0c.png)

For analysis the tolerance in the final time loop and to make [T student test](https://it.mathworks.com/help/stats/ttest.html) to verify hypotheses I calculated [mean](https://it.mathworks.com/help/matlab/ref/mean.html), [median](https://it.mathworks.com/help/matlab/ref/median.html) and [standard deviation](https://it.mathworks.com/help/matlab/ref/std.html).

![image](https://user-images.githubusercontent.com/80394968/170831129-9b5f95d9-f3f0-48b4-bc03-c5df5c419323.png)

Fourth analysis done on plot Time and plot the maximum and minimum tolerance band with standard deviation obtaining upper and lower standard deviation. In order to better understand more less how long it takes. As you can see in the plot below the area between two lines in the case of _MY SOLUTION_ is less than the area included in _YOUR SOLUTION_, this means that it takes Robot to make a complete turn in _MY SOLUTION_ more accurate than _YOUR SOLUTION_, that is mean my values are closer than yours. This fact can also be understood from std_1 and std_2 that std_2 __<__ std_1.

![image](https://user-images.githubusercontent.com/80394968/170830789-460ad082-9db2-419c-9837-dca0900e33eb.png)

last step do a T student Test with level of confidence Alpha = 0.05
```  
%hypothesis H0 : Time_1 > Time_2
%hypothesis H1 : Time_1 < Time_2 
```  



