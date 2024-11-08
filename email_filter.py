# email_filter.py

def filter_emails(input_file, output_file):
    # List of non-US country domains to filter out
    country_domains = [
        ".eu", ".fr", ".de", ".it", ".nl", ".es",  # Europe
        ".in", ".jp", ".cn", ".sg", ".hk", ".kr",  # Asia
        ".ae", ".sa", ".za",                       # Middle East & Africa
        ".ca", ".mx", ".br", ".ar",                # Americas (non-U.S.)
        ".au", ".co.uk", ".co.nz"                  # Oceania, UK, New Zealand
    ]
    
    # List of common public email domains to filter out
    public_domains = [
        "@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com"
    ]
    
    # Read emails from the input file and filter them
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            email = line.strip()
            # Check if the email does not end with any unwanted country domains or public domains
            if not any(email.endswith(domain) for domain in country_domains) and \
               not any(public_domain in email for public_domain in public_domains):
                outfile.write(email + "\n")

# Prompt user for input and output file names
input_file = input("Enter the input file name (e.g., emails.txt): ")
output_file = input("Enter the output file name (e.g., filtered_emails.txt): ")

# Run the email filter function
filter_emails(input_file, output_file)

print(f"Email filtering complete. Check the '{output_file}' file.")