# Project Plan

## Summary

In this project we will be creating a website for a mock company called _Dan's Rentals_. It will be a website that allows the owner (Dan) to manage his customers and employees, as well as manage the company's service: renting cars. 

There will be 3 levels of access to running or using the website, the owner, the employees, and the customers. The owner may provide service to customers, pay employees, and promote customers to employee status (or in reverse, demote back to a customer). Employees may provide services to customers, while customers can only request services. 

Obvious data that must be kept track of in this website are user accounts, balances, and inventory (as well as their associated availability status).

## Team Organization

We will be using Jira as our primary tool for organizing tasks that need to be done during a sprint and tracking progress. For questions that come up, we will also create different channels within our Discord group to organize our communication with each other. Also, every sprint we will switch who is SCRUM master. We will also have a designated SCRUM meeting scribe.

## Software Development Process

The software development process our group will be using will be the one we discussed in lecture:

#### Requirements Gathering

During this step we identify who the customer is, record the requirements they ask for, ask clarifying and detailed questions so all requirements are unknown (draw out requirements from the customer that they initially didn't think of), and identify use cases. For this project, we heard the requirements from Dan Watson during lecture and were given the opportunity to ask him any questions.

#### High-Level Design
              
This is the step where we will plan all the major components of our website, namely the database, models and views, the user interface, and the theme. Broadly speaking, it will be the step when we plan how we want the user to interact with our website.
              
#### Low-Level Design
          
The underlying structure of our website, whether it be functions, classes, html, or other pieces of code, will be the low-level design for this project.       

#### Development
          
This is where we will implement and write all of our code.

#### Testing
          
To ensure our website is fully functioning and can be demonstrated to our customer, we will need to make sure we test our website thoroughly. This includes designing and implementing unit tests, system tests, and regression tests to make sure every part of our website works. We also will need to allow time for finding bugs in our code if any of our tests fail.

#### Deployment
            
For our project this step will mainly be allowing others to use our website as though it is a fully functioning company/service. Since it's not a real service, we won't have to worry about database servers, continued support, and ongoing bug fixes.

#### Maintenance

This step is an ongoing process of dealing with bugs and changes to any languages or frameworks our code uses.    

#### Wrap-Up

Here we will discuss as a team what went right and wrong, as well as any takeaways we have from the project.

## Communication Policies

We will be having SCRUM stand-up meetings every Monday and Wednesday at 6 p.m. on Discord unless additional meeting time is needed or someone becomes unavailable during those times. Although we will be primarily using Discord for communication, we will also be using Jira for time management, listing and assigning tasks that need to be done during sprints, and easy creation of burn-down charts.  

## Risk Analysis

* An incorrect initial django setup could cause a lot of problems later on during code implementation. To avoid this problem, we will want to make sure over high-level design step in our software development process is well-thought-out.
* Being overambitious with what we want to do with our website could prevent us from meeting deadlines. We will try to keep things as simple as possible to avoid this risk.
* Insufficient planning and communication could cause wasted time or code conflicts. Strict adherence to our github rules and consistent meetings will help avoid this.
* A bad user interface (UI) could make the customer (the professor) unhappy. To avoid this from happening we will leave plenty of time for implementing our theme and design.
 
## (Reference to README.md)

Here's the reference to [README](../README.md) for the configuration management plan.