class Employee:
    """Class representing an employee that can exist independently."""
    
    def __init__(self, name: str, emp_id: str):
        """Initialize employee with name and ID.
        
        Args:
            name: Employee name
            emp_id: Unique employee identifier
        """
        self.name = name
        self.emp_id = emp_id
        self.department = None  # Track department assignment

    def assign_to_department(self, department) -> None:
        """Assign this employee to a department."""
        self.department = department
        print(f"{self.name} assigned to {department.dept_name}")

    def __str__(self) -> str:
        """String representation of employee."""
        dept = self.department.dept_name if self.department else "Unassigned"
        return f"Employee {self.name} (ID: {self.emp_id}) - Department: {dept}"

class Department:
    """Class representing a department that can aggregate employees."""
    
    def __init__(self, dept_name: str):
        """Initialize department with name and empty employee list."""
        self.dept_name = dept_name
        self.employees = []  # List of aggregated employees

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to this department.
        
        Args:
            employee: Employee object to add
        """
        if employee not in self.employees:
            self.employees.append(employee)
            employee.assign_to_department(self)
        else:
            print(f"{employee.name} is already in {self.dept_name}")

    def list_employees(self) -> None:
        """Print all employees in this department."""
        print(f"\nEmployees in {self.dept_name}:")
        for emp in self.employees:
            print(f"- {emp.name} (ID: {emp.emp_id})")

# Usage
it_dept = Department("Information Technology")
hr_dept = Department("Human Resources")

emp1 = Employee("Ali Khan", "E1001")
emp2 = Employee("Sara Ahmed", "E1002")

# Add employees to departments
it_dept.add_employee(emp1)  # Output: Ali Khan assigned to Information Technology
hr_dept.add_employee(emp2)  # Output: Sara Ahmed assigned to Human Resources

# Try adding same employee again
it_dept.add_employee(emp1)  # Output: Ali Khan is already in Information Technology

# List department employees
it_dept.list_employees()
hr_dept.list_employees()

# Print employee info
print("\n" + str(emp1))
print(str(emp2))
#NOTES:
#Here, Employee exists on its own, and we just pass it into Department.
#It’s like saying: “Ali works in IT.” But Ali can exist without IT.