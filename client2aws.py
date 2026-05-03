import pickle
from socket import *
from constRPC import *
from client import Client

c2   = Client(PORTC2)
data = c2.recvAny()
dbC2 = pickle.loads(data)
dbC2.appendData('Client 2')
print(dbC2.getValue())