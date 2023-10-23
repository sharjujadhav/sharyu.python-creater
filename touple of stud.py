66.Create a tuple of student names and their scores, then find the student with
the highest score.

students = ["Kenny", "Irvin", "Ezra", "Joe"] 

highest = []
for student in students: 
    print(student, ", input your 3 grades:")
    D = int(input("Discussion: "))
    Q = int(input("Quiz: "))
    A = int(input("Assignment: "))
    wg1 = D * (.20) 
    wg2 = Q * (.30) 
    wg3 = A * (.50) 
    WeightGrade = wg1 + wg2 + wg3 
    highest.append(WeightGrade)
    print("The average grade for " ,student, " is:", WeightGrade)
    print('\n')
    
    max_highest = max(highest)
    if highest is None:
        print("nothing")
    else:
        print("The student with the highest grade is:" ,student, "with a"\
          ,max_highest, "average.")
        print('\n')
