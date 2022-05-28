# Assignment-Research Track 2 (statistic analysis)

Introduction
================================

Statistical analysis between two solutions; _YOUR SOLUTION_ (created by Prof. Recchiuto) and _MY SOLUTION_ (created by me). Analysis is based on 15 different mapping modes that basically Roboto has to find the silver tokens and take it. There are 7 silver tokens across the map. The time it takes Robot to make a complete turn is collected in a matrix to compare between two solutions; over time I took into account, colision number, wrong way number and if there was crash during mission. The purpose of the analysis is to compare two solutions through the data collected above, inside a matrix and making different analyzes such as analyzing in Bar chart, Pie chart, level of accuracy through standard deviation and T student test to verify hypotheses.

Hypothesis
================================

Assumption considered that _YOUR SOLUTION_ has less time than _MY SOLUTION_, but _MY SOLUTION_ has more accurate time compare to _YOUR SOLUTION_. The following hypotheses can be verified through various analyzes

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

According to the analysis done and [horizontal Bar chart](https://it.mathworks.com/help/matlab/ref/barh.html) to compare the number of times that robot choose the wrong way and had to change the way. Again, as you can see in the chart, the numbers regarding  _MY SOLUTION_  are greater than y _YOUR SOLUTION_ so for this reason robot takes more time to do a complete turn.

![image](https://user-images.githubusercontent.com/80394968/170830314-9424f7f4-d92b-4430-a0d0-19249fb20c93.png)

Third analysis done and [Pie chart](https://it.mathworks.com/help/matlab/ref/pie.html) to understand percentage of success between the two programs. In _YOUR SOLUTION_ there were no cases of crash instead in _MY SOLUTION_ there were two crash.

![image](https://user-images.githubusercontent.com/80394968/170830526-6418dfb7-4be7-4593-abd4-d57bbb552c0c.png)

Media_1 =

  195.4313


Median_1 =

  194.3900


Std_1 =

   17.3881


Min_1 =

  171.3000


Max_1 =

  241.5900


Media_2 =

  198.7877


Median_2 =

  199.6000


Std_2 =

   14.2053


Min_2 =

  172.0600


Max_2 =

  222.1200

![image](https://user-images.githubusercontent.com/80394968/170830789-460ad082-9db2-419c-9837-dca0900e33eb.png)




