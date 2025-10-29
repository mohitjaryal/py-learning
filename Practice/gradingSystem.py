# WAP to give Grades to students based on their marks
marks = int(input('Enter your total marks :'))
if(marks>=90):
    print("Grade A") 
elif(marks>=80 and marks < 90):
    print("Grade B")
elif(marks<=70 and marks < 80):
    print("Grade C")
else:
    print("You're FAIL")
