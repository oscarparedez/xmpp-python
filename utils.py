REGISTER = "REGISTER"
LOGIN = "LOGIN"
LOGOUT = "LOGOUT"
DELETE_ACCOUNT = "DELETE_ACCOUNT"
START_CHAT = "START_CHAT"
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

YOU_SAY = "You say ('exit' to leave chat): "

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

def userMenu():
    option = input("\n \
1: Add contact\n \
2: List Contacts\n \
3: Show contact's information\n \
4: Start a conversation\n \
5: Chat privately\n \
6. Chat grouply\n \
7: Presence\n \
8: Exit\n \
    ")

    if option == "1":
        return ADD_CONTACT
    elif option == "2":
        return LIST_CONTACTS
    elif option == "3":
        return LIST_CONTACT
    elif option == "4":
        return START_CHAT
    elif option == "5":
        return CHAT_PRIVATE
    elif option == "6":
        return CHAT_GROUP
    elif option == "7":
        return PRESENCE
    elif option == "8":
        return EXIT
