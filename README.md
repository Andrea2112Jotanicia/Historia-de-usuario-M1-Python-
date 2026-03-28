
# Week 1
# Daily Sales System

## Overview
This project is a command-line based sales management system developed in Python. Its primary purpose is to allow users to register multiple sales, validate input data, process collected information, and generate a summarized report of total sales and income.

The system is designed with modular functions that handle user interaction, data validation, computation, and output formatting.

---

## Project Structure

The application is organized into a single main file containing multiple functions, each responsible for a specific task within the system:

- User interface display
- Data input and validation
- Sales registration
- Data processing
- Summary reporting
- Program flow control

---

## Execution Flow

### 1. Application Initialization
The program starts by executing the `main()` function. This serves as the entry point and coordinates the entire workflow of the system.

---

### 2. Welcome Interface
A welcome message is displayed to the user through a dedicated function. This improves user experience and clearly indicates the start of the program.

---

### 3. Sales Registration Loop
The system enters a loop where users can continuously register sales. This loop continues until the user decides to stop.

Each iteration performs the following steps:

#### a. Data Input
The user is prompted to enter:
- Product name
- Unit price
- Quantity sold

#### b. Data Validation
Each input is validated using specialized functions:
- Text validation ensures only alphabetic input for product names.
- Float validation ensures correct decimal values for prices.
- Integer validation ensures whole numbers for quantities.

Validation is enforced using loops and exception handling to guarantee correct data types.

#### c. Data Storage
Each sale is stored as a dictionary containing:
- Product name
- Price
- Quantity

All sales are accumulated in a list for further processing.

---

### 4. Continuation Control
After each sale registration, the system asks the user whether they want to continue.

This is handled through a control function that:
- Accepts only valid responses
- Determines whether the loop continues or terminates

---

### 5. Sales Calculation
Once data entry is complete, the system processes the collected data:

- Calculates total income by multiplying price and quantity for each sale
- Aggregates total quantity sold per product using a dictionary

This step separates computation logic from input handling, improving code organization.

---

### 6. Summary Report
The system generates a summary that includes:
- Total quantity sold for each product
- Overall income from all sales

The output is formatted for readability and presented in the console.

---

## Key Concepts Implemented

- Modular programming using functions
- Input validation with loops and exception handling
- Use of lists and dictionaries for data storage
- Control flow using `while` loops and conditional statements
- Separation of concerns (input, processing, output)
- Basic data aggregation techniques

---

## How to Run

1. Ensure Python is installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Execute the script using the Python interpreter.

---

## Purpose of the Project

This project demonstrates fundamental programming concepts in Python, including:
- Structured program design
- Robust user input handling
- Data processing and aggregation
- Interactive console applications

It is suitable for beginners learning how to build complete, functional programs with clean logic and user interaction.
---
# Week 2
# Inventory Management System

## Overview
This project is a command-line based Inventory Management System developed in Python. It allows users to manage a collection of products through an interactive menu, providing functionality to add items, display stored data, and compute basic inventory statistics.

The system is designed using modular programming principles, ensuring clear separation between validation, business logic, and user interaction.

---

## Core Architecture

The application is structured into three main components:

1. Input Validation Layer
2. Inventory Operations
3. User Interface and Control Flow

Each component is implemented through dedicated functions to maintain readability and scalability.

---

## Execution Workflow

### 1. Program Entry Point
The application starts by executing the `main()` function. This function initializes the inventory as an empty list and controls the main execution loop.

---

### 2. Interactive Menu System
A menu is displayed continuously, allowing the user to select different operations. The program remains active until the user explicitly chooses to terminate execution.

The menu acts as a dispatcher, routing the selected option to the corresponding function.

---

### 3. Input Validation Layer

All user inputs are validated before being processed. This ensures data integrity and prevents runtime errors.

- **String Validation**: Ensures that text inputs contain only alphabetic characters and spaces.
- **Float Validation**: Ensures that numeric inputs for prices are valid decimal numbers.
- **Integer Validation**: Ensures that quantity values are valid integers.

Validation is implemented using loops and exception handling, forcing correct input before proceeding.

---

### 4. Product Registration Process

When the user selects the option to add a product:

- The system requests product attributes (name, price, quantity).
- Each input is validated using the corresponding validation function.
- A product is represented as a dictionary containing its attributes.
- The product is appended to the inventory list.

This approach allows dynamic growth of the inventory.

---

### 5. Inventory Visualization

The system can display all stored products:

- If the inventory is empty, a message is shown indicating the absence of data.
- Otherwise, each product is iterated and displayed with its attributes.

This functionality provides a direct view of the current system state.

---

### 6. Statistical Computation

The system calculates aggregate metrics based on the stored inventory:

- Total inventory value is computed by summing the product of price and quantity for each item.
- Total quantity of items is calculated by summing all stored quantities.

These calculations are performed using iteration over the inventory list, demonstrating basic data aggregation techniques.

---

### 7. Control Flow Management

The application uses a loop controlled by a boolean flag:

- The loop continues running while the system is active.
- Conditional statements (`if/elif/else`) determine which operation to execute based on user input.
- Selecting the exit option updates the control flag and terminates the loop.

---

## Data Structures Used

- **List**: Stores all products dynamically.
- **Dictionary**: Represents each product with key-value pairs for attributes.

This combination enables flexible and structured data handling.

---

## Programming Concepts Applied

- Modular programming with functions
- Input validation using loops and exception handling
- Conditional logic for decision making
- Iterative structures (`while` and `for` loops)
- Data aggregation techniques
- Separation of concerns

---

## Execution Instructions

1. Ensure Python is installed in the environment.
2. Open a terminal or command interface.
3. Navigate to the directory containing the script.
4. Execute the program using the Python interpreter.

---

## Project Purpose

This project demonstrates fundamental programming practices in Python focused on:

- Building interactive console applications
- Managing structured data using lists and dictionaries
- Implementing robust input validation
- Applying control flow and modular design

It serves as a foundational example for understanding how small-scale management systems are structured and executed.
---

---

# Week 3
# Inventory Management System (CSV Persistence)

## Overview

This project implements a modular inventory management system in Python. It provides full CRUD (Create, Read, Update, Delete) operations, statistical analysis, and persistent storage using CSV files. The system is designed with separation of concerns, ensuring maintainability, scalability, and clarity.

The application is structured into three main modules (`app.py`, `servicios.py`, `archivos.py`) and a persistent data file (`inventario.csv`).

---

## System Architecture

### 1. `app.py` (Main Application Layer)

This is the entry point of the system. It is responsible for:

* Managing user interaction through a console-based menu
* Validating user input
* Coordinating calls to service and file modules
* Maintaining the execution loop until termination
* Triggering automatic persistence after data modifications
* Loading persisted data at startup

---

### 2. `servicios.py` (Business Logic Layer)

This module encapsulates all inventory-related operations:

* Product creation and storage
* Inventory visualization
* Product search functionality
* Update and deletion operations
* Statistical calculations

The inventory is represented as a list of dictionaries, where each dictionary corresponds to a product with predefined attributes.

---

### 3. `archivos.py` (Persistence Layer)

This module handles all file operations related to CSV persistence:

* Writing inventory data to a CSV file
* Automatically saving changes after modifications
* Loading data from an existing CSV file
* Validating file structure and content
* Handling exceptions related to file access and data integrity

---

### 4. `inventario.csv` (Data Storage)

This file acts as the persistent storage mechanism:

* Stores all inventory records
* Uses a structured CSV format with headers
* Allows data to persist across multiple executions
* Ensures compatibility with standard data tools

---

## Execution Flow

### Step 1: Application Startup

* The program initializes the inventory structure.
* It attempts to load existing data from the CSV file.
* If the file does not exist or is empty, the system starts with an empty inventory.

---

### Step 2: Menu Display

* The system presents a menu with multiple options.
* The user selects an operation by entering a numeric value.
* Input validation ensures only valid options are processed.

---

### Step 3: Operation Handling

Depending on the selected option, the system performs:

* **Create**: Adds a new product to the inventory
* **Read**: Displays all stored products
* **Search**: Locates a product by its identifier
* **Update**: Modifies existing product attributes
* **Delete**: Removes a product from the inventory
* **Statistics**: Computes aggregated metrics from the inventory
* **Save (Manual)**: Exports current data to a specified CSV file
* **Load**: Imports data from a CSV file with validation and merge/overwrite logic

---

### Step 4: Automatic Persistence

* After any modification (create, update, delete, or load), the system automatically updates the CSV file.
* This ensures that the stored data always reflects the current state of the inventory.

---

### Step 5: Data Validation

The system enforces strict validation rules:

* Text fields must contain valid strings
* Numeric fields must be valid numbers and non-negative
* CSV structure must match the expected schema
* Invalid records are safely ignored during loading

---

### Step 6: Error Handling

Robust error handling is implemented using exception management:

* File access issues are captured and reported
* Data conversion errors are handled gracefully
* The system prevents crashes and always returns control to the menu

---

### Step 7: Program Termination

* The system runs continuously within a controlled loop
* Execution ends only when the user selects the exit option
* All data remains محفوظ in the CSV file due to automatic persistence

---

## Key Design Principles

* **Modularity**: Each module has a single responsibility
* **Separation of Concerns**: UI, logic, and persistence are isolated
* **Data Integrity**: Validation ensures consistent data structure
* **Fault Tolerance**: Errors do not interrupt execution
* **Persistence**: Data is retained between sessions
* **Scalability**: The structure allows easy extension

---

## Conclusion

This project demonstrates how to build a structured and persistent inventory system using Python fundamentals. By combining modular design, file handling, and data validation, it achieves a robust solution suitable for academic and practical applications.