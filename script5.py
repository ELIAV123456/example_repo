
def wrong_input(choice , rooms_num , rooms_pepole_lst , rooms_capacitys_lst):
    if choice == "1":
        add_guest(rooms_num , rooms_pepole_lst , rooms_capacitys_lst , choice)
        return 1

    elif choice == "2":
        remove_guest(rooms_num , rooms_pepole_lst , choice)
        return 1

    elif choice == "3":
        transfer(rooms_num , rooms_pepole_lst , choice)
        return 1

    elif choice == "4":
        chack(rooms_num , rooms_pepole_lst , rooms_capacitys_lst)
        return 1

    elif choice == "99":
        print("Bye bye!")
        return 0


def chack(rooms_num , rooms_pepole_lst , rooms_capacitys_lst):
    for i in range(rooms_num - 1):
        print(f"Room #{i + 1}: {rooms_pepole_lst[i]} / {rooms_capacitys_lst[i]}")
    return 0

def transfer(rooms_num , rooms_pepole_lst , rooms_capacitys_lst , choice):
    print("Which room to cancel?")
    cancel = remove_guest(rooms_num , rooms_pepole_lst , choice)
    print("Which room to add?")
    add_guest(rooms_num , rooms_pepole_lst , rooms_capacitys_lst , choice)
    if cancel == 1:
        print("Cancel room is already empty!")

def remove_guest(rooms_num , rooms_pepole_lst , choice):
    which_room = int(input("Enter room number: "))
    if which_room < rooms_num and rooms_pepole_lst[which_room - 1] > 0:
        rooms_pepole_lst[which_room - 1] -= 1
        return rooms_pepole_lst
    if which_room >= rooms_num:
        print("Invalid room number, please try again: ")
    if rooms_pepole_lst[which_room - 1] == 0 and choice != "4" and choice != "3":
        print("Room is already empty!")

    elif rooms_pepole_lst[which_room - 1] == 0 and choice == "3":
        return 1

    return 0

def add_guest(rooms_num , rooms_pepole_lst , rooms_capacitys_lst , choice):
    which_room = int(input("Enter room number: "))
    while True:
        if which_room < rooms_num and rooms_pepole_lst[which_room - 1] >= 0 :
            if rooms_pepole_lst[which_room - 1] < rooms_capacitys_lst[which_room - 1]:
                if rooms_pepole_lst[which_room - 1] >= 0 and choice != "3":
                    rooms_pepole_lst[which_room - 1] += 1
                    return rooms_pepole_lst
                return 0

            elif rooms_pepole_lst[which_room - 1] >= rooms_capacitys_lst[which_room - 1]:
                print("Room is already full!")
                break

        else:
            Which_room = int(input("Invalid room number, please try again: "))

    return 0


def rooms_input():
    print("Room capacity input:")
    i = 1
    rooms_pepole_lst = []
    rooms_capacitys_lst = []

    while True:
        room_capacity = int(input(f"Room #{i}. Enter room capacity: "))
        another_room = input("Another room? yes / no: ")

        rooms_capacitys_lst.append(room_capacity)
        rooms_pepole_lst.append(0)
        i += 1

        if another_room == "no":
            return i ,rooms_capacitys_lst, rooms_pepole_lst
        elif another_room == "yes":
            continue
        else:
            print("wrong input try again")
            continue


def rooms_management(rooms_num, rooms_pepole_lst, rooms_capacitys_lst):
    while True:
        choice = input("Enter action num: 1. order room; 2. cancel room; 3. change rooms; 4. show rooms; 99. quit ")
        if choice == "1":
            add_guest(rooms_num, rooms_pepole_lst, rooms_capacitys_lst, choice)
        elif choice == "2":
            remove_guest(rooms_num, rooms_pepole_lst, choice)
        elif choice == "3":
            transfer(rooms_num, rooms_pepole_lst, rooms_capacitys_lst, choice)
        elif choice == "4":
            chack(rooms_num, rooms_pepole_lst, rooms_capacitys_lst)
        elif choice == "99":
            print("Bye bye!")
            break
        else:
            wrong = input("Wrong action num, try again:\n")
            answer = wrong_input(wrong, rooms_num, rooms_pepole_lst, rooms_capacitys_lst)
            if answer == 0:
                break


def main():
    print("Welcome to the Hostel Room Management App!")
    rooms_num, rooms_capacitys_lst, rooms_pepole_lst = rooms_input()
    rooms_management(rooms_num, rooms_pepole_lst, rooms_capacitys_lst)


main()
