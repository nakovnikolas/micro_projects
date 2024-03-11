class BankAccount:
    def __init__(self, account_number: str, balance: int = 0) -> None:
        """
        Constructor method to initialize the account number and balance.
        """
        self.account_number: str = account_number
        self.balance: int = balance

    def deposit(self, amount: int) -> None:
        """
        Method to deposit money into the account.
        """
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        """
        Method to withdraw money from the account.
        """
        self.balance -= amount

    def get_balance(self) -> None:
        print(f"Your balance is: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(
                self,
                account_number: str,
                balance: float = 0,
                interest_rate: int = 0
    ) -> None:
        """
        Constructor method to initialize
        the account number, balance, and interest rate.
        """
        super().__init__(account_number, balance)
        self.interest_rate: int = interest_rate

    def calculate_interest(self) -> None:
        """
        Method to calculate and add interest to the account balance.
        """
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest

    def __repr__(self) -> str:
        balance_print = f"This savings account balance is: {int(self.balance)}"

        return balance_print


if __name__ == "__main__":
    bank = BankAccount("123456789", 1000)
    bank.deposit(500)
    bank.withdraw(200)
    bank.get_balance()
    sav_acc = SavingsAccount("987654321", 2000, 5)
    sav_acc.calculate_interest()
    print(sav_acc)
