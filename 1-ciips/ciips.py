import ipaddress

input_file = input("Enter file path containing CIDRs: ").strip()

try:
    # Step 1: Read CIDRs and remove duplicate CIDRs
    with open(input_file, "r") as infile:
        cidrs = []
        seen_cidrs = set()

        for line in infile:
            cidr = line.strip()

            if not cidr:
                continue

            if cidr not in seen_cidrs:
                seen_cidrs.add(cidr)
                cidrs.append(cidr)

    # Step 2: Expand CIDRs and remove duplicate IPs
    unique_ips = set()
    total_generated = 0

    for cidr in cidrs:
        try:
            network = ipaddress.ip_network(cidr, strict=False)

            print(f"{cidr} -> {network.num_addresses} addresses")
            print(f"Range: {network.network_address} - {network.broadcast_address}")

            for ip in network:
                total_generated += 1
                unique_ips.add(str(ip))

        except ValueError:
            print(f"Invalid CIDR: {cidr}")

    # Step 3: Save unique IPs
    with open("ips.txt", "w") as outfile:
        for ip in sorted(unique_ips, key=ipaddress.ip_address):
            outfile.write(ip + "\n")

    print("\nDone!")
    print(f"Unique CIDRs processed : {len(cidrs)}")
    print(f"Total IPs generated    : {total_generated}")
    print(f"Unique IPs saved       : {len(unique_ips)}")
    print("Output saved to ips.txt")

except FileNotFoundError:
    print("Input file not found.")