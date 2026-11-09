
def show_intro():
    title = "=== MYSTERY ISLAND ==="
    intro = "Welcome"
    instruction = "The lighthouse is dark, the bridge is locked,\nand a rescue boat will arrive only if you restore the beacon"
    name = input("Enter your name to start the game: ")
    print(
        f"{title}\n\n"
        f"Welcome to mystery island {name}!!!\n\n"
        f"{instruction}"
    )
show_intro()