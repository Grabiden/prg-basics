# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
    [200, 50, 100],  # Week 1
    [180, 60, 110],  # Week 2
    [220, 55, 105],  # Week 3
    [210, 65, 95]    # Week 4
]

# Initialize totals
total_food = 0
total_transport = 0
total_utilities = 0
total_weekly_expenses = []
total_monthly_expenses = 0

# Calculate expenses
for week in monthly_expenses:
    week_total = sum(week)
    total_weekly_expenses.append(week_total)
    total_food += week[0]
    total_transport += week[1]
    total_utilities += week[2]
    total_monthly_expenses += week_total

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', total_food)
print('Transport:', total_transport)
print('Utilities:', total_utilities)
print('Week 1:', total_weekly_expenses[0])
print('Week 2:', total_weekly_expenses[1])
print('Week 3:', total_weekly_expenses[2])
print('Week 4:', total_weekly_expenses[3])
print('---------------')
print('TOTAL:', total_monthly_expenses)