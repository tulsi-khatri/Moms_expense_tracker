#Expense Tracker Project

expenses= [] # List of expenses in form of dictionary
print ("Welcome to expense tracker ")

while True:
    print("===MENU===")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Exit")

    choice = input("Please enter your choice:")
    
    #add expense
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


#view all expense
    elif(choice== "2"):
        if( len(expenses)==0):
            print("No expense added!")
        else:
            print("===== This is your expense=====")
            count = 1
            for expense in expenses:
                print(f"kharcha no.{count} : {expense['date']} , {expense['category']} , {expense['description']} , {expense['amount']}")
                
                count = count+1




#3 exit 
    elif(choice=="3"):
        print("Thank you for using our system.")
        break
    else:
        print("Invalid choice. Try again.")

# for basic display
import pandas as pd
print("===== This is your expense =====")
count = 1     #numbering k liye
for expense in expenses:
    print(f"kharcha no.{count} : {expense['date']} , {expense['category']} , {expense['description']} , {expense['amount']}")
    count +=1
#ab hum pandas use krege better analysis k liye (table bnane k liye)
df = pd.DataFrame(expenses)

print("\n===== Data Analysis =====")
total = df["amount"].sum()
print("Total Expense:" , total)

#category wise expense
category_total= df.groupby("category")["amount"].sum()       #"groupby"= same category ko group karta hai and ".sum"= har group ka total

print("\nCategory-wise Expense:")
print(category_total)

#for table view
print("\n==== Expense Table =====")
print(df)



