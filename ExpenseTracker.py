print("**********EXPENSE TRACKER**********")

total_expense=0

while(True):
    expense=input("Enter the amount of expense:")

    if(expense=="quit"):
        break
    expense=int(expense)
    
    total_expense=total_expense+expense

print("The total expenses are:", total_expense)