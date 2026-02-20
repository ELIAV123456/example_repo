
students_seats = [['Tamar', 'Yuval', 'Dolev'],
                  ['Daniel', 'Aviram', 'Hagar'],
                  ['Rotem', 'Michal' ,'Ohad']]

def chack(first_name , second_name):
    for row in range(students_seats):
        for column in range(students_seats[row]):
            if first_name == students_seats[row][column]:



def kelet():
    first_name = input("Enter first name: ")
    second_name = input("Enter second name: ")
    return first_name , second_name



def main():
    first_name , second_name = kelet()
    chack(first_name , second_name)



main()