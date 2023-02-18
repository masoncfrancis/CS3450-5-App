# CS3450-5-App

This repo contains code for Dan's Car Barn, a rental car management software project for CS 3450.

The repository's name comes from the course name and group number. 

Directory names are written in lowercase according to their purpose. 
File names are written in camelCase according to the purpose they serve. 

## Version Control Procedures

Each user story should be associated with it's own branch. Changes will **never** be pushed to the main branch. 

In order to submit to the main branch, a Pull Request must be created. Approval from at least one 
person must be given for a Pull Request to be merged.

Branch names are related to the feature being developed and the person developing them.

Unit testing will be completed before submitting pull requests.

## Tool Stack

This project is written in Python, using a Django web server. The database backend will use SQLite. 
UI will be done in HTML using the Bootstrap 5 framework. 
All development will be done on team members' local machines, using 
code cloned from this GitHub repo. 

## Build Instructions

### Prerequisites

Python 3.8+ is required for this project. If Python is not installed on your computer, please follow 
[these instructions](https://wiki.python.org/moin/BeginnersGuide/Download) to download and install it. 

Specific Python packages are required to run this project. More details are found in the following section. 

### Instructions

Code for the project may be cloned or downloaded from this GitHub repo.

#### Create a Virtual Environment

Once the code has been downloaded or cloned to a folder, it is recommended (but not required) to create a Python virtual environment. If you decide not to, please skip to the 'Install Project Dependencies' section. 
Otherwise, continue following the instructions in this section. 

Open a terminal in the project folder and run this command (replacing `python3` with `python` as necessary for your installation):

```
python3 -m venv venv
```

Next, you will need to switch to the virtual environment. To activate the virtual environment on a UNIX style operating system (Linux, macOS, etc.), run this command:

```
source venv/bin/activate
```

To activate the virtual environment in Windows, run this command from the project folder root:

```
.\venv\Scripts\activate
```

You will need to have this virtual environment activated in order to run the code in this project. If your virtual environment ever becomes deactivated, you may run the above command for your 
applicable OS again from the project folder root. 

#### Install Project Dependencies

This project requires a few packages to run properly.

With your Python virtual environment activated (if you are using one), run the following command from the project folder root (replacing `python3` with `python` as necessary for your installation):

```
python3 -m pip install -r requirements.txt
```

The project's required dependencies are now installed.

#### Start the Django Server

To start the project server, run this command from the project folder root (replacing `python3` with `python` as necessary for your installation):

```
python3 manage.py runserver
```

#### More Important Information

A file named 'common.env' will be used to hold environment variables shells, the real .env will not be committed to GitHub for security reasons and will be filled out by each developer.

## Unit Testing Instructions

Unit testing will be carried out using Python's unittest. We will unit test the back end code. The front end will not be unit tested.

As a best practice, unit testing will be completed before submitting pull requests.

## System Testing Instructions

Andrew will make sure the project runs on macOS. Mason will make sure it runs on Linux. Jack and Caleb will make sure it runs on Windows. 

As a point of information, it is most important for this project to run correctly on Linux because a real-world webserver that will run this software would be Linux. 

## Miscellaneous Development Notes

N/A
