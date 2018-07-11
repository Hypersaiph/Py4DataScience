# CALCULATE
# - profit each month
# - profit after tax each month
# - profit margin for each month
# - good months
# - bad months
# - the best month
# - the worst month

# use 0.01 precision
# present units with , miles separator

# Data
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

# calculating profit (revenue - expenses)
profit = list([])
for i in range(0, len(revenue)):
    profit.append(revenue[i] - expenses[i])

# profit
print(profit)

# Calculating tax (profit * 30%)
tax = [round(i * 0.3, 2) for i in profit]
# tax
print(tax)

# profit after tax
profit_after_tax = list([])

for i in range(0, len(profit)):
    after_tax = profit[i]-tax[i]
    if after_tax <= 0:
        print("BAD month:", after_tax)
    else:
        print("GOOD month:", after_tax)
    profit_after_tax.append(after_tax)

print(profit_after_tax)

# best month
print(max(profit_after_tax))

# worst month
print(min(profit_after_tax))