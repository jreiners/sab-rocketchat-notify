from rocketchat.api import RocketChatAPI
import os
import sys

api = RocketChatAPI(settings={'username': 'rc-account-email', 'password': 'rc-password', 'domain': 'http://rc-url.com:3000'})

def getPrivates():
    print("Private rooms:")
    rooms2 = api.get_private_rooms()
    for x in rooms2:
        print("Name: {}, ID: {}".format(x['name'], x['id']))

def getPublic():
    print("Public rooms")
    rooms = api.get_public_rooms()
    for x in rooms:
        print("Name: {}, ID: {}".format(x['name'], x['id']))
getPublic()
getPrivates()
