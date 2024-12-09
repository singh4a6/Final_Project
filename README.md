# Final_Project

My project codes were based on the topic "Password Manager with CSV Storage". It was a very interesting project and I learned a lot while working on this lab. It took me 3 hours to finish this lab.

# Password Manager with CSV Storage

## Overview

This script is a simple command-line-based password manager that allows users to:
- Add new passwords
- Retrieve stored passwords
- Update existing passwords
- Delete passwords
- Generate secure random passwords

Passwords are securely stored in a CSV file for easy management.

## Why This Script is Useful

Managing passwords manually is a tedious and error-prone task. This tool provides a simple way to organize and retrieve passwords while ensuring data is securely stored. It also generates random passwords to enhance security.

## Features

- **Add**: Store a website, username, and password in the CSV file.
- **Retrieve**: Fetch the username and password for a specific website.
- **Update**: Update the password for a stored website.
- **Delete**: Remove an entry for a website from the CSV.
- **Generate**: Create a random password of user-specified length.
- **Error Handling**: Handles invalid arguments, provides clear error messages, and checks input formats.

## Usage

```bash
python password_manager.py [options]

Options:
  -a, --add WEBSITE USERNAME PASSWORD  Add a new password entry
  -r, --retrieve WEBSITE               Retrieve passwords for a website
  -u, --update WEBSITE PASSWORD        Update the password for a website
  -d, --delete WEBSITE                 Delete the password for a website
  -g, --generate LENGTH                Generate a random password of specified length
  -h, --help                           Display this help message
