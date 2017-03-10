import sys

from client import Connection

class Helper:

    def __init__(self):
        self.connection = Connection("http://pac.fil.cool/uglix")
        self.itsTarget = None
        
    def connectionTest(self):
        print(self.connection.get("/"))
        
    def sessionStart(self, target):
        if target == "guest":
            print(self.connection.post('/bin/login', user = "guest", password = "guest"))
            self.itsTarget = target
            
        elif target == "tunderwood":
            print(self.connection.post('/bin/login', user = "tunderwood", password = "x+gC8HobK%"))    
            self.itsTarget = target

        else:
            print("Unknown target. Check your username.\n")

    def echo(self):
        kwds = {'name':'toto', 'age':'42'}
        print(self.connection.post('/bin/echo', **kwds))
            
    def mailList(self):
        print(self.connection.get("/home/" + self.itsTarget + "/INBOX"))

    def mailDisplay(self, number):
        print(self.connection.get("/home/" + self.itsTarget + "/INBOX/" + number))

    def mailDisplayBody(self, number):
        print(self.connection.get("/home/" + self.itsTarget + "/INBOX/" + number + "/body"))

    def mailSend(self, recipient, subjectText, contentText):
        print(self.connection.post('/bin/sendmail',
                                   to = recipient,
                                   subject = subjectText,
                                   content = contentText))

    def home(self):
        print(self.connection.get("/home/"))

    def helpdeskConnect(self):
        print(self.connection.get("/bin/crypto_helpdesk"))

    def ticketDisplay(self, number):
        print(self.connection.get("/bin/crypto_helpdesk/ticket/" + number))

    def ticketDisplayAttachment(self, number, filename):
        print(self.connection.get("/bin/crypto_helpdesk/ticket/"
                                  + number
                                  + "/attachment/" + filename))

    def ticketClose(self, ticketId):
        print(self.connection.post("/bin/crypto_helpdesk/ticket/" + ticketId
                                   + "/close", confirm=True))

    def ticketReopen(self, ticketId):
        print(self.connection.get("/bin/crypto_helpdesk/ticket/" + ticketId
                                  + "/reopen"))

    def ticketListOpened(self):
        print(self.connection.get("/bin/crypto_helpdesk/opened"))

    def ticketListClosed(self):
        print(self.connection.get("/bin/crypto_helpdesk/closed"))

    def ticketTitle(self, ticketId):
        print(self.connection.get("/bin/crypto_helpdesk/" + ticketId
                                  + "/title"))
