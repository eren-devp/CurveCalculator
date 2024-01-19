input_amount = int(input("Input count: "))
input_percentages = [100]
if input_amount != 1:
    input_percentages = []
    for i in range(input_amount):
        input_percentages.append(float(input(f"Enter {i+1}. input's percentage: ")))

grades = open("grades.txt").read().split("\n")

sum_grades = 0
na_count = 0
for i in grades:
    try:
        current_sum = 0
        i = i.split("\t")
        number = 0

        for j in i:
            current_sum += float(j) * float(input_percentages[number] / 100.0)
            number += 1

        sum_grades += current_sum

    except:
        na_count += 1

print(f"Average (with NA): {sum_grades / len(grades)}")
print(f"Average (without NA): {sum_grades / (len(grades) - na_count)}")
