
physics_marks = int(input("enter marks of physics"))
math_marks = int(input("enter marks of Mathematics"))
chemistry_marks = int(input("enter marks of chemistry"))
computer_marks = int(input("enter marks of computer"))
bio_marks = int(input("enter marks of biology"))

sum_of_marks = physics_marks + math_marks + chemistry_marks + computer_marks + bio_marks'
percentage = sum_of_marks / 5

if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 50:
    print("Grade E")
else:
    print("Grade F")

# Write a program to input month number and print number of days in that month.
