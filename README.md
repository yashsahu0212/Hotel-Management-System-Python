# Grand Hotel Management System (HMS)

## Overview of the Project
The **Grand Hotel Management System** is a modern, GUI-based desktop application designed to streamline daily hotel operations. It replaces traditional paper-based registers with an interactive digital dashboard.

The system manages a hotel configuration of **5 Floors and 75 Rooms**, handling the entire guest lifecycle from Check-In to Billing and Housekeeping. It utilizes a **Visual Room Map** to provide front-desk staff with real-time status updates (Occupied, Empty, or Dirty) at a glance.

## Features
* **Interactive Dashboard:** Real-time counters for Total Revenue, Occupancy Rates, and Dirty Rooms, along with a live table of current guests.
* **Visual Room Map:** A color-coded grid representing all 75 rooms:
    * 🟢 **Green:** Empty & Clean (Ready for booking)
    * 🔴 **Red:** Occupied (Guest inside)
    * 🟠 **Orange:** Dirty (Needs housekeeping)
* **Smart Billing System:** Automatically calculates rent based on room type and duration. It includes support for **Food & Beverage (Room Service)** charges.
* **Invoice Generation:** Generates professional text-based invoices (`.txt` files) that can be saved and printed.
* **Housekeeping Workflow:** Enforces a logic where rooms cannot be booked immediately after checkout until they are marked as "Cleaned".
* **Validation:** Prevents invalid inputs (e.g., entering letters in phone numbers).

##  Technologies & Tools Used
* **Programming Language:** Python 3.x
* **GUI Framework:** CustomTkinter (Modern UI wrapper for Tkinter)
* **Standard Libraries:** `datetime`, `tkinter.messagebox`
* **Data Structure:** Python Dictionaries (In-memory storage)

##  Steps to Install & Run
Follow these steps to set up the project on your local machine:

1.  **Install Python:** Ensure you have Python installed. You can check by running:
    ```bash
    python --version
    ```
2.  **Install Dependencies:** This project uses `customtkinter` for the modern interface. Install it using pip:
    ```bash
    pip install customtkinter
    ```
3.  **Download the Code:** Save the main python file (e.g., `hotel_app.py`) in a folder.
4.  **Run the Application:**
    ```bash
    python hotel_app.py
    ```

## Instructions for Testing
To verify the system works as expected, try this workflow:

1.  **Check-In a Guest:**
    * Go to **"Room Map"**.
    * Click on a **Green (Empty)** room (e.g., Room 101).
    * Enter a Guest Name and Phone Number. Click **"Confirm Check-In"**.
    * *Observation:* The button should turn **Red**.

2.  **Order Room Service:**
    * Click on the now **Red (Occupied)** Room 101.
    * Select "Lunch" from the dropdown and click **"Add Order"**.

3.  **Check-Out & Billing:**
    * Click on Room 101 again.
    * Click **"Generate Final Bill"**.
    * Enter `2` for number of days and press Enter.
    * Click **"Save/Print"** to see the text file invoice.
    * Click **"Mark Paid"**.
    * *Observation:* The button should turn **Orange**.

4.  **Housekeeping:**
    * Try to click the **Orange (Dirty)** Room 101.
    * The system will block check-in. Click **"Mark as Cleaned"**.
    * *Observation:* The button turns **Green** again.

## 📸 Screenshots
