from venmo_api import Client
from getpass import getpass
import json
import datetime
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
start_timestamp = int(datetime.datetime(2022, 4, 1).timestamp())
amounts = {}

def get_relevant_transactions():
    done = False
    relevant_transactions = []
    transactions = client.user.get_user_transactions(user_id=me.id)
    while transactions:
        for transaction in transactions:
            print(transaction.amount)
            choice = transaction.note.lower()
            print(choice)
            print(transaction.date_completed)
            if transaction.date_completed < start_timestamp:
                done = True
                break
            relevant_transactions.append(transaction)
        if done:
            break
        transactions = transactions.get_next_page()
    return relevant_transactions

relevant_transactions = get_relevant_transactions()

