import xmpp
import asyncio
from utils import *
from session import *
from client import *

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
option1 = ''
while option1 != EXIT:
    
    option1 = mainMenu()
    ####### DONE
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
        status = input("Status: ")
        about = input("About: ")

        xmpp = Client(username, password, status, about)
        xmpp.connect()
        xmpp.process(timeout = 5)

        option2 = ''
        while option2 != EXIT:
            option2 = userMenu()
            ####### DONE
            if option2 == ADD_CONTACT:
                contact = input("Name: ")
                xmpp.send_friend_request(contact)
                xmpp.process(timeout = 5)
            ####### DONE
            elif option2 == LIST_CONTACTS:
                xmpp.contact_list()
                xmpp.process(timeout = 5)
            ####### DONE
            elif option2 == LIST_CONTACT:
                contact = input("Name: ")
                xmpp.contact_list(specific = contact)
                xmpp.process(timeout = 5)
            elif (option2 == CHAT_PRIVATE):
                contact = input("Name: ")
                xmpp.send_message_to(contact)
                xmpp.process(forever=False)
            elif (option2 == CHAT_GROUP):
                group_id = input("Group ID: ")
                xmpp.send_message_to_group(group_id)
                xmpp.process(forever=False)

    ####### DONE
    elif (option1 == DELETE_ACCOUNT):
        username = input("JID: ")
        password = input("Password: ")
        xmpp = UnregisterClient(username, password)
        xmpp.connect()
        xmpp.process(forever=False)

exit()