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


4. Main Loop:
- Controls program execution.
- Uses a boolean flag instead of infinite loops for better control.

This design improves scalability, readability, and modularity.

