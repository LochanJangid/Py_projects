from customers import customer
from accounts import base_account
class Bank:
    """A Model for bank mangments."""
    def __init__(self, name: str):
        self.name = name
    
    def create_customer(self, name: str, phone: str, email: str):
        self.new_customer = customer.Customer(name, phone, email)
        print('create_customer method from bank/models.py')        
    
    def create_account(self, account_type: int, initial_balance: float = 0.0):
        if account_type == 1:
            return base_account.SavingsAccount(self.new_customer.name, initial_balance)
        if account_type == 2:
            return base_account.CurrentAccount(self.new_customer.name, initial_balance) 
        return False