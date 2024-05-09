import socket
from datetime import datetime
import pyfiglet
import sys

#Using pyfiglet to format our banner
ascii_banner = pyfiglet.figlet_format("Python port scanner!")

#Printing the banner
print(ascii_banner)
print("Note: This scanner automatically scans all ports")

#Input of host IP address we wish to scan
#Resolving the host name of the target IP
target = input("Please enter the IP you would like to scan: ")
targetIP = socket.gethostbyname(target)

#Printing information about the scan
print("-" * 50)
print("Scanning target: {}".format(targetIP))
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)

#Scanning ports of the target IP
try:
    for port in range(1, 65535):
        #Creating the socket pair
        #AF_INET states it is an IPV4 address
        #SOCK_STREAM states it is a TCP connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Default timeout if no SYN/ACK has been returned
        socket.setdefaulttimeout(1)
        #Result is equal to the connection on that port
        result = s.connect_ex((target, port))
        #If the connection is successful, print the port number
        if result == 0:
            print("Port {} is open".format(port))
        #Close the connection    
        s.close()

except KeyboardInterrupt:
    print("\n Closing program!")
    sys.exit()
except socket.gaierror:
    print("Host name could not be resolved!")
    sys.exit()
except socket.error:
    print("Host not responding!")
    sys.exit()
