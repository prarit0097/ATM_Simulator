class Account():
    def __init__(self,acc_no,name,pin,balance=0):
        self.acc_no = acc_no
        self.name= name
        self.__pin = pin    # Encapsulated PIN
        self.balance = balance
        self.transactions = {}

    def verify_pin(self,pin):
        return self.__pin == pin

    def update_pin(self,new_pin):
        self.__pin = new_pin
        return "✅ PIN updated successfully!"