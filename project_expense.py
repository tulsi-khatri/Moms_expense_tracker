expenses= [] 
print ("Welcome to expense tracker ")

while True:
    print("===MENU===")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Exit")

    choice = input("Please enter your choice:")
    
    
    if (choice =="1"):
        date = input(" Enter the date of the expense:")
        category = input("Enter the categroy: (Food , Travel , Makeup , Books)")
        description = input ("Enter the description:")
        amount = float(input ("Enter the amount:"))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }


        expenses.append(expense)
        print("Expenses adding succesfully.")



    elif(choice== "2"):
        if( len(expenses)==0):
            print("No expense added!")
        else:
            print("===== This is your expense=====")
            count = 1
            for expense in expenses:
                print(f"kharcha no.{count} : {expense['date']} , {expense['category']} , {expense['description']} , {expense['amount']}")
                
                count = count+1




 
    elif(choice=="3"):
        print("Thank you for using our system.")
        break
    else:
        print("Invalid choice. Try again.")


import pandas as pd
print("===== This is your expense =====")
count = 1     
for expense in expenses:
    print(f"kharcha no.{count} : {expense['date']} , {expense['category']} , {expense['description']} , {expense['amount']}")
    count +=1

df = pd.DataFrame(expenses)

print("\n===== Data Analysis =====")
total = df["amount"].sum()
print("Total Expense:" , total)


category_total= df.groupby("category")["amount"].sum()       

print("\nCategory-wise Expense:")
print(category_total)


print("\n==== Expense Table =====")
print(df)



