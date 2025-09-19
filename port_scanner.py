import socket
import sys

def scan_ports(target, ports):
    print(f"Scanning {target} for open ports...\n")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <target_ip>")
        sys.exit(1)

    target_ip = sys.argv[1]
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 3389]

    scan_ports(target_ip, ports_to_scan)
