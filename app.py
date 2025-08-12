class ATM:
    def __init__(self):
        self.pin = None
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
================ ATM MENU ================
1. Create PIN
2. Change PIN
3. Check Balance
4. Withdraw
5. Exit
===========================================
Enter your choice: """).strip()

            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.change_pin()
            elif user_input == "3":
                self.check_balance()
            elif user_input == "4":
                self.withdraw()
            elif user_input == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

    def create_pin(self):
        if self.pin is not None:
            print("PIN already created! Use option 2 to change it.")
            return
        self.pin = input("Enter new PIN: ").strip()
        while not self.pin.isdigit() or len(self.pin) != 4:
            print("PIN must be a 4-digit number.")
            self.pin = input("Enter new PIN: ").strip()

        try:
            self.balance = float(input("Enter initial balance: "))
            if self.balance < 0:
                raise ValueError
        except ValueError:
            print("Invalid balance! Setting balance to 0.")
            self.balance = 0

        print("PIN created successfully.")

    def change_pin(self):
        if not self.verify_pin():
            return
        new_pin = input("Enter new PIN: ").strip()
        while not new_pin.isdigit() or len(new_pin) != 4:
            print("PIN must be a 4-digit number.")
            new_pin = input("Enter new PIN: ").strip()
        self.pin = new_pin
        print("PIN changed successfully.")

    def check_balance(self):
        if not self.verify_pin():
            return
        print(f"Your balance is: ₹{self.balance:.2f}")

    def withdraw(self):
        if not self.verify_pin():
            return
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Withdrawal amount must be positive.")
            elif amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal successful! Remaining balance: ₹{self.balance:.2f}")
            else:
                print("Insufficient balance.")
        except ValueError:
            print("Invalid amount entered.")

    def verify_pin(self):
        if self.pin is None:
            print("PIN not created yet. Please create a PIN first.")
            return False
        entered_pin = input("Enter your PIN: ").strip()
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN.")
            return False


# Run the ATM
if __name__ == "__main__":
    ATM()