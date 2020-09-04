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

There are so many resources to learn the basics of Python that I would highly recommend looking on your own to see what works best for you. I put some links to the resources that I used when learning Python. After you read through and learn the basics, I would recommend completing a simple project to put your skills to the test. The point here is to learn Python, so don't feel limited to these two projects.

**1. Dice Rolling Simulator**
> Like the title suggests, this project involves writing a program that simulates rolling dice. When the program runs, 
> it will randomly choose a number between 1 and 6. (Or whatever other integer you prefer — the number of sides on the die is up 
> to you.) The program will print what that number is. It should then ask you if you’d like to roll again. For this project, 
> you’ll need to set the min and max number that your dice can produce. For the average die, that means a minimum of 1 and a 
> maximum of 6. You’ll also want a function that randomly grabs a number within that range and prints it.

**2. Guess the Number**
> Similar to the first project, this project also uses the random module in Python. The program will first randomly generate a 
> number unknown to the user. The user needs to guess what that number is. (In other words, the user needs to be able to input 
> information.) If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number 
> is too high or too low). If the user guesses correctly, a positive indication should appear. You’ll need functions to check if 
> the user input is an actual number, to see the difference between the inputted number and the randomly generated numbers, and 
> to then compare the numbers.

(Project ideas from https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/)

### Section 4 - API
#### Section References
https://www.dataquest.io/blog/python-api-tutorial/  
https://www.pythonforbeginners.com/scraping/scraping-wunderground  

APIs are most commonly used to send data between services. Because each API is set up differently, you'll have to rely heavily on documentation from the provider in order to use their API. When working with APIs, I always take this approach:
1. Pull **something** via the API (usually very simple request)
2. Pull something more specific towards the info you are trying to gather
3. Pull the data you really need

By slowly narrowing the scope, you are able to tell identify if an error is due to your usage of the API or lack of information in the space requested.

Relating back to our project, some APIs are done without using the "requests" package. Other programmers have created Python packages to specifically handle a certain API, and we can use these to reduce our workload. Try to pull any sort of data using one of the following APIs (these were included in Satellite Imagery 101).

Google Earth Engine API - https://developers.google.com/earth-engine/guides/python_install  
USGS API - https://mapbox.github.io/usgs/reference/api.html  
(NOTE: this requires an additional request for an API key before the service can be used) - https://gis.stackexchange.com/questions/300323/search-images-in-usgs-earth-explorer-using-python-api

### Section 5 - Images & Code
#### Section References
https://datacarpentry.org/image-processing/02-image-basics/   
https://www.earthdatascience.org/courses/use-data-open-source-python/intro-raster-data-python/fundamentals-raster-data/intro-to-the-geotiff-file-format/  
https://www.earthdatascience.org/courses/use-data-open-source-python/intro-raster-data-python/fundamentals-raster-data/  

At this point we should shift our focus towards downloading the satellite imagery from one of our sources, so I'm going to pause the project here for now. However, sometimes it's helpful to understand what exactly you are trying to extract. To provide some reference, I'm going to share some links that explain images from a programming mindset as well as the types of files that you'll likely encounter along the way.

For those curious, here's a sneak peak of actually playing with the images in Python using OpenCV
https://pythonprogramming.net/loading-images-python-opencv-tutorial/  