import mysql.connector
import random
from datetime import datetime, timedelta

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="ApnaBank"
)
cursor = conn.cursor()

cursor.execute("""
INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber, PreferredLanguage)
VALUES 
('Rahul', 'Sharma', 'rahul.sharma@example.com', '9876543210', 'Hindi'),
('Priya', 'Verma', 'priya.verma@example.com', '8765432109', 'English'),
('Amit', 'Patel', 'amit.patel@example.com', '7654321098', 'Gujarati'),
('Sita', 'Kumar', 'sita.kumar@example.com', '6543210987', 'Hindi'),
('Ravi', 'Singh', 'ravi.singh@example.com', '5432109876', 'Punjabi'),
('Anjali', 'Mehta', 'anjali.mehta@example.com', '4321098765', 'Marathi'),
('Vikram', 'Rao', 'vikram.rao@example.com', '3210987654', 'Telugu'),
('Neha', 'Gupta', 'neha.gupta@example.com', '2109876543', 'Bengali'),
('Arjun', 'Nair', 'arjun.nair@example.com', '1098765432', 'Malayalam'),
('Kavita', 'Desai', 'kavita.desai@example.com', '0987654321', 'Kannada');
""")

# Insert dummy data into Accounts table
cursor.execute("""
INSERT INTO Accounts (CustomerID, AccountNumber, AccountType, Balance, Password)
VALUES 
(1, '1234567890123456', 'Savings', 1000.00, 'password123'),
(2, '2345678901234567', 'Checking', 2000.00, 'password123'),
(3, '3456789012345678', 'Credit', 3000.00, 'password123'),
(4, '4567890123456789', 'Savings', 1500.00, 'password123'),
(5, '5678901234567890', 'Checking', 2500.00, 'password123'),
(6, '6789012345678901', 'Savings', 3500.00, 'password123'),
(7, '7890123456789012', 'Checking', 4500.00, 'password123'),
(8, '8901234567890123', 'Credit', 5500.00, 'password123'),
(9, '9012345678901234', 'Savings', 6500.00, 'password123'),
(10, '0123456789012345', 'Checking', 7500.00, 'password123');
""")
# Insert dummy data into Transactions table
transaction_types = ['Deposit', 'Withdrawal', 'Transfer', 'Payment']
descriptions = ['Initial deposit', 'ATM withdrawal', 'Transfer to another account', 'Bill payment']

for i in range(500):
    account_id = random.randint(1, 10)
    transaction_type = random.choice(transaction_types)
    amount = round(random.uniform(10.00, 1000000.00), 2)
    description = random.choice(descriptions)
    timestamp = datetime.now() - timedelta(days=random.randint(0, 365))
    cursor.execute("""
    INSERT INTO Transactions (AccountID, TransactionType, Amount, Timestamp, Description)
    VALUES (%s, %s, %s, %s, %s);
    """, (account_id, transaction_type, amount, timestamp, description))

# Insert dummy data into Cards table
cursor.execute("""
INSERT INTO Cards (AccountID, CardNumber, ExpiryDate, CVV, CardType, Status)
VALUES 
(1, '1111222233334444', '2025-12-31', 123, 'Debit', 'Active'),
(2, '5555666677778888', '2024-11-30', 456, 'Credit', 'Active'),
(3, '9999000011112222', '2023-10-31', 789, 'Debit', 'Blocked'),
(4, '2222333344445555', '2026-01-31', 321, 'Debit', 'Active'),
(5, '6666777788889999', '2025-02-28', 654, 'Credit', 'Active'),
(6, '3333444455556666', '2025-03-31', 987, 'Debit', 'Active'),
(7, '7777888899990000', '2024-04-30', 654, 'Credit', 'Active'),
(8, '4444555566667777', '2023-05-31', 321, 'Debit', 'Blocked'),
(9, '8888999900001111', '2026-06-30', 123, 'Credit', 'Active'),
(10, '0000111122223333', '2025-07-31', 456, 'Debit', 'Active');
""")

# Insert dummy data into Reports table
cursor.execute("""
INSERT INTO Reports (CustomerID, ReportType, Description, ReportStatus)
VALUES 
(1, 'Lost Card', 'Lost my debit card', 'Pending'),
(2, 'Fraudulent Transaction', 'Unauthorized transaction detected', 'In Progress'),
(3, 'General Query', 'Inquiry about loan options', 'Resolved'),
(4, 'Lost Card', 'Lost my credit card', 'Resolved'),
(5, 'Fraudulent Transaction', 'Suspicious activity on account', 'Pending'),
(6, 'General Query', 'Inquiry about account balance', 'Resolved'),
(7, 'Lost Card', 'Lost my debit card', 'Pending'),
(8, 'Fraudulent Transaction', 'Unauthorized transaction detected', 'In Progress'),
(9, 'General Query', 'Inquiry about loan options', 'Resolved'),
(10, 'Lost Card', 'Lost my credit card', 'Resolved');
""")

# Insert dummy data into Recommendations table
cursor.execute("""
INSERT INTO Recommendations (CustomerID, ProductType, Details)
VALUES 
(1, 'Credit Card', 'Recommended for premium credit card'),
(2, 'Loan', 'Eligible for personal loan up to $5000'),
(3, 'Investment', 'Suggested investment in mutual funds'),
(4, 'Insurance', 'Recommended health insurance plan'),
(5, 'Credit Card', 'Eligible for cashback credit card'),
(6, 'Loan', 'Eligible for home loan up to $100000'),
(7, 'Investment', 'Suggested investment in stocks'),
(8, 'Insurance', 'Recommended life insurance plan'),
(9, 'Credit Card', 'Eligible for travel credit card'),
(10, 'Loan', 'Eligible for car loan up to $20000');
""")

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Dummy data inserted successfully.")
