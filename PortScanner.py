import socket
from datetime import datetime

target = input("Enter the host name: ")
ip = socket.gethostbyname(target)

print ("Enter the range of ports to scan the Target")
startport= input("Enter the Start Port: ")
endport= input("Enter the End Port: ")

print("Given Target", ip , "is scanning")
time_init = datetime.now()

try:
    for port in range (int(startport), int(endport)):
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.settimeout(0.2)
        result = server_sock.connect_ex((ip, port))
        if result == 0:
            print("port {}: Open".format(port))
        else:
            pass
        server_sock.close()
except:
    print("couldn't connect to server")

time_finish = datetime.now()
total_time = time_finish - time_init

print("Total time to Scan the ports are: ",total_time)