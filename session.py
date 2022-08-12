import xmpp
import slixmpp
from slixmpp.exceptions import IqError, IqTimeout

def register(client, password):
	jid = xmpp.JID(client)
	account = xmpp.Client(jid.getDomain(), debug=[])
	account.connect()
	return bool(
	    xmpp.features.register(account, jid.getDomain(), {
	        'username': jid.getNode(),
	        'password': password
	    }))


class UnregisterClient(slixmpp.ClientXMPP):

    def __init__(self, jid, password):
        slixmpp.ClientXMPP.__init__(self, jid, password)

        # Plugins
        self.register_plugin('xep_0030') # Service Discovery
        self.register_plugin('xep_0004') # Data forms
        self.register_plugin('xep_0066') # Out-of-band Data
        self.register_plugin('xep_0077') # In-band Registration

        # Event handler
        self.add_event_handler("session_start", self.start)

    async def start(self, event):
        self.send_presence()
        await self.get_roster()
        await self.unregister()
        self.disconnect()

    async def unregister(self):
        print('unregister')
        response = self.Iq()
        response['type'] = 'set'
        response['from'] = self.boundjid.user
        response['password'] = self.password
        response['register']['remove'] = 'remove'

        try:
            await response.send()
            print(f"Account unregistered successfully: {self.boundjid}!")
        except IqError as e:
            print(f"Couldn't unregister account: {e.iq['error']['text']}")
            self.disconnect()
        except IqTimeout:
            print("No response from server.")
            self.disconnect()