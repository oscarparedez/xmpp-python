#Global vars

REGISTER = "REGISTER"
LOGIN = "LOGIN"
LOGOUT = "LOGOUT"
DELETE_ACCOUNT = "DELETE_ACCOUNT"
CHAT_PRIVATE = "CHAT_PRIVATE"
CHAT_GROUP = "CHAT_GROUP"
LIST_CONTACTS = "LIST_CONTACTS"
LIST_CONTACT = "LIST_CONTACT"
ADD_CONTACT = "ADD_CONTACT"
PRESENCE = "PRESENCE"
EXIT = "EXIT"
UNAVAILABLE = "UNAVAILABLE"
CHAT = 'chat'
GROUP_CHAT = 'groupchat'
SUBSCRIBE = "subscribe"
STATUS_AVAILABLE = "chat"
STATUS_UNAVAILABLE = 'xa'
STATUS_AWAY = 'away'
STATUS_BUSY = 'dnd'

YOU_SAY = "You say ('exit' to leave chat): "
NAME = "Name: "
STATUS_MESSAGE = "Status message: "

# First menu shown
def mainMenu():
    option = input("\n \
1: Register\n \
2: Login\n \
3: Delete account\n \
4: Exit\n \
    ")

    if option == "1":
        return REGISTER
    elif option == "2":
        return LOGIN
    elif option == "3":
        return DELETE_ACCOUNT
    elif option == "4":
        return EXIT

# Second menu shown
def userMenu():
    option = input("\n \
1: Add contact\n \
2: List Contacts\n \
3: Show contact's information\n \
4: Chat privately\n \
5. Chat grouply\n \
6: Presence\n \
7: Logout\n \
    ")

    if option == "1":
        return ADD_CONTACT
    elif option == "2":
        return LIST_CONTACTS
    elif option == "3":
        return LIST_CONTACT
    elif option == "4":
        return CHAT_PRIVATE
    elif option == "5":
        return CHAT_GROUP
    elif option == "6":
        return PRESENCE
    elif option == "7":
        return LOGOUT

# Status options menu
def statusMenu():
    option = input("\n \
1: Available\n \
2: Not Available\n \
3: Away\n \
4: Busy\n \
    ")
    if option == "1":
        return STATUS_AVAILABLE
    elif option == "2":
        return STATUS_UNAVAILABLE
    elif option == "3":
        return STATUS_AWAY
    elif option == "4":
        return STATUS_BUSY