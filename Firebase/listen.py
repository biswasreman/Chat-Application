import pyrebase

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

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


# Read messages from the database
def handle_message_added(messages):
    show_chat = db.child("messages").get()
    a = show_chat.val()


    print(f'{a.get("sender")}: {a.get("message")}')

db.child('messages').stream(handle_message_added)

