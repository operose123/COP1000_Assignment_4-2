employeeBonus = 0.0
productivityScore = 0.0

employeeName = str(input("Please enter the employee's name:"))
shiftCount = int(input("Enter employee's number of shifts completed:"))
transactionCount = int(input("Enter employee's number of transactions made:"))
transactionDollarValue = float(input("Enter employee's total transaction amount:"))

productivityScore = (transactionDollarValue/transactionCount)/shiftCount
if productivityScore <= 30.0:
  employeeBonus = 50.0
else:
  if productivityScore >= 31.0 and productivityScore <= 69.0:
    employeeBonus = 75.0
  else:
    if productivityScore >= 70.0 and productivityScore <= 199.0:
      employeeBonus = 100.0  
    else:
      employeeBonus = 200.00

print(f"Employee's Name: {employeeName}")
print(f"Employee's Bonus: ${employeeBonus}")
