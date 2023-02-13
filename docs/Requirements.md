# Glossary
[Intro And Context](#intro-and-context)  
[Users and their goals](#users-and-their-goals)  
[Requirements](#requirements)  
[Future Features](#future-features)
# Intro and Context
This is the requirements for a car rental application. It has customers, employees, managers, and uses provides a economy of things. Money is added arbitrarily and the cars don't really exist.

# <a name="userGoals"></a>Users and their goals
### Managers
A manager's job is to manage(preform CRUD operations on) employees, cars, and pay employees

### Employees
A employee's job is to interact with the vehicle and customer to provide rentals to customers. They also want to sell insurance.

### Customer
A customers goals is to rent a car.

# Requirements
## Functional Requirements
### Permissions
- Manager can manage employees/cars 
- Employees can checkout cars
- Users can place rental order on cars
- Users cannot manage data except their own
- Employees cannot create/destroy data
- Users can add money to their balance
- software must have input for employee hours

### Vehicles
- Cars must have available dates
- Cars can be lojacked by employee
- Cars cannot be double rented
- Cars show available dates
- Cars can be returned early or late

### Managers
- Manage users, examples include firing, creating new employees, paying employees
- Manage cars, CRUD operations on all vehicles
- Can act as employee if necessary


### Employees
- Rent a car to a customer
- Return a car from a customer
- Lojack stolen vehicles
- Verify rental information
- Verify return
- Retrieve lojacked vehicles
- Must be able to add insurance to rental

### Customer
- Can view cars
- Can rent cars
- Can add insurance to rental
- Can submit car breakdown for pickup
- Can submit complaints
## Non Functional Requirements
- Users are able to login
- Has a functional database
- Has a consistent theme and is easy to use
- Simple checkout flow
- Works on many browsers
- Doesn't get 'hung up' in places that would interrupt a user experience
- Customers cannot access employee things



# Future Features

## Functional

### Employee 
- Time Tracker
- Shows where car is on google maps
- Gives directions to car
### Customer
- Customer can submit application for job
- Shows location picker on google maps
- Insurance tiers

### Manager
- UI for editing database models outside of django admin
- Images can be uploaded instead of selected from

## Non functional
- Website is hosted on the internet




