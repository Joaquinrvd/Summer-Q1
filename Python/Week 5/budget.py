# Your task is to convert this program into a class 
# 1. Define your class 
# 2. Create your __init__() for your class 
# 3. Ceate your instance variable 
# 4. Refactor your code into a class 
# 5. Create a new python file called tester.py 
# 6. inport your budget class into your tester file 
# 7. Paste your tester code into the tester file 
# 8. Create an instance of your class named budget


class BudgetManager:
    def __init__(self, starting_funds):
        self.funds = starting_funds
        self.budgets = {}
        self.expenses = {}

    def add_budget(self, name, amount):
        if name in self.budgets:
            raise ValueError("Budget for item already exists")
        if amount > self.funds:
            raise ValueError("HEY!!! DONT YOU GET IT YOU ARE BROKE. GET SOME MONEY PEASANT!!!!🚫💵🗿🗿🗿🗿🗿")
        self.budgets[name] = amount
        self.funds -= amount
        self.expenses[name] = 0
        return self.funds

    def spend(self, name, amount):
        if name not in self.expenses:
            raise ValueError("Item not in budget")
        self.expenses[name] += amount
        budgeted = self.budgets[name]
        spent = self.expenses[name]
        return budgeted - spent

    def print_budget(self):
        print("  Budget             Budgeted     Spent     Remaining")
        print("-------------------------------------------------------")
        total_budgeted = 0
        total_spent = 0
        for name in self.budgets:
            budgeted = self.budgets[name]
            spent = self.expenses[name]
            remaining = budgeted - spent
            print(f'{name:20s} {budgeted:10.2f} {spent:10.2f} {remaining:10.2f}')
            total_budgeted += budgeted
            total_spent += spent
        total_remaining = total_budgeted - total_spent
        print("-------------------------------------------------------")
        print(f'{"Total":20s} {total_budgeted:10.2f} {total_spent:10.2f} {total_remaining:10.2f}')

manager = BudgetManager(2500)
print("Total Funds:", manager.funds)

manager.add_budget("Games", 60)
manager.add_budget("Better PC", 100)
manager.add_budget("Crunchyroll+", 10)
manager.add_budget("Rent(Homeless)", 2000)

manager.spend("Games", 60)
manager.spend("Better PC", 2000)
manager.spend("Crunchyroll+", 10)
manager.spend("Rent(Homeless)", 0)

manager.print_budget()
