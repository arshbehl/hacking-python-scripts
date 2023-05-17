import dns.resolver

# Set the target domain and record type
target_domain = input("Write a domain name: ")
all_record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]

# Create a DNS resolver
resolver = dns.resolver.Resolver()
for record_type in all_record_types:
    
    try:
        answers = resolver.resolve(target_domain, record_type)
    except: 
        continue

    # Printing the answers
    print(f"The DNS has recordes for {target_domain} ({record_type}):")

    for rdata in answers:
        print(f"{rdata}")
