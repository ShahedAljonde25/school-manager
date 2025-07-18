
from data_manager import read_t_data ,write_t_data
from models import Employee
class EmployeeManager:
    def __init__(self):
        self.employee = read_t_data()

    def AddEmployee(self):
        name = input("Enter employee name: ")
        emp_id = int(input("Enter employee ID: "))
        pos = input("Enter employee position: ")
        salary = float(input("Enter salary: "))
        emp = Employee(emp_id, name, pos, salary)
        self.employee.append(emp)
        write_t_data(self.employee)
        print("Employee added successfully.")

    def searchemp(self):
        if self.employee:
            emp_id = int(input("Enter employee ID to search: "))
            for e in self.employee:
                if e.id == emp_id:
                    print(f"Name: {e.name}, ID: {e.id}, Position: {e.pos}, Salary: {e.salary}")
                    return
            print("Employee not found!")
        else:
            print("No employee data available.")

    def updataemp(self):
        if self.employee:
            try:
                emp_id = int(input("Enter employee ID to update: "))
                for e in self.employee:
                    if e.id == emp_id:
                        e.id = int(input("Enter new ID: "))
                        e.pos = input("Enter new position: ")
                        e.salary = float(input("Enter new salary: "))
                        write_t_data(self.employee)
                        print("Employee updated successfully.")
                        return
                print("Employee not found.")
            except ValueError:
                print("Invalid input.")
        else:
            print("No employee data available.")

    def deletemp(self):
        if self.employee:
            emp_id = int(input("Enter employee ID to delete: "))
            for e in self.employee:
                if e.id == emp_id:
                    self.employee.remove(e)
                    write_t_data(self.employee)
                    print("Employee deleted successfully.")
                    return
            print("Employee not found.")
        else:
            print("No employee data available.")