hotel = {}

#Defining room types per floor using Tuple
floor_types = (
    "Unknown", 
    "1 Bedded Non-AC", # on 1st Floor 
    "1 Bedded AC",     # on 2nd Floor 
    "3 Bedded AC",     # on 3rd Floor 
    "2 Bedded Non-AC", # on 4th Floor 
    "2 Bedded AC"      # on 5th Floor
)

#Prices per day for each room type 
room_prices = {
    "1 Bedded Non-AC": 1000,
    "1 Bedded AC": 2000,
    "3 Bedded AC": 4500,
    "2 Bedded Non-AC": 2500,
    "2 Bedded AC": 3500
}

#using loops for room no. on each floor
for floor in range(1, 6):
    for r in range(1, 16):
        room_num = (floor * 100) + r
        r_type = floor_types[floor]
        
        # to know weather room is clean or dirty
        hotel[room_num] = {
            "type": r_type,
            "status": "Empty",       
            "cleanliness": "Clean",  
            "guest": {}              
        }

# function for knowing checkin/checkout status

def view_stats():
    print("\n--- HOTEL STATUS LOG ---")
    total_rooms = 75
    occupied_count = 0
    empty_count = 0
    dirty_count = 0
    clean_count = 0

    for room_num in hotel:
        details = hotel[room_num]
        if details["status"] == "Occupied":
            occupied_count += 1
        else:
            empty_count += 1
            
        if details["cleanliness"] == "Dirty":
            dirty_count += 1
        else:
            clean_count += 1

    print(f"Total Rooms: {total_rooms}")
    print(f"1. Full Rooms:  {occupied_count}")
    print(f"2. Empty Rooms: {empty_count}")
    print("------------------------")
    print(f"3. Clean Rooms: {clean_count}")
    print(f"4. Dirty Rooms: {dirty_count}")
    print("------------------------")

def check_in():
    print("\n--- CHECK-IN NEW GUEST ---")
    # Display rates for information
    print("Rates per day:")
    for r_type, price in room_prices.items():
        print(f"  - {r_type}: Rs. {price}")

    try:
        pref_floor = int(input("\nEnter preferred floor (1-5): "))
        if pref_floor < 1 or pref_floor > 5:
            print("Invalid floor number.")
            return
    except ValueError:
        print("Please enter a number.")
        return

    available_rooms = []
    start_id = pref_floor * 100
    end_id = start_id + 16

    for r_num in range(start_id + 1, end_id):
        #To give room to new guest, room must be empty AND clean
        if hotel[r_num]["status"] == "Empty" and hotel[r_num]["cleanliness"] == "Clean":
            available_rooms.append(r_num)

    if len(available_rooms) == 0:
        print("No clean rooms available on this floor.")
    else:
        print(f"Available Rooms: {available_rooms}")
        try:
            room_choice = int(input("Select Room Number: "))
            if room_choice in available_rooms:
                
                # --- Name validation ---
                while True:
                    name = input("Enter Guest Name: ").strip()
                    #To check if any character in the name is a digit
                    if not any(char.isdigit() for char in name):
                        break
                    else:
                        print("Error: Name cannot contain numbers. Please re-enter.")

                # --- Phone number validation ---
                while True:
                    phone = input("Enter Phone Number (10+ digits): ").strip()
                    # Check if all characters are digits and the length is = 10
                    if phone.isdigit() and len(phone) == 10:
                        break
                    else:
                        print("Error: Phone number must be 10 digits and contain only numbers. Please re-enter.")
                
                address = input("Enter Address: ")
                
                hotel[room_choice]["status"] = "Occupied"
                hotel[room_choice]["guest"] = {
                    "name": name, 
                    "phone": phone, 
                    "address": address
                }
                print(f"Check-in successful for {name} in Room {room_choice}.")
            else:
                print("Invalid room selection.")
        except ValueError:
            print("Invalid input.")

def check_out():
    print("\n--- CHECK-OUT & BILLING ---")
    try:
        room_num = int(input("Enter Room Number to checkout: "))
        
        if room_num in hotel:
            room_data = hotel[room_num]
            
            if room_data["status"] == "Occupied":
                guest_name = room_data['guest']['name']
                r_type = room_data['type']
                
                print(f"\nChecking out: {guest_name}")
                print(f"Room Type: {r_type}")
                
                # --- BILL CALCULATION ---
                try:
                    days = int(input("Enter number of days stayed: "))
                    if days < 1:
                        days = 1 # Minimum 1 day charge
                    
                    rate = room_prices[r_type]
                    total_bill = rate * days
                    
                    print("-----------------------------")
                    print(f"Rate per day:  Rs. {rate}")
                    print(f"Days Stayed:   {days}")
                    print(f"TOTAL BILL:    Rs. {total_bill}")
                    print("-----------------------------")
                    
                    confirm = input("Confirm Payment and Checkout? (yes or no): ")
                    if confirm.lower() == 'yes':
                        # Update Room Status
                        hotel[room_num]["status"] = "Empty"
                        hotel[room_num]["cleanliness"] = "Dirty" # Marked dirty
                        hotel[room_num]["guest"] = {} 
                        print("Checkout Complete. Room marked as DIRTY.")
                    else:
                        print("Checkout cancelled.")
                        
                except ValueError:
                    print("Invalid number of days entered.")
            else:
                print("This room is already empty.")
        else:
            print("Room does not exist.")
    except ValueError:
        print("Invalid input.")

def housekeeping():
    print("\n--- HOUSEKEEPING ---")
    dirty_rooms = []
    for r_num in hotel:
        if hotel[r_num]["cleanliness"] == "Dirty":
            dirty_rooms.append(r_num)
            
    if not dirty_rooms:
        print("All rooms are clean!")
        return

    print(f"Dirty Rooms: {dirty_rooms}")
    try:
        room_to_clean = int(input("Enter Room Number to clean: "))
        if room_to_clean in dirty_rooms:
            hotel[room_to_clean]["cleanliness"] = "Clean"
            print(f"Room {room_to_clean} is now CLEAN.")
        else:
            print("Room is not in the dirty list.")
    except ValueError:
        print("Invalid input.")

def guest_details():
    print("\n--- ROOM DETAILS ---")
    try:
        room_num = int(input("Enter Room Number: "))
        if room_num in hotel:
            room = hotel[room_num]
            print(f"\n[Room {room_num}]")
            print(f"Type: {room['type']}")
            print(f"Rate: Rs. {room_prices[room['type']]}/day")
            print(f"Status: {room['status']}")
            print(f"Condition: {room['cleanliness']}")
            
            if room['status'] == "Occupied":
                print(f"Guest: {room['guest']['name']}")
                print(f"Phone: {room['guest']['phone']}")
        else:
            print("Room not found.")
    except ValueError:
        print("Invalid number.")

# --- MAin function loop ---
def main():
    while True:
        print("\n=== HOTEL MANAGEMENT SYSTEM ===")
        print("1 = View Status Log")
        print("2 = Check-In")
        print("3 = Check-Out (Calculate Bill)")
        print("4 = Housekeeping")
        print("5 = Search Room")
        print("6 = Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            view_stats()
        elif choice == '2':
            check_in()
        elif choice == '3':
            check_out()
        elif choice == '4':
            housekeeping()
        elif choice == '5':
            guest_details()
        elif choice == '6':
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
