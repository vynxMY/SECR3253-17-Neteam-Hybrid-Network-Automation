"""
Member 1 - NETCONF Configuration Module

Responsibilities:
1. Configure IP Address
2. Configure Interface Description

Author: Member 1
"""

from ncclient import manager
import sys
import os

# Allow importing netconf_config.py from the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from netconf_config import DEVICE


# =====================================================
# Build XML Payloads
# =====================================================

def build_ip_config_payload(interface_name, ip_address, subnet_mask):
    """
    Build XML payload for configuring an IP address.
    """

    return f"""
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <GigabitEthernet>
            <name>{interface_name}</name>
            <ip>
              <address>
                <primary>
                  <address>{ip_address}</address>
                  <mask>{subnet_mask}</mask>
                </primary>
              </address>
            </ip>
          </GigabitEthernet>
        </interface>
      </native>
    </config>
    """


def build_description_payload(interface_name, description):
    """
    Build XML payload for configuring an interface description.
    """

    return f"""
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <GigabitEthernet>
            <name>{interface_name}</name>
            <description>{description}</description>
          </GigabitEthernet>
        </interface>
      </native>
    </config>
    """


# =====================================================
# Configuration Functions
# =====================================================

def configure_ip_address(interface_name, ip_address, subnet_mask):
    """
    Configure an IP address using NETCONF.
    """

    payload = build_ip_config_payload(
        interface_name,
        ip_address,
        subnet_mask
    )

    try:
        with manager.connect(**DEVICE) as m:

            m.edit_config(
                target="running",
                config=payload
            )

            print("\n[SUCCESS]")
            print(
                f"IP Address {ip_address}/{subnet_mask} configured on "
                f"GigabitEthernet{interface_name}"
            )

    except Exception as e:
        print("\n[ERROR]")
        print(e)


def configure_interface_description(interface_name, description):
    """
    Configure interface description using NETCONF.
    """

    payload = build_description_payload(
        interface_name,
        description
    )

    try:
        with manager.connect(**DEVICE) as m:

            m.edit_config(
                target="running",
                config=payload
            )

            print("\n[SUCCESS]")
            print(
                f"Description configured on GigabitEthernet{interface_name}"
            )

    except Exception as e:
        print("\n[ERROR]")
        print(e)


# =====================================================
# Menu
# =====================================================

def run_member1_menu():

    while True:

        print("\n========================================")
        print(" Member 1 - NETCONF Configuration ")
        print("========================================")
        print("1. Configure IP Address")
        print("2. Configure Interface Description")
        print("3. Exit")

        choice = input("\nSelect option: ")

        if choice == "1":

            interface = input(
                "Interface number (Example: 2): "
            )

            ip = input("IP Address: ")

            mask = input("Subnet Mask: ")

            configure_ip_address(
                interface,
                ip,
                mask
            )

        elif choice == "2":

            interface = input(
                "Interface number (Example: 2): "
            )

            description = input(
                "Interface Description: "
            )

            configure_interface_description(
                interface,
                description
            )

        elif choice == "3":

            print("\nExiting Member 1 Module...\n")
            break

        else:

            print("\nInvalid option.")


# =====================================================
# Main
# =====================================================

if __name__ == "__main__":
    run_member1_menu()
