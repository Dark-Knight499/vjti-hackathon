parse_otp_prompt = """
Extract the OTP from the following text, which has been extracted from the given image, and return it as a JSON object.
Ensure that the OTP is accurately identified and formatted correctly.
Text: {text}

Output Format:
{{
    "otp": "<type number>"
}}
OUTPUT JSON ONLY NO TEXT ONLY JSON AS IN EXAMPLE ABOVE JUST THE OBJECT NO OTHER THINGS
"""

parse_bank_details_prompt = """
Extract the bank account number and password from the following text, which has been extracted from the given image, and return it as a JSON object.
Ensure that both the account number and password are accurately identified and formatted correctly.
Text: {text}

Output Format:
{{
    "account_number": "<extracted_account_number>",
    "password": "<extracted_password>"
}}
OUTPUT JSON ONLY NO TEXT ONLY JSON AS IN EXAMPLE ABOVE JUST THE OBJECT NO OTHER THINGS
"""

parse_transfer_details_prompt = """
Extract the account number and amount from the following text, which has been extracted from the given image, and return it as a JSON object.
Ensure that both the account number and amount are accurately identified and formatted correctly.
The following text was extracted from the image please parse into the below json format
Text: {text}

Output Format:
{{
    "account_number": "<extracted_account_number>",
    "amount": "<extracted_amount>"
}}
OUTPUT JSON ONLY NO TEXT ONLY JSON AS IN EXAMPLE ABOVE JUST THE OBJECT NO OTHER THINGS
"""

parse_card_details_prompt = """
Extract the card number from the following text, which has been extracted from the given image, and return it as a JSON object.
Ensure that the card number is accurately identified and formatted correctly.
Text: {text}

Output Format:
{{
    "card_number": "<extracted_card_number>"
}}
OUTPUT JSON ONLY NO TEXT ONLY JSON AS IN EXAMPLE ABOVE JUST THE OBJECT NO OTHER THINGS
"""
