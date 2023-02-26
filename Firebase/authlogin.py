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

firebaseapp = pyrebase.initialize_app(firebaseConfig)


auth = firebaseapp.auth()



# Authentication and Login

email = input("Enter your email: ")
password = input("Enter your password: ")

try:

    user = auth.sign_in_with_email_and_password(email,password)
    auth.send_email_verification(user['idToken'])
    print("Email verification has been sent!")
    # print("Successfully signed in!")

except:
    print("Invalid Email or Password! Please try again!")


# Signup

email = input("Enter your email: ")
password = input("Enter your password: ")
confirm_password = input("Enter your password again: ")

if password == confirm_password:

    try:
        auth.create_user_with_email_and_password(email,password)
        print("User created successfully!")
    except:
        print("Email already exists!")

else:

    print("Password doesn't match!")



