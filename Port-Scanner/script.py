import socket
import threading

def scan_ports_on_listen(host_ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a connection timeout

    result = sock.connect_ex((host_ip, port))  # Attempt to connect to the port

    if result == 0:  # If the connection is successful, the port is open
        print(f"Port {port} is open")
        return True  # Return True if the port is open
    else:
        print(f"Port {port} is closed")
        return False  # Return False if the port is closed
    sock.close()  # Close the socket

def port_listener(target_host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((target_host, port))  # Bind to the port
        print(f"Listening on port {port}...")
        sock.listen(1)  # Start listening
        print(f"Port {port} is open and listening.")
    except socket.error as message:
        print(f"Bind unsuccessful on port {port}: {message}")
    finally:
        sock.close()  # Close the socket

def scan_and_listen(target_host, start_port, end_port):
    open_ports = []  # List to store open ports

    for port in range(start_port, end_port + 1):  # Iterate through the port range
        # Create a thread to listen on the port
        listen_thread = threading.Thread(target=port_listener, args=(target_host, port))
        listen_thread.start()

        # Scan the port to check if it's open
        if scan_ports_on_listen(target_host, port):
            open_ports.append(port)  # Add the open port to the list

        # Wait for the listening thread to finish
        listen_thread.join()

    # Print all open ports at the end
    if open_ports:
        print("\nSummary of open ports:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("\nNo open ports found.")

if __name__ == "__main__":
    target_host = input("Enter the host IP address: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    scan_and_listen(target_host, start_port, end_port)