import os
import subprocess
import requests
import time
import platform
import webbrowser
import shutil
from termcolor import colored

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_public_ip():
    try:
        response = requests.get("https://ifconfig.me")
        return response.text.strip()
    except requests.RequestException:
        return "Failed to retrieve public IP"

def get_device_info():
    os_name = platform.system() + " " + platform.version()
    device_model = platform.machine()
    username = os.environ.get("USERNAME") or os.environ.get("USER") or "Unknown User"
    return os_name, device_model, username

def create_network(ssid):
    print(colored("Connection Approved", "green"))
    command = f"sudo hostapd -B /etc/hostapd/{ssid}.conf"
    os.system(command)
    print(colored(f"Network {ssid} created", "green"))

def remove_network(ssid):
    command = f"sudo pkill -f 'hostapd.*{ssid}'"
    os.system(command)
    print(colored(f"Network {ssid} removed", "red"))

def set_password(ssid, password):
    config_file = f"/etc/hostapd/{ssid}.conf"
    with open(config_file, "w") as f:
        f.write(f"ssid={ssid}\nwpa_passphrase={password}\n")
    print(colored(f"Password for network {ssid} set", "yellow"))

def remove_password(ssid):
    config_file = f"/etc/hostapd/{ssid}.conf"
    with open(config_file, "w") as f:
        f.write(f"ssid={ssid}\n")
    print(colored(f"Password for network {ssid} removed", "yellow"))

def display_warning():
    print(colored("You are ABSOLUTELY sure that the actions committed by this program will not harm other people and communities when using 'BadApple'...", "red"))
    try:
        choice = input("Do you agree? (y/n): ")
        if choice.lower() != "y":
            print(colored("Someday you'll understand what the word law means, a sneaky little hacker>:)", "red"))
            exit()
    except EOFError:
        print(colored("Input error detected. Exiting program.", "red"))
        exit()

def get_all_device_info():
    while True:
        clear_terminal()
        os_name, device_model, username = get_device_info()
        public_ip = get_public_ip()
        
        print(f"OS Name: {os_name}\tDevice Model: {device_model}\tUsername: {username}")
        print(f"Public IP: {public_ip}")
        print("--------------------------------------------")
        time.sleep(10)

def main():
    display_warning()
    print(colored("""
····························································
: ______           __      _______               __        :
:|   __ \.---.-.--|  |    |   _   |.-----.-----.|  |.-----.:
:|   __ <|  _  |  _  |    |       ||  _  |  _  ||  ||  -__|:
:|______/|___._|_____|    |___|___||   __|   __||__||_____|:
:                                  |__|  |__|              :
····························································
    """, "red"))
    print(colored("welcome to bad apple ", "red") + colored("v.1.1.0. (alpha)", "magenta", attrs=["italic"]))
    
    while True:
        try:
            command = input(colored("apple> ", "red"))
            parts = command.split()
            if not parts:
                continue
            
            cmd = parts[0]
            args = parts[1:]
            
            if cmd == "mknetwork" and len(args) == 1:
                create_network(args[0])
            elif cmd == "rmnetwork" and len(args) == 1:
                remove_network(args[0])
            elif cmd == "setpass" and len(args) == 2:
                set_password(args[1], args[0])
            elif cmd == "rmpass" and len(args) == 1:
                remove_password(args[0])
            elif cmd == "BadAppleSong":
                webbrowser.open("https://www.youtube.com/watch?v=9lNZ_Rnr7Jc")
            elif cmd == "getinfo":
                get_all_device_info()
            elif cmd == "exit":
                print(colored("Thanks for using Bad Apple", "green"))
                break
            else:
                print("Unknown command")
        except EOFError:
            print(colored("Input error detected. Exiting program.", "red"))
            break

if __name__ == "__main__":
    main()
