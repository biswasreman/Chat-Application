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

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


while True:
    sender = "Person1"
    message = input('Person1: ')

    data = {
        'sender': sender,
        'message': message
    }

    db.child('person1').set(data)





