from venmo_api import Client
from getpass import getpass

access_token = Client.get_access_token(username=input('Username: '),
                                        password=getpass())
print('My token:', access_token)
