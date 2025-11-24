# Project Statement: Grand Hotel Management System

## 1. Problem Statement
Managing daily hotel operations using manual methods like paper registers or disconnected spreadsheets is inefficient and highly prone to human error. Hotels face critical challenges such as:
* **Room Status Confusion:** Accurately tracking which rooms are occupied, empty, or awaiting housekeeping in real-time across multiple floors.
* **Billing inaccuracies:** Manually calculating final bills that combine varying room tariffs, different stay durations, and additional room service charges often leads to miscalculations.
* **Operational Lag:** The delay in communication between the front desk and housekeeping regarding rooms that have vacated and need cleaning.

This project addresses these issues by providing a centralized, digital solution to automate room management, billing, and status tracking.

## 2. Scope of the Project
The Grand Hotel Management System is a desktop GUI application designed to manage the end-to-end guest lifecycle for a specific hotel configuration.

**IN SCOPE:**
* Managing a fixed inventory of **75 rooms spread across 5 floors**, with distinct room types (e.g., 1 Bed AC, 3 Bed AC) and associated pricing.
* **Visual Status Tracking:** Providing a color-coded, interactive map of all rooms indicating their real-time state (Available, Occupied, Dirty).
* **Guest Operations:** Handling Check-In with validation, recording guest details, and managing Check-Out processes.
* **Room Service Integration:** Allowing staff to add food and beverage orders to a guest's running tab.
* **Financials:** Automated calculation of the final bill including rent, room service, and tax, with the ability to generate and save text-based invoices.
* **Housekeeping Logic:** Enforcing a workflow where rooms automatically become "Dirty" after checkout and must be marked "Clean" before being rented again.

**OUT OF SCOPE:**
* Persistent data storage (database integration); data resets when the application closes.
* Online web booking or payment gateway integration.
* Multi-user role management (e.g., separate logins for admin vs. staff).

## 3. Target Users
* **Front Desk Receptionists:** To rapidly identify available rooms, register arriving guests, and process checkouts efficiently.
* **Hotel Managers:** To gain an immediate overview of the hotel's performance through real-time occupancy statistics and revenue totals on the dashboard.
* **Housekeeping Staff (via Front Desk):** To identify rooms marked as "Dirty" that require immediate cleaning to become rentable again.

## 4. High-Level Features
* **Interactive Visual Room Map:** A 5-floor grid view where rooms are color-coded buttons (Green=Ready, Red=Occupied, Orange=Dirty) allowing context-aware actions on click.
* **Real-time Executive Dashboard:** Displays key metrics (Total Revenue, Occupancy Count) and a live, scrollable table of currently active guests and their details.
* **Smart Billing Engine:** Automatically calculates total dues based on varying room rates, stay duration, and accumulated room service orders.
* **Invoice Generation:** Produces professional, itemized text-file invoices that can be saved locally for printing.
* **Integrated Room Service Menu:** Ability to select items from a predefined food menu and add costs directly to an occupied room's folio.
* **Input Validation:** Ensures data integrity by validating guest names (letters only) and phone numbers (digits only) during check-in.
