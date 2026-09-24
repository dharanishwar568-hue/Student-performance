students = {
    "AID26001": "DHARANISHWAR",
    "AID26002": "HARISH",
    "AID26003": "ESWAR",
    "AID26004": "MANOJ",
    "AID26005": "JANARTHANAN",
    "AID26006": "ASHOK",
    "AID26007": "PRAVEEN",
    "AID26008": "KUMAR",
    "AID26009": "SURESH",
    "AID26010": "MUTHU"
}

def performance():
    marks = int(input("Enter marks: "))
    present = int(input("Enter present days: "))

    cgpa = marks / 300 * 10
    attendance = present / 150 * 100

    return cgpa, attendance
def grade(cgpa):
    if cgpa >= 9.0:
        print("GRADE : O")
    elif cgpa >= 8.0:
        print("GRADE : A+")
    elif cgpa >= 7.0:
        print("GRADE : A")
    elif cgpa >= 6.0:
        print("GRADE : P")
    else:
        print("GRADE : F")

def lab():
    marks = int(input("enter your lab marks: "))
    totalmarks = 100
    lab_present = int(input("enter your lab attendance: "))
    lab_attendance = lab_present / 50 * 100
    return marks, lab_attendance

roll = input("Enter roll number: ")

if roll in students:
    cgpa, attendance = performance()
    marks,lab_attendance=lab()
    print("==========STUDENT PERFORMANCE OF SEMESTER==========")
    print("Name:", students[roll])
    print("CGPA:", round(cgpa, 2))
    print("Attendance:", round(attendance, 2), "%")
    grade(cgpa)
    print("LAB MARKS = ", marks)
    print("LAB ATTENDANCE = ", lab_attendance)
    
else:
    print("Invalid Roll Number")