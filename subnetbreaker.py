import ipaddress

def get_subnets(subnet, output_prefix):
    network = ipaddress.IPv6Network(subnet)
    subnets = list(network.subnets(new_prefix=output_prefix))
    return subnets

def write_subnets_to_file(subnets, filename):
    with open(filename, 'w') as file:
        for subnet in subnets:
            file.write(str(subnet) + '\n')

# Example usage
subnet = "2a13:df80::/32"
output_prefix = 48
filename = "subnets.txt"

subnets = get_subnets(subnet, output_prefix)
write_subnets_to_file(subnets, filename)
