grades = open("grades.txt").read().split("\n")

sum = 0
for i in grades:
    try:
        sum += float(i)
    except:
        pass

print(f"Average: {sum/len(grades)}")