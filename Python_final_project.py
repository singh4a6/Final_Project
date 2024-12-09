import csv
import hashlib
import random
import string
import argparse
import os
import re
import sys


CSV_FILE = "passwords.csv"


def initialize_csv():
    """Ensure the CSV file exists with the appropriate headers."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Website", "Username", "Password"])


def add_password(website, username, password):
    """Add a new password entry to the CSV."""
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([website, username, password])
    print(f"Password for {website} added successfully.")


def retrieve_password(website):
    """Retrieve passwords for a specific website."""
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        found = False
        for row in reader:
            if row["Website"] == website:
                found = True
                print(f"Website: {row['Website']}, Username: {row['Username']}, Password: {row['Password']}")
        if not found:
            print(f"No passwords found for {website}.")


def update_password(website, new_password):
    """Update the password for a specific website."""
    rows = []
    updated = False
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Website"] == website:
                row["Password"] = new_password
                updated = True
            rows.append(row)

    if updated:
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Website", "Username", "Password"])
            writer.writeheader()
            writer.writerows(rows)
        print(f"Password for {website} updated successfully.")
    else:
        print(f"No passwords found for {website}.")


def delete_password(website):
    """Delete the password for a specific website."""
    rows = []
    deleted = False
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Website"] == website:
                deleted = True
                continue
            rows.append(row)

    if deleted:
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Website", "Username", "Password"])
            writer.writeheader()
            writer.writerows(rows)
        print(f"Password for {website} deleted successfully.")
    else:
        print(f"No passwords found for {website}.")


def generate_password(length):
    """Generate a random password of specified length."""
    if not isinstance(length, int) or length <= 0:
        print("Invalid length for password. Please enter a positive integer.")
        return

    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    print(f"Generated password: {password}")
    return password


def main():
    initialize_csv()
    parser = argparse.ArgumentParser(description="Password Manager with CSV Storage")
    parser.add_argument("-a", "--add", nargs=3, metavar=("WEBSITE", "USERNAME", "PASSWORD"), help="Add a new password entry")
    parser.add_argument("-r", "--retrieve", metavar="WEBSITE", help="Retrieve passwords for a website")
    parser.add_argument("-u", "--update", nargs=2, metavar=("WEBSITE", "PASSWORD"), help="Update the password for a website")
    parser.add_argument("-d", "--delete", metavar="WEBSITE", help="Delete the password for a website")
    parser.add_argument("-g", "--generate", metavar="LENGTH", type=int, help="Generate a random password of specified length")
    args = parser.parse_args()

    if args.add:
        website, username, password = args.add
        if not re.match(r"^[\w.-]+$", website):
            print("Error: Invalid website name format. Use alphanumeric characters, dots, underscores, or dashes.")
            sys.exit(1)
        add_password(website, username, password)

    elif args.retrieve:
        retrieve_password(args.retrieve)

    elif args.update:
        website, password = args.update
        update_password(website, password)

    elif args.delete:
        delete_password(args.delete)

    elif args.generate:
        generate_password(args.generate)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
