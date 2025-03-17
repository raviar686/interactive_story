inventory = ["food", "knife", "first aid kit"]

def add_item(item):
    inventory.append(item)
    print(f"You received: {item}!")

def remove_item(item):
    if item in inventory:
        inventory.remove(item)
        print(f"You lost your {item}!")
    else:
        print(f"You don't have {item} to lose.")

def show_inventory():
    if inventory:
        print("\nYour current supplies: " + ", ".join(inventory))
    else:
        print("\nYou have no supplies left!")

def get_choice(prompt, options):
    while True:
        choice = input(prompt).strip().lower()
        if choice == "stop":
            print("You have chosen to leave. Goodbye!")
            exit()
        elif choice == "inventory":
            show_inventory()
        elif choice == "help":
            print("\nHelp - List of Commands:")
            print("- 'stop' to quit the game.")
            print("- 'inventory' to view your current supplies.")
            print("- 'yes' or 'no' to answer yes/no questions.")
            print("- 'help' to view this list of commands again.")
            print("- Type your choice to proceed in the story.")
            print("\nUse these commands to navigate the game!")
        elif choice in options:
            return choice
        else:
            print("Invalid choice. Please try again.")
