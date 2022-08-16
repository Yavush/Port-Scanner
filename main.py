#Basit bir website port tarayıcı.

import socket
import os


DEFAULT_TIMEOUT = 0.5


SUCCESS = 0

def check_port(*Host_port, timeout=DEFAULT_TIMEOUT):

    sock = socket.socket()
    sock.settimeout(timeout)


    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    connected = sock.connect_ex(Host_port) is SUCCESS


    sock.close()

    # True dönerse port açık, false dönerse port kapalıdır.
    return connected

checkPort = input("Port taraması yapmak istediğiniz site : ")
checkPortNo = int(input("Taramak istediğiniz port numarası : "))

con = check_port(checkPort, checkPortNo)
print(con)
