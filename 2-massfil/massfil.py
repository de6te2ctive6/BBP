#!/usr/bin/env python3

def main():
    # Ask for masscan output file
    file_path = input("Enter masscan output file path: ").strip()

    # Ask for ports (example: 80,443,8080)
    ports_input = input("Enter ports (comma-separated): ").strip()
    target_ports = {p.strip() for p in ports_input.split(",") if p.strip()}

    found = {}

    try:
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()

                # Skip comments and empty lines
                if not line or line.startswith("#"):
                    continue

                parts = line.split()

                # Expected format:
                # open tcp 80 192.168.1.1 123456789
                if len(parts) < 4:
                    continue

                port = parts[2]
                ip = parts[3]

                if port in target_ports:
                    found.setdefault(port, []).append(ip)

    except FileNotFoundError:
        print("File not found.")
        return

    print("\nResults:\n")

    for port in sorted(target_ports, key=int):
        print(f"Port {port}:")
        ips = found.get(port, [])
        if ips:
            for ip in ips:
                print(f"  {ip}")
        else:
            print("  No IPs found.")
        print()


if __name__ == "__main__":
    main()