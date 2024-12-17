import requests
from langchain_core.tools import tool
import json
from twilio.rest import Client
import gtts as gTTS
import os
from dotenv import load_dotenv
load_dotenv()
@tool
def get_account_details(account_number: str) -> dict:
    """Gets the details of a bank account.
    Args:
        account_number: The account number to get details for
    Returns:
        Dictionary with account details or error message
    """
    try:
        response = requests.get(f"http://localhost:5000/api/balance/{account_number}")
        data = response.json()
        if "error" in data:
            return {"error": "Account not found"}
        return data
    except Exception as e:
        return {"error": str(e)}


@tool
def get_account_balance(account_number: str) -> dict:
    """Gets the details of a bank account.
    Args:
        account_number: The account number to get details for
    Returns:
        Dictionary with account details or error message
    """
    try:
        response = requests.get(f"http://localhost:5000/api/balance/{account_number}")
        data = response.json()
        if "error" in data:
            return {"error": "Account not found"}
        return data
    except Exception as e:
        return {"error": str(e)}

@tool
def get_transaction_details(account_number: str) -> dict:
    """Gets the details of transactions for a given account.
    Args:
        account_number: The account number to get transaction details for
    Returns:
        Dictionary with transaction details or error message
    """
    try:
        response = requests.get(f"http://localhost:5000/api/transactions/{account_number}")
        data = response.json()
        if "error" in data:
            return {"error": "Transactions not found"}
        return data
    except Exception as e:
        return {"error": str(e)}

@tool
def get_card_details(account_number: str, card_number: str) -> dict:
    """Gets the details of a card associated with a given account.
    Args:
        account_number: The account number to check
        card_number: The card number to get details for
    Returns:
        Dictionary with card details or error message
    """
    try:
        response = requests.get(f"http://localhost:5000/api/get_all_cards/{account_number}")
        data = response.json()
        
        if "error" in data:
            return {"error": "Account not found"}

        cards = data.get("cards", [])
        for card in cards:
            if str(card[0]) == str(card_number):
                return {"card_details": card}
        return {"error": "Card not found"}
    except Exception as e:
        return {"error": str(e)}

@tool
def get_full_account_details(account_number: str) -> dict:
    """Gets the full details of an account.
    Args:
        account_number: The account number to get details for
    Returns:
        Dictionary with full account details or error message
    """
    try:
        response = requests.get(f"http://localhost:5000/api/get_all_info/{account_number}")
        data = response.json()
        if "error" in data:
            return {"error": "Account not found"}
        return data
    except Exception as e:
        return {"error": str(e)}

@tool
def save_audio(account_number: str) -> dict:
    """Saves an audio file with the transaction details.
    Args:
        account_number: The account number to get transaction details for
    Returns:
        Dictionary with the status of the operation or error message
    """
    try:
        # Get transaction details
        transaction_details = get_transaction_details(account_number)
        if "error" in transaction_details:
            return {"error": "Failed to get transaction details"}

        # Extract transaction details
        transactions = transaction_details.get('transactions', [])
        if not transactions:
            return {"error": "No transactions found"}

        # Assuming we want to save details of the latest transaction
        latest_transaction = transactions[0]

        # Create the message text
        message_text = (
            f"Transaction ID: {latest_transaction[0]}, "
            f"Account ID: {latest_transaction[1]}, "
            f"Transaction Type: {latest_transaction[2]}, "
            f"Amount: {latest_transaction[3]}, "
            f"Timestamp: {latest_transaction[4]}, "
            f"Description: {latest_transaction[5]}"
        )

        # Convert text to speech
        tts = gTTS.gTTS(text=message_text, lang='en')
        audio_file = f"transaction_{account_number}.mp3"
        tts.save(audio_file)

        return {"status": "Audio saved", "file": audio_file}
    except Exception as e:
        return {"error": str(e)}

@tool
#wrie down a function to send whatsapp message
def send_whatsapp()->dict:
    """ Sends a WhatsApp message with transaction details.
    Args:
        None
    Returns:
        None
    """
    try:
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Transaction details',
            to=os.getenv("WHATSAPP_NUMBER"),
            media_url=["https://github.com/Dark-Knight499/media-files/raw/refs/heads/main/transaction_1.mp3"]
        )

        print(message.sid)
        return {"status": "Message sent"}
    except Exception as e:
        return {"error": str(e)}
if __name__ == "__main__":
    try:
        from dotenv import load_dotenv
        load_dotenv()
        # print(get_account_balance("1234567890123456"))
        # print(get_transaction_details("1234567890123456"))
        # print(get_card_details("1234567890123456", "1234567890123456"))
        # print(get_full_account_details("1234567890123456"))
        print(send_whatsapp.invoke({}))
    except Exception as e:
        print(f"An error occurred: {e}")