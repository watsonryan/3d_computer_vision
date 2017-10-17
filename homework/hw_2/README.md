# Homework Assignment 2
## Harris Corner Detector                                                                          
This directory contains a python implementation of the Harris corner detector.     
 
## How to run       

First, make the script excutable, by running the following line in terminal. 

````bash
chmod +x detect_corners.py
````

 Now, we can run the Harris corner detector over a test image. To excute the script, the only required input is the image path.      
 
 ````bash 
 ./detect_corners.py -i checkerboard.py 
 ````
 
To see a list of aditional options, you can run

 ````bash
 ./detect_corners.py -h
 ````
 
 By default, the script will run the following command, where the input image path is required.                                  

````bash
./detect_corners.py -o output.png -w 5 -k 4e-2 -t 10000
````
