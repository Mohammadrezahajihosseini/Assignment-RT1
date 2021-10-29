from __future__ import print_function

import time
from sr.robot import *

"""
Exercise 3 python script

We start from the solution of the exercise 2
Put the main code after the definition of the functions. The code should make the robot:
	- 1) find and grab the closest silver marker (token)
	- 2) move the marker on the right
	- 3) find and grab the closest golden marker (token)
	- 4) move the marker on the right
	- 5) start again from 1

The method see() of the class Robot returns an object whose attribute info.marker_type may be MARKER_TOKEN_GOLD or MARKER_TOKEN_SILVER,
depending of the type of marker (golden or silver). 
Modify the code of the exercise2 to make the robot:

1- retrieve the distance and the angle of the closest silver marker. If no silver marker is detected, the robot should rotate in order to find a marker.
2- drive the robot towards the marker and grab it
3- move the marker forward and on the right (when done, you can use the method release() of the class Robot in order to release the marker)
4- retrieve the distance and the angle of the closest golden marker. If no golden marker is detected, the robot should rotate in order to find a marker.
5- drive the robot towards the marker and grab it
6- move the marker forward and on the right (when done, you can use the method release() of the class Robot in order to release the marker)
7- start again from 1

	When done, run with:
	$ python run.py exercise3.py
"""


a_ths = 50
""" float: Threshold for the control of the orientation for silver box"""
a_thg = 20
""" float: Threshold for the control of the orientation for golden box"""
d_ths = 0.4
""" float: Threshold for the control of the linear distance for silver box"""
d_thg = 5.5
""" float: Threshold for control from the sides of golden box"""

R = Robot()
""" instance of the class Robot"""

def drive(speed, seconds):
    """
    Function for setting a linear velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
    

def find_token_silver():#function to find silver tokens 

    silver_dist=100 #Default distance of silver tokens
    
    #condition defined to find only silver tokens based on -120 < token.rot_y < 105 from the center of the robot
    for token in R.see():
        if  (token.dist < silver_dist ) &  (token.info.marker_type==MARKER_TOKEN_SILVER ) & (-120 < token.rot_y < 105):
            silver_dist=token.dist
            silver_rot_y=token.rot_y
            
    if silver_dist==100:
     return -1, -1
    else:
     return silver_dist, silver_rot_y

def find_token_golden():#function to find golden tokens:

    golden_dist=100 #Default distance of golden tokens
    
    #condition defined to find only golden tokens
    for token in R.see():
        if (token.dist < golden_dist ) &  (token.info.marker_type==MARKER_TOKEN_GOLD):
            golden_dist=token.dist
            golden_rot_y=token.rot_y
      
    if golden_dist==100:
     return -1, -1
    else:
     return golden_dist, golden_rot_y

while 1:
    silver_dist, silver_rot_y= find_token_silver() # we look for markers
    golden_dist, golden_rot_y= find_token_golden() 
    if silver_dist==-1:
        print("I don't see any silver token!!")
	exit()  #if no silver markers are detected, the program ends
    elif silver_dist <d_ths: 
        print("Found it!")
        R.grab() #if we are close to the silver token, we grab it.
        print("Gotcha")
        turn(30, 2)
        drive(20,2)
	R.release() #f we took silver token, move it and leave it behind
	drive(-20,2)
	turn(-30,2)
    if -a_ths<= silver_rot_y <= a_ths: # if the robot is well aligned with the silver token, we go forward
        print("right way, go.")
        drive(10, 0.5)
    elif silver_rot_y <= -a_ths: # if the robot is not well aligned with the  silver token, we move it on the left or on the right
        print("Left a bit...")
        turn(-25, 0.1)
    elif silver_rot_y >= a_ths:
        print("Right a bit...")
        turn(+25, 0.1)         
    if golden_rot_y >= d_thg:#if the robot is approaching from the sides to golden token we turn left or right
    	print ("I'm near to golden box a little right")
    	turn(-15,0.1)
    	drive(10,0.1)
    elif golden_rot_y <= -d_thg+0.4: 
        print("I'm near to golden box a little left")
        turn (15,0.1)
        drive(10,0.1)
    elif -a_thg<= golden_rot_y <= a_thg: #if the robot is oriented towards the golden token, we go back
        print("Ah, So near to Golden Box!!!!")
        drive(-10, 0.5)


