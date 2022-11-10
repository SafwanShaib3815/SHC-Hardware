#!/usr/bin/python
#
# Demo code for CENG 355 created by Austin Tian
# Based on the reference from pyrebase
# Website: https://github.com/thisbejim/Pyrebase
# --------------------------------------

import time
from time import sleep
# please install this package by using "pip install pyrebase4" or "pip3 install pyrebase4"
import pyrebase
import random
import self as self
import re


class User_db:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    # configuration of the database access
    # Global objects: config and user
    # ====================================================================================================
    config = {
        "apiKey": "AIzaSyBSi0GAMC8quBMtVfXZ-elPTCkQ6S7jGeM",  # replace this with your Firebase apiKey
        "authDomain": "smarthomecontroller-a7978.firebaseapp.com",  # replace this with your firebaseid.firebaseapp.com
        "databaseURL": "https://smarthomecontroller-a7978-default-rtdb.firebaseio.com/",
        # replace this with your databaseURL. s
        "storageBucket": "smarthomecontroller-a7978.appspot.com",  # replace this with your firebaseid.appspot.com
    }
    user = None

      # define user as a global variable to access from all the functions.


    # ====================================================================================================

    # The authorization function
    # ====================================================================================================
    def GetAuthorized(self,firebase):
        global user
        auth = firebase.auth()  # Get a reference to the auth service
        # authenticate a user
        try:
            user = auth.sign_in_with_email_and_password(self.email, self.password)  # replace this with your username and password of the account
            #print(user)# display the user information, if successful
        except:
            print("Not authorized")
            #user = None


    # The function to initialize the database.
    # ====================================================================================================
    def dbInitialization(self):
        firebase = pyrebase.initialize_app(self.config)  # has to initialize the database
        self.GetAuthorized(firebase)  # get authorized to operate on the database.
        return firebase


    # The function to get the data from firebase database.
    # ====================================================================================================
    def GetDatafromFirebase(self,db):
        results = db.child("Door Records/testing").get(user["idToken"]).val();  # needs the authorization to get the data.
        print("These are the records from the Database")
        print(results)
        return

    # The function to send the data to firebase database.
    # ====================================================================================================
    def sendtoFirebase(self,db, sensordata):
        result = db.child("Door Records/testingsss").push(sensordata, user["idToken"])  # needs the authorization to save the data
        print(result)
        return


    # The function to send the data to firebase database's user authorized section.
    # Each user has a separate record tree, and it is only accessible for the authorized users.
    # ====================================================================================================

    def sendtoUserFirebase_set(self,db, sensordata):
        #tyr and catch block to extract the .com from user email string
        try:
            user_email = re.search('(^.+)....', user["email"]).group(1)# this will guarantee the data is stored into the user directory
        except AttributeError:
            print("error with creating string out of user email, returning..")
        for key in sensordata:
            #if key == "Timestamp": #skip sending a separate time stamp record
                #continue
                #result = db.child(user_email).child(key).push(sensordata[key], user["idToken"])  # sending current value to its location according to current key
            if sensordata[key] is not None: #Only record time of the sensor data being sent
                result = db.child(user_email).child(key).child("Real_Time").set(sensordata[key], user["idToken"])  # send time of each record
        #print(result)
        return
    def sendtoUserFirebase_push(self,db, sensordata):
        #tyr and catch block to extract the .com from user email string
        try:
            user_email = re.search('(^.+)....', user["email"]).group(1)# this will guarantee the data is stored into the user directory
        except AttributeError:
            print("error with creating string out of user email, returning..")
        for key in sensordata:
            #if key == "Timestamp": #skip sending a separate time stamp record
                #continue
                #result = db.child(user_email).child(key).push(sensordata[key], user["idToken"])  # sending current value to its location according to current key
            if sensordata[key] is not None: #Only record time and send the data of the intended sensor 
                result = db.child(user_email).child(key).child("Records").push(sensordata[key], user["idToken"])  # send time of each record
                result_t = db.child(user_email).child(key).child("Records").push(time.ctime(), user["idToken"])  # send time of each record


        #print(result, result)
        return



    # The function to set up the record structure to be written to the database.
    # ====================================================================================================
    def setupData(self, temp, humid, motion, smoke, rfid):
        sensor = {"Temperature": temp,
                  "Humidity": humid,
                  "Motion": motion,
                  "Smoke": smoke,
                  "RFID": rfid}
        return sensor


    # The following code would write and read the database with the authorized user
    # ====================================================================================================
    def data_send_set(self, temp, humid, motion, smoke, rfid ):  # test code to send and receive data from the firebase database.
        #print("\nsending to the real time field in the Firebase")
        firebase = self.dbInitialization()
        if user is not None:  # if authorization is not failed.
            sensordata = self.setupData(temp, humid, motion, smoke, rfid)  # this is the epoch time for this record.
            #self.sendtoFirebase(firebase.database(), sensordata)  # save to the public access data tree
            self.sendtoUserFirebase_set(firebase.database(), sensordata)  # save to the user specific userdata tree

            #self.GetDatafromFirebase(firebase.database())  # this statement is outside the while loop and to read the data back

    def data_send_push(self, temp, humid, motion, smoke, rfid ):  # test code to send and receive data from the firebase database.
        #print("\nSending to the records field of the Firebase")
        firebase = self.dbInitialization()
        if user is not None:  # if authorization is not failed.
            sensordata = self.setupData(temp, humid, motion, smoke, rfid)  # this is the epoch time for this record.
            #self.sendtoFirebase(firebase.database(), sensordata)  # save to the public access data tree
            self.sendtoUserFirebase_push(firebase.database(), sensordata)  # save to the user specific userdata tree

            #self.GetDatafromFirebase(firebase.database())  # this statement is outside the while loop and to read the data back


