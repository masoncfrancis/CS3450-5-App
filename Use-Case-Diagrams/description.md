## **Name:** LogIn
**Participating Actor(s):** Person (may be Customer, Manager, or Employee)

**Entry Condition:**
- Person has account
- Person has computer with internet access

**Exit Condition:**
- Person is logged into their account

**Event Flow:**
1. Person navigates to site
2. Person enters credentials
3. App checks credentials against database, requiring person to try again if their credentials don't match
4. App fetches data related to account and displays the person's account view

**Exceptional Cases:**
- TimeOut
- ServerDown

## **Name:** ReserveCar
**Participating Actor(s):** Customer

**Entry Condition:** 
- Customer is logged in
- Customer has enough money for the reservation

**Exit Condition:**
- Customer has reservation

**Event Flow:**
- Customer searches for cars, limiting search by availability and/or price range
- Customer selects one they want
- Customer pays for reservation, optionally adding insurance
- Database is updated to reflect car's unavailability over the reserved time window
- Customer is sent order number / confirmation code

**Exceptional Cases:**
- Cancel

## **Name:** PickUpReservedCar
**Participating Actor(s):** Customer, Employee

**Entry Condition:**
- Customer is at business location
- Customer has confirmation code
- Employee is logged in

**Exit Condition:**
- Customer leaves with car

**Event Flow:**
1. Customer asks to pick up their car
2. Employee verifies customer's reservation via confirmation code
3. Employee clicks button (or however else we implement this) to tell the app that the car has been picked up
4. Customer leaves with car

**Exceptional Cases:**
- WrongConfirmationCode

## **Name:** ReturnCar
**Participating Actor(s):** Customer, Employee

**Entry Condition:**
- Customer has car
- Customer is at business location
- Employee is logged in

**Exit Condition:**
- Business has car back

**Event Flow:**
1. Customer tells employee they're back to return the car
2. Employee does quick inspection of car
3. Employee clicks button to tell the app that the car has been returned
4. App updates car's availability
5. Customer leaves, without the car

**Exceptional Cases:**
- CarDamaged

## **Name:** ReclaimCar
**Participating Actor(s):** Employee

**Entry Condition:**
- Car is checked out
- Employee is logged in

**Exit Condition:**
- Car is checked back in

**Event Flow:**
1. Car is reported stolen or is overdue
2. Employee clicks button to LoJack the car
3. Employee (same or other) goes to retrieve LoJacked car
4. Car is returned to business location
5. Employee clicks button to indicate car is checked back in and available to rent/reserve

**Exceptional Cases:**
- LoJackFail
- CantLocateCar

## **Name:** FileComplaint
**Participating Actor(s):** Customer or Employee (Person)

**Entry Condition:**
- Person is logged in

**Exit Condition:**
- Complaint sent to Manager

**Event Flow:**
1. Person clicks button to file a complaint
2. Person writes their complaint
3. Person clicks "Submit"
4. Complaint is saved in the database to be dealt with by Manager

**Exceptional Cases:**
- Cancel

## **Name:** HandleComplaint
**Participating Actor(s):** Manager, Person (Customer or Employee / "Complainer")

**Entry Condition:**
- Manager is logged in
- There are complaints to deal with

**Exit Condition:**
- Complaint is marked as resolved

**Event Flow:**
1. Manager selects a complaint to handle
2. Manager sends a response and (ideally) does something in the real world to address the complaint (i.e. reprimanding a rude employee, improving the quality of the service, ensuring the cars are cleaned better, etc.)
3. Person sees reply and marks complaint as resolved
4. Complaint is removed from the database

**Exceptional Cases:**
- StillUnsatisfied

## **Name:** PayEmployees
**Participating Actor(s):** Manager

**Entry Condition:**
- Manager is logged in
- Manager has money
- Employee(s) have hours for which they haven't been paid

**Exit Condition:**
- Employees have been paid

**Event Flow:**
1. Manager sees they owe employees for hours worked
2. Manager selects "pay" and chooses amount calculated by system
3. Manager authorizes payment
4. Employees are notified they have been paid

**Exceptional Cases:**
- RefusePayment

