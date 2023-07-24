# HTTP_Login_SQL_Bypass
Credit due to  Sagiv Michael and his tool SQL-login-bypass 
at https://github.com/sAjibuu/SQL-login-bypass

Mines not better; but python makes everything better right?

HTTP Login Page Brute Force with SQL Queries

This Python script performs a brute force attack on a web login page using a list of SQL queries. The script sends HTTP POST requests to the specified URL and checks the response for a specified error message that indicates a failed login attempt. If the error message is not found in the response, the script assumes that the current SQL query is a valid credential.
Prerequisites

    Python 3
    requests library

You can install the requests library using pip:

bash

pip install requests

Usage

bash

python brute_force.py -u <url> -w <wordlist> -r <request> -e <error> [options]

    -u, --url: The URL of the login page. This argument is required.
    -w, --wordlist: The path to the wordlist file. This file should contain SQL injection payloads, one per line. This argument is required.
    -r, --request: The request body. This should contain the string FUZZ at the point where the SQL injection payload should be inserted. This argument is required.
    -e, --error: The error message that indicates a failed login attempt. This argument is required.
    -H, --header: An optional HTTP header to include in the requests, in the format key:value.
    -c, --cookie: An optional cookie to include in the requests, in the format key=value.
    -s, --ssl: If set to True, the script will not check the SSL/TLS certificate of the server. The default is False.
    -C, --csrf: If set to True, the script will attempt to bypass CSRF protection. This feature is not currently implemented. The default is False.
    -v, --verbose: If set to True, the script will print the full response text for each request. The default is False.

Example

bash

python brute_force.py -u https://example.com/login -w sql_payloads.txt -r "username=FUZZ&password=pass" -e "Invalid username"

This command will read SQL injection payloads from sql_payloads.txt, insert each payload into the request body at the point marked by FUZZ, and send a POST request to https://example.com/login. If the response does not contain the string "Invalid username", the script will print the current payload as a valid credential.
