import customtkinter as ctk
from tkinter import messagebox
import datetime
#  theme to Dark mode 
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# DATABASE & CONFIGURATION
hotel_db = {}

# prices of room types
room_prices = {
    "1 Bedded Non-AC": 1000,
    "1 Bedded AC": 2000,
    "3 Bedded AC": 4500,
    "2 Bedded Non-AC": 2500,
    "2 Bedded AC": 3500
}
# Menu for Room Service
food_menu = {
    "Tea/Coffee": 50, 
    "Breakfast": 250, 
    "Lunch": 400, 
    "Dinner": 550, 
    "Water": 30
}

# Floor plan configuration
floor_types = (
    "Unknown", 
    "1 Bedded Non-AC", 
    "1 Bedded AC", 
    "3 Bedded AC", 
    "2 Bedded Non-AC", 
    "2 Bedded AC"
)
 # tthis loop runs once when the program starts.
# it creates 75 rooms' (5 Floors x 15 Rooms).
for floor in range(1, 6):
    for r in range(1, 16):
        room_num = (floor * 100) + r
        
        # creating the room entry in our database
        hotel_db[room_num] = {
            "type": floor_types[floor], 
            "status": "Empty",
            "cleanliness": "Clean",
            "guest": {},
            "revenue": 0

        }


# **********88888MAIN APPLICATION CLASS***************
class hotelmanagmentsystem(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window Setup
        self.title("Grand Hotel Management System")
        self.geometry("1100x750")

        # Grid Layout Configuration
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)


        self.setup_sidebar()
        self.setup_main_area()
        
        self.show_dashboard() 

    def setup_sidebar(self):
        """Creates the left-side menu buttons."""
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        # App logo
        ctk.CTkLabel(self.sidebar, text="HMS DASHBOARD", font=("Arial", 20, "bold")).pack(pady=30)
        
        # Navigation Buttons
        self.btn_dash = ctk.CTkButton(self.sidebar, text="Overview", command=self.show_dashboard, fg_color="transparent", border_width=2)
        self.btn_dash.pack(pady=10, padx=20, fill="x")
        
        self.btn_rooms = ctk.CTkButton(self.sidebar, text="Room Map", command=self.show_room_grid, fg_color="transparent", border_width=2)
        self.btn_rooms.pack(pady=10, padx=20, fill="x")

        # Exit Button (Red color to indicate caution)
        self.btn_exit = ctk.CTkButton(self.sidebar, text="Exit System", fg_color="#cf3434", hover_color="#8a1c1c", command=self.destroy)
        self.btn_exit.pack(side="bottom", pady=30, padx=20, fill="x")

    def setup_main_area(self):
        """Creates the main container where different pages load."""
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    # PAGE 1: DASHBOARD 
    def show_dashboard(self):
        """Displays the main overview with stats and guest list."""
        self.clear_main()
        
        # 1. Calculate the Real-Time Stats
        total_rev = sum(room['revenue'] for room in hotel_db.values())
        occupied = sum(1 for room in hotel_db.values() if room['status'] == "Occupied")
        dirty = sum(1 for room in hotel_db.values() if room['cleanliness'] == "Dirty")
        
        # 2. Display the Title
        ctk.CTkLabel(self.main_frame, text="Hotel Status Overview", font=("Arial", 28, "bold")).pack(anchor="w", pady=10)
        
        # 3. Create the colored cards
        stats_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        stats_frame.pack(fill="x", pady=10)
        
        
        self.create_stat_card(stats_frame, "Total Revenue", f"Rs. {total_rev}", "#2CC985", 0) # Green
        self.create_stat_card(stats_frame, "Occupancy", f"{occupied} / 75", "#3B8ED0", 1)     # Blue
        self.create_stat_card(stats_frame, "Dirty Rooms", f"{dirty}", "#E04F5F", 2)           # Red

        # 4. Create the 'Live Guest List' Table
        ctk.CTkLabel(self.main_frame, text="Current Guests Details", font=("Arial", 20, "bold")).pack(anchor="w", pady=(30, 10))

        # Table Headers
        header_frame = ctk.CTkFrame(self.main_frame, height=40, fg_color="#333333")
        header_frame.pack(fill="x", padx=10)
        
        headers = ["Room No", "Room Type", "Guest Name", "Phone Number"]
        weights = [1, 2, 2, 2] # Adjusts column widths
        
        for i, h in enumerate(headers):
            lbl = ctk.CTkLabel(header_frame, text=h, font=("Arial", 14, "bold"))
            lbl.grid(row=0, column=i, sticky="ew", padx=10, pady=5)
            header_frame.grid_columnconfigure(i, weight=weights[i])

        # Scrollable area for the rows
        scroll_list = ctk.CTkScrollableFrame(self.main_frame, fg_color="transparent")
        scroll_list.pack(fill="both", expand=True, padx=5)

        # Loop through DB to find occupied rooms
        has_guests = False
        
        for r_num, room in hotel_db.items():
            if room["status"] == "Occupied":
                has_guests = True
                
                # Create a row for each guest
                row_frame = ctk.CTkFrame(scroll_list, fg_color="#2b2b2b")
                row_frame.pack(fill="x", pady=2)
                
                data = [str(r_num), room["type"], room["guest"]["name"], room["guest"]["phone"]]
                
                for i, d in enumerate(data):
                    lbl = ctk.CTkLabel(row_frame, text=d, font=("Arial", 13))
                    lbl.grid(row=0, column=i, sticky="ew", padx=10, pady=10)
                    row_frame.grid_columnconfigure(i, weight=weights[i])

        if not has_guests:
            ctk.CTkLabel(scroll_list, text="No guests currently checked in.", text_color="gray").pack(pady=20)

    def create_stat_card(self, parent, title, value, color, col_idx):
        """Helper function to make the stats cards look nice."""
        card = ctk.CTkFrame(parent, fg_color=color, height=140)
        card.grid(row=0, column=col_idx, padx=10, sticky="ew")
        parent.grid_columnconfigure(col_idx, weight=1)
        
        ctk.CTkLabel(card, text=title, font=("Arial", 16), text_color="white").pack(pady=(20, 5))
        ctk.CTkLabel(card, text=value, font=("Arial", 30, "bold"), text_color="white").pack(pady=5)

    # PAGE 2: ROOM GRID MAP
    def show_room_grid(self):
        """Shows all 75 rooms as clickable buttons."""
        self.clear_main()
        ctk.CTkLabel(self.main_frame, text="Live Room Map", font=("Arial", 24, "bold")).pack(anchor="w", pady=(0, 10))
        
        # Legend for colors
        legend_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        legend_frame.pack(anchor="w", pady=5)
        ctk.CTkLabel(legend_frame, text="🟩 Empty & Clean   🟥 Occupied   🟧 Dirty (Needs Cleaning)").pack(anchor="w")

        # Scrollable area because 75 rooms is a lot
        scroll = ctk.CTkScrollableFrame(self.main_frame)
        scroll.pack(fill="both", expand=True)

        for floor in range(1, 6):
            # Floor Header
            f_frame = ctk.CTkFrame(scroll, fg_color="transparent")
            f_frame.pack(fill="x", pady=10)
            ctk.CTkLabel(f_frame, text=f"Floor {floor} ({floor_types[floor]})", font=("Arial", 16, "bold"), text_color="gray").pack(anchor="w")
            
            # Grid for buttons
            grid_frame = ctk.CTkFrame(scroll)
            grid_frame.pack(fill="x")
            
            for r in range(1, 16):
                r_num = (floor * 100) + r
                status = hotel_db[r_num]["status"]
                clean = hotel_db[r_num]["cleanliness"]
                
                # Decide Button Color
                btn_color = "#2CC985" # Green
                if status == "Occupied": btn_color = "#E04F5F" # Red
                elif clean == "Dirty": btn_color = "#E59110"   # Orange
                
                # Create the button
                btn = ctk.CTkButton(grid_frame, text=f"{r_num}", width=60, height=50, fg_color=btn_color,
                                    command=lambda x=r_num: self.open_room_actions(x))
                btn.grid(row=0, column=r-1, padx=3, pady=5)

    # POPUP: ROOM ACTIONS
    def open_room_actions(self, r_num):
        """Opens a small window to manage a specific room."""
        window = ctk.CTkToplevel(self)
        window.title(f"Manage Room {r_num}")
        window.geometry("400x550")
        window.attributes("-topmost", True)
        
        room = hotel_db[r_num]
        
        # Header Info
        ctk.CTkLabel(window, text=f"Room {r_num}", font=("Arial", 22, "bold")).pack(pady=10)
        ctk.CTkLabel(window, text=f"Type: {room['type']}", text_color="gray").pack()
        
        # when ROOM IS OCCUPIED
        if room["status"] == "Occupied":
            g = room['guest']
            
            # Show Guest Info
            info_frame = ctk.CTkFrame(window)
            info_frame.pack(pady=10, padx=20, fill="x")
            ctk.CTkLabel(info_frame, text=f"Guest: {g['name']}").pack(pady=2)
            ctk.CTkLabel(info_frame, text=f"Phone: {g['phone']}").pack(pady=2)
            
            # Rooom Service Section
            ctk.CTkLabel(window, text="--- Room Service ---").pack(pady=5)
            self.food_var = ctk.StringVar(value="Select Item")
            ctk.CTkOptionMenu(window, variable=self.food_var, values=list(food_menu.keys())).pack(pady=5)
            ctk.CTkButton(window, text="Add Order", command=lambda: self.add_food(r_num, self.food_var.get())).pack(pady=5)
            
            # Checkout Button\
            ctk.CTkLabel(window, text="--- Checkout ---").pack(pady=(20, 5))
            ctk.CTkButton(window, text="Generate Final Bill", fg_color="#E04F5F", hover_color="#8a1c1c", 
                          command=lambda: self.open_bill_window(r_num, window)).pack(pady=10)

        # when ROOM IS DIRTY
        elif room["cleanliness"] == "Dirty":
            ctk.CTkLabel(window, text="⚠️ This room is DIRTY", font=("Arial", 16), text_color="orange").pack(pady=30)
            ctk.CTkButton(window, text="Mark as Cleaned", fg_color="#E59110", 
                          command=lambda: [self.perform_clean(r_num), window.destroy(), self.show_room_grid()]).pack(pady=20)
            
        # WHEN ROOM IS EMPTY ---
        else:
            ctk.CTkLabel(window, text="New Check-In", font=("Arial", 16)).pack(pady=5)
            
            entry_name = ctk.CTkEntry(window, placeholder_text="Guest Name (Letters only)")
            entry_name.pack(pady=5)
            
            entry_phone = ctk.CTkEntry(window, placeholder_text="Phone (Digits only)")
            entry_phone.pack(pady=5)
            
            ctk.CTkButton(window, text="Confirm Check-In", fg_color="#2CC985",
                          command=lambda: [self.perform_checkin(r_num, entry_name.get(), entry_phone.get()), 
                                           window.destroy(), self.show_room_grid()]).pack(pady=20)

    # BILLING & INVOICE 
    def open_bill_window(self, r_num, parent_window):
        """Opens the Invoice Generator window."""
        bill_win = ctk.CTkToplevel(self)
        bill_win.title("Invoice Generator")
        bill_win.geometry("500x700")
        bill_win.attributes("-topmost", True)
        bill_win.grab_set()

        ctk.CTkLabel(bill_win, text="How many days stayed?", font=("Arial", 14)).pack(pady=10)
        
        # Input for days
        entry_days = ctk.CTkEntry(bill_win)
        entry_days.pack(pady=5)
        entry_days.focus() 

        # TExt area to show the bill
        bill_text_area = ctk.CTkTextbox(bill_win, width=400, height=400, font=("Courier", 12))
        bill_text_area.pack(pady=10)

        btn_frame = ctk.CTkFrame(bill_win)
        btn_frame.pack(pady=10)

        # function to update the bill text
        def generate_preview(event=None):
            try:
                days_str = entry_days.get()
                if not days_str.isdigit():
                    messagebox.showerror("Error", "Days must be a number.")
                    return
                days = int(days_str)
                if days < 1: days = 1
                
                # Create the text
                bill_str = self.create_bill_string(r_num, days)
                
                # Show it
                bill_text_area.delete("1.0", "end")
                bill_text_area.insert("0.0", bill_str)
                
                # Unlock the buttons
                btn_pay.configure(state="normal")
                btn_print.configure(state="normal")
            except Exception as e:
                messagebox.showerror("Error", f"Error generating bill: {e}")

        # Bind Enter key for convenience
        entry_days.bind('<Return>', generate_preview)
        ctk.CTkButton(bill_win, text="Preview Bill (Enter)", command=generate_preview).pack(pady=5)

        # Print Button
        btn_print = ctk.CTkButton(btn_frame, text="Save/Print", state="disabled", fg_color="#3B8ED0",
                                  command=lambda: self.save_bill_file(r_num, bill_text_area.get("1.0", "end")))
        btn_print.pack(side="left", padx=5)

        # Pay Button
        btn_pay = ctk.CTkButton(btn_frame, text="Mark Paid", state="disabled", fg_color="#E04F5F",
                                command=lambda: self.finalize_checkout(r_num, bill_win, parent_window))
        btn_pay.pack(side="left", padx=5)

    def create_bill_string(self, r_num, days):
        """Calculates the total and formats the invoice text."""
        room = hotel_db[r_num]
        guest = room['guest']
        rate = room_prices[room['type']]
        rent_total = rate * days
        
        # Header
        bill =  "====================================\n"
        bill += "          HOTEL GRAND INVOICE       \n"
        bill += "====================================\n"
        bill += f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        bill += f"Bill No: INV-{r_num}-{datetime.datetime.now().strftime('%M%S')}\n\n"
        
        bill += f"Guest:    {guest['name']}\n"
        bill += f"Phone:    {guest['phone']}\n"
        bill += f"Room:     {r_num} ({room['type']})\n"
        bill += "------------------------------------\n"
        bill += f"{'Description':<20} {'Amount':>10}\n"
        bill += "------------------------------------\n"
        bill += f"{f'Rent ({days} days)':<20} {rent_total:>10}\n"
        
        # Add food items
        food_total = 0
        for item in guest['orders']:
            bill += f"{item['item']:<20} {item['price']:>10}\n"
            food_total += item['price']
            
        bill += "------------------------------------\n"
        
        # Totals
        subtotal = rent_total + food_total
        tax = int(subtotal * 0.10) # 10% Tax
        grand_total = subtotal + tax
        
        bill += f"{'Subtotal':<20} {subtotal:>10}\n"
        bill += f"{'Tax (10%)':<20} {tax:>10}\n"
        bill += "------------------------------------\n"
        bill += f"{'GRAND TOTAL':<20} {grand_total:>10}\n"
        bill += "====================================\n"
        
        # Temporarily save total for the checkout function
        room['temp_revenue'] = grand_total 
        return bill

    def save_bill_file(self, r_num, bill_content):
        """Saves the bill to a text file."""
        filename = f"Bill_Room_{r_num}.txt"
        with open(filename, "w") as f:
            f.write(bill_content)
        messagebox.showinfo("Printed", f"Bill saved successfully as:\n{filename}")

    def finalize_checkout(self, r_num, bill_window, parent_window):
        """Completes the checkout process."""
        room = hotel_db[r_num]
        
        # Add to total revenue
        if 'temp_revenue' in room:
            room['revenue'] += room['temp_revenue']
        
        # Reset the room
        room["status"] = "Empty"
        room["cleanliness"] = "Dirty" # Room needs cleaning after guest leaves
        room["guest"] = {}
        
        messagebox.showinfo("Success", "Checkout Complete!\nRoom is marked DIRTY.")
        bill_window.destroy()
        parent_window.destroy()
        self.show_dashboard() # Refresh dashboard stats

    # --- HELPER FUNCTIONS ---
    def perform_checkin(self, r_num, name, phone):
        """Validates input and checks a guest in."""
        # Simple Validation
        if not name.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Name must contain letters only.")
            return
        if not phone.isdigit():
            messagebox.showerror("Error", "Phone must be digits.")
            return
        
        # Update DB
        hotel_db[r_num]["status"] = "Occupied"
        hotel_db[r_num]["guest"] = {"name": name, "phone": phone, "orders": []}
        messagebox.showinfo("Success", "Check-in Successful!")

    def perform_clean(self, r_num):
        """Marks a dirty room as clean."""
        hotel_db[r_num]["cleanliness"] = "Clean"
        messagebox.showinfo("Housekeeping", "Room is now Clean.")

    def add_food(self, r_num, item):
        """Adds a food item to the guest's bill."""
        if item == "Select Item": return
        price = food_menu[item]
        hotel_db[r_num]["guest"]["orders"].append({"item": item, "price": price})
        messagebox.showinfo("Kitchen", f"Sent {item} to Room {r_num}")

    def clear_main(self):
        """Removes all widgets from the main frame before loading a new page."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

# --- ENTRY POINT ---
if __name__ == "__main__":
    app = hotelmanagmentsystem()
    app.mainloop()
