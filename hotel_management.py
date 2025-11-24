hotel = {}

#Defining room types per floor using Tuple
floor_types = (
    "Unknown", 
    "1 bedded Non-AC", # on 1st Floor 
    "1 bedded AC",     # on 2nd Floor 
    "3 bedded AC",     # on 3rd Floor 
    "2 bedded Non-AC", # on 4th Floor 
    "2 bedded AC"      # on 5th Floor
)

#Prices per day for  room  
room_prices = {
    "1 bedded Non-AC": 1000,
    "1 bedded AC": 2000,
    "3 bedded AC": 4500,
    "2 bedded Non-AC": 2500,
    "2 bedded AC": 3500
}

# loops for room no. on each floor
for floor in range(1, 6):
    for r in range(1, 16):
        room_num = (floor * 100) + r
        r_type = floor_types[floor]
        
        # to know  room is clean or dirty
        hotel[room_num] = {
            "type": r_type,
            "status": "Empty",       
            "cleanliness": "Clean",  
            "guest": {}              
        }

#  for knowing checkin/checkout status

def view_stats():
    print("\n--- HOTEL STATUS LOG ---")
    totalrooms = 75
    occupiedcount = 0
    emptycount = 0
    dirtycount = 0
    cleancount = 0

    for room_num in hotel:
        details = hotel[room_num]
        if details["status"] == "Occupied":
            occupied_count += 1
        else:
            emptycount += 1
            
        if details["cleanliness"] == "Dirty":
            dirtycount += 1
        else:
            cleancount += 1

    print(f"Total Rooms: {totalrooms}")
    print(f"1. full Rooms:  {occupiedcount}")
    print(f"2. empty Rooms: {emptycount}")
    print("------------------------")
    print(f"3. clean Rooms: {cleancount}")
    print(f"4. dirty Rooms: {dirtycount}")
    print("------------------------")

def check_in():
    print("\n--- CHECK-IN  NEW GUEST ---")
    # Display rates for information
    print("Rates per day:")
    for r_type, price in room_prices.items():
        print(f"  - {r_type}: Rs. {price}")

    try:
        pref_floor = int(input("\nEnter preferred floor (1-5): "))
        if pref_floor < 1 or pref_floor > 5:
            print("invalid floor number.")
            return
    except ValueError:
        print("please enter a number.")
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
        print(f"available Rooms: {available_rooms}")
        try:
            room_choice = int(input("select room number: "))
            if room_choice in available_rooms:
                
                # --- Name validation ---
                while True:
                    name = input("enter guest name: ").strip()
                    #To check if any character in the name is a digit
                    if not any(char.isdigit() for char in name):
                        break
                    else:
                        print("Error: name can not contain numbers. please re-enter.")

                # --- Phone number validation ---
                while True:
                    phone = input("enter phone number (10+ digits): ").strip()
                    # Check if all characters are digits and the length is = 10
                    if phone.isdigit() and len(phone) == 10:
                        break
                    else:
                        print("error: phone number must be 10 digits and contain only numbers. please re-enter.")
                
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
    print("\n- chech-out & billing -")
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
                    
                    print()


                    print(f"Rate per day:  Rs. {rate}")
                    print(f"Days Stayed:   {days}")
                    print(f"TOTAL BILL:    Rs. {total_bill}")
                    print()
                    
                    confirm = input("Confirm Payment and Checkout? (yes or no): ")
                    if confirm.lower() == 'yes':
                        # Update Room Status
                        hotel[room_num]["status"] = "Empty"
                        hotel[room_num]["cleanliness"] = "Dirty" 
                        hotel[room_num]["guest"] = {} 
                        print("checkout complete. room marked as DIRTY.")
                    else:
                        print("checkout cancelled.")
                        
                except ValueError:
                    print("invalid number of days entered.")
            else:
                print("this room is already empty.")
        else:
            print("room does not exist.")
    except ValueError:
        print("invalid input.")

def housekeeping():
    print("\n- HOUSEKEEPING -")
    dirty_rooms = []
    for r_num in hotel:
        if hotel[r_num]["cleanliness"] == "Dirty":
            dirty_rooms.append(r_num)
            
    if not dirty_rooms:
        print("All rooms are clean")
        return

    print(f"Dirty Rooms: {dirty_rooms}")
    try:
        roomnumber_clean = int(input("Enter Room Number to clean: "))
        if roomnumber_clean in dirty_rooms:
            hotel[roomnumber_clean]["cleanliness"] = "Clean"
            print(f"Room {roomnumber_clean} is now CLEAN.")
        else:
            print("room is not in the dirty list.")
    except ValueError:
        print("invalid input.")

def guest_details():
    print("\n- room details -")
    try:
        room_num = int(input("enter Room Number: "))
        if room_num in hotel:
            room = hotel[room_num]
            print(f"\n[room {room_num}]")

            print(f"type: {room['type']}")


            print(f"rate: Rs. {room_prices[room['type']]}/day")
            print(f"status: {room['status']}")
            print(f"condition: {room['cleanliness']}")
            
            if room['status'] == "Occupied":
                print(f"Guest: {room['guest']['name']}")
                print(f"Phone: {room['guest']['phone']}")
        else:
            print("room not found.")
    except ValueError:
        print("invalid number.")

#  main function loop
def main():
    while True:
        print("\n= HOTEL MANAGEMENT SYSTEM =")

        print("1 = view status log")

        print("2 = check-in")


        print("3 = check-out (calculate bill)")
        print("4 = housekeeping")
        print("5 = search room")
        print("6 = exit")
        
        choice = input("enter choice: ")




        
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
