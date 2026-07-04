from ncclient import manager
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from netconf_config import DEVICE


def build_user_payload(username, password, privilege=15):
    """Builds the NETCONF edit-config XML payload to create a local user."""
    return f"""
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <username xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
          <name>{username}</name>
          <privilege>{privilege}</privilege>
          <secret>
            <secret>{password}</secret>
          </secret>
        </username>
      </native>
    </config>
    """


def create_user_account(username, password, privilege=15):
    """Connects to the device and creates the local user account."""
    payload = build_user_payload(username, password, privilege)
    with manager.connect(**DEVICE) as m:
        response = m.edit_config(target="running", config=payload)
        print(f"[Member2] User '{username}' created with privilege {privilege}")
        return response


def build_banner_payload(banner_text):
    """Builds the NETCONF edit-config XML payload to set the MOTD banner."""
    return f"""
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <banner>
          <motd>
            <banner>{banner_text}</banner>
          </motd>
        </banner>
      </native>
    </config>
    """


def configure_banner(banner_text):
    """Connects to the device and applies the MOTD banner."""
    payload = build_banner_payload(banner_text)
    with manager.connect(**DEVICE) as m:
        response = m.edit_config(target="running", config=payload)
        print(f"[Member2] Banner set to: '{banner_text}'")
        return response


def run_member2_menu():
    """Simple menu for main.py to call into this module."""
    print("\n--- User & Banner Configuration (Member 2) ---")
    print("1. Create User Account")
    print("2. Configure Banner")
    choice = input("Select option: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        create_user_account(username, password)
    elif choice == "2":
        banner_text = input("Banner text: ")
        configure_banner(banner_text)
    else:
        print("Invalid option.")


if __name__ == "__main__":
    # Example usage - do not commit real passwords to GitHub
    create_user_account("netadmin", "Cisco123!", privilege=15)
    configure_banner("Authorized Access Only - SECR3253 Group Project")
