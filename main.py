
def show_intro():
    title = "=== MYSTERY ISLAND ==="
    instruction = "The lighthouse is dark, the bridge is locked,\nand a rescue boat will arrive only if you restore the beacon"
    name = input("Enter your name to start the game:\n")
    print(
        f"\n{title}\n\n"
        f"Welcome to mystery island {name}!!!\n\n"
        f"{instruction}"
    )
    return name
user_name = show_intro()

def create_player():
    players_name = user_name
    energy = 5
    location = "Beach"
    inventory = []

    user_info = {
        "players_name": players_name,
        "energy": energy,
        "location": location,
        "inventory": inventory
    }
    return user_info

def show_status():
    