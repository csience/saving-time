#!/usr/bin/env python2

# https://www.raywenderlich.com/3932/networking-tutorial-for-ios-how-to-create-a-socket-based-iphone-app-and-server

from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor

class iPhoneChat(Protocol): # iPhoneChat extends Protocol and extends connectionMade 'hook'
    def connectionMade(self):
        self.factory.clients.append(self)
        print "[*] A has client connected."
        print "clients are ", self.factory.clients

    def connectionLost(self, reason):
        self.factory.clients.remove(self)

    def dataReceived(self, data):
        # split the string to find out the command
        a = data.split(':')
        print a
        # if it is "iam", store the name of the client
        if len(a) > 1:
            command = a[0]
            content = a[1]

            msg = ""
            if command == "iam":
                self.name = content
                msg = self.name + " has joined"

            elif command == "msg":
                msg = self.name + ": " + content
                print msg

            for c in self.factory.clients:
                c.message(msg)

    def message(self, message):
        self.transport.write(message + '\n') # \n escape character so socket detects when message transmission has completed

# factory to handle connections
factory = Factory()
factory.protocol = iPhoneChat
factory.clients = []
reactor.listenTCP(80, factory)
print "[*] iPhone chat server started"
# create Twisted event loop
reactor.run()