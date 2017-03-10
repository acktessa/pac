from client import Connection

c = Connection("http://pac.fil.cool/uglix")

#print(c.post("/bin/login", user="guest", password="guest"))

print(c.get("/home/guest/INBOX"))
