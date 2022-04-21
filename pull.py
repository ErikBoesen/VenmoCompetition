from venmo_api import Client
import json
import datetime
from unidecode import unidecode
import time

with open('credentials.json', 'r') as f:
    credentials = json.load(f)

# Initialize api client using an access-token
client = Client(access_token=credentials['access_token'])


me = client.user.get_my_profile()
start_timestamp = int(datetime.datetime(2022, 4, 1).timestamp())

def get_relevant_transactions():
    done = False
    relevant_transactions = []
    transactions = client.user.get_user_transactions(user_id=me.id)
    while transactions:
        for transaction in transactions:
            if transaction.date_completed < start_timestamp:
                done = True
                break
            relevant_transactions.append(transaction)
        if done:
            break
        transactions = transactions.get_next_page()
    return relevant_transactions

def get_amounts():
    transactions = get_relevant_transactions()
    artist_amounts = {artist: 0 for artist in ('amine', 'masego', 'japanese_breakfast', 'sofi_tukker')}
    user_amounts = {}
    for transaction in transactions:
        artist = unidecode(transaction.note.lower().replace(' ', '_'))
        if artist in artist_amounts:
            artist_amounts[artist] += transaction.amount

            user = transaction.actor.display_name
            if user not in user_amounts:
                user_amounts[user] = 0
            user_amounts[user] += transaction.amount

    print(artist_amounts)
    with open('web/artist_amounts.json', 'w') as f:
        json.dump(artist_amounts, f)
    print(user_amounts)
    with open('web/user_amounts.json', 'w') as f:
        json.dump(user_amounts, f)

while True:
    get_amounts()
    time.sleep(2)
