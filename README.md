# findTlsVersion


This Python script allows you to check which Transport Layer Security (TLS) versions are supported by a remote server.

## Prerequisites

Before using this script, ensure that you have the following:

- Python 3.x installed on your system.
- The necessary Python libraries (`socket` and `ssl`) should be available. These libraries are typically included with Python.
- An active internet connection to access the server you want to check.

## Usage

1. Clone the repository or download the `main.py` script to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script using the following command:
        python main.py


4. The script will connect to a remote server (by default, it connects to `www.google.com` on port 443) and check which TLS versions are supported.

5. The supported TLS versions will be displayed in the terminal along with the TLS version negotiated during the connection.

## Configuration

- You can specifyt the host and port using the arguments --host and --port

- The `tls_versions` list in the script contains the TLS versions to check. You can customize this list to include or exclude specific versions.

## Troubleshooting

If you encounter any issues while running the script, consider the following:

- Ensure that your Python environment has internet connectivity.

- Verify that your system's DNS settings are configured correctly to resolve hostnames.

- Check for firewall or security software that might be blocking outgoing connections.

- If you're behind a proxy server, configure your Python environment to use the appropriate proxy settings.

## Author

Anantha Krishnan
