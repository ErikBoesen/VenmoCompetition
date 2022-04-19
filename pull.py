from venmo_api import Client
from getpass import getpass
import json
import unidecode

"""
access_token = Client.get_access_token(username=input('Username: '),
                                        password=getpass())
print("My token:", access_token)
"""
with open('credentials.json', 'r') as f:
    credentials = json.load(f)

# Initialize api client using an access-token
client = Client(access_token=credentials['access_token'])


me = client.user.get_my_profile()
transactions = client.user.get_user_transactions(user_id=me.id)
amounts = {}
while transactions:
    for transaction in transactions:
        print(transaction.amount)
        choice = transaction.note.lower()
        print(choice)
    transactions = transactions.get_next_page()
