class Student:
    def __init__(self, sid, name, m1, m2, m3, birth_year, fee_paid):
        self.sid = sid
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.birth_year = birth_year
        self.fee_paid = fee_paid
        self.total_fee = 50000

    def calculate_cgpa(self):
        avg = (self.m1 + self.m2 + self.m3) / 3
        return (avg / 10)

    def calculate_age(self):
        return (2026 - self.birth_year)

    def calculate_fee_balance(self):
        return (self.total_fee - self.fee_paid)
    def print_studentdetails(self):
        print("Student ID:", self.sid)
        print("Name:", self.name)
        print("CGPA:", round(self.calculate_cgpa(), 2))
        print("Age:", self.calculate_age())
        print("Fee Balance:", self.calculate_fee_balance())
class College:
    def __init__(self, code, name, location, s1, s2, s3):
        self.college_code = code
        self.college_name = name
        self.location = location
        # Directly assigning the 3 student objects
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def display_report(self):
        print("COLLEGE DETAILS")
        print("Name:", self.college_name)
        print("Code:", self.college_code)
        print("Location:", self.location)
        print("STUDENT ACADEMIC REPORT:")       
        self.s1.print_studentdetails()
        self.s2.print_studentdetails()
        self.s3.print_studentdetails()
# --- Execution ---
# 1. Create three objects for Student class
std1 = Student(50, "SUJITH", 90, 90, 90, 2006, 30000)
std2 = Student(102, "Jashu", 60, 70, 70, 2006, 50000)
std3 = Student(103, "Reshma", 80, 80, 80, 2006, 50000)
# 2. Create one object for College class and pass the 3 students
my_college = College("ANES001", "ANITS", "Visakhapatnam", std1, std2, std3)
# 3. Display report
my_college.display_report()
