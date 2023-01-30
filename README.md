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

A new project will be created using the command:

```
$ django-admin startproject mysite
```

Code for the project may be copied down from this GitHub repo.

A file named 'common.env' will be used to hold environment variables shells, the real .env will not be committed to GitHub for security reasons and will be filled out by each developer.

## Unit Testing Instructions

Unit testing will be carried out using Python's unittest. We will unit test the back end code. The front end will not be unit tested.

As a best practice, unit testing will be completed before submitting pull requests.

## System Testing Instructions

Andrew will make sure the project runs on macOS. Mason will make sure it runs on Linux. Jack and Caleb will make sure it runs on Windows. 

As a point of information, it is most important for this project to run correctly on Linux because a real-world webserver that will run this software would be Linux. 

## Miscellaneous Development Notes

N/A
