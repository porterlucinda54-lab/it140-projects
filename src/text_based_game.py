"""Project Two starter for the student's text-based adventure game."""
# Lucinda Porter
# SNHU IT-140 Project Two: Text-Based Adventure Game

def show_instructions():
    """Display the game objective and available commands."""
    print("\nDragon Text Adventure Game")
    print("Collect all 6 items before entering the room with the dragon.")
    print("Move commands: go north, go south, go east, go west")
    print("Item command: get <item name>")
    print("Type 'quit' to end the game.\n")


def show_status(current_room, inventory, rooms):
    """Display the player's current room, inventory, and room item."""
    print("\n" + "-" * 35)
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")

    room_item = rooms[current_room].get("item")
    if room_item:
        print(f"You see a {room_item}")

    print("-" * 35)


def main():
    """Run the game's movement, item collection, and win/loss logic."""
    rooms = {
        "Great Hall": {
            "north": "Dungeon",
            "south": "Bedroom",
            "east": "Kitchen",
            "west": "Library",
        },
        "Bedroom": {
            "north": "Great Hall",
            "east": "Cellar",
            "item": "Armor",
        },
        "Cellar": {
            "west": "Bedroom",
            "item": "Helmet",
        },
        "Kitchen": {
            "west": "Great Hall",
            "north": "Dining Room",
            "item": "Potion",
        },
        "Dining Room": {
            "south": "Kitchen",
            "item": "Dragon",
        },
        "Library": {
            "east": "Great Hall",
            "north": "Gallery",
            "item": "Spell Book",
        },
        "Gallery": {
            "south": "Library",
            "east": "Dungeon",
            "item": "Shield",
        },
        "Dungeon": {
            "south": "Great Hall",
            "west": "Gallery",
            "item": "Sword",
        },
    }

    current_room = "Great Hall"
    inventory = []
    villain_room = "Dining Room"
    total_items = 6

    show_instructions()

    while True:
        # The villain ends the game if the player enters too early.
        if current_room == villain_room:
            if len(inventory) == total_items:
                print("\nCongratulations! You have collected all items and defeated the dragon!")
            else:
                print("\nNOM NOM... GAME OVER!")
                print("You entered the dragon's room before collecting all 6 items.")
            print("Thanks for playing the game. Hope you enjoyed it.")
            break

        # Check for a win after collecting every item.
        if len(inventory) == total_items:
            print("\nCongratulations! You have collected all items and defeated the dragon!")
            print("Thanks for playing the game. Hope you enjoyed it.")
            break

        show_status(current_room, inventory, rooms)
        command = input("Enter your move: ").strip().lower()

        if command == "quit":
            print("Thanks for playing the game. Hope you enjoyed it.")
            break

        if command.startswith("go "):
            direction = command[3:].strip()

            if direction in rooms[current_room]:
                next_room = rooms[current_room][direction]

                # Moving into the villain's room ends the game.
                if next_room == villain_room:
                    current_room = next_room
                else:
                    current_room = next_room
            else:
                print("You can't go that way. Please choose a valid direction.")

        elif command.startswith("get "):
            requested_item = command[4:].strip()
            room_item = rooms[current_room].get("item")

            if room_item and requested_item == room_item.lower():
                inventory.append(room_item)
                del rooms[current_room]["item"]
                print(f"{room_item} has been added to your inventory!")
            elif room_item:
                print(f"That item is not available. You see: {room_item}")
            else:
                print("There is no item to collect in this room.")

        else:
            print("Invalid command. Enter 'go north', 'go south', 'go east', 'go west', or 'get <item name>'.")


if __name__ == "__main__":
    main()

# TODO: Add the full-name comment required by Project Two directions.


def show_instructions():
    """Display the game objective and available commands."""
    # TODO: Print instructions that match your game and commands.
    pass


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    # TODO: Show the current room.
    # TODO: Show the current inventory.
    # TODO: Show the current-room item when one is available.
    pass


def main():
    """Run the main gameplay loop."""
    # TODO: Create the full room/item dictionary from your Project One map.

    # TODO: Set the player's starting room.

    # TODO: Create the player's inventory.

    # TODO: Call the instruction function at the appropriate time.

    # TODO: Create the gameplay loop.
    # Within the loop:
    #   - Show player status.
    #   - Prompt for the player's next command.
    #   - Handle valid movement commands.
    #   - Handle valid get-item commands.
    #   - Validate invalid commands.
    #   - Update room/inventory state when appropriate.
    #   - Detect and display the required winning outcome.
    #   - Detect and display the required losing outcome.
    #   - End the loop when the player has won or lost.
    pass


if __name__ == "__main__":
    main()
