# Композиция
MONTHS_IN_YEAR = 12


class Salary:
    def __init__(self, month_pay):
        self.month_pay = month_pay

    def year_salary(self):
        return self.month_pay * MONTHS_IN_YEAR

class Employee:

    def __init__(self, pay, bonus):
        #self.pay = pay
        self.bonus = bonus
        self.salary = Salary(pay)

    def annual_salary(self):
        return self.salary.year_salary() + self.bonus


employee = Employee(pay=5000, bonus=1000)
annual_salary = employee.annual_salary()
print(annual_salary)
