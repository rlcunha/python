# This is a sample Python script.
import os
import time
import uuid
from azure.iot.device import IoTHubDeviceClient, Message
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from urllib2 import Request, urlopen
import json

path1 = '42.974049,-81.205203|42.974298,-81.195755'
request=Request('http://maps.googleapis.com/maps/api/elevation/json?locations='+path1+'&sensor=false')
response = urlopen(request)
elevations = response.read()


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    conn_str = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")
    # The client object is used to interact with your Azure IoT hub.
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the client.
    device_client.connect()

    # send 2 messages with 2 system properties & 1 custom property with a 1 second pause between each message
    for i in range(1, 3):
        print("sending message #" + str(i))
        msg = Message("test wind speed " + str(i))
        msg.message_id = uuid.uuid4()
        msg.correlation_id = "correlation-1234"
        msg.custom_properties["tornado-warning"] = "yes"
        device_client.send_message(msg)
        time.sleep(1)

    # send 2 messages with only custom property with a 1 second pause between each message
    for i in range(3, 5):
        print("sending message #" + str(i))
        msg = Message("test wind speed " + str(i))
        msg.custom_properties["tornado-warning"] = "yes"
        device_client.send_message(msg)
        time.sleep(1)

    # send 2 messages with only system properties with a 1 second pause between each message
    for i in range(5, 7):
        print("sending message #" + str(i))
        msg = Message("test wind speed " + str(i))
        msg.message_id = uuid.uuid4()
        msg.correlation_id = "correlation-1234"
        device_client.send_message(msg)
        time.sleep(1)

    # send 2 messages with 1 system property and 1 custom property with a 1 second pause between each message
    for i in range(7, 9):
        print("sending message #" + str(i))
        msg = Message("test wind speed " + str(i))
        msg.message_id = uuid.uuid4()
        msg.custom_properties["tornado-warning"] = "yes"
        device_client.send_message(msg)
        time.sleep(1)

    # send only string messages
    for i in range(9, 11):
        print("sending message #" + str(i))
        device_client.send_message("test payload message " + str(i))
        time.sleep(1)

    # finally, disconnect
    device_client.disconnect()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
