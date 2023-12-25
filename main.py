grades = open("grades.txt").read().split("\n")

sum = 0
for i in grades:
    try:
        sum += float(i)
    except: # If we are not able to convert it to float then we will get a error massage. (NA)
        pass

print(f"Average: {sum / len(grades)}")
