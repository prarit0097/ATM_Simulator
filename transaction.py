from datetime import datetime

class Transaction():
    def __init__(self,type,amount,balance_after):
        self.timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.type = type
        self.amount =amount
        self.balance_after = balance_after