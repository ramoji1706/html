#54. names  ="emp1,emp2,emp3,emp4" iterate through the employee names.

names = "ram,akhil,surya,sangeeth,kashi,dinesh"

employeeNames= names.split(',')
for employee in employeeNames:
    print(employee)