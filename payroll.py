import csv
class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base = float(base_salary)
    def net_salary(self, allowances=0, deductions=0):
        return self.base + float(allowances) - float(deductions)

def export_payslips(employees, filename='payslips.csv'):
    with open(filename,'w',newline='',encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(['id','name','base','net'])
        for e in employees:
            w.writerow([e.emp_id, e.name, e.base, e.net_salary()])