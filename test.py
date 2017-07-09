from Node import NodeClass 
import time
import threading


def printMsg(msg):
    print(msg.payload)


def printTopic(msg):
    print(msg.topic)


n1 = NodeClass("robor/#", printMsg)
n2 = NodeClass("roro", printTopic)

n1.run("iot.eclipse.org", 1883, 60)
n2.run("iot.eclipse.org", 1883, 60)
