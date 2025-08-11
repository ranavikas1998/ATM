class  Atm:
    def  __init__(self):
        self.pin=''
        self.balance=''
        self.menu()

    def menu(self):
        user_input=input("""
        hi  may  I  help  you?
        1. Press  1  to create  pin.
        2. Press  2  change  pin.
        3.Press to  check balance.
        4. Press  to withdraw 
        5. Anything  else  to  exit.
        """)

        if  user_input =="1":
            self.create_pin()
        elif user_input=="2":
            self.change_pin()
        elif user_input=="3":
            self.check_balance()
        elif  user_input=="4":
            self.withdraw()
    def  create_pin(self):
        user_pin=input("enter  your  pin")
        self.pin=user_pin

        user_balance=int(input("enter  your balance"))
        self.balance=user_balance
        print("pin created  successfully")
        self.menu()

    def  change_pin(self):
        old_pin=input("enter  old  pin")
        if old_pin==self.pin:
            new_pin=input("enter  new pin")
            self.pin=new_pin
            print("pin changed  successfully")
            self.menu()
        else:
            print("wrong  pin entered")
            self.menu()
    def  check_balance(self):
        user_pin=input("enter  your  pin")
        if user_pin==self.pin:
            print("your balance  is:",self.balance)
            self.menu()
        else:
            print("wrong  pin entered")
            self.menu()

    def  withdraw(self):
        user_pin=input("enter  your  pin")
        if user_pin==self.pin:
            amount=int(input("enter amount to withdraw"))
            if amount<=self.balance:
                self.balance=self.balance-amount
                print("withdrwal successfull.balace is:" ,self.balance)
                self.menu()
            else:
                print("below balance")
                self.menu()
        else:
            print("wrong amount entered")
            self.menu()

obj = Atm()
