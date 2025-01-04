class konto():
    def __init__(self, numer, balance):
        self.numer = numer
        self.balance = balance
    def deposit(self,funds):
        self.balance += funds
        return self.balance
    def withdraw(self,funds):
        if funds > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= funds
    def display_info(self):
        print(f"Account Number: {self.numer}")
        print(f"Balance: {self.balance}")
def main():
    account = konto("12 3456 5555 9090 1111 0000 7722",0)
    account.display_info()
    account.deposit(25.3)
    account.display_info()

main()    