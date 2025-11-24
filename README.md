# Hotel Management System (Console-Based)

##  Overview of the Project
This is a robust, console-based **Hotel Management System** developed in Python. It is designed to simulate the day-to-day operations of a hotel with 5 floors and 75 rooms. The system streamlines room allocation, guest management, billing, and housekeeping operations without requiring complex databases or external libraries.

The project demonstrates efficient use of Python's core data structures (Dictionaries, Tuples, Loops) to manage real-time data states such as room occupancy (Full/Empty) and cleanliness (Clean/Dirty).

##  Features
* **Hotel Status Log:** View a real-time summary of total occupied, empty, clean, and dirty rooms.
* **Smart Check-In:**
    * Automatic validation to ensure guests are only assigned rooms that are **Empty AND Clean**.
    * Input validation for **Guest Name** (prevents numbers) and **Phone Number** (ensures 10 digits).
* **Check-Out & Billing:**
    * Calculates total bill based on room type rates and duration of stay.
    * **Automatic Status Update:** Upon checkout, the room is automatically marked as **"Dirty"** and cannot be re-booked until cleaned.
* **Housekeeping Module:** A dedicated function to mark specific "Dirty" rooms as "Clean" to make them available for new guests.
* **Room Search:** Retrieve details of a specific room, including guest info, rate, and current condition.
* **Floor Configuration:**
    * **1st Floor:** 1 Bedded Non-AC
    * **2nd Floor:** 1 Bedded AC
    * **3rd Floor:** 3 Bedded AC
    * **4th Floor:** 2 Bedded Non-AC
    * **5th Floor:** 2 Bedded AC

##  Technologies/Tools Used
* **Language:** Python 3.x
* **Core Concepts:** Dictionary Mapping, Nested Loops, Error Handling (`try-except`), Input Validation.
* **IDE:** Compatible with VS Code, PyCharm, IDLE, or any standard terminal.
* **No External Libraries:** Runs on standard Python.

##  Steps to Install & Run the Project
1.  **Prerequisites:** Ensure you have Python installed on your computer. You can verify this by typing `python --version` in your terminal.
2.  **Download:** Save the python script (e.g., `hotel_manager.py`) to a folder on your computer.
3.  **Run:** Open your terminal or command prompt, navigate to the folder, and run:
    ```bash
    python hotel_manager.py
    ```

##  Instructions for Testing
Follow this workflow to verify the logic of the system:

1.  **View Status:** Select Option `1`. You should see 75 Empty rooms and 75 Clean rooms initially.
2.  **Test Check-In (Validation):**
    * Select Option `2`. Choose Floor `1`.
    * Select Room `101`.
    * Try entering numbers in the Name field (System should reject it).
    * Try entering a 5-digit phone number (System should reject it).
    * Enter valid details to complete check-in.
3.  **Test Check-Out & Billing:**
    * Select Option `3`. Enter Room `101`.
    * Enter `2` days. The system should calculate the bill (Rate x 2).
    * Confirm payment.
4.  **Test Housekeeping Logic:**
    * Try to Check-In to Room `101` again. The system should **not** list it as available because it is "Dirty".
    * Select Option `4` (Housekeeping).
    * Enter Room `101` to clean it.
    * Now, Room `101` should be available for booking again.

##  Screenshots
 * Main Dashboard
<img width="529" height="256" alt="Image" src="https://github.com/user-attachments/assets/45e99682-a403-48f1-9d71-b95de00fd143" />

 * Status Log
   
<img width="724" height="421" alt="Image" src="https://github.com/user-attachments/assets/eb4ba504-5f51-4df5-b90b-69c49cf2ad1a" />

 * Check-in

<img width="1160" height="570" alt="Image" src="https://github.com/user-attachments/assets/a770b1ae-7db9-469d-bd7e-6ee019f31042" />

* Check-out

<img width="644" height="528" alt="Image" src="https://github.com/user-attachments/assets/cab2603b-3eca-4a32-9289-b80b86e4d365" />

* House keeping 

<img width="583" height="312" alt="Image" src="https://github.com/user-attachments/assets/5d5b6fa4-cfae-4ea8-8c7d-564865276c5b" />

* Search Room

<img width="644" height="464" alt="Image" src="https://github.com/user-attachments/assets/c5d5eea0-2c12-4614-89b6-ceffb6d59b57" />





