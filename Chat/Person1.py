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



#  working with Database


while True:


    show = input("What you want ? i or s?: ")

    if show == "i":
        chat = input("Person1: ")
        person2 = {}
        person2["chatting"] = chat
        database.child("person1").set(person2)

    elif show == "s":
        show_chat = database.child("person2").get()
        a = show_chat.val()
        print(f"Person2:",a.get("chatting"))
        continue
    




