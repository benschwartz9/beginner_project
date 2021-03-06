
# Intermediate Project (11/8)

  

### Overview

(11/8 Update): The "Basics" section is done. More sections are to come

Most people are split up into specific subteams. Everyone should complete Basics as it contains information that is required by anyone who wants to work with images. In contrast to the beginner project, I've elected to add "homework" problems called tasks to demonstrate your understanding. Make sure to read the articles before you begin so you understand the task at hand. The results folder contains the output to what your code should do.

If you choose to complete this project as part of your participation for the class, then you will need to reach out to me to check your answer. You should already know if your solution is correct by comparing it to the images in the Results folder, but I won't count you as complete until we get a chance to talk. That way, I can clear up and questions and make sure you understand what you are doing. Remember, the goal is to learn! 

Feel free to reach out if you are stuck!

  

### Basics
First we are going to learn [how an image is stored on a computer](https://www.kdnuggets.com/2018/07/basic-image-data-analysis-numpy-opencv-p1.html)

This hopefully gives some good conceptual knowledge of the task at hand. But how do we access and modify these pixels? Like many things in Python, we can use a package to accomplish this. Much of Python programming is figuring out which packages to use and how to use them. For this project, we are going to simplify the process by recommending that you use OpenCV. However, we are not going to give the the exact webpages for how to use each method. This will be part of what you have to figure out. As a hint, I often use [this](https://opencv-python-tutroals.readthedocs.io/en/latest/#) website to learn more about how to use OpenCV. You are free to use google or any other resources, however.

One very helpful thing to know is that Numpy and OpenCV work very closely together. When you read in an image using `cv2.imread("filename")`, you the result is stored as a Numpy array. You should prove this to yourself by running the Python function`type(variable)` to see that the value returned from `imread` is a `<class 'numpy.ndarray'>`.

**Task 1**  
Using OpenCV, open up the file Purdue_Logo.jpg (in the images folder). First, we are going to get some information out of the picture. Print the following: 
- Dimensions/shape of the image
- Value of the pixel at (400, 400)
- Datatype of the image 
- Total number of pixels/size of the image

Let's look at what some of these values mean. If done correctly, the dimensions of the image should look something like (X, Y, Z). This might be surprising at first, why are there 3 dimensions to a 2d image? What exactly does this Z dimension hold and why is it 3? If you can't answer this question, you might want to [reread this article](https://www.kdnuggets.com/2018/07/basic-image-data-analysis-numpy-opencv-p1.html). 

The datatype of an image is especially important as it can be the source of many errors. In Python, the programmer does not typically need to think about how numbers are stored. Python takes care of that for you. However, Numpy arrays are much more specific on how they store their numbers, similiar to other languages like Java or C. I recommend you look up what the data type actually means. If you are getting errors, one common source of these problems is that you are using an incorrect data type, so this is something to keep an eye out for.

Now, we are going to do the most basic type of image transformation. Make a 20x20 red square in the bottom right corner of the image by directly changing the values of each pixel. (Hint: You shouldn't have to directly reference each pixel by hand). Save the changed image as Purdue_Logo_Result.jpg

**Task 2**  
While changing the value of each pixel allows us to modify images freely, it is a tedious process for applying filters to an image. Thankfully, OpenCV helps us out by simplifying these filters into a single method. I am going to increase the difficulty for this task by providing less resources, as I will continue to into the future. Still, it will be up to you to find the correct methods to complete this task. However, I will get you started on the right track. To complete this task, find a way to convert an image to grayscale. Then, use a threshold to keep the part of the image that you want.
[Here](https://en.wikipedia.org/wiki/Thresholding_(image_processing)) is a good place to get started on understanding what thresholding is. You will most like have to do further research to get a better understanding of what it does.

For Task 2, write a Python script which takes Purdue_Logo.jpg and outputs it as a binary file with the P (and TM) as 1's and the background as 0's. In addition, print the following statements:
- Shape of the original image (Purdue_Logo.jpg)
- Shape of the grayscaled image
- Shape of the final binary image
- Pixel value of the binary image at (10, 10)
- Pixel value of the binary image at (400, 400)


**Task 3**  
For the last task of the "basic" session, we are going to learn how to user OpenCV in order to blur and find the edges of an image. There are multiple ways to do this, and there is no perfect answer to this step. However, a general recommendation is to blur the image before trying to find its edges. Using Jet.jpg, you are going to output two images:
- Jet_Edges.jpg -> Shows the edges of the jet in white
- Jet_Blur.jpg -> A blurred image of the jet, used to achieve the image above. 
 
Compare your images to Jet_Blur.jpg and Jet_Edges.jpg in the Results folder to make sure that you are at least close (maybe even better) to my solution. While you don't have to be exact, you should be able to adjust the threshold values to achieve something very close. 
  

# Original Beginner Project

## John Deere Golf Course Boundary - Beginner Project

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

  

**--Update--**

Most APIs can be reached using the *requests* packages. Sometimes, other programmers will create an API wrapper, which is a Python package that does most of the heavy lifting when it comes to retrieving data through the API. Here is an example for USGS of a raw API being exposed (which would be accessed through *requests*) and a wrapper which simplifies the process for you.

Raw API - https://streamstats.usgs.gov/docs/streamstatsservices/#/

API Wrapper - https://mapbox.github.io/usgs/index.html#

  

If you choose to use Google Earth Engine, it is highly recommended that you use their wrapper instead of trying to make the requests package work.

  

To show another example of using requests to access data, I have uploaded the tool that my team built last year to access data from the NOAA API (NOAA_API_Example.py). The script does a bit more than just pull data from the API, but you can just ignore the other sections for this example.

  

### Section 5 - Images & Code

#### Section References

https://datacarpentry.org/image-processing/02-image-basics/

https://www.earthdatascience.org/courses/use-data-open-source-python/intro-raster-data-python/fundamentals-raster-data/intro-to-the-geotiff-file-format/

https://www.earthdatascience.org/courses/use-data-open-source-python/intro-raster-data-python/fundamentals-raster-data/

  

At this point we should shift our focus towards downloading the satellite imagery from one of our sources, so I'm going to pause the project here for now. However, sometimes it's helpful to understand what exactly you are trying to extract. To provide some reference, I'm going to share some links that explain images from a programming mindset as well as the types of files that you'll likely encounter along the way.

  

For those curious, here's a sneak peak of actually playing with the images in Python using OpenCV

https://pythonprogramming.net/loading-images-python-opencv-tutorial
