import os
import time
import random


# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Attack and Miss Descriptions  
# Same as before
attack_descriptions = {
    (1, 10): "Your attack barely connects, inflicting minor damage.",
    (11, 20): "A solid hit, you deal a decent blow to your enemy.",
    (21, 30): "A powerful strike, causing significant damage!",
    (31, 40): "An incredibly forceful attack, devastating your foe!"
}

# Same as before

miss_descriptions = {
    1: "Your attack misses completely, leaving you off balance.",
    2: "The enemy dodges skillfully, evading your attack."
}


# Relation Table
# Same as before

weapon_armor_relation = {
    "edged": {"low": 3, "high": 1},
    "blunt": {"low": 1, "high": 3}
}


# Target Destruction Descriptions Table
destruction_descriptions = {
    (0, 10): "Your target is destroyed with a final blow!",
    (11, 20): "Your target collapses spectacularly under your powerful attack!",
    (21, 30): "An overwhelming force utterly annihilates your target!"
}

# Define rooms and their descriptions
rooms = {
    "start": {
        "description": "You are in a small, dimly lit room. There is a door to the east.",
        "east": "hallway",
    },
    "hallway": {
        "description": "You find yourself in a long hallway. There are doors to the north and south.",
        "north": "bedroom",
        "south": "kitchen",
    },
    "bedroom": {
        "description": "This is a cozy bedroom. There's a window to the west.",
        "west": "hallway",
    },
    "kitchen": {
        "description": "You are in a well-equipped kitchen. There's a door to the north.",
        "north": "hallway",
    },
}

# Current room
current_room = "start"

# Global Variables
hit_pool = 500
AS = 243  # Example Attack Score
DS = 199  # Example Defense Score
weapon_type = "edged"
armor_type = "low"

# Function to simulate the attack
def simulate_attack_with_timer():
    global hit_pool

    AvD = weapon_armor_relation[weapon_type][armor_type]
    roll = random.randint(1, 100)

    total = AS - DS + AvD + roll
    success = total >= 100

    if success:
        damage = total - 100 + AvD
        hit_pool -= damage
        description = "an unremarkable attack."
        for damage_range, desc in attack_descriptions.items():
            if 100 + damage_range[0] <= total <= 100 + damage_range[1]:
                description = desc
                break

        print(f"AS +{AS} vs DS +{DS} + AvD +{AvD} = +{total - 100} with d100 +{roll} = +{total} Success!")

        # Display the timer bar
        for i in range(6):  # 6 half-second intervals for 3 seconds 
            time.sleep(0.5)  # Wait for half a second
            print("█", end="", flush=True)  # Print a block to represent the timer bar

        print(f"\nYou hit for +{damage} damage. {description}")
    else:
        miss_message = miss_descriptions[random.randint(1, len(miss_descriptions))]
        print(f"AS +{AS} vs DS +{DS} + AvD +{AvD} = +{total - 100} with d100 +{roll} = +{total} Fail.")
        print(miss_message)


    if hit_pool <= 0:
        overkill = abs(hit_pool)
        destruction_message = "Your target is destroyed!"
        for damage_range, desc in destruction_descriptions.items():
            if range[0] <= overkill <= range[1]:
                destruction_message = desc
                break
        print(destruction_message)

# Function to reset the game
def reset_game():
    global hit_pool
    hit_pool = 500
    print("\nGame reset. Your target is at full health.\n")

# Main Game Loop
def main():
    clear_screen()
    print("Welcome to the Adventure Game")
    print("-------------------------------\n")

    # Initialize the player's location
    current_room = "start"

    while True:
        if current_room == "combat":
            # If the player is in a combat scenario, execute the combat loop
            command = input("Enter a command (attack/reset/exit): ").strip().lower()
            if command == "attack":
                simulate_attack_with_timer()
                print("\n")  # Adding a line break after each combat roll
            elif command == "reset":
                reset_game()
            elif command == "exit":
                print("Exiting combat...")
                current_room = "start"  # Return to the starting room
            else:
                print("Invalid command. Please enter 'attack', 'reset', or 'exit'.\n")
        else:
            # If the player is exploring a room, handle room-related commands
            print(rooms[current_room]["description"])  # Display the current room's description
            command = input("Enter a command (look/direction/exit): ").strip().lower()

            if command == "look":
                # Display the current room's description again
                print(rooms[current_room]["description"])
            elif command in rooms[current_room]:
                # If the direction entered is valid for the current room, move to the new room
                current_room = rooms[current_room][command]
            elif command == "exit":
                print("Exiting the game...")
                break
            elif command == "enter_combat":
                print("Entering combat...")
                current_room = "combat"  # Enter the combat room
            else:
                print("Invalid command. Please enter 'look', a valid direction, 'enter_combat', or 'exit'.\n")

if __name__ == "__main__":
    main()

