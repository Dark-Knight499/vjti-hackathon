import requests
import json
def validate_account_number(account_number):
    """
    Validate account number by checking if it exists in the bank database
    """
    try:
        response = requests.get(f"http://localhost:5000/api/balance/{account_number}")
        data = response.json()
        if "error" in data:
            return "invalid"
        if data["balance"]:  # If account exists, balance will be returned
            return "valid"
        return "invalid"
    except Exception as e:
        return "invalid"

def validate_transaction_details(from_account, to_account, amount):
    """
    Validate transaction details by checking both accounts and attempting a transfer
    """
    try:
        # First validate both accounts exist
        if validate_account_number(from_account) == "invalid" or \
           validate_account_number(to_account) == "invalid":
            return "invalid"

        # Check if transfer is possible
        response = requests.get(
            f"http://localhost:5000/api/transfer/{from_account}/{to_account}/{amount}"
        )
        data = response.json()
        
        if "error" in data:
            return "invalid"
        return "valid"
    except Exception as e:
        return "invalid"

def validate_card_details(account_number, card_number):
    """
    Validate card details by checking account info
    """
    try:
        response = requests.get(f"http://localhost:5000/api/get_all_cards/{account_number}")
        data = response.json()
        
        if "error" in data:
            return "invalid"

        # Check if card exists in account's cards
        cards = data.get("cards")
        print(cards)

        for card in cards:
            if str(card[0]) == str(card_number):  # Assuming card number is second field
                return "valid"
        return "invalid"
    except Exception as e:
        return "invalid"

def validate_full_details(account_number):
    """
    Validate and get complete account details
    """
    try:
        response = requests.get(f"http://localhost:5000/api/get_all_info/{account_number}")
        data = response.json()
        if "error" in data:
            return "invalid"
        return "valid"
    except Exception as e:
        return "invalid"

# Example usage:
if __name__ == "__main__":
    # Test account validation
    # print(validate_account_number("1234567890123456"))
    
    # # Test transaction validation
    # print(validate_transaction_details("1234567890123456", "2345678901234567", 100.00))
    
    # Test card validation
    print(validate_card_details("1234567890123456", "1111222233334444"))
    
    # Test full details validation
    print(validate_full_details("2345678901234567"))
