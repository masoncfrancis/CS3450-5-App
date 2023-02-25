# Glossary
[Intro And Context](#intro-and-context)  
[Users and their goals](#users-and-their-goals)  
[Requirements](#requirements)  
[Future Features](#future-features)
# Intro and Context
This is the requirements document for a car rental application. It has different user types (manager, employees, and customers) and provides an economy of things. Money will be added arbitrarily by the manager to user's balances, and the vehicles that users are reserving won't really exist.

# <a name="userGoals"></a>Users and their goals
### Managers
A manager's job is to manage (preform CRUD operations on) employees, vehicles and their assigned reservations, and pay employees. They will also be able to manage complaints filed by customers.

### Employees
An employee's job is to manage active reservations (this includes lo-jacking vehicles and picking them). They can also be given the option to sell insurance. The customer for this website has also asked that employees be allowed to make reservations, so they will be able to have a personal balance and make reservations just like customers. 

### Customer
A customer's primary "goal" will be able to reserve vehicles, file complaints, and add to their balance.

# Requirements
## Functional Requirements
### Permissions
- A manager can pay and change the status of employees, and resolve filed complaints from customers
- Employees can reserve vehicles, lo-jack and pick up targeted vehicles, and submit an "hours worked" request to the manager to be paid
- Customers may only interact with their own balances and active reservations
- Employees cannot create/destroy data
- Users can add money to their balance

### Vehicles
- Cars must be able to display available dates
- Cars can be lo-jacked by an employee and picked up
- Cars cannot be double rented
- Cars can be returned early or late

### Manager
- Can manage all users (including firing/hiring and paying employees)
- Manage vehicles (CRUD operations on all vehicles)
- Can act as an employee (if necessary)


### Employees
- Can lo-jack vehicles and pick them up
- Verify a return
- Add insurance to a rental

### Customer
- Can view active reservations
- Can rent vehicles
- Can add insurance to rental
- Can submit car breakdown for pickup
- Can submit complaints

## Non Functional Requirements
- Users are able to log-in
- A functional database
- Website has a consistent theme and is easy to use
- Simple checkout flow
- Works on different browsers
- Doesn't get 'hung up' in places that would interrupt a user experience

# Future Features

## Functional

### Employee 
- "Time Tracker" for reservations
- Can see where a vehicle is on Google Maps

### Customer
- Customer can request to be an employee
- Insurance tiers

### Manager
- UI for editing database models outside of django admin
- Images can be uploaded instead of selected from

## Non functional
- Website is hosted on the internet




