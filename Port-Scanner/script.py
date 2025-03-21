import socket
import threading

# Function to check if a port is open
def scan_port(host_ip, port, open_ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a connection timeout

    result = sock.connect_ex((host_ip, port))  # Attempt to connect to the port

    if result == 0:  # If the connection is successful, the port is open
        print(f"Port {port} is open (connected)")
        open_ports.append(port)  # Add the open port to the list
    else:
        print(f"Port {port} is closed or filtered (no response)")
    sock.close()  # Close the socket

# Function to scan a range of ports using threading
def scan_ports_with_threading(target_host, start_port, end_port):
    open_ports = []  # List to store confirmed open ports
    threads = []  # List to store thread objects

    for port in range(start_port, end_port + 1):  # Iterate through the port range
        # Create a thread for each port scan
        thread = threading.Thread(target=scan_port, args=(target_host, port, open_ports))
        threads.append(thread)
        thread.start()  # Start the thread

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Print all confirmed open ports at the end
    if open_ports:
        print("\nSummary of confirmed open ports:")
        for port in sorted(open_ports):  # Sort the ports for better readability
            print(f"Port {port} is open")
    else:
        print("\nNo confirmed open ports found.")

if __name__ == "__main__":
    target_host = input("Enter the host IP address: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    scan_ports_with_threading(target_host, start_port, end_port)