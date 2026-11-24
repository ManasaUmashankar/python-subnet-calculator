import ipaddress


def calculate_subnet(cidr):
    try:
        network = ipaddress.ip_network(cidr, strict=False)

        hosts = list(network.hosts())

        if hosts:
            first_host = str(hosts[0])
            last_host = str(hosts[-1])
        else:
            first_host = None
            last_host = None

        return {
            "valid": True,
            "network_address": str(network.network_address),
            "broadcast_address": str(network.broadcast_address),
            "subnet_mask": str(network.netmask),
            "prefix_length": network.prefixlen,
            "total_addresses": network.num_addresses,
            "usable_hosts": len(hosts),
            "first_host": first_host,
            "last_host": last_host
        }

    except ValueError:
        return {"valid": False}