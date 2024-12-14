import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="12345678"
)
cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS ApnaBank")
cursor.execute("CREATE DATABASE IF NOT EXISTS ApnaBank")
cursor.execute("USE ApnaBank")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(15) UNIQUE,
    PreferredLanguage VARCHAR(20) DEFAULT 'English',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Accounts (
    AccountID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT NOT NULL,
    AccountNumber VARCHAR(20) UNIQUE NOT NULL,
    AccountType ENUM('Savings', 'Checking', 'Credit') NOT NULL,
    Balance DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
    Password VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,
    AccountID INT NOT NULL,
    TransactionType ENUM('Deposit', 'Withdrawal', 'Transfer', 'Payment') NOT NULL,
    Amount DECIMAL(15, 2) NOT NULL,
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Description TEXT,
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Cards (
    CardID INT AUTO_INCREMENT PRIMARY KEY,
    AccountID INT NOT NULL,
    CardNumber VARCHAR(16) UNIQUE NOT NULL,
    ExpiryDate DATE NOT NULL,
    CVV INT NOT NULL,
    CardType ENUM('Debit', 'Credit') NOT NULL,
    Status ENUM('Active', 'Inactive', 'Blocked') NOT NULL DEFAULT 'Active',
    DisabledReason TEXT,
    DisabledTimestamp TIMESTAMP NULL,
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Reports (
    ReportID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT NOT NULL,
    ReportType ENUM('Lost Card', 'Fraudulent Transaction', 'General Query') NOT NULL,
    Description TEXT,
    ReportStatus ENUM('Pending', 'In Progress', 'Resolved') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ResolvedAt TIMESTAMP NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Recommendations (
    RecommendationID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT NOT NULL,
    ProductType ENUM('Credit Card', 'Loan', 'Investment', 'Insurance') NOT NULL,
    Details TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
""")

conn.commit()
conn.close()

print("Database and tables created successfully.")
