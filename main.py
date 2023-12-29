grades = open("grades.txt").read().split("\n")

sum_grades = 0
na_count = 0
for i in grades:
    try:
        sum_grades += float(i)
    except:
        na_count += 1

print(f"Average (with NA): {sum_grades / len(grades)}")
print(f"Average (without NA): {sum_grades / (len(grades) - na_count)}")