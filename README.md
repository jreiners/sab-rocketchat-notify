# sab-rocketchat-notify
Looking for a simple bot to post to a rocket.chat channel within my RC server. Here it is.
    
    sudo python -m pip install rocket-python
    
first configure the API line with your rocketchat username and password, and server URL and run, you should get output like so:

    [20:27 justin ~]$ python rctest.py
    Public rooms
    Name: general, ID: GENERAL
    Name: quickbox, ID: Gbbk7fgNLWisw2ZuR
    Name: test, ID: CsG97m467vAo5Xsn
    Private rooms:
    Name: private1, ID: 2zsYWT5FrahC45GM
    
Modify 
