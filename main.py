# Copyright (c) 2013 Tom McLoughlin
import socket
# Configuration
myNick  = "Bot"
myIdent = "Bot"
myReal  = "Bot"
myIRC   = "irc.example.com"
myPort  = "6667"
myChan  = "#example" # only supports a single channel

# Do not edit below this line
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(myIRC,myPort)
socket.send( 'NICK ',myNick )
socket.send( 'USER ',myIdent, myIdent, myIdent,' :',myReal,'\r\n' )
socket.send( 'JOIN ',myChan )
# ok, now you can edit ^_^
while True:
        server = socket.recv ( 4096 )
    if server.find ( 'PING' ) != -1:
        socket.send ( 'PONG ' + net.split() [ 1 ] + '\r' )
    if server.find ( 'cookie' ) != -1:
        socket.send ( 'PRIVMSG ',myChan,' :mmmm cookies ;)\r\n' )
print "Bot successfully connected to IRC"
