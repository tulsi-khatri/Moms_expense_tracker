->Overview:

This is a simple command-line based Expense Tracker built using Python. It helps users record daily expenses, categorize them, and view basic spending analysis. The project demonstrates fundamental Python concepts along with basic data analysis using Pandas.


->Features:
.Add new expenses with date, category, description, and amount
.View all recorded expenses in a structured format
.Simple menu-driven interface
.Basic financial summary
.Category-wise expense analysis using Pandas
.Displays complete expense table


->Technologies Used:
.Python
.Pandas


->How It Works:
1. The user runs the program.
2. A menu appears with options:
  -Add Expense
  -View Expenses
  -Exit
3. All expenses are stored in a Python list as dictionaries.
4. After exiting, data is converted into a Pandas DataFrame.
5. Basic analysis is performed:
  -Total expense calculation
  -Category-wise spending
  -Tabular representation of all data

   
->How to Run:
Install dependencies using `pip install pandas` and run the application with `python project_expense.py` in the terminal.

  
Sample Output:

Total Expense: 2500

Category-wise Expense:
Food      1200
Travel     800
Books      500

Expense Table:
       date     category   description   amount
0  2026-04-19   Food       Lunch         300
1  2026-04-19   Travel     Bus fare      200



->Future Improvements:
.Save data to CSV file
.Load previous expenses automatically
.Add graphs for visualization (Matplotlib)
.Monthly expense summary
.Budget limit alerts



->Author:
Tulsi Khatri
BTech Student | Python & AI/ML Enthusiast
