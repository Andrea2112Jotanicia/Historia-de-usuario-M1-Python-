# Inventory Management System

## Overview
This project is a modular inventory management system built in Python. It allows users to manage products, perform CRUD operations, and persist data using CSV files.

## Execution Flow

1. The program starts by initializing an empty inventory.
2. A control loop displays a menu continuously.
3. The user selects an option from the menu.
4. Based on the option:
   - Add product
   - Display inventory
   - Search product
   - Update product
   - Delete product
   - Generate statistics
   - Save data to CSV
   - Load data from CSV
5. The system processes the request using service and file modules.
6. The loop continues until the user selects the exit option.

## Architecture

- app.py → Main control flow and user interaction
- servicios.py → Business logic (CRUD + statistics)
- archivos.py → File handling (CSV persistence)

## Requirements

- Python 3.x

## How to Run

Run the main file:

```
python app.py
```
## EXPLANATION OF DESIGN DECISIONS

The system is divided into three modules to ensure separation of concerns:

1. Validation Methods:
- Used to ensure correct user input.
- Prevent runtime errors and enforce data integrity.

2. Service Methods (CRUD):
- Encapsulate business logic.
- Allow reuse and maintainability.

3. File Methods (CSV):
- Implement persistence.
- Use 'with' to ensure safe file handling.

4. Main Loop:
- Controls program execution.
- Uses a boolean flag instead of infinite loops for better control.

This design improves scalability, readability, and modularity.

