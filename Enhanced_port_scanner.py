import socket
import argparse
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for each connection attempt
        result = sock.connect_ex((target, port))  # Returns 0 if the port is open
        sock.close()
        return port, result == 0
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return port, False

def scan_ports(target, start_port, end_port, report_file):
    print(f"\nStarting scan on {target}")
    print(f"Scanning ports from {start_port} to {end_port}...\n")
    
    open_ports = []
    ports = range(start_port, end_port + 1)
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        future_to_port = {executor.submit(scan_port, target, port): port for port in ports}
        
        for future in as_completed(future_to_port):
            port, is_open = future.result()
            if is_open:
                print(f"Port {port} is open")
                open_ports.append(port)
    
    print("\nScan completed!")
    print(f"Open ports: {open_ports}" if open_ports else "No open ports found.")


    with open(report_file, "w") as file:
        file.write(f"Port scan report for {target}\n")
        file.write(f"Scanning ports from {start_port} to {end_port}\n")
        file.write(f"Open ports:\n")
        if open_ports:
            for port in open_ports:
                file.write(f"{port}\n")
        else:
            file.write("No open ports found.\n")
    
    print(f"Report saved to {report_file}")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Enhanced Port Scanner with Multi-Threading")
    parser.add_argument("target", help="Target IP address or hostname to scan")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")
    parser.add_argument("--report", type=str, default="port_scan_report.txt", help="Report file name (default: port_scan_report.txt)")
    
    args = parser.parse_args()
    
    target = args.target
    start_port = args.start
    end_port = args.end
    report_file = args.report
    
    start_time = datetime.now()
    
    scan_ports(target, start_port, end_port, report_file)
    
    end_time = datetime.now()
    print(f"\nTime taken: {end_time - start_time}")
