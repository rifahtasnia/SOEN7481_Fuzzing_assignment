import random

def validate_user(username, password):
    if not isinstance(username, str) or not isinstance(password, str):
        return "Invalid username or password type."
    if len(username) < 3 or len(password) < 5:
        return "Username or password too short."
    return "Valid user"

def validate_transaction(amount, currency, operation):
    if not isinstance(amount, (int, float)):
        return "Invalid amount type."
    if amount < 0:
        return "Amount cannot be negative."
    supported_currencies = ["USD", "EUR", "GBP", "INR"]
    if currency not in supported_currencies:
        return f"Unsupported currency: {currency}."
    if operation not in ["deposit", "withdraw", "transfer"]:
        return "Invalid operation."
    return "Valid transaction"

def process_transaction(user_input):
    if not isinstance(user_input, dict):
        return "Invalid input: Expected dictionary."

    username = user_input.get("username")
    password = user_input.get("password")
    amount = user_input.get("amount", 0)
    currency = user_input.get("currency", "USD")
    operation = user_input.get("operation", "deposit")
    recipient = user_input.get("recipient", None)

    user_status = validate_user(username, password)
    if user_status != "Valid user":
        return user_status

    transaction_status = validate_transaction(amount, currency, operation)
    if transaction_status != "Valid transaction":
        return transaction_status

    balance = random.randint(50, 500)  # Simulating stored balance
    transaction_log = []

    if operation == "deposit":
        balance += amount
        transaction_log.append(f"Deposited {amount} {currency}")
    elif operation == "withdraw":
        if amount > balance:
            return "Insufficient balance."
        balance -= amount
        transaction_log.append(f"Withdrew {amount} {currency}")
    elif operation == "transfer":
        if not isinstance(recipient, str) or len(recipient) < 3:
            return "Invalid recipient for transfer."
        if amount > balance:
            return "Insufficient balance for transfer."
        balance -= amount
        transaction_log.append(f"Transferred {amount} {currency} to {recipient}")

    # Validation on transaction limit
    if balance > 1000:
        return "Maximum balance limit exceeded."

    return {"status": "success", "new_balance": balance, "transactions": transaction_log}



test_inputs = [
    {"username": "Alice", "password": "pass123", "amount": 50, "currency": "USD", "operation": "deposit"},
    {"username": "Bob", "password": "123", "amount": 30, "currency": "EUR", "operation": "withdraw"},
    {"username": "Charlie", "password": "securepass", "amount": 200, "currency": "GBP", "operation": "transfer", "recipient": "Dave"},
    {"username": "Dave", "password": "testpass", "amount": -20, "currency": "INR", "operation": "deposit"},
    {"username": 123, "password": 456, "amount": 10, "currency": "USD", "operation": "deposit"},
    {"username": "Eve", "password": "mypassword", "amount": 9999, "currency": "USD", "operation": "withdraw"},
    "not a dictionary"
]

test_results = {str(test): process_transaction(test) for test in test_inputs}

test_results