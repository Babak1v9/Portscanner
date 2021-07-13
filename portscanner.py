import socket
from IPy import IP


def scan(target, port_count):
    converted_ip = check_ip(target)
    print("\n" + "Converted IP: " + str(converted_ip))
    print("-_0 - Scanning Target..." + "\n")
    for port in range(1, int(port_count)):
        scan_ports(converted_ip, port)


def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(socket):
    return socket.recv(1024)  # amount of bytes we want to receive


def scan_ports(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print("[+] Port" + str(port) + " is open. Banner: " + str(banner.decode().strip('\n')))  # remove b' and \n
        except:
            print("[+] Port" + str(port) + " is open. No Banner received.")
    except:
        pass

if __name__ == "__main__":
    targets = input('[+] Enter Target(s) to scan (split targets with \',\'): ')
    port_num = input('Enter the number of Ports you want to be scanned: ')
    if ',' in targets:
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(' '), port_num)
    else:
        scan(targets, port_num)