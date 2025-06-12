# atm.py
from account import Account
from transaction import Transaction
from storage import load_accounts, save_accounts

class ATM:
    def __init__(self):
        self.accounts = self._create_account_objects(load_accounts())
        self.current_account = None

    def _create_account_objects(self, accounts_data):
        accounts = {}
        for acc_no, details in accounts_data.items():
            acc = Account(
                acc_no=acc_no,
                name=details['name'],
                pin=details['pin'],
                balance=details['balance']
            )
            acc.transactions = [
                Transaction(t['type'], t['amount'], t['balance_after'])
                for t in details.get('transactions', [])
            ]
            accounts[acc_no] = acc
        return accounts

    def login(self, acc_no, pin):
        if acc_no in self.accounts and self.accounts[acc_no].verify_pin(pin):
            self.current_account = self.accounts[acc_no]
            return True
        return False

    def deposit(self, amount):
        self.current_account.balance += amount
        self._add_transaction("deposit", amount)
        return f"₹{amount} deposited. New balance: ₹{self.current_account.balance}"

    def withdraw(self, amount):
        if amount > self.current_account.balance:
            raise ValueError("Insufficient balance")
        self.current_account.balance -= amount
        self._add_transaction("withdraw", amount)
        return f"₹{amount} withdrawn. New balance: ₹{self.current_account.balance}"

    def _add_transaction(self, type, amount):
        new_trans = Transaction(type, amount, self.current_account.balance)
        self.current_account.transactions.append(new_trans)

    def mini_statement(self):
        statement = "\n📝 Mini Statement (Last 5):\n"
        for t in self.current_account.transactions[-5:]:
            statement += f"{t.timestamp} | {t.type.upper()} | ₹{t.amount}\n"
        return statement

    def save_data(self):
        accounts_data = {}
        for acc_no, acc in self.accounts.items():
            accounts_data[acc_no] = {
                "name": acc.name,
                "pin": acc._Account__pin,  # Access private PIN
                "balance": acc.balance,
                "transactions": [
                    {"type": t.type, "amount": t.amount, 
                     "timestamp": t.timestamp, "balance_after": t.balance_after}
                    for t in acc.transactions
                ]
            }
        save_accounts(accounts_data)