from __future__ import print_function

import time
from sr.robot import *

"""
Exercise 2 python script

Put the main code after the definition of the functions. The code should make the robot grab the closest marker (token)
Steps to be performed: - hint: use a while loop for the control of the robot
1 - call the function find_token() to retrieve the distance and the angle between the robot and the closest marker
2a - if no markers are detected, exit from the program.
2b - otherwise, drive the robot towards the marker. If the distance between the robot and the marker is less than d_th
     meters, the robot can grab the marker, by using the method grab() of the class Robot. Otherwise, the 
     robot should be driven toward the token. The robot is a non-holonomic robot, so you should control the 
     angle, by calling the method turn, if rot_y is greater then a_th or lower then -a_th (check the sign!).
     On the contrary, if -a_th < rot_y < a_th, you can use the method drive to move the robot forward.
3 - after you grab the marker, you can exit the program (function exit()).

   When done, run with:
	$ python run.py exercise2.py
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
     return silver_dist, silver_rot_y,

def find_token_golden():#function to find golden tokens:

    golden_dist=100 #Default distance of golden tokens
    
    #condition defined to find only golden tokens
    for token in R.see():
        if (token.dist < golden_dist ) &  (token.info.marker_type==MARKER_TOKEN_GOLD):
            golden_dist=token.dist
            golden_rot_y=token.rot_y
      
    if silver_dist==100:
     return -1, -1
    else:
     return golden_dist, golden_rot_y

#here goes the code
	
	
