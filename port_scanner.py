import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

# ANSI Color Codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

open_ports = []
lock = None

def get_banner(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            banner = s.recv(1024).decode().strip()
            return banner
    except:
        return ""

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"
                banner = get_banner(ip, port)
                return (port, True, service, banner)
    except:
        pass
    return (port, False, "", "")

def format_port_results(results):
    print(f"\n{CYAN}{'Port':<8}{'Service':<15}{'Banner'}{RESET}")
    print("-" * 50)
    for port, is_open, service, banner in sorted(results):
        if is_open:
            print(f"{GREEN}{port:<8}{service:<15}{banner}{RESET}")
    print()

def port_scan(target, start_port, end_port, max_threads=100):
    try:
        ip = socket.gethostbyname(target)
        print(f"{YELLOW}Scanning {target} [{ip}] from port {start_port} to {end_port}...{RESET}\n")
    except socket.gaierror:
        print(f"{RED}Hostname could not be resolved.{RESET}")
        return

    results = []
    total_ports = end_port - start_port + 1
    scanned = 0

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            scanned += 1
            sys.stdout.write(f"\rProgress: {scanned}/{total_ports} ports scanned")
            sys.stdout.flush()

    format_port_results(results)

if __name__ == "__main__":
    target = input("Enter target host (e.g. 127.0.0.1 or scanme.nmap.org): ")
    try:
        start_port = int(input("Enter start port (e.g. 1): "))
        end_port = int(input("Enter end port (e.g. 100): "))
    except ValueError:
        print(f"{RED}Please enter valid port numbers.{RESET}")
        sys.exit(1)

    port_scan(target, start_port, end_port)
