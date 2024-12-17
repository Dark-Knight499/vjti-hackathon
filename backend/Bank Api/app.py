from flask import Flask, render_template, jsonify
from flask_cors import CORS
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="12345678",
    database="ApnaBank"
)
cursor = conn.cursor()
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/balance/<int:account_number>')
def get_balance(account_number):
    try:
        cursor.execute("SELECT Balance FROM Accounts WHERE AccountNumber = %s", (account_number, ))
        return jsonify(cursor.fetchall())
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/block_card/<int:account_number>/<int:card_number>')
def cancel_card(account_number, card_number):
    try:
        cursor.execute("UPDATE Cards SET Status = 'Blocked' WHERE AccountID = %s AND CardNumber = %s", (account_number, card_number))
        conn.commit()
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/transactions/<int:account_number>')
def get_transactions(account_number):
    try:
        cursor.execute("SELECT * FROM Transactions JOIN Accounts ON Transactions.AccountID = Accounts.AccountID WHERE Accounts.AccountNumber = %s", (account_number, ))
        return jsonify({"transactions": cursor.fetchall()})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/transfer/<int:from_account>/<int:to_account>/<float:amount>')
def transfer(from_account, to_account, amount):
    try:
        cursor.execute("SELECT Balance FROM Accounts WHERE AccountNumber = %s", (from_account, ))
        from_balance = cursor.fetchone()[0]
        if from_balance < amount:
            return jsonify({"error": "Insufficient Balance"})
        cursor.execute("UPDATE Accounts SET Balance = Balance - %s WHERE AccountNumber = %s", (amount, from_account))
        cursor.execute("UPDATE Accounts SET Balance = Balance + %s WHERE AccountNumber = %s", (amount, to_account))
        conn.commit()
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/get_all_info/<int:account_number>')
def get_all_info(account_number):
    try:
        cursor.execute("SELECT * FROM Accounts WHERE AccountNumber = %s", (account_number, ))
        account = cursor.fetchone()
        cursor.execute("SELECT * FROM Transactions WHERE AccountID = %s", (account[0], ))
        transactions = cursor.fetchall()
        cursor.execute("SELECT * FROM Cards WHERE AccountID = %s", (account[0], ))
        cards = cursor.fetchall()
        cursor.execute("SELECT * FROM Customers WHERE CustomerID = %s", (account[1], ))
        customer = cursor.fetchone()
        return jsonify({
            "account": account,
            "transactions": transactions,
            "cards": cards,
            "customer": customer
        })
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/get_all_cards/<int:account_number>')
def get_all_cards(account_number):
    try:
        cursor.execute("SELECT CardNumber FROM Cards JOIN Accounts ON Cards.AccountID = Accounts.AccountID WHERE Accounts.AccountNumber = %s", (account_number, ))
        return jsonify({"cards": cursor.fetchall()})
    except Exception as e:
        return jsonify({"error": str(e)})
    
if __name__ == '__main__':
    app.run(debug=True)

