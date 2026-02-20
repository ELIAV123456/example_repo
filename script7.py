



def top_students(lst):
    for i in range(10):
        if lst[i] > 90:
            print("you are top student")

def calc_avg(avg , lst):
    up_avg = 0
    down_avg = 0
    for i in range(10):
        if lst[i] > avg:
            up_avg += 1

        elif lst[i] <= 60:
            down_avg += 1
    return up_avg , down_avg

def avg(lst):
    total = 0
    for i in range (10):
        total += lst[i]
    avg = total / len(lst)
    return avg

def create_lst():
    lst = []
    for i in range (10):
        grade = int(input("Enter your grade: "))
        lst.append(grade)
    return lst

def main():
    lst = create_lst()
    Avg = avg(lst)
    higher_avg , lower_avg = calc_avg(Avg , lst)
    top_students(lst)
    print("avg is: ", Avg)
    print("Higher avg is: ", higher_avg)
    print("Lower avg is: ", lower_avg)
    print(ord('a'))

if __name__ == '__main__':
    main()