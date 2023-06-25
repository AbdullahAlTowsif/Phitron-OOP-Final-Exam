class Bank:
    def __init__(self) -> None:
        self.accounts = []
        self.total_balance = 0
        self.clients_loan_amount = 0
        self.enabled_loan = True

    def create_new_account(self,name):
        account = Account(name)
        self.accounts.append(account)
        return account
    
    def get_account(self,name):
        for account in self.accounts:
            if account.name == name:
                return account
        return 'Bhag Yeahase!!'
    
    def get_total_balance(self):
        return self.total_balance
    
    def get_total_loan_amount(self):
        return self.clients_loan_amount
    
    def enable_loan(self):
        self.enabled_loan = True

    def disable_loan(self):
        self.enabled_loan = False

class Account:
    def __init__(self,name) -> None:
        self.name = name
        self.balance = 0
        self.clients_trans_history = []

    def deposit(self,amount):
        self.balance += amount
        self.clients_trans_history.append(f'Deposited balance: {amount}')

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            self.clients_trans_history.append(f'Withdrawn balance: {amount}')
        else:
            print('Insufficient Balance')

    def transferred_amount(self,amount,recpt):
        if self.balance >= amount:
            self.balance -= amount
            recpt.deposit(amount)
            self.clients_trans_history.append(f'Transferred: {amount} to {recpt.name}')
        else:
            print('Insufficient Balance')

    def take_loan(self,bank):
        if bank.enabled_loan:
            loan_amount = self.balance * 2
            self.balance += loan_amount
            bank.clients_loan_amount += loan_amount
            self.clients_trans_history.append(f'Loan Taken: {loan_amount}')
        else:
            print('Loan Disabled')

    def check_balance(self):
        return self.balance
    
    def transaction_history(self):
        return self.clients_trans_history
    

bank = Bank()
client1 = bank.create_new_account('Chulbul Pandey')
client2 = bank.create_new_account('Babu Rao')

client1.deposit(50000)
client1.withdraw(200)

client1.transferred_amount(700,client2)
client2.transferred_amount(1300,client2)

print(f'{client2.name} current balance {client2.check_balance()}')

client1.take_loan(bank)

print(f'{client1.name} current balance: {client1.check_balance()}')
print(client1.transaction_history())

print(bank.get_total_balance())
print(bank.get_total_loan_amount())
bank.disable_loan()