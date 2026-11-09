
def show_intro():
    title = "========== MYSTERY ISLAND =========="
    instruction = "The lighthouse is dark, the bridge is locked,\nand a rescue boat will arrive only if you restore the beacon"
    name = input("Enter your name to start the game:\n")
    print(
        f"\n{title}\n\n"
        f"Welcome to mystery island {name}!!!\n\n"
        f"{instruction}"
    )
    return name
user_name = show_intro()

def create_player(user_name):
    players_name = user_name
    energy = 5
    location = "Beach"
    inventory = []

    user_info = {
        "Name": players_name,
        "Energy": energy,
        "Location": location,
        "Inventory": inventory
    }
    return user_info
information = create_player(user_name)

def show_status(information):
    print(
        f"\n========== PLAYER STATUS ==========\n"
    )
    for key, value in information.items():
        print(f"{key}: {value}")  

show_status(information)

def display_menu():
    print(
        f"\n========== MYSTERY ISLAND MENU ==========\n\n"
        f"1. Explore current location\n"
        f"2. Move to another location\n"
        f"3. View inventory\n"
        f"4. Check player status\n"
        f"5. Quit game"
    )
    menu = input("Enter your choice: ")
    return menu