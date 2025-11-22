# Hotel Management System (Python) 

A simple, console based Hotel Management System in Python. This project demonstrates the use of fundamental programming concepts like Loops, If-Else statements and Data Structures such as Dictionaries,Lists,Tuples to manage hotel operations
##  Features

1.  **Hotel Configuration:**
    * 5 Floors with 15 rooms each (Total 75 rooms).
    * Specific room types per floor (e.g- 1st Floor: 1 Bed Non-AC, 5th Floor: 2 Bed AC).
2.  **Room Status Logging:**
    * Track **Full vs. Empty** rooms.
    * Track **Clean vs. Dirty** rooms.
3.  **Check-In System:**
    * Guests can only check into rooms that are both **Empty** and **Clean**.
    * Collects guest details (Name, Phone, Address).
4.  **Check-Out & Billing:**
    * Calculates bill based on **Room Type Price × Days Stayed**.
    * **Automatic Dirty Status:** Upon checkout, the room is automatically marked as "Dirty".
5.  **Housekeeping:**
    * Manual process to clean "Dirty" rooms so they become available for booking again.

## Technical Details

This project was built with python basics
* **No External Libraries:** Runs on standard Python.
* **Data Structures Used:**
    * `Dictionary`: To store room data (Status, Guest Info) and Prices.
    * `List`: To handle logic for available and dirty rooms.
    * `Tuple`: For immutable data like Floor configurations.

##  Pricing Structure (Configured in Code)

* **1 Bedded Non-AC:** 1000/day
* **1 Bedded AC:** 2000/day
* **3 Bedded AC:** 4500/day
* **2 Bedded Non-AC:** 2500/day
* **2 Bedded AC:** 3500/day

##  Future Improvements

* Will Add a GUI using Tkinter.
