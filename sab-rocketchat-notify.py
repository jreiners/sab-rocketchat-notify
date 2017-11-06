#!/usr/bin/python
'''
rocketchat bot script, sends messagetext to any channel you specify using rocketchat API.
By jreiners
'''

from rocketchat.api import RocketChatAPI
import os
import sys

messagetext = 'I just grabbed *"{}"* from the *"{}"* category. I acquired it from the *"{}"* newsgroup'
# unless DEFAULT room is used, this needs to be the room code from
'''
rocketchat_rooms = {}

for x in rooms:
        rocketchat_rooms[x['name']] = x['id']

rocketchat_rooms
'''
roomname = 'GENERAL_or_RoomID from above'
api = RocketChatAPI(settings={'username': 'registered_user_email', 'password': 'userpass', 'domain': 'http://url:3000'})

# uncomment below to print command line args, for troubleshooting.
#input = [sys.argv]
#print(input)

print("sent notification to #quickbox chatroom.")

api.send_message( messagetext.format(sys.argv[3], sys.argv[5], sys.argv[6]) , roomname)

sys.exit(0)
