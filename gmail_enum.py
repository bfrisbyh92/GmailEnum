import requests
import argparse
from colorama import Back, Fore, Style

def main(email_list_file, output_file=None):
    valid_accounts = []
    not_valid_accounts = []
    
    with open(email_list_file, 'r') as f:
        emails = f.read().splitlines()
        
    banner = """
█▀▀ █▀▄▀█ ▄▀█ █ █░░   █▀▀ █▄░█ █░█ █▀▄▀█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
█▄█ █░▀░█ █▀█ █ █▄▄   ██▄ █░▀█ █▄█ █░▀░█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄"""
    banner2 = 'hͪᴛⷮᴛⷮрⷬs͛://giͥᴛⷮhͪuͧвⷡ.cͨoͦmͫ/вⷡfrͬiͥs͛вⷡyhͪ92/GmͫaͣiͥlEͤnuͧmͫ'
    
    print('\n \n' + banner + '\n \n' + banner2 + '\n \n')
    print(f"Total lines in wordlist: {len(emails)}")

    for email in emails:
        if not email.endswith('@gmail.com'):
            email = email + '@gmail.com'
        url_req = f"https://mail.google.com/mail/gxlu?email={email}"
        r = requests.get(url=url_req)
        data = str(r.headers)
        cookie_true = data.find("Set-Cookie")

        if cookie_true != -1:
            valid_accounts.append(email)
            print(f"[+] {email} is a valid account")
        else:
            not_valid_accounts.append(email)
            print(f"[-] {email} not valid")

    if valid_accounts and output_file:
        with open(output_file, 'w') as f:
            f.write('\n'.join(valid_accounts))
        print(f"\n{len(valid_accounts)} Valid accounts saved to {output_file}")
    elif valid_accounts:
        print("No output file specified. Valid accounts not saved.")
    else:
        print("No valid accounts found.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check if email accounts are valid.')
    parser.add_argument('-e', '--email_list', help='Path to the email list file')
    parser.add_argument('-o', '--output_file', help='Path to the output file')
    args = parser.parse_args()

    if args.email_list:
        email_list_file = args.email_list
    else:
        email_list_file = input("Enter the path to the email list file: ")

    main(email_list_file, args.output_file)


## Todo's
# Add Color with Colorama
# Add a verbose mode showing all attempts