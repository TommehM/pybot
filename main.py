# Copyright (c) 2013 Tom McLoughlin
import socket
# Configuration
myNick  = "Bot"
myIdent = "Bot"
myReal  = "Bot"
myIRC   = "irc.example.org"
myPort  = "6667"
myChan  = "#example" # only supports a single channel

# Do not edit below this line
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(myIRC,myPort)
socket.send( 'NICK ',myNick )
socket.send( 'USER ',myIdent, myIdent, myIdent' :',myReal'\r\n' )
socket.send( 'JOIN ',myChan )
# ok, now you can edit ^_^
while True:
	net = socket.recv ( 4096 )
	if net.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + net.split() [ 1 ] + '\r\n' )
    if net.find ( 'cookie' ) != -1:
      irc.send ( 'PRIVMSG ',myChan,' :mmmm cookies ;)\r\n' )
print net
