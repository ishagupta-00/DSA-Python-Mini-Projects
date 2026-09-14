# DSA Python Mini Projects

This repository contains 5 small Python projects made while learning **Python programming and basic DSA concepts**.

The purpose of making these projects was not just to write code, but to understand how different programming concepts work together in a complete program.

## Projects

1. ATM Simulation
2. Car Drive Simulation
3. Login System
4. Student Marks Analyzer
5. Number Analyzer

---

# 1. Starting With Python

Before understanding these projects, it is important to understand some basic Python concepts used in them.

Python is a programming language with simple and readable syntax. A Python program is made by writing instructions that tell the computer what to do.

For example:

```python
name = input("Enter your name: ")
print("Hello", name)
```

Here the program does two things:

* `input()` asks the user for information.
* The entered value is stored in `name`.
* `print()` displays the result.

So, the basic flow is:

```text
User gives input
       |
       v
Program processes the input
       |
       v
Program gives output
```

The same basic idea is used in all the projects in this repository.

---

# 2. Variables

A variable is a name used to store some value in a program.

For example:

```python
name = "Isha"
marks = 85
```

Here:

* `name` is a variable.
* `"Isha"` is the value stored in it.
* `marks` is another variable.
* `85` is its value.

We use variables because programs need to remember information while they are running.

### Example from the projects

In the Car Drive Simulation:

```python
speed = 50
fuel = 20
```

The program needs to remember the current speed and fuel, so these values are stored in variables.

---

# 3. Data Types

A data type tells Python what kind of value we are working with.

Some common types used in these projects are:

### String

Used for text.

```python
name = "Isha"
```

`name` contains a string.

Strings are used for things like:

* Student names
* Usernames
* Passwords
* Account holder names

### Integer

Used for whole numbers.

```python
age = 20
```

### Float

Used for numbers that can contain decimal values.

```python
marks = 85.5
balance = 2500.50
```

This is useful for:

* Marks
* Money
* Fuel
* Distance

### Boolean

A Boolean has only two values:

```python
True
False
```

For example, in the Car Drive Simulation:

```python
engine = False
```

This means the engine is currently OFF.

When the engine starts:

```python
engine = True
```

Now the engine is ON.

---

# 4. Input

`input()` is used when we want the user to enter something.

Example:

```python
name = input("Enter your name: ")
```

The program waits for the user to type something.

If the user enters:

```text
Isha
```

then `name` stores `"Isha"`.

### Important point

`input()` normally gives the entered value as a string.

For example:

```python
marks = input("Enter marks: ")
```

Even if the user enters `85`, Python initially treats it as text.

If we want to use it as a number, we need type conversion.

---

# 5. Type Conversion

Type conversion means changing a value from one data type to another.

For example:

```python
marks = int(input("Enter marks: "))
```

Here:

1. `input()` takes the value.
2. `int()` converts it into an integer.
3. The result is stored in `marks`.

Common conversions used in these projects:

* `int()` - converts a value into an integer.
* `float()` - converts a value into a decimal number.
* `str()` - converts a value into a string.

### Example

```python
amount = float(input("Enter amount: "))
```

`float()` is useful in the ATM project because an amount can contain decimal values.

---

# 6. Output

`print()` is used to display information on the screen.

Example:

```python
print("Hello", name)
```

The program can use `print()` to show:

* Results
* Error messages
* Menu options
* Account information
* Student marks
* Car status

---

# 7. Operators

Operators are symbols used to perform operations on values.

### Arithmetic operators

Some operators used in these projects are:

| Operator | Meaning        | Example  |
| -------- | -------------- | -------- |
| `+`      | Addition       | `10 + 5` |
| `-`      | Subtraction    | `10 - 5` |
| `*`      | Multiplication | `10 * 5` |
| `/`      | Division       | `10 / 5` |
| `%`      | Remainder      | `10 % 3` |

### Example

The Car Drive Simulation uses:

```text
Distance = Speed x Time
```

In Python:

```python
distance = speed * time
```

The Number Analyzer uses addition to calculate the total of numbers.

---

# 8. Modulus Operator

The `%` operator gives the remainder after division.

For example:

```python
10 % 2
```

The result is `0`.

This is useful for checking whether a number is even or odd.

```python
number % 2 == 0
```

If the remainder is `0`, the number is even.

Example:

```text
10 % 2 = 0  -> Even
15 % 2 = 1  -> Odd
```

This logic is used in the Number Analyzer.

---

# 9. Conditions

Conditions allow a program to make decisions.

For example:

```python
if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

The program checks the condition:

```text
Are marks greater than or equal to 50?
```

* If yes, it prints `Pass`.
* Otherwise, it prints `Fail`.

Conditions are used throughout these projects.

Examples:

* Checking whether the ATM balance is enough.
* Checking whether the engine is ON.
* Checking whether marks are valid.
* Checking whether the login details are correct.

---

# 10. if, elif and else

When there are multiple possible conditions, we can use `if`, `elif` and `else`.

Example from the Student Marks Analyzer:

```python
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
else:
    grade = "F"
```

Python checks the conditions from top to bottom.

The first condition that becomes true is used.

This is useful when there are multiple possibilities.

---

# 11. Loops

A loop is used when we want to repeat some instructions.

Two main loops are used in these projects:

* `for` loop
* `while` loop

---

# 12. For Loop

A `for` loop is generally used when we want to process items one by one.

Example:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

The loop works like this:

1. Take `10`.
2. Run the code.
3. Take `20`.
4. Run the code.
5. Take `30`.
6. Run the code.
7. Stop after all items are processed.

The same idea is used in the Student Marks Analyzer to process every student and in the Number Analyzer to process every number.

---

# 13. While Loop

A `while` loop keeps running as long as a condition is true.

Example:

```python
while attempts > 0:
    # login code
```

In the Login System, a `while` loop is useful because the user can try to login more than once.

It is also used when we need to keep asking the user for valid input.

For example, if a PIN is not 4 digits, the program can ask again.

---

# 14. Functions

A function is a block of code created for a particular task.

Example:

```python
def find_largest(numbers):
    # code
```

Here:

* `def` is used to create a function.
* `find_largest` is the function name.
* `numbers` is the input given to the function.

Functions are useful because a large program can be divided into smaller parts.

For example, instead of writing the complete ATM program in one place, different tasks are separated into functions:

* `create_account()`
* `login()`
* `deposit_money()`
* `withdraw_money()`
* `check_balance()`
* `change_pin()`

This makes the code easier to read and understand.

---

# 15. Parameters and Arguments

A function can receive information from outside.

Example:

```python
def find_largest(numbers):
```

Here, `numbers` is a parameter.

When we call:

```python
find_largest(my_numbers)
```

`my_numbers` is the argument passed to the function.

This allows the same function to work with different data.

---

# 16. Return

A function can send a result back using `return`.

Example:

```python
def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

The function calculates the sum and returns the result.

Then the returned value can be stored:

```python
total = calculate_sum(numbers)
```

This is used in the Number Analyzer and other projects.

---

# 17. Lists

A list is a data structure used to store multiple values together.

Example:

```python
numbers = [10, 20, 30, 40]
```

Instead of creating separate variables:

```python
number1 = 10
number2 = 20
number3 = 30
number4 = 40
```

we can store them together in one list.

Lists are useful in these projects for:

* Storing numbers.
* Storing students.
* Storing transactions.

---

# 18. List Indexing

Each item in a Python list has a position called an index.

Python starts indexing from `0`.

Example:

```python
numbers = [10, 20, 30]
```

The positions are:

```text
10 -> index 0
20 -> index 1
30 -> index 2
```

So:

```python
numbers[0]
```

gives:

```text
10
```

This is useful when we need to access a particular item.

---

# 19. append()

`append()` is used to add a new item to the end of a list.

Example:

```python
numbers = [10, 20]
numbers.append(30)
```

Now the list becomes:

```text
[10, 20, 30]
```

In the ATM project, `append()` is used to add new transactions to the transaction list.

In the Student Marks Analyzer, it is used to add each student to the student list.

---

# 20. len()

`len()` tells us how many items are present.

Example:

```python
numbers = [10, 20, 30]
```

```python
len(numbers)
```

gives:

```text
3
```

In the Student Marks Analyzer, `len()` helps calculate the number of students.

For example:

```text
Average = Total Marks / Number of Students
```

The number of students can be found using:

```python
len(students)
```

---

# 21. Dictionaries

A dictionary stores information using **key-value pairs**.

Example:

```python
student = {
    "name": "Isha",
    "marks": 85,
    "grade": "A"
}
```

Here:

* `"name"` is a key.
* `"Isha"` is its value.
* `"marks"` is a key.
* `85` is its value.
* `"grade"` is a key.
* `"A"` is its value.

A dictionary is useful when different pieces of information belong to the same object.

For example, a student has:

* Name
* Marks
* Grade

So we can store all of them together.

Dictionaries are also used for:

* ATM account information.
* Car information.
* Login information.

---

# 22. Accessing Dictionary Values

We can access a dictionary value using its key.

Example:

```python
student["marks"]
```

This gives:

```text
85
```

In the ATM project:

```python
data["balance"]
```

is used to access the current account balance.

---

# 23. List of Dictionaries

Sometimes we need to store many objects, where each object has different information.

For example, the Student Marks Analyzer has many students.

One student can be:

```python
{
    "name": "Isha",
    "marks": 85,
    "grade": "A"
}
```

Many students can be stored inside a list:

```python
students = [
    {
        "name": "Isha",
        "marks": 85,
        "grade": "A"
    },
    {
        "name": "Rahul",
        "marks": 72,
        "grade": "B"
    }
]
```

This combines two concepts:

* List -> stores multiple students.
* Dictionary -> stores information about one student.

---

# 24. Input Validation

Input validation means checking whether the information entered by the user is acceptable.

This is important because users can enter incorrect data.

Examples from these projects:

### ATM

* PIN must contain exactly 4 digits.
* Deposit cannot be negative.
* Withdrawal cannot be greater than balance.

### Student Marks Analyzer

* Marks must be between 0 and 100.
* Student name cannot be empty.

### Login System

* Username cannot be empty.
* Password must contain at least 4 characters.

### Car Simulation

* Acceleration must be positive.
* Fuel amount must be positive.
* Speed cannot go beyond the maximum limit.

Validation prevents invalid values from being used in the program.

---

# 25. try-except

Sometimes a program can get an unexpected input and produce an error.

For example:

```python
amount = float(input("Enter amount: "))
```

If the user enters:

```text
hello
```

Python cannot convert `"hello"` into a float.

This can cause a `ValueError`.

To handle this, we can use:

```python
try:
    amount = float(input("Enter amount: "))
except ValueError:
    print("Please enter a valid amount.")
```

This means:

* `try` contains the code that may produce an error.
* `except` handles the error.
* The program can show a proper message instead of stopping suddenly.

This is used in several projects for numeric input.

---

# 26. Menu-Driven Programming

A menu-driven program gives the user multiple choices.

For example, the ATM menu contains:

```text
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Mini Statement
5. Last Transaction
6. Change PIN
7. Account Details
8. Logout
```

The user enters a choice.

The program checks the choice using `if-elif-else` and calls the required function.

This type of structure is used in:

* ATM Simulation
* Car Drive Simulation

It makes the program easier for the user to operate.

---

# 27. File Handling

File handling means reading data from a file or writing data into a file.

Normally, variables lose their values when the program closes.

For example:

```python
balance = 5000
```

If the program closes, this variable no longer exists.

To keep data for later, we can save it in a file.

The ATM project uses a JSON file for this purpose.

---

# 28. JSON

JSON stands for **JavaScript Object Notation**.

It is a common format used for storing structured data.

The ATM project uses:

```text
atm_data.json
```

to store information such as:

* Account holder name
* Account number
* PIN
* Balance
* Transactions

Python provides the `json` module to work with JSON files.

The program can:

* Read existing data.
* Update the data.
* Save the updated data.

This means the ATM data can remain available even after the program is closed.

---

# 29. datetime

The ATM project uses Python's `datetime` module.

It is used to get the current date and time.

For example, when a transaction happens, the program stores its date and time.

A transaction can contain information like:

```text
Deposit
Amount: 500
Date: 14-09-2026 18:30:00
```

This makes the mini statement more useful.

---

# 30. Basic DSA Concepts

The projects in this repository are beginner-level projects, but they also use some basic DSA ideas.

## Data Structure

A data structure is a way of organizing and storing data so that it can be used efficiently.

The main data structures used here are:

* Lists
* Dictionaries

---

# 31. Traversal

Traversal means visiting elements one by one.

For example:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

The program visits:

```text
10
20
30
```

one by one.

Traversal is used in:

* Number Analyzer
* Student Marks Analyzer
* ATM transaction processing

---

# 32. Searching

Searching means checking data to find something we need.

For example, in the Number Analyzer we need to find the largest number.

Suppose:

```text
numbers = [10, 25, 15, 40, 20]
```

The program can do this:

1. Start with `10` as the largest.
2. Compare `25` with `10`.
3. `25` is larger, so largest becomes `25`.
4. Compare `15` with `25`.
5. `15` is smaller, so keep `25`.
6. Compare `40` with `25`.
7. `40` is larger, so largest becomes `40`.
8. Compare `20` with `40`.
9. `20` is smaller.
10. Final largest value is `40`.

This is a simple way of searching through a list.

---

# 33. Finding Minimum

The same idea can be used to find the smallest number.

Suppose:

```text
[10, 25, 15, 5, 20]
```

Steps:

1. Start with `10` as the smallest.
2. Compare `25`.
3. `25` is not smaller.
4. Compare `15`.
5. `15` is not smaller.
6. Compare `5`.
7. `5` is smaller, so update the smallest value.
8. Continue checking the remaining numbers.
9. Final smallest value is `5`.

---

# 34. Counting

Counting means keeping track of how many times something happens.

For example, the Number Analyzer counts even and odd numbers.

We start with:

```python
even_count = 0
odd_count = 0
```

Then every number is checked.

If the number is even:

```python
even_count += 1
```

If it is odd:

```python
odd_count += 1
```

At the end, we know how many even and odd numbers were entered.

---

# 35. Project 1 - ATM Simulation

**File:** `atm_simulation.py`

The ATM Simulation is a menu-driven program that behaves like a simple ATM.

## Main Features

* Account creation
* 4-digit PIN
* PIN confirmation
* Account number generation
* Login
* 3 login attempts
* Balance checking
* Deposit
* Withdrawal
* Mini statement
* Last transaction
* PIN change
* Account details
* Logout
* JSON data storage

## Account Creation

When no account is available, the program asks for:

* Account holder name
* 4-digit PIN
* PIN confirmation
* Initial deposit

The program validates the PIN before creating the account.

It also generates an account number and stores the account information.

## Login

The user enters the PIN.

The program compares the entered PIN with the stored PIN.

There are 3 attempts.

If the correct PIN is entered:

```text
Login successful
```

If all attempts are incorrect, access is blocked for that session.

## Deposit

Suppose the current balance is:

```text
Rs. 5000
```

and the user deposits:

```text
Rs. 1000
```

The program performs:

```text
5000 + 1000 = 6000
```

The new balance becomes:

```text
Rs. 6000
```

The transaction is also added to the transaction list.

## Withdrawal

Suppose:

```text
Balance = Rs. 6000
Withdrawal = Rs. 2000
```

The program checks whether:

```text
2000 <= 6000
```

Since enough balance is available:

```text
6000 - 2000 = 4000
```

The new balance becomes Rs. 4000.

If the requested amount is greater than the balance, the withdrawal is rejected.

## Mini Statement

Transactions are stored in a list.

The program displays the latest 5 transactions.

Each transaction contains:

* Type
* Amount
* Date and time

## Change PIN

The program first checks the current PIN.

Only after the current PIN is correct can the user create a new PIN.

The new PIN is also checked to make sure it contains exactly 4 digits.

---

# 36. ATM Algorithm

### Account Creation

1. Load existing data.
2. Check whether an account exists.
3. If no account exists, ask for account holder name.
4. Ask for a 4-digit PIN.
5. Check whether the PIN contains exactly 4 digits.
6. Ask the user to confirm the PIN.
7. Ask for the initial deposit.
8. Validate the deposit.
9. Generate an account number.
10. Store the account details.
11. Save the data in the JSON file.

### Login

1. Set the number of attempts to 3.
2. Ask for the PIN.
3. Compare it with the stored PIN.
4. If correct, allow access.
5. If incorrect, reduce the number of attempts.
6. Continue until login succeeds or attempts become 0.
7. Block access for the session if all attempts fail.

### Withdrawal

1. Take the withdrawal amount.
2. Check whether it is a valid number.
3. Check whether the amount is positive.
4. Compare the amount with the current balance.
5. If enough balance is available, subtract the amount.
6. Store the transaction.
7. Save the updated data.

---

# 37. Project 2 - Car Drive Simulation

**File:** `car_drive_simulation.py`

This project simulates some basic actions of a car.

The program keeps four main values:

```text
Speed
Distance
Fuel
Engine status
```

## Starting State

```text
Speed = 0 km/h
Distance = 0 km
Fuel = 20 litres
Engine = OFF
```

## Start Engine

If the engine is OFF, the program changes its value to ON.

If the engine is already ON, it tells the user that it is already running.

## Accelerate

The user enters an acceleration value.

The program:

1. Checks whether the engine is ON.
2. Checks whether fuel is available.
3. Takes the acceleration value.
4. Increases the speed.
5. Makes sure the speed does not go above 120 km/h.
6. Reduces a small amount of fuel.

## Brake

The user enters a braking value.

The program subtracts this value from the current speed.

If the speed becomes negative, it is set to 0.

A car cannot have negative speed.

## Drive

The user enters the driving time.

The program calculates distance using:

```text
Distance = Speed x Time
```

For example:

```text
Speed = 40 km/h
Time = 2 hours

Distance = 40 x 2
         = 80 km
```

Fuel is also reduced according to the distance travelled.

## Refuel

The user enters the amount of fuel to add.

The program:

* Checks that the amount is positive.
* Adds the fuel.
* Makes sure total fuel does not exceed 50 litres.

---

# 38. Car Simulation Algorithm

1. Create the car dictionary.
2. Set speed to 0.
3. Set distance to 0.
4. Set fuel to 20 litres.
5. Set engine to OFF.
6. Display the menu.
7. Take the user's choice.
8. Check whether the selected operation is allowed.
9. Update the car values.
10. Display the updated information.
11. Repeat until the user chooses Exit.

---

# 39. Project 3 - Login System

**File:** `login_system.py`

This project demonstrates the basic logic behind a login system.

The user first creates an account.

The program stores:

* Username
* Password

Then the user tries to login using those details.

## Account Creation

The program checks:

* Username should not be empty.
* Password should contain at least 4 characters.

After successful account creation, the user is asked to login.

## Login

The user enters:

* Username
* Password

The program compares both values with the stored information.

Both must match for successful login.

## Example

Stored information:

```text
Username = Isha
Password = python123
```

If the user enters:

```text
Username = Isha
Password = wrong
```

the login fails because the password does not match.

The program allows 3 attempts.

---

# 40. Login System Algorithm

1. Ask the user to create a username.
2. Check whether the username is empty.
3. Ask the user to create a password.
4. Check the password length.
5. Store both values in a dictionary.
6. Set login attempts to 3.
7. Ask for username and password.
8. Compare them with stored values.
9. If both match, login is successful.
10. Otherwise, decrease the attempt count.
11. Continue until login succeeds or attempts become 0.
12. Block login for the current session after all failed attempts.

---

# 41. Project 4 - Student Marks Analyzer

**File:** `student_marks_analyzer.py`

This project takes marks of multiple students and analyzes their basic performance.

## Information Stored

For each student, the program stores:

* Name
* Marks
* Grade

This information is stored using a dictionary.

Multiple student dictionaries are stored inside a list.

## Marks Validation

Marks must be between:

```text
0 and 100
```

If the user enters:

```text
105
```

the program does not accept it.

The user is asked to enter the marks again.

## Grade Calculation

The program checks the marks using conditions.

```text
90 - 100 -> A+
80 - 89  -> A
70 - 79  -> B
60 - 69  -> C
50 - 59  -> D
Below 50 -> F
```

## Pass/Fail

The program considers:

```text
Marks >= 50 -> Pass
Marks < 50  -> Fail
```

If marks are 80 or above, the program also displays:

```text
Keep it up! Great performance.
```

## Average

The program first calculates total marks.

Then:

```text
Average = Total Marks / Number of Students
```

For example:

```text
Marks = 80, 70, 90

Total = 80 + 70 + 90
      = 240

Average = 240 / 3
        = 80
```

## Highest Scorer

The program compares students one by one.

It starts with the first student as the highest scorer.

If another student has higher marks, that student becomes the new highest scorer.

This continues until all students have been checked.

---

# 42. Student Marks Algorithm

1. Ask for the number of students.
2. Create an empty student list.
3. Take the name of each student.
4. Validate that the name is not empty.
5. Take the marks.
6. Check that marks are between 0 and 100.
7. Calculate the grade.
8. Create a dictionary for the student.
9. Add the dictionary to the student list.
10. Calculate total marks.
11. Calculate average marks.
12. Compare student marks to find the highest scorer.
13. Display every student's result.
14. Display the class summary.

---

# 43. Project 5 - Number Analyzer

**File:** `number_analyzer.py`

The Number Analyzer takes multiple numbers from the user and performs different operations.

## Operations

* Sum
* Subtraction
* Average
* Largest number
* Smallest number
* Even count
* Odd count

## Storing Numbers

First, an empty list is created:

```python
numbers = []
```

Every number entered by the user is added using:

```python
numbers.append(number)
```

For example, if the user enters:

```text
10
20
15
5
```

the list becomes:

```text
[10, 20, 15, 5]
```

## Sum

The program starts with:

```python
total = 0
```

Then it visits every number and adds it.

```text
0 + 10 = 10
10 + 20 = 30
30 + 15 = 45
45 + 5 = 50
```

Final sum:

```text
50
```

## Subtraction

The program starts with the first number.

For:

```text
10, 20, 15, 5
```

it performs:

```text
10 - 20 - 15 - 5
```

The result is calculated step by step.

## Average

The program uses:

```text
Average = Sum / Number of Values
```

For:

```text
10, 20, 15, 5
```

```text
Sum = 50
Number of values = 4

Average = 50 / 4
        = 12.5
```

## Largest Number

The program starts with the first number as the largest.

Then it compares every other number with it.

This is a simple traversal and searching logic.

## Smallest Number

The same method is used for the smallest number.

## Even and Odd Count

Every number is checked using the modulus operator.

```python
number % 2 == 0
```

If the remainder is 0, `even_count` is increased.

Otherwise, `odd_count` is increased.

---

# 44. Number Analyzer Algorithm

1. Ask how many numbers the user wants to enter.
2. Create an empty list.
3. Take each number from the user.
4. Add every number to the list.
5. Calculate the sum by traversing the list.
6. Calculate subtraction.
7. Calculate the average.
8. Take the first number as the largest.
9. Compare every remaining number with the largest.
10. Update the largest when a bigger value is found.
11. Repeat the process to find the smallest value.
12. Check every number for even or odd.
13. Increase the correct counter.
14. Display all results.

---

# 45. Error Handling and Validation Used in Projects

The projects are designed to handle common incorrect inputs.

Examples:

### Invalid number

If the program expects:

```text
Enter marks:
```

and the user enters:

```text
abc
```

the program handles the error using `try-except`.

### Invalid marks

If the user enters:

```text
120
```

the Student Marks Analyzer rejects it because marks must be between 0 and 100.

### Invalid PIN

If the user enters:

```text
123
```

the ATM rejects it because the PIN must contain exactly 4 digits.

### Insufficient balance

If the user has:

```text
Balance = Rs. 1000
```

and tries to withdraw:

```text
Rs. 1500
```

the program rejects the withdrawal because the balance is not enough.

### Invalid car operation

The Car Drive Simulation checks conditions such as:

* Engine must be ON before driving.
* Fuel must be available.
* Speed cannot become negative.
* Fuel cannot exceed the tank capacity.

---

# 46. How the Concepts Connect

The important part of these projects is that concepts are not used separately. They work together.

For example, in the Student Marks Analyzer:

```text
Input
  |
  v
Variable
  |
  v
Validation
  |
  v
Dictionary
  |
  v
List
  |
  v
Loop
  |
  v
Condition
  |
  v
Calculation
  |
  v
Output
```

Similarly, the ATM project combines:

```text
Functions
    +
Dictionary
    +
List
    +
Conditions
    +
Loops
    +
File Handling
    +
JSON
    +
Exception Handling
```

This is how basic programming concepts come together to make a complete program.

---

# 47. How to Run the Projects

### Step 1

Install Python on the computer.

### Step 2

Open this repository in VS Code.

### Step 3

Open the project folder.

### Step 4

Select any `.py` file.

### Step 5

Run the file using the Run button or terminal.

For example:

```bash
python number_analyzer.py
```

Other projects can be run in the same way:

```bash
python atm_simulation.py
python car_drive_simulation.py
python login_system.py
python student_marks_analyzer.py
```

---

# 48. ATM Data File

The ATM project creates a local file named:

```text
atm_data.json
```

It is used to store:

* Account holder information
* Account number
* PIN
* Balance
* Transactions

The file is included in `.gitignore`.

This means the local test data file is not pushed to GitHub.

---

# 49. What I Practiced

While making these projects, I practiced:

### Python

* Variables
* Data types
* Input and output
* Type conversion
* Operators
* Conditions
* Loops
* Functions
* Lists
* Dictionaries
* String handling

### Problem Solving

* Input validation
* Searching
* Traversal
* Counting
* Calculations
* Menu-based logic
* Breaking a problem into smaller functions

### File and Data Handling

* File handling
* JSON
* Reading and writing data
* Date and time

### DSA Basics

* Lists
* Traversal
* Searching
* Counting
* Finding maximum and minimum values

### Development Tools

* VS Code
* Git
* GitHub

---

# 50. Future Improvements

These are beginner-level projects, so there are many things that can be improved later.

Some possible improvements are:

* Add a graphical user interface.
* Add database support.
* Improve login security.
* Add more ATM features.
* Add more car simulation features.
* Add more student analysis options.
* Add more DSA-based mini projects.
* Improve the overall user interface of the programs.

---

# Author

**Isha Gupta**

Python and DSA Practice Projects
