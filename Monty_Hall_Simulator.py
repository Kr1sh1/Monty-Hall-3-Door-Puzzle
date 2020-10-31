from random import shuffle, choice
from copy import copy

print("One of these doors has a prize, the other two do not!\n")

prizes = [0, 0, 1]
shuffle(prizes)

doors = {}
for door in range(3):
    doors[str(door + 1)] = prizes[door]

chosen_door = input("Pick a door!\n\n"
    "1)\n"
    "2)\n"
    "3)\n")

not_chosen_doors = copy(doors)
not_chosen_doors.pop(chosen_door)

if 1 in not_chosen_doors.values():
    revealed_door = list(not_chosen_doors.keys())[list(not_chosen_doors.values()).index(0)]
else:
    revealed_door = choice(list(not_chosen_doors))

status = ["", "", ""]
status[int(chosen_door) - 1] = "Your Choice"
status[int(revealed_door) - 1] = "No Prize!"

print("\nA door was revealed!\n\n"
    f"1) {status[0]}\n"
    f"2) {status[1]}\n"
    f"3) {status[2]}\n")

while True:
    switch_choice = input("Do you want to switch your choice? (y/n)").lower()
    if switch_choice == "y" or switch_choice == "yes":
        not_chosen_doors.pop(revealed_door)
        chosen_door = not_chosen_doors.popitem()[0]
        break
    elif switch_choice == "n" or switch_choice == "no":
        break
    else:
        print("I didn't recognise what you said, try again")

if doors[chosen_door] == 1:
    print("You won!!")
else:
    print("Better luck next time!")