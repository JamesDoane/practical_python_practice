expenses = []
total = sum(expenses)

# for x in expenses:
#     sum += x
for i in range(7):
    expenses.append(input("how much did you spend on lunch on each day"))


print("you spent $", total, " on lunch this week", sep='')