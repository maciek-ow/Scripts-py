import socket
import sys

def scan_ports(host_ip, start_port, end_port): #definition of function which takes hosts ip , starting port and ending port
    print(f"Scanning ports on {host_ip}...") #printing that script is running

    for port in range(start_port, end_port): #iterates through ports range
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a connection timeout

        result = sock.connect_ex((host_ip, port)) #creating a socket and attemtpitng to connect to it

        if result != 0: #checking connection result, if it is 0 it means that connection was succesfull
             port_listener(host_ip,port)
        sock.close() #closing socket
def scan_ports_on_listen(host_ip,port): #definition of function which takes hosts ip , starting port and ending port
    #for port in range(start_port, end_port): #iterates through ports range
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a connection timeout

    result = sock.connect_ex((host_ip, port)) #creating a socket and attemtpitng to connect to it

    if result == 0: #checking connection result, if it is 0 it means that connection was succesfull
        print(f"Port {port} is open") # printing open port
    sock.close() #closing socket
def port_listener(target_hosts,start_port, end_port):
    for port in range(start_port, end_port):
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         result = sock.connect_ex((target_hosts, port))
         if result == 0:
            print(f"Port {port} is open")
         else:
            try:
                # With the help of bind() function 
                # binding host and port
                sock.bind((target_hosts, port))
      
            except socket.error as message:
     
        # if any error occurs then with the 
        # help of sys.exit() exit from the program 
                print(f"Bind unsuccesfull on: {port}")
                sys.exit()
     
    # print if Socket binding operation completed    
  
    # With the help of listening () function
    # starts listening
    sock.listen(0)
    scan_ports_on_listen(target_hosts,port)
    # print the address of connection
    sock.close()
if __name__ == "__main__": # checks if this file is run directly.
    target_hosts = input("Enter the host IP address: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    port_listener(target_hosts, start_port, end_port)
