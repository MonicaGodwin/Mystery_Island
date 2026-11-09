
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
    locations = ["Beach", "Jungle","Cave","Old Bridge","Lighthouse"]
    current_location = "Beach"
    inventory = []

    user_info = {
        "Name": players_name,
        "Energy": energy,
        "Locations": locations,
        "Current_location": current_location,
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

def explore_location(information):
    location = information["Current_location"]
    if location == "Beach":
        print(
            f"The waves crash against the shore.\n "
            f"You notice pieces of the shipwreck scattered across the sand.\n"
            f"Something useful might be hidden nearby."
        )
    elif location == "Jungle":
        print(
            f"Thick trees surround you.\n"
            f"You hear strange sounds coming from the bushes.\n"
            f"There are two paths ahead."
        )
    elif location == "Cave":
        print(
            f"You discover a dark cave."
            f"Strange markings cover its walls."
            f"Perhaps there's a secret hidden inside."
        )
    elif location == "Old Bridge":
        print(
            f"You reach an old, damaged bridge."
            f"It looks dangerous. You might need something to make crossing possible."
        )
    elif location == "Lighthouse":
        print(
            f"You finally reach the lighthouse."
            f"he beacon is dark, and the rescue boat is nowhere to be seen."
        )