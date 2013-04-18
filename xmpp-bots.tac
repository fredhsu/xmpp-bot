from twisted.application import service
from twisted.words.protocols.jabber.jid import JID

from wokkel import client, xmppim
from bot import EchoBotProtocol

users = dict()
f = open('users.txt')
line = f.readline()
while line:
    user = line.split()[0]
    status = line.split()[1]
    statusLine = f.readline()
    users[user] = [status, statusLine]
    line = f.readline()

password = 'cisco'

application = service.Application('XMPP client')

for user, stat in users.iteritems():
    jid = JID(user + "@indigoskylight.com")
    xmppClient = client.XMPPClient(jid, password)
    xmppClient.logTraffic = True
    echobot = EchoBotProtocol()
    echobot.setHandlerParent(xmppClient)
    xmppClient.setServiceParent(application)
    presence = xmppim.PresenceClientProtocol()
    presence.setHandlerParent(xmppClient)
    presence.available(show = stat[0], statuses = {stat[0]: stat[1]})
    #presence.available()

