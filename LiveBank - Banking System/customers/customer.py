from accounts import base_account

class Customer:
    def __init__(self, name: str, phone: str, email: str):
        """Intialize name, phone, email attribute to instance."""
        self.name = name
        self.phone = phone
        self.email = email
    
    def add_account(self):
        """Add newly created account obj and connect it to last customer."""
        base_account.Savings
    
    def get_account(self):
        # Get full detail of account and print them in a very buitifull way
        pass
    
    def __str__(self):
        return f'Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}'
    



