import pickle
from socket import *
from constRPC import *
from client import Client
from dbclient import DBClient

c1   = Client(PORTC1)
dbC1 = DBClient(HOSTS, PORTS)
dbC1.create()
dbC1.appendData('Client 1')
c1.sendTo(HOSTC2, PORTC2, dbC1)