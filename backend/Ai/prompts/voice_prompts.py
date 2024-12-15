parse_otp_prompt = """
Extract the OTP from the following user input and return it as a JSON object.
I had asked the user to say their OTP. The user has said the following:
User Input:
OTP: {otp}
Now you have to parse it and return the OTP as a JSON object.

Output Format:
{{
    "otp": "<type number>"
}}
    OUTPUT JSON ONLY NO TEXT ONLY JSON AS IN EXAMPLE ABOVE JUST THE OBJECT NO OTHER THINGS
"""
parse_bank_details_prompt = """
Extract the bank account number and password from the following user input and return it as a JSON object.
I had asked the user to say their bank account number and password. The user has said the following:
User Input:
Account Number: {account_number}, Password: {password}
Now you have to parse it and return the account number and password as a JSON object.

Output Format:
{{
    "account_number": "<extracted_account_number>",
    "password": "<extracted_password>"
}}
OUTPUT JSON ONLY NO TEXT ONLY JSON AS IN EXAMPLE ABOVE JUST THE OBJECT NO OTHER THINGS
"""
parse_transfer_details_prompt = """
Extract the account number and amount from the following user input and return it as a JSON object.
I had asked the user to say the account number to which they want to transfer money. The user has said the following:
User Input:
Account Number: {account_number}, Amount: {amount}
Now you have to parse it and return the account number and amount as a JSON object.

Output Format:
{{
    "account_number": "<extracted_account_number>",
    "amount": "<extracted_amount>"
}}
OUTPUT JSON ONLY NO TEXT ONLY JSON AS IN EXAMPLE ABOVE JUST THE OBJECT NO OTHER THINGS
"""
parse_card_details_prompt = """
Extract the card number from the following user input and return it as a JSON object.
I had asked the user to say their card number. The user has said the following:
User Input:
Card Number: {card_number}
Now you have to parse it and return the card number as a JSON object.

Output Format:
{
    "card_number": "<extracted_card_number>"
}
OUTPUT JSON ONLY NO TEXT ONLY JSON AS IN EXAMPLE ABOVE JUST THE OBJECT NO OTHER THINGS
"""

