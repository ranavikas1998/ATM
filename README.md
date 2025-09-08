💳 ATM Simulation (Python)

A simple, menu-driven ATM simulation program written in Python.
This project allows users to create a PIN, change their PIN, check account balance, and withdraw money – all via a command-line interface (CLI).

✨ Features

Create PIN → Set a new PIN

Change PIN → Verify old PIN before setting a new one

Check Balance → View the current account balance

Withdraw Money → Withdraw cash if sufficient balance is available

Menu-driven CLI → Easy navigation with intuitive options

📂 Repository Contents

app.py → Main Python script containing ATM functionality

.idea/ → IDE (PyCharm/IntelliJ) settings (optional)

⚙️ Requirements

Python 3.x installed on your system

(This project only uses Python’s built-in libraries, no external dependencies required)

🚀 Getting Started

Clone this repository:

git clone https://github.com/ranavikas1998/ATM.git
cd ATM


Run the script:

python app.py

▶️ Run the Application

When you start the program (python app.py), you’ll see a menu like this:

----- ATM Menu -----
1. Create PIN
2. Change PIN
3. Check Balance
4. Withdraw Money
5. Exit
--------------------
Enter your choice:


👉 Just type the option number (1–5) to perform the respective action.

🔎 How It Works

Create PIN

User is prompted to set a 4-digit PIN.

This PIN is stored in memory (runtime only).

Change PIN

First, the system asks for the current PIN.

If entered correctly, the user can set a new PIN.

Check Balance

Displays the current balance of the account.

Default balance can be set inside app.py (e.g., ₹10,000).

Withdraw Money

Asks user to enter the withdrawal amount.

If sufficient funds exist, the balance is reduced.

Otherwise, a message shows “Insufficient Balance”.

Exit

Closes the program gracefully.

🧑‍💻 Example Usage
----- ATM Menu -----
1. Create PIN
2. Change PIN
3. Check Balance
4. Withdraw Money
5. Exit
--------------------
Enter your choice: 1
Set your new PIN: 1234
PIN created successfully!

Enter your choice: 3
Your balance is: ₹10000

Enter your choice: 4
Enter withdrawal amount: 2000
Transaction successful! New balance: ₹8000

📌 Notes

The data (PIN & balance) is stored temporarily in memory.

Once you exit the program, the data resets.

Future versions can add file/database storage for persistence.
