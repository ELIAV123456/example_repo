import random

def who_many_until_double(sides):
    count = 0

    while True:
        first_cube = random.randint(1, sides)
        second_cube = random.randint(1, sides)
        count += 1

        if first_cube == second_cube:
            return count


def avg_double(num_for_roll, sides):
    result_sum = 0
    for i in range(num_for_roll):
        result_sum += result
        result_avg = result_sum / num_for_roll
        return result_avg


sides = int(input("How many sides would you like?: "))
num_for_roll = int(input("How many times would you like?: "))
result = who_many_until_double(sides)

print(f"the roll it takes is:{result}")
print(f"the avg  rolls to get double is:{avg_double(num_for_roll, sides)}")
