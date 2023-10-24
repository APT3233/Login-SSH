
#-----------------Customized by APT3233-------------------
# Don't change anything

import argparse
import logging
import socket

def scan_port(host, port):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, port))
        s.close()
        return 1
    except socket.timeout:
        return 0
    except socket.error:
        return -1

def main():
    

    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description="Port scanner")
    parser.add_argument("host", help="The hostname or IP address of the target host.")

    args = parser.parse_args()

    for port in range(1, 3501):
        status = scan_port(args.host, port)
        if status == 1:
            logging.info(f"Port {port} is open.")

if __name__ == "__main__":
    main()
