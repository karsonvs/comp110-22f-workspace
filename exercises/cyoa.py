"""A choose your own adventure game."""

__author__ = "73061113"

import random as r
points: int = 3
health: int = 10
potion_number: int = 4
player: str = ""
enemy: str = ""
enemy_health: int = 0
MAGIC_SPARKLE: str = "\U00002728"


def greet() -> None:
    """Introduces the player to the game."""
    global player
    print("Welcome to Aslandia! You have been transported to a magical world of mystery and you will have to battle your way out.")
    player = input("Enter your name to begin: ")


def attack(num: int) -> int:
    """Allows the player to attack the enemy."""
    global enemy_health
    global points
    assert num < 3
    assert points >= 0
    if num == 2 and points >= 3:
        points = points - 3
        return enemy_health - 5
    else:
        points = points - 1
        return enemy_health - 2


def potions(num: int) -> int:
    """Allows the player to increase their health."""
    global health
    global potion_number
    assert num < 3
    assert potion_number > 0
    if num == 1:
        return health + 3
    else:
        potion_number = potion_number - 1
        return health + 10
        

def enemy_attack() -> None:
    """Creates a random attack from the enemy that damages the player."""
    global health
    damage: int = r.randint(1, 6)
    if damage % 2 == 0:
        health = health - 3
    else:
        health = health - 1


def introduction():
    """Has a choose your own adventure aspect, implements procedure."""
    global enemy
    global enemy_health
    global points
    global player
    print(f"Hello, {player} I am Sherman the flying pig here to help you start your journey. You're off to a great start! It appears your mana level is {points}.")
    choice_1: str = input("Do you want to enter the forest (1) or climb the mountain (2)? ")
    if choice_1 == "1":
        print("You enter the forest.")
        choice_2: str = input("Deep in the forest you approach a fork in the road. The first path leads to more forest (1) the second appears to lead to a field (2). Which way do you go? ")
        if choice_2 == "1":
            print("As you continue through the forest, a tree nymph approaches and grants you one mana for your stunning looks.")
            points += 1
            print(f"Your mana level is now {points}")
            enemy = "Ogre"
            enemy_health = 20
        else:
            print("As you approach the field, you realize its filled with poppies. It's too late to turn back and you slowly drift off...")
            print("...")
            print("...")
            print("...")
            print("You wake up groggy and disoriented, Sherman informs you that while asleep a witch placed hex on you!")
            points -= 1
            print(f"Your mana level is now {points}")
            enemy = "Witch"
            enemy_health = 15
    else: 
        print("You begin your trek up the mountain.")
        choice_3: str = input("As you make your ascent, you approach a cave. Do you want to enter the cave (1) or continue climbing (2)? ")
        if choice_3 == "1":
            print("You enter the cave unsure of what will happen next. You hear a low growl in the distance...")
            print("Sherman is afraid of the noise and grants you an extra point of mana to aid you in your adventure.")
            points += 1
            print(f"Your mana level is now {points}")
            enemy = "Cave Yeti"
            enemy_health = 20
        else:
            print("You climb up the mountain until you reach the peak.")
            print("The freezing cold at the peak is overbearing and causes you to lose one mana.")
            points -= 1
            print(f"Your mana level is now {points}")
            enemy = "Grand Wizard Kris Jordan"
            enemy_health = 25
    print(f"You are now battling the {enemy}.")


def main() -> None:
    """The main section where the game loops."""
    global potion_number
    global enemy
    global enemy_health
    global points
    global health
    greet()
    introduction()
    move: str = "0"
    while health > 0 and enemy_health > 0 and move != "-1":
        print(f"You have {points} mana. You have {health} health.")
        move = input("Enter 1 for attack or 2 for health potions (Enter -1 at any point to quit.) ")
        if move == "1":
            print("1. Light attack (1 mana) \n2. Heavy attack (3 mana)")
            attack_choice: str = input("Light attack (1) or Heavy attack (2)? ")
            if attack_choice == "1":
                enemy_health = attack(1)
                print(f"{enemy}'s health is now {enemy_health}")
            else:
                enemy_health = attack(2)
                print(f"{enemy}'s health is now {enemy_health}")
        else:
            print(f"1. Small health potion \n2. Large health potion ({potion_number} left)")
            potion_choice: str = input("Small health potion (1) or Large health potion (2)? ")
            if potion_choice == "1":
                health = potions(1)
                print(f"Your health is now {health}")
            else:
                health = potions(2)
                print(f"Your health is now {health}")
        print(f"{enemy} is charging up an attack...")
        enemy_attack()
        print(f"BAM! Your health is now {health}")
        points += 3
    if health <= 0:
        print("Sorry you lost. Come back soon!")
    elif enemy == "Grand Wizard Kris Jordan":
        print(f"Congratulations, you beat the most important boss, you have been blessed with a 4.0 GPA in COMP110 {MAGIC_SPARKLE}")
    else:
        print(f"Congratulations, you won! You defeated {enemy} and can safely return home. Thanks for playing!")


if __name__ == "__main__":
    main()