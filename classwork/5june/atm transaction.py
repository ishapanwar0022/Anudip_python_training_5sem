# List of transactions
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Variables
balance = 0
deposits = []
withdrawals = []

# Traverse transaction list
for amount in transactions:

    # Calculate balance
    balance += amount

    # Separate deposits and withdrawals
    if amount > 0:
        deposits.append(amount)
    else:
        withdrawals.append(amount)

# Assume first deposit is largest
largest_deposit = deposits[0]

# Find largest deposit
for d in deposits:
    if d > largest_deposit:
        largest_deposit = d

# Assume first withdrawal is largest withdrawal
largest_withdrawal = withdrawals[0]

# Find largest withdrawal
for w in withdrawals:
    if w < largest_withdrawal:
        largest_withdrawal = w

# Display output
print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)