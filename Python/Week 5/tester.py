import budget

manager = budget.BudgetManager(2500)

manager.add_budget("Games", 60)
manager.add_budget("Better PC", 100)
manager.add_budget("Crunchyroll+", 10)
manager.add_budget("Rent(Homeless)", 2000)

manager.spend("Games", 60)
manager.spend("Better PC", 2000)
manager.spend("Crunchyroll+", 10)
manager.spend("Rent(Homeless)", 0)

manager.print_budget()