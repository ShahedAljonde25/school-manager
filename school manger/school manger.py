
from employee_manager import EmployeeManager 

from student_manager import StudentManager
def main():
    student_mgr = StudentManager()
    employee_mgr = EmployeeManager()

    while True:
        print("""
======== School Management System ========
1 - Student management
2 - Employee management
3 - exit              
""")
        choix = input("Enter your choice: ")
        if choix == "1":
            print("""
====== Student Manager ======
1) Add student
2) Delete student
3) Search student
""")
            sub = input("Enter your choice: ")
            if sub == "1":
                student_mgr.addstudant()
            elif sub == "2":
                student_mgr.deletstd()
            elif sub == "3":
                student_mgr.scarhe_std()
            else:
                print("Invalid choice.")
        elif choix == "2":
            print("""
====== Employee Manager ======
1) Add employee
2) Delete employee
3) Update employee
4) Search employee
""")
            sub = input("Enter your choice: ")
            if sub == "1":
                employee_mgr.AddEmployee()
            elif sub == "2":
                employee_mgr.deletemp()
            elif sub == "3":
                employee_mgr.updataemp()
            elif sub == "4":
                employee_mgr.searchemp()
            else:
                print("Invalid choice.")
        elif choix =="3":
            break        
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
