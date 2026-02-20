def students_test_check(name):
    counter = 0
    score = int(input("Enter a score:"))

    if score >= 90 and score <= 100 and score >= 0:
        counter += 1

    return counter , score

def get_to_test():
    total_count = 0

    while True:
        total_grade = 0
        name = input("Enter your name:")

        for i in range(3):
            counter,score = students_test_check(name)
            total_grade += score

        if total_grade >= 270:
            total_count += counter
            print("name that pass the entry level:", name)
            print("the total number of student that pass is:",total_count)

get_to_test()