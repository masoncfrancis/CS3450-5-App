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
- ServerDown
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
- ServerDown

## **Name:** ReclaimCar
**Participating Actor(s):** 

**Entry Condition:**

**Exit Condition:**

**Event Flow:**

**Exceptional Cases:**

## **Name:** FileComplaint
**Participating Actor(s):** 

**Entry Condition:**

**Exit Condition:**

**Event Flow:**

**Exceptional Cases:**

## **Name:** PayEmployees
**Participating Actor(s):** 

**Entry Condition:**

**Exit Condition:**

**Event Flow:**

**Exceptional Cases:**

## **Name:**
**Participating Actor(s):** 

**Entry Condition:**

**Exit Condition:**

**Event Flow:**

**Exceptional Cases:**

