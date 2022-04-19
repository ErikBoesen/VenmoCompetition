from venmo_api import Client
from getpass import getpass

"""
access_token = Client.get_access_token(username=input('Username: '),
                                        password=getpass())
print("My token:", access_token)
"""

# Initialize api client using an access-token
client = Client(access_token=access_token)

# Search for users. You get a maximum of 50 results per request.
users = client.user.search_for_users(query="Peter")
for user in users:
   print(user.username)

# Or pass a callback to make it multi-threaded
def callback(users):
   for user in users:
       print(user.username)

client.user.search_for_users(query="peter",
                            callback=callback,
                            limit=10)
