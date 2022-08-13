import logging
from time import time
from traceback import print_tb
import slixmpp
import asyncio
import xmpp
import time
from slixmpp.exceptions import IqError, IqTimeout
from utils import *

class Client(slixmpp.ClientXMPP):
    def __init__(self, jid, password, status, status_message):
        slixmpp.ClientXMPP.__init__(self, jid, password)

        self.jid = jid
        self.status = status
        self.status_message = status_message

        self.contacts = self.roster[self.jid]
        
        # # plugins
        self.register_plugin('xep_0030') # Service Discovery
        self.register_plugin('xep_0199') # Ping
        self.register_plugin('xep_0004') # Data Forms
        self.register_plugin('xep_0060') # PubSub
        self.register_plugin('xep_0085') # Chat State Notifications
        self.register_plugin('xep_0045') # MUC

		# events
        self.add_event_handler('session_start', self.start)
        self.add_event_handler("message", self.chat_dm)
        self.add_event_handler("groupchat_message", self.chat_group)

    async def start(self, event):
        self.send_presence(pshow=self.status, pstatus=self.status_message)
        try:
            # Ask for roster
            await self.get_roster()
            print("Login successfully:", self.jid)
        except:
            print("Could not log in.")
            self.disconnect()

    #Send friend request
    def send_friend_request(self, recipient):
        try:
            # Subscribe
            self.send_presence_subscription(recipient, self.jid)
            print("Contact added: ", recipient)
        except:
            print("Could not add contact.")

    #Contact List
    def contact_list(self, specific = None):
        self.get_roster()
        self.contacts = self.roster[self.jid]

        if(len(self.contacts.keys()) == 0):
            print("You have no contacts in your contact list.")

        if not specific:
            for contact in self.contacts.keys():
                if contact != self.jid:
                    print("Contact: ", {contact})
                    info = list(self.client_roster.presence(contact).values())
                    if info[0]['status'] != '':
                        print("Status Message: ", info[0]['status'])
                    else:
                        print("Status Message: -")
                    if info[0]['show'] != '':
                        print("Status: ", info[0]['show'])
                    else:
                        print("Status: -")
        else:
            for contact in self.contacts.keys():
                if specific == contact:
                    print("Contact: ", {contact})
                    info = list(self.client_roster.presence(contact).values())
                    if info[0]['status'] != '':
                        print("Status Message: ", info[0]['status'])
                    else:
                        print("Status Message: -")
                    if info[0]['show'] != '':
                        print("Status: ", info[0]['show'])
                    else:
                        print("Status: -")
    
    #Send DM
    def send_message_to(self, recipient, type):
        message = input(YOU_SAY)
        if message == "exit":
            self.disconnect()
        self.send_message(
            mto = recipient, 
            mbody = message, 
            mtype = CHAT, 
            mfrom = self.jid
        )

    #Chat
    def chat_dm(self, message):
        if message['type'] == CHAT:

            sender = str(message['from'])
            sender = sender[:sender.index("/")]
            body = str(message['body'])
            
            print(sender, "says: ", body)
            reply = input(YOU_SAY)
            if reply == "exit":
                self.disconnect()
            message.reply(reply).send()
            #Receive images and docs
            # if sender != self.jid and validators.url(body):
            #     webbrowser.open(body)

    def send_message_to_group(self, group_id):
        self.plugin['xep_0045'].join_muc(group_id, self.jid)
        message = input(YOU_SAY)
        if message == "exit":
            self.disconnect()
        self.send_message(
            mto=group_id,
            mbody=message,
            mtype=GROUP_CHAT
        )

    def chat_group(self, message):
        if message['type'] == GROUP_CHAT:

            sender = str(message['from'])
            sender = sender[:sender.index("/")]
            body = str(message['body'])
            
            print(sender, "says: ", body)
            reply = input(YOU_SAY)
            if reply == "exit":
                self.disconnect()
            message.reply(reply).send()