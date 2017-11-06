# sab-rocketchat-notify

![alt text](https://i.imgur.com/OSlxXdl.png)

Looking for a simple bot to post to a rocket.chat channel within my RC server. Here it is.
    
    sudo python -m pip install rocket-python

## Finding your roomId:
first configure the API lines in both scripts with your rocketchat username and password, and server URL and run, you should get output like so:

    api = RocketChatAPI(settings={'username': 'rocketchat_user_email', 'password': 'rocketchat_user_pass', 'domain': 'http://rocketchat.reiners.io:3000'})

running the find-rooms.py should display this output if your authentication works correctly

    [20:27 justin ~]$ ./find-rooms.py
    Public rooms
    Name: general, ID: GENERAL
    Name: quickbox, ID: Gbbk7fgNLWisw2ZuR
    Name: test, ID: CsG97m467vAo5Xsn
    Private rooms:
    Name: private1, ID: 2zsYWT5FrahC45GM

## Notification script setup:

Modify the same line `api = ` within `sab-rocketchat-notify.py` with correct user settings.

Modify the `roomId =` line with your ID you found running the `find-rooms.py` script.

copy `sab-rocketchat-notify.py` file to `/home/<user>/SABnzbd/scripts` and select from within sabnzbd.
