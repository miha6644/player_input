import json


class FootballPlayer:
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


while True:
    print("\nEnter some Football player's data!")

    first_name = input("\nFirst name: ")
    last_name = input("Last name: ")
    height_cm = float(input("Enter the height of the player (cm): "))
    weight_kg = float(input("Enter the weight of the player (kg): "))
    goals = int(input("Enter player's goals: "))
    yellow_cards = int(input("Enter player's yellow cards: "))
    red_cards = int(input("Enter player's red cards: "))

    new_player = FootballPlayer(first_name=first_name,
                                last_name=last_name,
                                height_cm=height_cm,
                                weight_kg=weight_kg,
                                goals=goals,
                                yellow_cards=yellow_cards,
                                red_cards=red_cards
                                )

    with open("players.json", "w") as players_file:
        players_file.write(str(new_player.__dict__))

    print(f"\nAdded player data: {first_name} {last_name}; height: {height_cm}cm, weight: {weight_kg}kg,"
          f"goals: {goals}, yellow cards: {yellow_cards}, red cards: {red_cards}")

    repeat = input("\nWould you like to add another player(y/n)? ")
    if repeat == "n":
        break
