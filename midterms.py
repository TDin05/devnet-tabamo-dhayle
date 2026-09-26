"""
Midterm Practical Exam — Network Device Inventory Tool
Student: [Dhayle Tabamo]
"""

devices = []  # starts empty — the user adds devices as the program runs

def display_menu():
    # print the menu, return the user's choice
    print("=== Network Devices Inventory ===")
    print("1. Add a device")
    print("2. View all devices")
    print("3. Count active vs inactive devices")
    print("4. Find a device by name")
    print("5. Exit")

    choice = input("Enter a number: ")
    
    pass

def add_device(device_list):
    # ask for name, IP, status — build the string, add to the list
    print("Add a device: ")
    device_list = input("Add new device (device name - IP - Active/Not Active)")
    pass

def view_devices(device_list):
    # loop through and print every device — handle empty list
    for devices in device_list:
        try:
            print(devices)
        except:
            print("there are no devices here...")

    pass

def count_active_inactive(device_list):
    # loop through, count Active vs Inactive, return both
    for devices in device_list:
        print(devices[-1])
    pass

def find_device(device_list):
    # ask for a name, search the list, print result or "not found"
    find = input("Enter device name")
    
    pass

# BONUS (optional)
def remove_device(device_list):
    # your code here
    pass

def main():
    running = True
    while running:
        choice = display_menu()
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit
        display_menu
        if choice == 1:
            add_device()
        elif choice == 2:
            view_devices()
        elif choice == 3:
            count_active_inactive()
        elif choice == 4:
            find_device()
        elif choice == 5:
            running = False
        else:
            print("Enter a one of the choices!")


main()