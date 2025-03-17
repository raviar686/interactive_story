import random

# Introduction to the interactive story
def introduction():
    print("""This is my interactive story, 'Escape The Woods'. In it, you will embark on an adventure in the woods.
You will make decisions that change the course of your journey.
Please freely type 'help' to see your list of commands.
If you ever want to quit, just type 'stop'. Good Luck!\n""")

# Inventory system added
inventory = ["food","knife","first aid kit"]
def add_item(item):
  inventory.append(item)
  print(f"You received: {item}!")

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

def remove_item(item):
  if item in inventory:
    inventory.remove(item)
    print(f"You lost your {item}!")
  else:
    print(f"You don't have {item} to lose.")

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

# Different story paths
def tunnel_path():
    print("\nYou have chosen the straight path.")
    print("As you continue, you see a dark tunnel that may be a shortcut.")
    choice = get_choice("Do you wish to go through the tunnel? (yes/no): ", ["yes", "no"])

    if choice == "yes":
        print("You step into the tunnel, and begin your trek throught the long dark tunnel...")
        blocked_path()
    else:
        print("You decide to take the safer route around the tunnel.")
        print("The path gets hilly, but after descending the last hill, you exit the forest!!")
        around_tunnel_choice()

def blocked_path():
    print("\nA pile of rocks blocks your path. You need to clear at least 3 big rocks to move forward.")

    rocks_cleared = 0
    for attempt in range(5):  # Player has 5 chances
        choice = input("Do you push a rock (yes/no)? ").strip().lower()

        if choice == "yes":
            rocks_cleared += 1
            print(f"You move a rock! ({rocks_cleared}/3 cleared)")
            if rocks_cleared >= 3:
                print("You have cleared enough space to continue!")
                return  # Success leads forward
        else:
            print("You hesitate and lose time.")

    print("You couldn't clear enough space. You need to find another way out.")
    find_new_exit()  # Now properly called if the player fails


def find_new_exit():
    print("\nYou search for another way out of the tunnel...")
    print("You find three possible options:")

    choice = get_choice("Do you (climb a rock wall / crawl through a gap / follow underground water)? ",
                        ["climb a rock wall", "crawl through a gap", "follow underground water"])

    if choice == "climb a rock wall":
        print("\nYou start climbing the jagged wall.")
        print("Halfway up, your foot slips, but you manage to catch yourself.")
        print("With effort, you reach the top and find an opening to the outside!")

    elif choice == "crawl through a gap":
        print("\nYou squeeze through a narrow gap between fallen rocks.")
        print("It's a tight fit, but after some struggle, you make it through.")
        print("On the other side, you find a tunnel leading to an exit!")

    else:  # follow underground water
        print("\nYou follow the underground stream, wading through the cold water.")
        print("The tunnel gets smaller, and you start to worry, but finally, you see light ahead.")
        print("You emerge at a hidden spring in the forest, finally out of the woods!")

    print("\nAfter a tough journey, you have escaped the tunnel and the woods.")


def around_tunnel_choice():
    print("\nAs you take the safer path around the tunnel, the trail becomes more rugged and uneven.")
    print("You eventually come across a fast-moving river blocking your way.")
    print("You have limited time before nightfall, so you must decide quickly.")

    while True:
        choice = get_choice("How do you proceed? (wade through / build a raft / find a shortcut): ", ["wade through", "build a raft", "find a shortcut"])

        if choice == "wade through":
            print("You attempt to wade through the river, but the current is strong!")
            if "tarp" in inventory:
                print("You use your tarp as support to get across safely.")
                break
            else:
                print("Without proper support, you slip and get soaked, you lose!")
                remove_item("food")
                break

        elif choice == "build a raft":
            if "knife" in inventory:
                print("You use your knife to cut branches and tie them together to form a raft.")
                print("The raft helps you cross the river safely.")
                break
            else:
                print("You don't have the right tools to build a raft. Try another option.")

        else:
            print("You search for another way and notice a narrow fallen tree forming a bridge.")
            print("It looks risky, but it might save you time.")
            risk_choice = get_choice("Do you cross the log or look for another route? (cross/look): ", ["cross", "look"])
            if risk_choice == "cross":
                print("You carefully walk across, balancing with every step...")
                print("With a sigh of relief, you make it across and continue your journey.")
                break
            else:
                print("You spend extra time searching and find a safer but longer path around the river.")
                print("Though it took longer, you continue your journey safely.")
                break

def house_path():
    print("\nYou have chosen the left path.")
    print("As you continue, you find a house off to the right.")
    choice = get_choice("Do you want to check it out? (yes/no): ", ["yes", "no"])

    if choice == "yes":
        print("You cautiously approach the house and knock on the door...")
        print("Someone opens the door and asks who you are. You tell them you are trying to travel through these woods")
        print("You ask if they know of any good paths to the other side of the woods.")
        print("They tell you that there is a shortcut but they will only help you if you help them replace a broken beam of their house.")
        next_house_choice()
    else:
        print("You ignore the house and keep walking.")
        around_house_choice()

def next_house_choice():
  print("\nYou ponder on if you should take the time to help the mysterious home owner repair their house.")
  choice = get_choice("Do you want to help them repair their house? (yes/no): ", ["yes", "no"])

  if choice == "yes":
      print("You have agreed to help them so they lead you to the support beam of the front right of their house.")
      print("They ask you to help them lower the old beam. After a few minutes the old beam gets removed.")
      print("Next you hold up the new beam as the guy hammers it in. After it is all done the guy seems very thankful.")
      print("He offers to not only show you the shortcut but also provide you with essential supplies.")
      print("He shows you to the shortcut which is about a two minute walk into his backyard. He then provide you with supplies.")
      add_item("flashlight")
      add_item("water bottle")
      add_item("tarp")

def around_house_choice():
    print("\nAs you continue walking, you begin to hear low growls from the bushes...")
    print("A brown bear appears from around the bushes and snarls at you.")

    choice = get_choice("What do you do? (run/climb tree/stay still/use item): ", ["run", "climb tree", "stay still", "use item"])

    if choice == "run":
        print("You turn and sprint as fast as you can!")
        print("The bear chases after you. You must make another choice quickly!")
        second_bear_choice()

    elif choice == "climb tree":
        print("You quickly climb up a nearby tree.")
        print("The bear growls and paws at the trunk, but eventually loses interest and leaves.")
        print("You wait for a few minutes before climbing down and continuing on your journey.")
        print("Eventually, you find a road leading out of the woods!")

    elif choice == "stay still":
        print("You stay completely still, hoping the bear loses interest.")
        print("The bear sniffs the air, grunts, and eventually turns away.")
        print("After a tense moment, you carefully back away and continue on your journey.")
        print("Soon, you spot a clearing that leads out of the woods!")

    elif choice == "use item":
        show_inventory()
        item_choice = get_choice("Which item do you want to use? (food/knife/first aid kit/nothing): ", inventory + ["nothing"])

        if item_choice == "food":
            remove_item("food")
            print("You toss some food to the bear. It stops growling and starts eating, giving you time to slip away.")

        elif item_choice == "knife":
            print("You grip your knife, but realize fighting a bear is a terrible idea. The bear roars and lunges at you!")
            print("You drop the knife and barely escape by running!")
            second_bear_choice()

        elif item_choice == "first aid kit":
            print("You hold up the first aid kit. The bear is unimpressed. That was a bad idea!")
            second_bear_choice()

        else:
            print("You hesitate too long! The bear growls louder.")
            second_bear_choice()

    print("\nAfter a long trek, you finally see the edge of the forest.")
    print("With relief, you step out of the woods, finally safe!")


def second_bear_choice():
    choice = get_choice("Do you keep running or try to hide? (run/hide): ", ["run", "hide"])

    if choice == "run":
        print("You sprint through the woods, dodging trees and leaping over roots.")
        print("The bear chases but eventually slows down and gives up.")
        print("Out of breath, you find a safe spot to rest before continuing your journey.")

    else:
        print("You dive into a bush and stay completely silent.")
        print("The bear sniffs around but doesn't find you. After a while, it moves on.")
        print("You carefully emerge and continue on your way, shaken but safe.")


def bridge_path():
    print("\nYou have chosen the right path.")
    print("As you continue, you see an old bridge with a path proceeding it.")

    choice = get_choice("Do you want to cross the bridge? (yes/no): ", ["yes", "no"])

    if choice == "yes":
        print("You slowly cross the bridge, but the bridge begins to creak and planks fall...")
        print("You sprint across the bridge to the other side.")
        next_bridge_choice()
    else:
        print("You decide it's best to avoid the risky bridge and keep going on your path.")
        find_supplies_near_bridge()  # New function before avoid_bridge_choice

def find_supplies_near_bridge():
    print("\nBefore moving on, you notice an abandoned backpack lying near the bridge.")
    choice = get_choice("Do you want to search the backpack? (yes/no): ", ["yes", "no"])

    if choice == "yes":
        if random.choice([True, False]):  # 50% chance of finding a flashlight
            print("You rummage through the backpack and find a flashlight!")
            add_item("flashlight")
        else:
            print("You check the backpack, but it's empty. Looks like someone took everything already.")

    print("You leave the bridge behind and continue down the path.")
    avoid_bridge_choice()

def next_bridge_choice():
    print("\nAs you check your bag, you realize some things are missing...")
    if inventory:
        lost_item = inventory.pop(0)
        print(f"Oh no! You lost your {lost_item} while rushing across the bridge.")
    else:
        print("Luckily, you had no supplies to lose.")

    choice = get_choice("\nDo you want to keep on moving or look for your lost supplies? (keep moving/look for supplies): ", ["keep moving", "look for supplies"])

    if choice == "keep moving":
        print("You decide to keep on your path even if you are missing some supplies.")
        keep_moving_bridge()
    else:
        print(f"You decide to go looking for your missing {lost_item}.")

        if random.choice([True, False]):  # 50% chance to find the item
            add_item(lost_item)
            print(f"After some searching, you find your {lost_item} stuck between the planks!")
        else:
            print("You search for a while but can't find it. You decide to keep moving forward.")

        keep_moving_bridge()  # Continue the journey after searching


def avoid_bridge_choice():
    print("\nYou decide it's best to avoid the risky bridge and take another path.")
    print("The trail leads you into a dense part of the forest, where the trees block out most of the light.")
    print("As you continue, you realize you are lost!")

    choice = get_choice("What do you do? (climb tree/use flashlight/keep walking): ", ["climb tree", "use flashlight", "keep walking"])

    if choice == "climb tree":
        print("You climb up a tall tree to get a better view.")
        print("From the top, you spot a path leading out of the forest! You climb down and head in that direction.")
    elif choice == "use flashlight":
        if "flashlight" in inventory:
            print("You use your flashlight to scan the area and find a trail marker on a tree.")
            print("Following the markers, you find your way back to the main path.")
        else:
            print("You don't have a flashlight! You stumble in the dark and must keep walking blindly.")
            avoid_bridge_choice()  # Loops back for another choice
    else:
        print("You keep walking, hoping to find your way out.")
        print("After what feels like hours, you finally stumble onto a clear path leading out of the forest.")


def keep_moving_bridge():
    print("\nAs you continue, you see small clouds of smoke rising in the distance away from the path...")
    choice = get_choice("Do you want to investigate the smoke or keep moving? (investigate/keep moving): ", ["investigate", "keep moving"])

    if choice == "investigate":
        print("You decide to check out the source of the smoke.")
        print("As you get closer, you see a small campsite with a fire burning.")
        print("A lone traveler waves at you, inviting you over.")
        traveler_encounter()

    else:
        print("You decide not to take any risks and continue down your path.")
        print("After some time, the trees begin to thin out, and you see the edge of the forest!")
        print("With determination, you push forward and finally exit the woods, reaching safety.")

def traveler_encounter():
  print("\nYou cautiously approach the campsite, staying alert for any danger.")
  print("A lone traveler sits by the fire, roasting something on a stick.")
  print('"Didn’t expect company out here," they say with a friendly smile.')
  print('"You look like you’ve had a rough journey. Care for some supplies?"')

  choice = get_choice("Do you accept the supplies? (yes/no): ", ["yes", "no"])

  if choice == "yes":
        print("\nYou decide to accept the traveler's generosity.")
        print("They hand you a water bottle and some food, wishing you luck on your journey.")
        add_item("water bottle")
        add_item("food")
        print("Feeling refreshed, you thank the traveler and continue on your path.")

  else:
        print("\nYou politely decline, unsure if you should trust a stranger in the woods.")
        print("The traveler shrugs. 'Suit yourself,' they say, returning to their meal.")
        print("You leave the campsite behind and press forward on your journey.")

  print("\nAfter more walking, the trees begin to thin, and sunlight breaks through.")
  print("With a final push forward, you finally reach the edge of the forest!")
  print("You have successfully made it out of the woods.")


# Start the game
if __name__ == "__main__":
    introduction()
    start_adventure()
