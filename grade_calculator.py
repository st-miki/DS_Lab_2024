score = float(input("Enter the student's score (0-100): "))

if score > 100 or score < 0:
    print("Invalid score. Please enter a score between 0 and 100.")
elif score >= 85:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 55:
    print("Grade: C")
elif score >= 40:
    print("Grade: D")
else:
    print("Grade: F")
