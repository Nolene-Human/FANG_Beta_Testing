## ----------------------------------------THIS IS 'LOGIN FUNCTION' ------------------------------------------------------##
 ## -------------------------------- Called form fang.py when user select login---------------------------------------------##
## -------------------------- Uses Firebase_Config Functions to verify and log in users -----------------------------------##

### FUTURE DEVELOPMENT ###
# - Tick box in this area is not ideal
# - Form does not reset or hides when user logs in

## ______________________________________________________________________________________________________________________##

# Streamlit
import streamlit as lit
import requests


## ______________________________________________________________________________________________________________________##

#import launch_pages # Import applications Launch page function
#import registered_pages.ZeroTrustFunctions.passwordvault

## ______________________________________________________________________________________________________________________##

import Firebase.firebaseconfig # Firebase Configuartion and Authentication Function
#import registered_pages.zero_trust # if successfull navigate user to the zero_trust landing page -> User Dashboard

database=Firebase.firebaseconfig.firebase_database()
auth= Firebase.firebaseconfig.firebase_auth()




## ______________________________________________________________________________________________________________________##
def login(email,password):
     
          # Calling Firebase Config Authentication Function
     try:                         
               user=auth.sign_in_with_email_and_password(email,password) # Authenticates registered users agains password

               name=database.child(user["idToken"]).child('AccountName').get().val() #read user data from database and write a greeting  message
               lit.sidebar.subheader("Hi " + name + " Network")
               #user_page()
                   
     except requests.exceptions.HTTPError as err:
          lit.write(err)
          lit.error("There is a problem with the details you entered, please retry.")  
          lit.subheader("""Forgot your password?
              You can reset your password in the drop down list""")        
     
      
          

## ||________________________________________________End of Login______________________________________________________________________||##

## ||______________________________________________Start the User Page_________________________________________________________________||##




