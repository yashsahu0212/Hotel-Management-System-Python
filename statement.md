# Hotel Management System

## Problem Statement
Manual management of hotel operations—such as tracking room availability, calculating bills, and monitoring room cleanliness—is prone to human error and inefficiency. Hotel staff often struggle to get a real-time view of which rooms are occupied, empty, or dirty. There is a need for a digital solution to automate these processes, ensuring accurate billing and smoother guest management.

## Scope of the project
The scope of this project is to develop a console-based Hotel Management System that manages the operational lifecycle of a guest's stay. 
* **Inventory Management:** The system manages a fixed inventory of **75 rooms** distributed across **5 floors**, with specific room types and pricing for each floor.
* **Operational Flow:** It covers the entire flow from guest Check-In to Check-Out.
* **Maintenance:** It includes a housekeeping module to track and update the hygiene status of rooms (Clean vs. Dirty) to prevent booking dirty rooms.
* **Data Persistence:** The current scope uses runtime memory to store data during the active session.

## Target users
1.  **Front Desk / Receptionists:** To check guests in, allocate rooms, and generate bills upon checkout.
2.  **Housekeeping Staff:** To view the list of dirty rooms and update their status to "Clean" once serviced.
3.  **Hotel Managers:** To view the "Status Log" for a high-level overview of occupancy rates and hotel efficiency.

## High-level features
* **Real-time Dashboard:** A status log displaying the count of Full, Empty, Clean, and Dirty rooms.
* **Smart Check-In:** * Allows selection of preferred floor.
    * Automatically filters and displays only rooms that are both "Empty" and "Clean."
    * Includes input validation for Guest Name (no numbers) and Phone Number (must be 10 digits).
* **Automated Billing System:** Calculates the total bill based on the specific room type's daily rate and the duration of the stay during Check-Out.
* **Housekeeping Management:** Automates the room condition cycle; rooms are automatically marked "Dirty" upon checkout and must be manually cleaned via the housekeeping menu before they can be re-booked.
* **Room Search:** Ability to look up specific room details to view current status, guest details, and room amenities.
