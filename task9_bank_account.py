class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        # 1. Private variable (Encapsulation)
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f" Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print(" Invalid deposit amount.")

    # 2. Withdraw securely
    def withdraw(self, amount):
        if amount <= 0:
            print(" Invalid withdrawal amount.")
        elif amount > self.__balance:
            print(f" Insufficient funds. Your balance is only ₹{self.__balance}.")
        else:
            self.__balance -= amount
            print(f" Withdrew ₹{amount}. New balance: ₹{self.__balance}")

    # 3. Securely view the balance
    def get_balance(self):
        return self.__balance


# --- Testing the Bank ---

# 4. Create an account
my_account = BankAccount("Rajath", 5000)

print(f"Welcome, {my_account.account_holder}!")

# This works securely!
my_account.deposit(1500)

#  UNCOMMENTING THIS WOULD CAUSE AN ERROR! The balance is protected.
# print(my_account.__balance)

# --- Test new methods ---
my_account.withdraw(2000)       # Should work!
my_account.withdraw(10000)      # Should fail (Insufficient funds)
print(f"Final Balance: ₹{my_account.get_balance()}")