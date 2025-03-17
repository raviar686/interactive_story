from inventory import show_inventory, add_item, remove_item, get_choice
from paths import tunnel_path, house_path, bridge_path, blocked_path, find_new_exit, around_tunnel_choice, next_house_choice, around_house_choice, second_bear_choice, traveler_encounter, keep_moving_bridge

# Introduction to the interactive story
def introduction():
    print("""This is my interactive story, 'Escape The Woods'. In it, you will embark on an adventure in the woods.
You will make decisions that change the course of your journey.
Please freely type 'help' to see your list of commands. 
If you ever want to quit, just type 'stop'. Good Luck!\n""")

# Function to start the adventure
def start_adventure():
    print("As you enter the woods, you see three paths. Which do you choose?")
    choice = get_choice("Path 1, 2, or 3: ", ["1", "2", "3"])

    if choice == "1":
        tunnel_path()
    elif choice == "2":
        house_path()
    else:
        bridge_path()
