import random

class Door:
    def __init__(self, door_number: int):
        self.__winner = False
        self.__door_number = door_number

    def setWinner(self):
        self.__winner = True

    def isWinner(self) -> bool:
        return self.__winner

    def getDoorNumber(self) -> int:
        return self.__door_number

#Get a door by its door number
def getDoor(door_number):
    for door in doors:
        if door.getDoorNumber() == door_number:
            return door

#Get doors other than the chosen one
def getOtherDoors(chosen_door):
    door_numbers = [0, 1, 2]
    door_numbers.remove(chosen_door)
    return door_numbers

if __name__ == "__main__":
    wins = 0
    losses = 0

    choice = ""
    while choice not in ["s", "d", "r"]:
        choice = input("switch door(s), don't change door(d), choose random door(r)").lower()

    while 1:
        doors = [Door(0), Door(1), Door(2)]
        doors[random.randint(0, 2)].setWinner()
        chosen_door = random.randint(0, 2)

        if choice == "d":
            if getDoor(chosen_door).isWinner():
                wins += 1
            else:
                losses += 1
        
        elif choice == "s":
            if getDoor(chosen_door).isWinner():
                losses += 1
            else:
                wins += 1

        else:
            #Remove at random one of the other 2 doors - neither are winner doors
            if getDoor(chosen_door).isWinner():
                deleted_door = random.choice(getOtherDoors(chosen_door))
                doors.remove(getDoor(deleted_door))

            #Remove the loser door out of the other 2 doors
            else:
                other_doors = getOtherDoors(chosen_door)
                for door_number in other_doors:
                    if not getDoor(door_number).isWinner():
                        doors.remove(getDoor(door_number))
                        break

            if random.choice(doors).isWinner():
                wins += 1
            else:
                losses += 1

        if (wins + losses) % 100000 == 0:
            print(f"{choice=}, {wins=}, {losses=}, total = {wins + losses}, win rate = {wins / (wins + losses)}")