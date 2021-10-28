# Assignment-Research Track 1 (Python Robotics Simulator)

Abstract 
================================

The concept of this assignment is to develop a Python-language code to simulate a robot circulating in a plant, in the meantime it has to pick up the silver tokens and put it behind it and if it encounters the golden tokens it has to avoid touching it and go back or change direction. According to this code, you have to understand how to use the medotics R. see (), R. grab (), R. release () and how to use find_token () to find out what kind of token is in front of robot.

Introduction
================================
This python simulator was already programmed by _Harry Cutts_ in 2017, here is reported in a sort of assignment for Reseach Track 1 course of the first year Robotic Engineering. Assignment is modified from the original model by prof. _Carmine Tommaso Recchiuto_ is compiled in python brought to linux in 3 formats by exercises. To compile assignment you only need to modify exercises 2 and 3 to get desired results.

Materials and Methods
=========================
Before compiling program you have to install it and running on the basic program explained in the part _Installing and running_ ,in case after installing there have been any problems before programming you can refer apart _Troubleshooting_ and for program execution you can see part _Execution_. An imporatnte challenge in this job is that robotic sensors can detect boxes around all directions (from -180.0 degrees to 180.0 degrees). So you have to develop a python code first to know the type of token, to do this two functions __def find_token_silver()__ and __def find_token_golden()0__ have been defined in code, which are in order to find the silver token and golden token. Methods and conditions have been defined within each function, one of which is the __R.see()__ method which is used within a __for()__ loop. R is going to say Robot() if it sees a token. and with another method which is __token.info.marker_type__ knows it type of token. Consequently I defined in a __while__ loop conditions by chance to meet silver token or golden token which to understand better I did a flwochart, and if you encounter silver token you have to grab it with the __grab()__ method and release it in the back if with the __release()__ method and continue to run in the plan without touching golden token and find more silver tokens.

Installing and running
----------------------
The simulator requires a Python 2.7 installation, the [pygame](http://pygame.org/) library, [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).

Pygame, unfortunately, can be tricky (though [not impossible](http://askubuntu.com/q/312767)) to install in virtual environments. If you are using `pip`, you might try `pip install hg+https://bitbucket.org/pygame/pygame`, or you could use your operating system's package manager. Windows users could use [Portable Python](http://portablepython.com/). PyPyBox2D and PyYAML are more forgiving, and should install just fine using `pip` or `easy_install`.

## Troubleshooting

When running `python run.py <file>`, you may be presented with an error: `ImportError: No module named 'robot'`. This may be due to a conflict between sr.tools and sr.robot. To resolve, symlink simulator/sr/robot to the location of sr.tools.

On Ubuntu, this can be accomplished by:
* Find the location of srtools: `pip show sr.tools`
* Get the location. In my case this was `/usr/local/lib/python2.7/dist-packages`
* Create symlink: `ln -s path/to/simulator/sr/robot /usr/local/lib/python2.7/dist-packages/sr/`

## Execution

To run one or more scripts in the simulator, use `run.py`, passing it the file names. 

I am proposing you three exercises, with an increasing level of difficulty.
The instruction for the three exercises can be found inside the .py files (exercise1.py, exercise2.py, exercise3.py).

When done, you can run the program with:

```bash
$ python run.py exercise1.py
```

You have also the solutions of the exercises (folder solutions)

```bash
$ python run.py solutions/exercise1_solution.py
```

Results
==============
The results obtained are brought in the form of images to understand better.

![Immagine](https://user-images.githubusercontent.com/80394968/139293917-306d8437-15b6-47ee-af65-8fac06ac4eec.png)
![Alt text](relative/path/to/img.jpg?raw=true "Title")
