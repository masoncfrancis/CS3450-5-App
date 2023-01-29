# Glossary
[Intro And Context](#intro-and-context)  
[Users and their goals](#users-and-their-goals)  
[Requirements](#requirements)  
[Future Features](#future-features)
# Intro and Context
This is the requirements for a car rental application. It has customers, employees, managers, and uses provides a economy of things. Money is added arbitrarily and the cars don't really exist.

# <a name="userGoals"></a>Users and their goals
### Managers
A manager's job is to manage employees, cars, and pay employess

### Employees
A employee's job is to interact with the vehicle and customer to provide rentals to customers. They also want to sell insurance.

### Customer
A customers goals is to rent a car.

# Requirements
## Functional Requirements
### Permissions
- manager can manage employees/cars 
- employees can checkout cars
- users can place rental order on cars
- users cannot manage data except their own
- employees cannot create/destroy data
- users can add money to their balance
- Software must have input for employee hours

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
- retrieve lojacked vehicles
- Must be able to add insurance to rental

### Customer
- can view cars
- can rent cars
- can add insurance to rental
- Can submit car breakdown for pickup
- can submit complaints
## Non Functional Requirments
- Users are able to login
- Has a functional database
- Has a consistent theme and is easy to use
- simple checkout flow
- works on many browsers
- Doesn't get 'hung up' in places that would interrupt a user expereince
- customers cannot access employee things



# Future Features

## Functional

### Employee 
- Time Tracker
- Shows where car is on google maps
- gives directions to car
### Customer
- customer can submit application for job
- shows location picker on google maps
- insurance tiers

### Manager
- UI for editing database models outside of django admin
- images can be uploaded instead of selected from

## Non functional
- Website is hosted on the internet




