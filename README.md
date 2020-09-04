# John Deere Golf Course Boundary - Beginner Project
This project is divided up into several sections. Each section is independent of each other.
In addition, this is not a tutorial. The project contains several problems so that you can practice your skills before working on the main project. I've listed some helpful links below, but you are encourged to explore other resources. 

While the project is geared towards Python, most of the sections can be completed in any language.

### General Resources
https://www.tutorialspoint.com/python/index.htm
https://www.w3schools.com/python/
https://towardsdatascience.com/a-beginners-guide-to-python-for-data-science-60ef022b7b67

### Section 1 - Python Environment Setup
#### Section References
https://www.tutorialspoint.com/python/python_environment.htm
https://www.python.org/downloads/
https://www.jetbrains.com/pycharm/
https://code.visualstudio.com/
https://www.spyder-ide.org/

The first thing you need to be able to do is run Python. There are many different ways to run Python, but if you don't already have a preference, we will run it on your local machine.

Coding in Python is as simple as editing a text file. Typically, we use an IDE (integrated development environment) to edit and run our Python scripts all in one place. There are many IDE's available for Python, but I would recommend Spyder, PyCharm, or VS Code. 

In order to make our code do something, we need a Python interpreter. You can download it from https://www.python.org/downloads/ If you choose to use Spyder, I believe the interpreter already comes installed.

Once you download an IDE and Python, it is time to run your first script. Try to run helloworld.py, which is shown in this repository. If you are unfamiliar with Github and aren't sure how to copy the file to your machine, you can simply create a new file on your machine called "helloworld.py" and copy the contents of the helloworld.py on Github into your script.

The output should be 
> Hello World!

### Section 2 - Installing Python Packages
#### Section References
https://realpython.com/what-is-pip/
https://pypi.org/project/requests/

Rather than writing it all yourself, you can use code other programmers wrote wrapped up in packages. "pip" is a package manager, which allows you to easily download other people's packages and incorporate it in your code. To test your ability to use pip, install the "requests" package using the instructions from the website pypi (https://pypi.org/project/requests/)

Now, you can test that requests is successfully install by running "runrequests.py". If it's working, you should get the response 
> Response returned: 200, OK

Now, you should be able to install any package you might find useful. Some that I think will be useful are
https://pypi.org/project/numpy/
https://pypi.org/project/matplotlib/
https://pypi.org/project/pandas/
https://pypi.org/project/Pillow/
https://pypi.org/project/opencv-python/

To finish this section, download at least one of the following packages and use it in your own Python program


### Section 3 - Basic Python
#### Section References
https://www.tutorialspoint.com/python/index.htm
https://www.w3schools.com/python/

There are so many resources to learn the basics of Python that I would highly recommend looking on your own to see what works best for you. I put some links to the resources that I used when learning Python. After you read through and learn the basics, I would recommend completing a simple project to put your skills to the test. Keep in mind, the point here is to learn Python.

> 1. Dice Rolling Simulator
> The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice. When the program runs, 
> it will randomly choose a number between 1 and 6. (Or whatever other integer you prefer — the number of sides on the die is up 
> to you.) The program will print what that number is. It should then ask you if you’d like to roll again. For this project, 
> you’ll need to set the min and max number that your dice can produce. For the average die, that means a minimum of 1 and a 
> maximum of 6. You’ll also want a function that randomly grabs a number within that range and prints it.