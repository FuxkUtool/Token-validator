import hashlib
import os
from colorama import Fore, init

green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
yellow = Fore.YELLOW

print(f'''
    {green}FuxkUTOOLS
                {red}coded by iampopg & himld
    ''')

# Function to generate a user ID from the input username
def generate_user_id(username):
    return username

# Function to generate a token for the user ID
def generate_token(user_id, secret_key):
    # Concatenate user_id and secret_key (you should use a real secret key)
    data_to_hash = user_id + secret_key
    # Hash the concatenated data using SHA-256 (you can choose a different hash function)
    hashed_data = hashlib.sha256(data_to_hash.encode()).hexdigest()
    return hashed_data

# Rest of the code remains the same...
# Function to check if a provided token is in the token file
def check_token_in_file(token_to_check, token_file):
    with open(token_file, 'r') as file:
        for line in file:
            if line.strip() == token_to_check:
                return True
    return False

# Function to mark a token as used
def mark_token_as_used(token_to_mark, used_tokens_file):
    with open(used_tokens_file, 'a') as file:
        file.write(token_to_mark + '\n')

# Function to check if a token has been marked as used
def check_token_used(token_to_check, used_tokens_file):
    if not os.path.isfile(used_tokens_file):
        return False
    with open(used_tokens_file, 'r') as file:
        for line in file:
            if line.strip() == token_to_check:
                return True
    return False

# Example usage
token_file = "/home/bullshit/Documents/badmus/Token.txt"  # Replace with the path to your token file
used_tokens_file = "/home/bullshit/Documents/badmus/used_token_file.txt"  # Replace with the path to your used tokens record file
username = input("Enter your username: ")  # Modified to accept username input

# Generate the user ID from the username
user_id = generate_user_id(username)

token = input("Enter your token: ")

if check_token_in_file(token, token_file):
    if check_token_used(token, used_tokens_file):
        print(yellow + "Token used by another user. Welcome back!")
    else:
        print(green + "Congratulations! Token is valid and not used before. Welcome!")
        mark_token_as_used(token, used_tokens_file)
else:
    print(red + "Token is invalid.")
    