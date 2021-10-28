# Assignment-Research Track 1 (Python Robotics Simulator)

Abstract 
================================

The concept of this assignment is to develop a Python-language code to simulate a robot circulating in a plant, in the meantime it has to pick up the silver tokens and put it behind it and if it encounters the golden tokens it has to avoid touching it and go back or change direction. According to this code, you have to understand how to use the medotics R. see (), R. grab (), R. release () and how to use find_token () to find out what kind of token is in front of robot.

Introduction
----------------------
This python simulator was already programmed by *Harry Cutts
Installing and running
The simulator requires a Python 2.7 installation, the [pygame](http://pygame.org/) library, [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).

Pygame, unfortunately, can be tricky (though [not impossible](http://askubuntu.com/q/312767)) to install in virtual environments. If you are using `pip`, you might try `pip install hg+https://bitbucket.org/pygame/pygame`, or you could use your operating system's package manager. Windows users could use [Portable Python](http://portablepython.com/). PyPyBox2D and PyYAML are more forgiving, and should install just fine using `pip` or `easy_install`.

## Troubleshooting

When running `python run.py <file>`, you may be presented with an error: `ImportError: No module named 'robot'`. This may be due to a conflict between sr.tools and sr.robot. To resolve, symlink simulator/sr/robot to the location of sr.tools.

On Ubuntu, this can be accomplished by:
* Find the location of srtools: `pip show sr.tools`
* Get the location. In my case this was `/usr/local/lib/python2.7/dist-packages`
* Create symlink: `ln -s path/to/simulator/sr/robot /usr/local/lib/python2.7/dist-packages/sr/`

## Exercise
-----------------------------

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

Robot API
---------
