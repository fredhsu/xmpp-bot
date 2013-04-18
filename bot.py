# Jabber demo bot
# Fred Hsu (fhsu@cisco.com): CMO Demonstrations 
import time
from twisted.words.xish import domish
from wokkel.xmppim import MessageProtocol, AvailablePresence
from twisted.web import server, resource
from twisted.internet import reactor

class EchoBotProtocol(MessageProtocol, resource.Resource):
    isLeaf = True
    numberRequests = 0

    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        return "I am request #" + str(self.numberRequests) + "\n"
    

    def connectionMade(self):
        print "Connected!"

        # send initial presence
        #self.send(AvailablePresence())

        #reactor.listenTCP(8080, server.Site(EchoBotProtocol()))
        #reactor.run()

    def connectionLost(self, reason):
        print "Disconnected!"

    def onMessage(self, msg):
        donna = 'dshim@cisco.com/Donnas-MacBook-Pro'
        adam = 'adaczec2@cisco.com/Adam Czech'
        print str(msg)

        if msg["type"] == 'chat' and hasattr(msg, "body"):
            reply = domish.Element((None, "message"))
            reply["to"] = msg["from"]
            reply["from"] = msg["to"]
            reply["type"] = 'chat'
            if msg["from"] == adam:
                reply.addElement("body", content="What is your bidding my lord?")
            

	    if str(msg.body) == 'status: away':
                self.send(AvailablePresence(show='away'))
                reply.addElement("body", content="Going away")
            elif str(msg.body).lower().startswith('can you'):
                reply.addElement("body", content="Yes")
		time.sleep(1)
            elif str(msg.body).lower().startswith('hey'):
		heyreply = "Hey good to hear from you"
		time.sleep(1)
                reply.addElement("body", content=heyreply)
            elif str(msg.body) == 'status: chat':
                self.send(AvailablePresence())
                reply.addElement("body", content="I'm back")
	    elif str(msg.body) == 'status: xa':
		self.send(AvailablePresence(show='xa'))
                reply.addElement("body", content="Going away")
            elif str(msg.body) == 'b@d robot':
                reply.addElement("body", content="Fuck you!!! ... I'm a real boy!!!")
            elif str(msg.body) == 'message:':
                #iself.send(AvailablePresence(statusLine='This is my status Line '))
                reply.addElement("body", content="!!!!!!!!")
            else:
                print "continue\n" #reply.addElement("body", content=str(msg.body))
            
	    localtime = time.asctime( time.localtime(time.time()) )
            print "Local current time :", localtime
	    self.send(reply)
