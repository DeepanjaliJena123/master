class BankingSystem:
    def __init__(self):
        self.accounts = {}
        self.transactions = {}

    def create_account(self, account_id):
        if account_id in self.accounts:
            return "false"
        self.accounts[account_id] = 0
        self.transactions[account_id] = 0
        return "true"

    def deposit(self, account_id, amount):
        if account_id not in self.accounts:
            return ""
        self.accounts[account_id] += amount
        self.transactions[account_id] += amount
        return str(self.accounts[account_id])

    def pay(self, account_id, amount):
        if account_id not in self.accounts or self.accounts[account_id] < amount:
            return ""
        self.accounts[account_id] -= amount
        self.transactions[account_id] += amount
        return str(self.accounts[account_id])

    def top_activity(self, n):
        sorted_accounts = sorted(self.transactions.items(), key=lambda item: item[1], reverse=True)
        top_accounts = sorted_accounts[:n]
        result = [f"{acc} ({self.accounts[acc]})" for acc, _ in top_accounts]
        return ", ".join(result)

def process_queries(queries):
    bank = BankingSystem()
    results = []

    for query in queries:
        operation = query[0]

        if operation == "CREATE_ACCOUNT":
            _, timestamp, account_id = query
            result = bank.create_account(account_id)
            results.append(result)

        elif operation == "DEPOSIT":
            _, timestamp, account_id, amount = query
            amount = int(amount)
            result = bank.deposit(account_id, amount)
            results.append(result)

        elif operation == "PAY":
            _, timestamp, account_id, amount = query
            amount = int(amount)
            result = bank.pay(account_id, amount)
            results.append(result)

        elif operation == "TOP_ACTIVITY":
            _, timestamp, n = query
            n = int(n)
            result = bank.top_activity(n)
            results.append(result)

    return results

def solution(queries):
    return process_queries(queries)

# Example usage:
queries = [
    ["CREATE_ACCOUNT", "1", "account1"],
    ["CREATE_ACCOUNT", "2", "account2"],
    ["CREATE_ACCOUNT", "3", "account3"],
    ["DEPOSIT", "4", "account1", "2000"],
    ["DEPOSIT", "5", "account2", "3000"],
    ["DEPOSIT", "6", "account3", "4000"],
    ["TOP_ACTIVITY", "7", "3"],
    ["PAY", "8", "account1", "1500"],
    ["PAY", "9", "account2", "250"],
    ["DEPOSIT", "10", "account3", "250"],
    ["TOP_ACTIVITY", "11", "3"]
]

results = solution(queries)

print(results)
