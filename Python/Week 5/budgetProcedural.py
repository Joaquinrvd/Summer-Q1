funds = 2500
budgets = {}
expenses = {}
def addbudget(name, amount):
    global funds
    if name in budgets:
        raise ValueError("budget for item already exists")
    if amount > funds:
        raise ValueError("HEY!!! DONT YOU GET IT YOU ARE BROKE. GET SOME MONEY PEASENT!!!!🚫💵🗿🗿🗿🗿🗿")
    budgets[name] = amount
    funds -= amount
    #or funds -= amount
    expenses[name] = 0
    return funds

def Spend(name, amount):
    if name not in  expenses:
        raise ValueError("Item not in budget")
    expenses[name] += amount
    budgeted = budgets[name]
    spent = expenses[name]
    return budgeted - spent

def PrintBudget():
    print("  Budget             budgeted     Spent     Remaining")
    print("-------------------------------------------------------")
    totalBudgeted = 0
    totalSpent = 0
    totalRemaining = 0
    for name in budgets:
        budgeted = budgets[name]
        spent = expenses[name]
        remainingBuget = budgeted
        print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f}, '
               f'{remainingBuget:10.2f}')
        totalBudgeted += budgeted
        totalSpent += spent
        totalRemaining += remainingBuget
    print(f'{"Total":15}, {totalBudgeted:10.2f}, {totalSpent:10.2f}, '
          f'{totalBudgeted - totalSpent:10.2f}')


print("Total Funds: ", funds)
addbudget("Games", 60)
addbudget("Better PC", 1000)
addbudget("Crunchyroll+", 10)
addbudget("Rent(Homeless)", 0)

Spend("Games", 60)
Spend("Better PC", 200)
Spend("Crunchyroll+", 10)
Spend("Rent(Homeless)", 0)

PrintBudget()