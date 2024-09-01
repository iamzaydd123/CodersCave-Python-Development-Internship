def get_income():
    income = float(input("Enter your monthly income: "))
    return income

def get_expenses():
    expenses = {}
    while True:
        category = input("Enter expense category (or type 'done' to finish): ")
        if category.lower() == 'done':
            break
        amount = float(input("Enter amount for {}: ".format(category)))
        expenses[category] = amount
    return expenses

def get_savings_goal():
    savings_goal = float(input("Enter your monthly savings goal: "))
    return savings_goal

def calculate_budget(income, expenses, savings_goal):
    total_expenses = sum(expenses.values())
    remaining_balance = income - total_expenses - savings_goal
    return total_expenses, remaining_balance

def display_budget_summary(income, total_expenses, savings_goal, remaining_balance):
    print("\n--- Budget Summary ---")
    print("Income: Rs. {:.2f}".format(income))
    print("Total Expenses: Rs. {:.2f}".format(total_expenses))
    print("Savings Goal: Rs. {:.2f}".format(savings_goal))
    print("Remaining Balance: Rs. {:.2f}".format(remaining_balance))
    
    if remaining_balance > 0:
        print("Great! You have met your savings goal and have Rs. {:.2f} left.".format(remaining_balance))
    elif remaining_balance == 0:
        print("Good job! You have met your savings goal exactly.")
    else:
        print("Warning! You are over your budget by Rs. {:.2f}.".format(abs(remaining_balance)))

def main():
    print("Welcome to the Budget Planner!\n")

    income = get_income()
    expenses = get_expenses()
    savings_goal = get_savings_goal()

    total_expenses, remaining_balance = calculate_budget(income, expenses, savings_goal)
    
    display_budget_summary(income, total_expenses, savings_goal, remaining_balance)

if __name__ == "__main__":
    main()
