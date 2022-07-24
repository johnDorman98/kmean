<a id="toc"></a>
# Table of contents
 1. [Introduction](#introduction)
 2. [Features](#features)
 3. [Installation](#installation)
 4. [Usage](#usage)
 5. [License](#license)
 6. [Author](#author)

<a id="introduction"></a>
## Welcome to my kmeans program. 👋 
This is a project where I implemented my own kmeans algorithm to cluster data based on the number of clusters desired by the user and run for a user-defined number of iterations.

---

<a name="features"></a>
## Features 
* It asks the user to choose which csv file they wish to read.
* Let the user define the number of iterations and clusters for the algorithm.
* Plots the clusters in different colors along with their final centroid.
* prints off various data based on the data within each cluster.

---

<a name="installation"></a>
## Installation 
* In order for this program to work, you will need two main things. The first is Python installed on your computer, and the second is an IDE to run the program.
* Below is a link that will take you through the setup and installation for Python.
  
    [Python installation link](https://medium.com/co-learning-lounge/how-to-download-install-python-on-windows-2021-44a707994013)

* Now that you have confirmed that Python is installed and working, we can download the program and run it. In order to download the zip file for the program, you can click on the download button below.

    [Download Project](https://github.com/johnDorman98/kmeans/archive/refs/heads/main.zip)

* In this case, you can choose to extract it where you wish to. Once it has been extracted, open the folder and you will see a file named "kmeans.py" and various csv files. Extract all of this to a new folder where you can find it.

---

<a name="usage"></a>
## Usage  
* Because this project is more involved, we will be installing an IDE to run the program and also to download our imports. We will run the code from this IDE and the one we will use for this example is VSCode. However, you are welcome to use any IDE that works with Python.
* I will share a link to a guide by Visual Studio Code on how to install VSCode.
    
    [Link for VSCode installation](https://code.visualstudio.com/docs/setup/windows)

* The next step is to get VSCode setup for Python, so below is a guide also by Visual Studio Code on how to get it setup.

    [Link for Python setup with VSCode](https://code.visualstudio.com/docs/python/python-tutorial)

* Once you have VSCode installed and setup, we can move onto the next steps on how to get the program running.
  * You should be greeted with a screen similar to the one below.
    ![VSCode opened](https://user-images.githubusercontent.com/98963869/180655219-337d8971-e921-4ea5-898c-3d17d8c0235a.png)
  
  * Click on open folder and navigate to the new folder you created, which should only have the extracted files within, as shown below. However, inside of the zipped folder, you can also simply extract the folder named kmeans-main and open that.
    ![Folder example](https://user-images.githubusercontent.com/98963869/180655370-383db6ee-dce1-43b0-bd74-c9b67016738e.png)

  * Now that you have selected the new folder, you should have a screen similar to the one below.
    ![File open in VSCode](https://user-images.githubusercontent.com/98963869/180655540-9e35d536-f4b2-4668-8337-08ef3769b5cc.png)

  * The next step is to use them to install the imports so that the program is able to run correctly. So you want to double click on kmeans.py. It will then open it and next click on ***Terminal*** at the top of the VSCode and then on ***New Terminal***. This should open a terminal window on the bottom prompting you for an input. Type in `pip install python-math`.
  * Once that has finished installing the maths module, you can then install the next required module by typing in `pip install -U matplotlib`.
  * Now everything we need to run the program is installed. The next step is to run the program by pressing on the run button as shown below.
    ![Run python file](https://user-images.githubusercontent.com/98963869/180655888-33e48714-b23a-4661-9f2e-597c9bc16bd7.png)

* You will now be promted in the terminal for various inputs, which will then plot the clusters and centroids based on the number of clusters and iterations you have selected. At the end, once you have entered all of the required inputs, you will be given a display such as the one below.
    ![kmeans display](https://user-images.githubusercontent.com/98963869/180656030-bf7d9c9f-b84c-45ad-aaee-d08a03602db2.png)


---

<a name="license"></a>
## License 

Distributed under the GNU General Public License v3.0. See `LICENSE.txt` for more information.

---

<a name="author"></a>
## Author 

🖥️ **John Dorman**

* Github: [@johnDorman98](https://github.com/johnDorman98)

---

## Show your support

Give a ⭐️ if this project helped you!

[Back to the top of the page](#table-of-contents)
