from src.subnet_calculator import calculate_subnet

print("=" * 45)
print("           PYTHON SUBNET CALCULATOR")
print("=" * 45)

cidr = input("\nEnter an IPv4 address with CIDR: ").strip()

if not cidr:
    print("\nError: Please enter an IP address and CIDR prefix.")

else:
    result = calculate_subnet(cidr)

    if result["valid"]:

        print("\n========== NETWORK REPORT ==========")

        print("Network Address   :", result["network_address"])
        print("Broadcast Address :", result["broadcast_address"])
        print("Subnet Mask       :", result["subnet_mask"])
        print("CIDR Prefix       :", "/" + str(result["prefix_length"]))

        print("\n========== HOST DETAILS ==========")

        print("Total Addresses   :", result["total_addresses"])
        print("Usable Hosts      :", result["usable_hosts"])
        print("First Usable IP   :", result["first_host"])
        print("Last Usable IP    :", result["last_host"])

        print("\n========================================")

    else:
        print("\nError: Invalid IPv4 CIDR input.")