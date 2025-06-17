'''
class Student: #parent/base class
    def __init__(self): #self contains object memory (s1) #function/method
        self.roll=int(input("Enter Roll ")) #s1.roll
        self.stname=input("Enter Name ") #s1.name
        self.marks=float(input("Enter Marks ")) #s1.marks

    def display_student(self): #function/method
        print(f'Roll:{self.roll} Name:{self.stname} Marks:{self.marks}')


class School(Student): #child/derived class #inheritance
    def __init__(self):
        super().__init__()  #student constructor calling
        self.id=int(input("Enter School ID "))
        self.sname=input("Enter School Name ")

    def display_school(self):
        print(f'ID:{self.id} Name:{self.sname}')

s1=School()
s1.display_student()
s1.display_school()
'''


class Company: #parent/base class
    def __init__(self):
        self.company_name=input("Enter Company Name ")
        self.company_address=input("Enter Company Address ")

    def display_company(self):
        print(f'Company Name:{self.company_name} Company Address:{self.company_address}')


class Employee(Company):
    def __init__(self):
        super().__init__() #company constructor calling
        self.id=int(input("Enter Employee ID "))
        self.ename=input("Enter Employee Name ")
        self.salary=float(input("Enter Employeee Salary "))

    def display_employee(self):
        print(f'ID:{self.id} Employee Name:{self.ename} Employee Salary:{self.salary}')

e1=Employee()
e1.display_company()
e1.display_employee()

        
        












