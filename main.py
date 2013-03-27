# Copyright (c) 2013 Tom McLoughlin
import socket
# Configuration
myNick  = "Bot"
myIdent = "Bot"
myReal  = "Bot"
myIRC   = "irc.kottnet.net"
myPort  = 6667
myChan  = "#TomM" # only supports a single channel
# Do not edit below this line
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((myIRC, myPort))
sock.send('NICK ' + myNick)
sock.send('USER ' + myIdent + myIdent + myIdent + ' :' + myReal + '\r\n')
sock.send('JOIN ' + myChan)
# ok, now you can edit ^_^
while True:
    server = sock.recv ( 4096 )
    if server.find ( 'PING' ) != -1:
        sock.send ( 'PONG ' + net.split() [ 1 ] + '\r' )
    if server.find ( 'cookie' ) != -1:
        sock.send ( 'PRIVMSG ' + myChan + ' :mmmm cookies ;)\r\n' )
