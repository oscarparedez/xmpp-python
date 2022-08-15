import xmpp
import asyncio
from utils import *
from session import *
from client import *

# Patch to avoid xmpp issue
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
option1 = ''
# Menu that iterates over Register, Login and Delete account
while option1 != EXIT:
    
    option1 = mainMenu()
    if (option1 == REGISTER):
        username = input("Usuario (name@alumchat.xyz)>>> ")
        password = input("Contraseña>>> ")
        if register(username, password):
            print("Registered")
        else:
            print("Error")
    elif (option1 == LOGIN):
        username = input("JID: ")
        password = input("Password: ")
        status = statusMenu()
        about = input("About: ")

        # Initialize client object
        xmpp = Client(username, password, status, about)
        xmpp.connect()
        xmpp.process(timeout = 5)

        option2 = ''
        # Menu that iterates over user options
        while option2 != LOGOUT:
            option2 = userMenu()
            if option2 == ADD_CONTACT:
                contact = input(NAME)
                xmpp.send_friend_request(contact)
                xmpp.process(timeout = 5)
            elif option2 == LIST_CONTACTS:
                xmpp.contact_list()
                xmpp.process(timeout = 5)
            elif option2 == LIST_CONTACT:
                contact = input(NAME)
                xmpp.contact_list(specific = contact)
                xmpp.process(timeout = 5)
            elif option2 == CHAT_PRIVATE:
                contact = input(NAME)
                xmpp.send_message_to(contact)
                xmpp.process(forever=False)
            elif option2 == CHAT_GROUP:
                group_id = input("Group ID: ")
                xmpp.send_message_to_group(group_id)
                xmpp.process(forever=False)
            elif option2 == PRESENCE:
                status = statusMenu()
                status_message = input("Status message: ")
                xmpp.update_presence(status, status_message)
                xmpp.process(timeout = 5)
            elif option2 == LOGOUT:
                xmpp.disconnect(wait=False)
    elif (option1 == DELETE_ACCOUNT):
        username = input("JID: ")
        password = input("Password: ")
        # Initialize unregister client object
        xmpp = UnregisterClient(username, password)
        xmpp.connect()
        xmpp.process(forever=False)

exit()