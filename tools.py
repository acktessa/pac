import sys

from client import Connection
from openssl import *

class Helper:

    def __init__(self):
        self.connection = Connection("http://pac.fil.cool/uglix")
        self.itsTarget = None
        self.user = 'tunderwood'
        self.password = 'x+gC8HobK%'
        
    def connectionTest(self):
        print(self.connection.get("/"))
        
    def sessionStart(self, target):
        if target == "guest":
            print(self.connection.post('/bin/login', user = "guest", password = "guest"))
            self.itsTarget = target
            
        elif target == "tunderwood":
            print(self.connection.post('/bin/login', user = 'tunderwood', password = 'x+gC8HobK%'))    
            self.itsTarget = target

        else:
            print("Unknown target. Check your username.\n")

    def chapGetChallenge(self):
        data = self.connection.get("/bin/login/CHAP")
        return (data['challenge'])

    def chapGetPlainText(self):
        username = self.user
        challenge = self.chapGetChallenge()
        plainText = username + '-' + challenge
        return (plainText)

    def chapBuildChallengeResponse(self):
        plainText = self.chapGetPlainText()
        cryptedPlainText = encrypt(plainText, self.password)
        return (cryptedPlainText)

    def chapConnect(self):
        challengeResponse = self.chapBuildChallengeResponse()
        print(self.connection.post("/bin/login/CHAP",
                                   user = self.user,
                                   response = challengeResponse))
        self.itsTarget = self.user

    def souleymaneConnect(self):
        challenge = self.connection.get('/bin/login/CHAP')
        return self.connection.post('/bin/login/CHAP', user=self.user, response=encrypt(self.user + '-' + challenge['challenge'], self.password))
        
    def echo(self):
        kwds = {'name':'toto', 'age':'42'}
        print(self.connection.post('/bin/echo', **kwds))

    def fileGetContent(self, filename):
        file = open(filename, 'r')
        content = file.read()
        file.close()
        return (content)
        
    def mailList(self):
        print(self.connection.get("/home/" + self.itsTarget + "/INBOX"))

    def mailDisplay(self, number):
        print(self.connection.get("/home/" + self.itsTarget + "/INBOX/" + number))

    def mailBodyDisplay(self, number):
        print(self.connection.get("/home/" + self.itsTarget + "/INBOX/" + number + "/body"))

    def mailBodyGet(self, number):
        return self.connection.get("/home/" + self.itsTarget + "/INBOX/" + number + "/body")

    def mailBodySave(self, number):
        body = self.connection.get("/home/" + self.itsTarget + "/INBOX/" + number + "/body")
        file = open('mail-body', 'w')
        file.write(body)
        file.close()
        
    def mailSend(self, recipient, subjectText, contentText):
        kwds = {'to': recipient, 'subject': subjectText, 'content': contentText}
        print(self.connection.post('/bin/sendmail', **kwds))

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

    def ticketDownloadAttachment(self, number, filename):
        file = open(filename, 'w')
        content = self.connection.get("/bin/crypto_helpdesk/ticket/"
                                  + number
                                  + "/attachment/" + filename)
        file.write(content)
        file.close()
        
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

    def keyManagerGetInfo(self, user):
        print(self.connection.get("/bin/key-management/" + user))

    def keyManagerDownloadPublicKey(self, user):
        public_key = self.connection.get("/bin/key-management/" + user + "/pk")
        file = open('public-key', 'w')
        file.write(public_key)
        file.close()

    def keyManagerUploadPublicKey(self, pk):
        print(self.connection.post("/bin/key-management/upload-pk", public_key = pk))

    def keyManagerUploadPublicKeyForce(self, pk):
        print(self.connection.post("/bin/key-management/upload-pk", public_key = pk, confirm = True))

