from abc import ABC, abstractmethod

class BankAccount(ABC):
    """a Abstract Base Class for bank accounts."""
    def __init__(self, account_holder: str, intial_balance: float = 0.0):
        """Intializing account holder and account balance attributes."""
        self.account_holder = account_holder
        self.account_balance = intial_balance
    
    @abstractmethod
    def deposite(self, amount: float):
        pass
    
    @abstractmethod
    def withdraw(self, amount: float):
        pass
    
    def add_transaction(self, transaction_type: str, amount: float):
        """A method that add transaction to DB."""
        # use sqlite or make your self your version and use it
    
    def get_transaction_history(self):
        """A method that get transaction data for that perticular user that in present."""
        # use sqlite data and get details for current user
    
    @property
    def balance(self):
        return self.account_balance
    
    @property
    def account_holder(self):
        return self.account_holder

    def __str__(self):
        return f'BankAccount[Holder: {self.account_holder}, Balance ₹{self.account_balance:,}]'

class SavingsAccount(BankAccount):
    """A blueprint for savings accounts."""
    def __init__(self, account_holder: str, intial_balance: float = 0.0):
        """Get BankAccount __init__ method and give its parameters as its need."""
        super().__init__(account_holder, intial_balance)
    
    def deposite(self, amount: float):
        """Deposit the amount and update it to DB."""
        self.account_holder += amount
        pass
    
    def withdraw(self, amount: float):
        """Withdraw the amount and update it to DB."""
        pass
    
    def add_interest(self):
        """Add interest as their time and update it to DB."""
        pass

class CurrentAccount(BankAccount):
    """A blueprint for current accounts."""
    def __init__(self, account_holder: str, intial_balance: float = 0.0):
        """Get BankAccount __init__ method and give its parameters as its need."""
        super().__init__(account_holder, intial_balance)
    
    def deposite(self, amount: float):
        """Deposit the amount and update it to DB."""
        pass
    
    def withdraw(self, amount: float):
        """Withdraw the amount and update it to DB."""
        pass