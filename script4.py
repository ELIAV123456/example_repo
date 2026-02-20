"""
ההוסטל של מריה
"""

def wrong_input(choice, rooms_num, rooms_people_lst, rooms_capacitys_lst): #תפריט
    if choice == "1":
        add_guest(rooms_num, rooms_people_lst, rooms_capacitys_lst)
        return 1

    elif choice == "2":
        remove_guest(rooms_num, rooms_people_lst)
        return 1

    elif choice == "3":
        transfer(rooms_num, rooms_people_lst, rooms_capacitys_lst)
        return 1

    elif choice == "4":
        chack(rooms_num, rooms_people_lst, rooms_capacitys_lst)
        return 1

    elif choice == "99":
        print("Bye bye!")
        return 0


def chack(rooms_num, rooms_people_lst, rooms_capacitys_lst): #הדפסת חדרים
    for i in range(rooms_num):
        print(f"Room #{i + 1}: {rooms_people_lst[i]} / {rooms_capacitys_lst[i]}")


def remove_guest(rooms_num, rooms_people_lst): #הוצאה מחדר
    Which_room = int(input("Enter room number: "))

    while True:
        if 1 <= Which_room <= rooms_num: #בדיקת קלט
            if rooms_people_lst[Which_room - 1] == 0:
                print("Room is already empty!")
                return 0

            rooms_people_lst[Which_room - 1] -= 1
            return 1

        Which_room = int(input("Invalid room number, please try again: "))


def add_guest(rooms_num, rooms_people_lst, rooms_capacitys_lst): #הוספה לחדר
    Which_room = int(input("Enter room number: "))

    while True:
        if 1 <= Which_room <= rooms_num: #בדיקת קלט
            if rooms_people_lst[Which_room - 1] >= rooms_capacitys_lst[Which_room - 1]:
                print("Room is already full!")
                return 0

            rooms_people_lst[Which_room - 1] += 1
            return 1

        Which_room = int(input("Invalid room number, please try again: "))


def transfer(rooms_num, rooms_people_lst, rooms_capacitys_lst): #העברת חדרים
    print("Which room to cancel?")
    from_room = int(input("Enter room number: "))

    if not (1 <= from_room <= rooms_num): #בדיקת קלט
        print("Invalid room number, please try again: ")
        return

    print("Which room to add?")
    to_room = int(input("Enter room number: "))

    if rooms_people_lst[from_room - 1] == 0:
        print("Cancel room is already empty!")
        return

    if not (1 <= to_room <= rooms_num): #בדיקת קלט
        print("Invalid room number, please try again: ")
        return

    if rooms_people_lst[to_room - 1] >= rooms_capacitys_lst[to_room - 1]:
        print("Added room is already full!")
        return

    rooms_people_lst[from_room - 1] -= 1
    rooms_people_lst[to_room - 1] += 1


def rooms_input(): #קליטת חדרים
    print("Room capacity input:")
    rooms_people_lst = [] #רשימת אנשים בכל חדר
    rooms_capacitys_lst = [] #רשימת אנשים מקסימלית בכל חדר
    room_num = 1

    while True:
        room_capacity = int(input(f"Room #{room_num}. Enter room capacity: "))
        rooms_capacitys_lst.append(room_capacity)
        rooms_people_lst.append(0)

        another_room = input("Another room? yes / no: ")

        if another_room == "yes":
            room_num += 1
        elif another_room == "no":
            break
        else:
            print("Wrong action num, try again: ")

    return room_num , rooms_people_lst , rooms_capacitys_lst


def rooms_management(rooms_num, rooms_people_lst, rooms_capacitys_lst): #תפריט
    while True:
        choice = input("Enter action num: 1. order room; 2. cancel room; 3. change rooms; 4. show rooms; 99. quit ")

        if choice == "1":
            add_guest(rooms_num, rooms_people_lst, rooms_capacitys_lst)

        elif choice == "2":
            remove_guest(rooms_num, rooms_people_lst)

        elif choice == "3":
            transfer(rooms_num, rooms_people_lst, rooms_capacitys_lst)

        elif choice == "4":
            chack(rooms_num, rooms_people_lst, rooms_capacitys_lst)

        elif choice == "99":
            print("Bye bye!")
            break

        else: #אם הבחירה לא נמצאת האופציות
            choice = input("Wrong action num, try again: ")
            wrong_input(choice, rooms_num, rooms_people_lst, rooms_capacitys_lst) #קראיה לפונקיצה תפריט השגויה
            #כן אני יודע שזה מיותר
            #אבל לא מצאתי דרך אחרת לסדר את זה ובטסטים זה היה חלק

def main(): #main
    print("Welcome to the Hostel Room Management App!")
    rooms_num, rooms_people_lst, rooms_capacitys_lst = rooms_input()
    rooms_management(rooms_num, rooms_people_lst, rooms_capacitys_lst)


main()
