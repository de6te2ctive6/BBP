#!/usr/bin/env python3

from urllib.parse import urlparse

def main():
    file_path = input("Enter httpx output file path: ").strip()

    ips = []
    ports = set()

    try:
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parsed = urlparse(line)

                ip = parsed.hostname
                port = parsed.port

                # Assign default ports if omitted
                if port is None:
                    if parsed.scheme == "https":
                        port = 443
                    elif parsed.scheme == "http":
                        port = 80

                if ip:
                    ips.append(ip)
                if port:
                    ports.add(port)

    except FileNotFoundError:
        print("File not found.")
        return

    # Remove duplicate IPs while preserving order
    ips = list(dict.fromkeys(ips))

    print("\nIPs:\n")
    for ip in ips:
        print(ip)

    print("\nPorts:")
    print(",".join(str(p) for p in sorted(ports)))

    print("\nSuggested nmap command:\n")
    print(f'nmap -sV -p{",".join(str(p) for p in sorted(ports))} {" ".join(ips)}')

if __name__ == "__main__":
    main()