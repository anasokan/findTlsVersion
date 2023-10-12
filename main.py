import socket
import ssl
import argparse

# Initialize a list to store supported TLS versions
supported_versions = []

# Function to check TLS version support
def check_tls_version(host, port, version):
    try:
        context = ssl.create_default_context()
        context.minimum_version = version
        context.maximum_version = version
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        with socket.create_connection((host, port)) as sock:
            print(f'Testing {version} for {host}:{port}')
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                negotiated_version = ssock.version()
                return negotiated_version

    except ssl.SSLError as e:
        print('SSL error')
        print(e)
        return None
    except ConnectionResetError as e:
        print('Connection reset error')
        return None

# Parse command line arguments
parser = argparse.ArgumentParser(description='Check supported TLS versions for a host and port.')
parser.add_argument('--host', default='google.com', help='Hostname to connect to (default: google.com)')
parser.add_argument('--port', type=int, default=443, help='Port to connect to (default: 443)')
args = parser.parse_args()

# List of TLS versions to check
tls_versions = [ssl.TLSVersion.TLSv1_3, ssl.TLSVersion.TLSv1_2, ssl.TLSVersion.TLSv1_1, ssl.TLSVersion.TLSv1]

# Check supported TLS versions
for version in tls_versions:
    negotiated_version = check_tls_version(args.host, args.port, version)
    if negotiated_version:
        supported_versions.append((version, negotiated_version))

# Print the supported TLS versions
if supported_versions:
    for version, negotiated_version in supported_versions:
        print(f'Supported TLS Version for {args.host}:{args.port}: {str(version)} (Negotiated: {negotiated_version})')
        
else:
    print(f'No supported TLS versions found for {args.host}:{args.port}')
