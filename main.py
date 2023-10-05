import socket
import ssl

# Define the server's address and port
hostname = 'www.google.com'
# List of TLS versions to check
tls_versions = [ssl.TLSVersion.TLSv1_3, ssl.TLSVersion.TLSv1_2, ssl.TLSVersion.TLSv1_1, ssl.TLSVersion.TLSv1]

# Initialize a list to store supported TLS versions
supported_versions = []

# Function to check TLS version support
def check_tls_version(version):
    #print(version)
    try:

        context = ssl.create_default_context()
        context.minimum_version = version
        context.maximum_version = version

        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the negotiated TLS version
                negotiated_version = ssock.version()
                #print(negotiated_version);
                return negotiated_version

    except ssl.SSLError as e:
        print('ssl error');
        return None
    except ConnectionResetError as e:
        print('connection reset error');
        return None


# Check supported TLS versions
for version in tls_versions:
    negotiated_version = check_tls_version(version)
    if negotiated_version:
        supported_versions.append((version, negotiated_version))

# Print the supported TLS versions
if supported_versions:
    for version, negotiated_version in supported_versions:
        print(f'Supported TLS Version for {hostname}: {str(version)} (Negotiated: {negotiated_version})')
else:
    print(f'No supported TLS versions found for {hostname}')
