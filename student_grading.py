def gradeCalc(pct):
    if pct >= 90:
        return "A+"
    elif pct >= 80:
        return "A"
    elif pct >= 70:
        return "B"
    elif pct >= 60:
        return "C"
    elif pct >= 50:
        return "D"
    else:
        return "F"


print("Report Card Generator")
studentName = input("Name of student: ")
numSubs = int(input("Number of subjects: "))

subs = []
totalMarks = 0
totalMax = 0

for i in range(numSubs):
    sname = input(f"\nSubject {i+1}: ")
    got = int(input(f"Marks scored in {sname}: "))
    maxm = input("Max marks (press enter if 100): ")
    if maxm.strip() == "":
        maxm = 100
    else:
        maxm = int(maxm)

    perc = (got / maxm) * 100
    subs.append([sname, got, maxm, perc, gradeCalc(perc)])

    totalMarks += got
    totalMax += maxm

overallPerc = (totalMarks / totalMax) * 100

print("\n--- Result ---")
for s in subs:
    print(f"{s[0]} : {s[1]}/{s[2]}  --> {s[3]:.1f}% Grade {s[4]}")

print("-------------")
print("Total:", totalMarks, "/", totalMax)
print("Overall %:", round(overallPerc, 2))
print("Final Grade:", gradeCalc(overallPerc))
