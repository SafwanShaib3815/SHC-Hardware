import time
import user_db

db = user_db.User_db("somemail@mail.com", "Admin1234#")

sensordata = {"Temperature": 20,
              "Humidity": 48,
              "Motion": "no motion",
              "Smoke": "no smoke",
              "RFID": "white card",
              "Timestamp": None}

db.data_send(20, 48, "no motion", "no smoke", "rfid white")
