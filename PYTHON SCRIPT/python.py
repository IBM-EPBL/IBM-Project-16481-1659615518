import wiotp.sdk.device
import time
import os
import datetime
import random
myConfig = {
    "identity":{
        "orgId":"m0zw1j",
        "typeId": "raspberry",
        "deviceId": "8138191060"
        },
    "auth":{
        "token": "d525!T5ZUiwPeMf5u*"
        }
    }
client=wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers=None)
client.connect()

def myCommandCallback(cmd):
    print("message received from ibm iot platform: %s" %cmd.data['command'])
    m=cmd.data['command']
    if(m=="motoron"):
        print("motor is switched on")
    elif(m=="motoroff"):
        print("motor is switched off")
    print(" ")

while True:
    soil=random.randint(0,100)
    temp=random.randint(-20,125)
    hum=random.randint(0,100)
    myData={'soil_moisture':soil,'temperature':temp,'humidity':hum}
    client.publishEvent(eventId="status",msgFormat="json",data=myData,qos=0,onPublish=None)
    print("published data successfully: %s", myData)
    time.sleep(2)
    client.commandCallback = myCommandCallback
client.disconnect()
