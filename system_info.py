import os
import platform
import socket
import getpass
import datetime
import re

try:
    import psutil
except ImportError:
    print("Installing required package: psutil")
    os.system("pip install psutil")
    import psutil


def line():
    print("=" * 60)


def system_information():
    line()
    print("        PYTHON SYSTEM INFORMATION TOOL")
    line()

    print(f"Operating System : {platform.system()} {platform.release()}")
    print(f"Machine Name     : {platform.node()}")
    print(f"Processor        : {platform.processor()}")
    print(f"CPU Cores        : {psutil.cpu_count(logical=True)}")

    ram = psutil.virtual_memory()
    print(f"Total RAM        : {ram.total / (1024 ** 3):.2f} GB")
    print(f"Used RAM         : {ram.used / (1024 ** 3):.2f} GB")
    print(f"RAM Usage        : {ram.percent}%")

    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print(f"IP Address       : {ip}")
    except Exception:
        print("IP Address       : Unable to detect")

    print(f"Username         : {getpass.getuser()}")

    print(
        f"Date & Time      : "
        f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    )

    line()


def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    if score <= 2:
        return "WEAK ❌"
    elif score <= 4:
        return "MEDIUM ⚠️"
    else:
        return "STRONG ✅"


def password_checker():
    line()
    print("           PASSWORD STRENGTH CHECKER")
    line()

    password = getpass.getpass("Enter password: ")

    result = password_strength(password)

    print(f"\nPassword Strength: {result}")

    if len(password) < 8:
        print("Tip: Use at least 8 characters.")

    if not re.search(r"[A-Z]", password):
        print("Tip: Add uppercase letters.")

    if not re.search(r"[0-9]", password):
        print("Tip: Add numbers.")

    if not re.search(r"[^A-Za-z0-9]", password):
        print("Tip: Add special characters.")

    line()


def main():
    while True:
        print("\n")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║             PYTHON SECURITY TOOL                        ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║  1. System Information                                  ║")
        print("║  2. Password Strength Checker                           ║")
        print("║  3. Exit                                                 ║")
        print("╚══════════════════════════════════════════════════════════╝")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            system_information()

        elif choice == "2":
            password_checker()

        elif choice == "3":
            print("\nThank you for using Python Security Tool! 🚀")
            break

        else:
            print("\nInvalid choice ❌")


if __name__ == "__main__":
    main()