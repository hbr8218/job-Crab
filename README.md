# Job Crab
A job's portal scrapper

## Table of contents
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspects](#technical-aspects)
  * [Installation](#installation)
  * [Run](#run)
  * [To Do](#to-do)
  * [Bug Request](#bug-request)


## Overview
Job Crab is job portal scapper of a job portal website which works by taking user's given job's skill and location where he/she want to look on. It yeilds informations of the jobs with various job's attributes like job's title, location, salary, company name and ratings from first fifty web pages of the vary job portal website and saves all information in a csv file. 


![job_crab](https://user-images.githubusercontent.com/42790586/88427279-40c9ff80-ce10-11ea-9814-ccd98350cd59.gif)

## Motivation
I feel that it would be easier for students to compare amongst various jobs by just looking at the csv file and thus could apply for the jobs accordingly. Also, I being a Machine leaning Enthusiast, it is necessary for me to have the skill of web scapping so that as to build my own dataset for any machine learning project


## Technical Aspects
The project is divided into two parts:- <br />
1. Tracing Right div elements in the website.
2. Storing all informantion of jobs in a csv file.

## Installation
The code is written in python3. So if you don't have python3 installed on your system then do the followings:-

### For Linux(Ubuntu) and macOS users
- `sudo apt-get install python3`
- `sudo apt-get install python3-pip`
- `pip3 install virtualenv`
- In your project directory, excecute `virtualenv venv` where 'venv' is the name of your virtual environment for the project.
- Activate your virtual environment using `path/bin/activate`, where path should be absolute path of the virtual environment.
- Update ~/.bashrc using:- <br />
```echo "source `which activate.sh` "``` <br />
`source ~/.bashrc`
- create a .env file in the project's root directory and add the write the followings:- <br />
`source path/bin/activate` <br />
BASE_URI="ENTER_THE_URI_OF_WEBSITE"

  

### For Windows users:-
Above steps(for linux and macOS users) may not work for windows user so they can do the following steps:-
- Install python3 (Refer any good video and blogs)
- Install virtualenv and activate it (Refer any good video and blogs)
- Add environment variables:- <br />
BASE_URI="ENTER_THE_URI_OF_WEBSITE"


## Run
Run the following command to install all required libraries/dependencies:- <br />
`pip install -r requirements.txt` <br />
Finally, Execute `python app.py` to run the app.

## To Do
1. Include more job portal websites to be scrapped.
2. Option to download generated csv files.
3. API version of Job Crab.


## Bug Request
If you have any bug or suggestion regarding this project, just let me know @ _hbr8218@gmail.com_ .


