import pyrebase
import time

firebaseConfig ={

    'apiKey' : "AIzaSyCceNZuKaeJKx3OUbdM2g-wBEojTX4AQBk",
    'authDomain' : "chatapplicationreman.firebaseapp.com",
    'projectId' : "chatapplicationreman",
    'storageBucket' : "chatapplicationreman.appspot.com",
    'messagingSenderId' : "665043228341",
    'appId' : "1:665043228341:web:96de182cf7acb98db690fc",
    'measurementId' : "G-1NSWXPJG5W",
    'databaseURL' : "https://chatapplicationreman-default-rtdb.firebaseio.com/"

    }

firebaseapp = pyrebase.initialize_app(firebaseConfig)

database = firebaseapp.database()




# Database





while True:
    show = input("What you want ? i or s?: ")

    if show == "i":
        chat = input("Person2: ")
        person2 = {}
        person2["chatting"] = chat
        database.child("person2").set(person2)

    elif show == "s":
        show_chat = database.child("person1").get()
        a = show_chat.val()
        print(f"Person1:",a.get("chatting"))
        continue
            



















# clearx = '\033[2J'
# returnx = '\033[H'

# # Database

# print(clearx)

# while True:
#     # enter = input("Please press enter to reload: ")
#     person1 = {}
#     show_chat = database.child("person1").get()
#     a = show_chat.val()
#     # print(f"{returnx}","Person2:",a["chatting"])
#     print(f"Person2:",a["chatting"])
    
